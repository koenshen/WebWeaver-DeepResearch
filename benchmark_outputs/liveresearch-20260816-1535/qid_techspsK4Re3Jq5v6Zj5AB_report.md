

# Design Options for a gRPC-Based API Layer Serving Heterogeneous Clients

## Executive Summary

Building a gRPC-based API layer that simultaneously serves mobile, web (via gRPC-Web), desktop, and IoT/edge clients requires careful architectural choices. The core tension is between gRPC's native performance (HTTP/2, Protobuf binary serialization, streaming) and the browser's inability to speak native gRPC. For IoT/edge, the trade-off is between bandwidth efficiency and the overhead of HTTP/2 connection establishment. This report analyzes four principal design options, each with distinct trade-offs across scalability, developer productivity, infrastructure cost, and client integration ease.

---

## Option 1: Pure gRPC + gRPC-Web with Envoy Proxy

**How it works:** The gRPC backend serves native gRPC. An Envoy proxy sits in front with the `grpc_web` HTTP filter, translating gRPC-Web requests from browsers into native gRPC upstream. Mobile, desktop, and IoT clients use native gRPC stubs. Web browsers use the gRPC-Web JavaScript client.

### Pros
1. **Unified backend contract:** A single `.proto` file and a single gRPC server serve all client types. The Envoy proxy handles the browser translation, so the backend logic is identical for all clients.
2. **Best latency for non-browser clients:** Native gRPC over HTTP/2 with Protobuf binary serialization delivers 5–10× lower latency vs. REST/JSON for equivalent workloads, especially for small payloads (see benchmark data [here](https://tech-insider.org/grpc-vs-rest-2026)).
3. **Strongly typed, auto-generated clients:** Protobuf code generation for all platforms (Java/Kotlin for Android, Swift for iOS, Dart/Flutter, C++, Go, etc.) ensures type safety and reduces manual serialization bugs.

### Cons
1. **Bidirectional streaming is unavailable in browsers:** gRPC-Web only supports unary and server-streaming calls. Client-streaming and bidirectional streaming are not possible in the browser (see [official gRPC-Web documentation](https://grpc.io/blog/state-of-grpc-web) and [Kreya deep-dive](https://kreya.app/blog/grpc-web-deep-dive)).
2. **Operational complexity of the proxy:** Envoy must be deployed, configured, monitored, and scaled. The proxy adds a network hop and a potential bottleneck. Envoy configuration for gRPC-Web requires understanding of HTTP filters, CORS, and upstream clusters.
3. **Debugging opacity:** gRPC-Web traffic is binary and opaque to standard browser dev tools. Issues in the proxy translation layer are harder to diagnose than plain REST calls.

### Trade-off Analysis

| Dimension | Assessment |
|-----------|-----------|
| **Scalability** | Good for non-browser clients (native gRPC is highly scalable). Browser clients are limited by the Envoy proxy layer. Envoy itself is high-performance (~10k+ QPS per CPU core per [Envoy latency benchmarks](https://groups.google.com/g/envoy-dev/c/55j2PF18K1g)), but the proxy becomes a stateful intermediary that must be scaled horizontally. |
| **Developer Productivity** | High: single `.proto` definition, auto-generated stubs for all languages, IDE support via Protobuf plugins. However, debugging gRPC-Web requires extra tooling (e.g., Buf Studio, Kreya, Postman gRPC support). |
| **Infrastructure Cost** | Moderate: the Envoy proxy adds CPU/memory overhead. For a small deployment, a single Envoy instance suffices. At scale, the proxy cost is non-trivial but manageable. Native gRPC clients eliminate the need for a separate load balancer (gRPC's client-side load balancing can be used). |
| **Ease of Client Integration** | High for native clients (just compile the `.proto`). Medium for web: requires adding the `grpc-web` npm package, configuring the Envoy endpoint, and working within the streaming limitations. |

**Sources:** [gRPC-Web state and limitations](https://grpc.io/blog/state-of-grpc-web), [Envoy gRPC-Web filter documentation](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/other_protocols/grpc), [Kreya gRPC-Web deep-dive](https://kreya.app/blog/grpc-web-deep-dive), [Datadog on gRPC load balancing](https://www.datadoghq.com/blog/grpc-at-datadog)

---

## Option 2: gRPC Backend with Envoy gRPC-JSON Transcoding (RESTful Fallback for Browsers)

**How it works:** The gRPC backend remains the source of truth. Envoy's `grpc_json_transcoder` filter translates HTTP/JSON requests from browsers into gRPC calls. The `.proto` file includes `google.api.http` annotations to define the RESTful mapping. Browsers call the API as a standard REST/JSON API; mobile, desktop, and IoT clients use native gRPC.

### Pros
1. **Full browser compatibility:** Any browser can call the API with standard `fetch` or `axios`. No special gRPC-Web client library, no proxy for gRPC-Web translation. The transcoded endpoint looks like a normal REST API.
2. **Simplified debugging:** REST/JSON responses are human-readable and can be inspected with browser dev tools, curl, or Postman. This dramatically lowers the barrier for frontend developers.
3. **Unified backend logic:** The same gRPC service implementation handles both native gRPC and REST clients. The transcoding is purely a proxy-layer concern.

### Cons
1. **No streaming for REST clients:** The transcoder only supports unary calls. While server-streaming can be mapped to an array response, the client receives the entire array at once—no event-driven streaming. Client and bidirectional streaming are not available over REST.
2. **Performance overhead of transcoding:** Every request goes through JSON parsing, protobuf serialization, and back. This adds ~40–100 µs per request (see [Envoy latency benchmarks](https://groups.google.com/g/envoy-dev/c/55j2PF18K1g)). Also, payload sizes are larger (JSON vs. binary Protobuf).
3. **Dual maintenance of annotations:** The `google.api.http` annotations in `.proto` files must be kept in sync with the actual gRPC service definition. Breaking changes in the service must be reflected in the transcoding annotations.

### Trade-off Analysis

| Dimension | Assessment |
|-----------|-----------|
| **Scalability** | Good. Envoy transcoding is computationally cheap (~40 µs per request). The REST path can be cached by CDNs (HTTP caching semantics apply), which is a major advantage over pure gRPC/gRPC-Web. The gRPC path remains highly scalable. |
| **Developer Productivity** | High for frontend (standard REST patterns). Medium for backend: developers must maintain both `.proto` service definitions and HTTP annotations. The [Envoy transcoder documentation](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/grpc_json_transcoder_filter) provides guidance but adds configuration overhead. |
| **Infrastructure Cost** | Moderate: Envoy is required. The transcoder filter is built into Envoy (no additional license cost). CDN caching of transcoded REST responses can reduce backend load, potentially lowering compute costs. |
| **Ease of Client Integration** | Very high for browsers (standard REST). High for native clients (gRPC stubs). IoT/edge devices can choose either pathway depending on bandwidth and capability. |

**Sources:** [Envoy gRPC-JSON transcoder documentation](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/grpc_json_transcoder_filter), [Red Hat blog on gRPC-to-REST transcoding](https://www.redhat.com/en/blog/grpc-to-rest-transcoding-with-openshift-and-service-mesh), [.NET gRPC JSON transcoding announcement](https://devblogs.microsoft.com/dotnet/announcing-grpc-json-transcoding-for-dotnet), [Envoy latency benchmarks](https://groups.google.com/g/envoy-dev/c/55j2PF18K1g)

---

## Option 3: Connect Protocol (Buf's Connect) — No Proxy Required

**How it works:** Buf's [Connect](https://connectrpc.com/docs/introduction) protocol is an alternative to gRPC-Web that works natively over HTTP/1.1, HTTP/2, and HTTP/3. Connect servers are fully gRPC-compatible (any gRPC client can call a Connect server, and Connect clients can call any gRPC server). The Connect protocol is a simple POST-only protocol that works natively in browsers without a proxy. It supports three protocols simultaneously: gRPC, gRPC-Web, and Connect's own protocol.

### Pros
1. **No proxy required for browser support:** Connect servers speak the gRPC-Web protocol natively, eliminating the need for Envoy or any other intermediary. This reduces infrastructure complexity and eliminates one network hop.
2. **Full streaming support in browsers:** Connect's own protocol supports client streaming and bidirectional streaming (via `duplex: 'half'` and, in the future, `duplex: 'full'`). This is a significant advantage over gRPC-Web, which lacks client and bidirectional streaming (see [Kreya comparison](https://kreya.app/blog/grpc-web-deep-dive)).
3. **Seamless multi-protocol support:** A single Connect server can serve native gRPC clients, gRPC-Web clients, and Connect protocol clients simultaneously. This allows gradual migration and heterogeneous client support without protocol fragmentation.

### Cons
1. **Smaller ecosystem and community:** Connect is newer than gRPC/gRPC-Web. While it has Go, TypeScript, and Kotlin support, the ecosystem of tools, middleware, and integrations is less mature than gRPC's.
2. **Limited language support:** Connect currently supports Go, TypeScript, Swift, Kotlin, and Java. If your IoT/edge devices use C++, Rust, or Python, you may need to use the gRPC protocol compatibility layer rather than Connect's native protocol.
3. **Performance overhead on the Connect protocol path:** Connect's own protocol is designed for simplicity and debuggability, but it may have slightly higher overhead than native gRPC for high-throughput scenarios, especially for streaming (the Connect protocol wraps messages in a 5-byte envelope with an end-of-stream flag vs. gRPC's native HTTP/2 trailers).

### Trade-off Analysis

| Dimension | Assessment |
|-----------|-----------|
| **Scalability** | Good. Connect servers are built on `net/http` in Go and scale well. The ability to eliminate the proxy hop improves end-to-end latency. However, the Connect protocol's JSON support may increase payload size vs. pure gRPC. |
| **Developer Productivity** | High. Connect's `connect-es` TypeScript client generates idiomatic, type-safe code that feels like a native REST client. The `buf` CLI provides linting, breaking change detection, and code generation. The Connect protocol is debuggable with `curl` and browser dev tools. |
| **Infrastructure Cost** | Lower than Options 1 and 2 because no proxy is required. This eliminates the CPU/memory cost of running Envoy sidecars or standalone proxies. The Buf Schema Registry is a paid product, but the Connect libraries are open source. |
| **Ease of Client Integration** | Very high for browsers (no proxy, native HTTP). High for mobile/desktop (gRPC compatibility). Medium for IoT/edge: if using gRPC protocol, integration is straightforward; if using Connect protocol, language support may be a limiting factor. |

**Sources:** [Connect official documentation](https://connectrpc.com/docs/introduction), [Buf blog: Connect-Web announcement](https://buf.build/blog/connect-web-protobuf-grpc-in-the-browser), [DEV community comparison](https://dev.to/stevenacoffman/browser-client-to-grpc-server-routing-options-connect-grpc-web-grpc-gateway-and-more-52cm), [Kreya gRPC-Web vs. Connect](https://kreya.app/blog/grpc-web-deep-dive)

---

## Option 4: Hybrid Layered Architecture (gRPC Internal + Protocol-Specific Gateways)

**How it works:** The core business logic is implemented as a gRPC service. Multiple API gateways or adapters sit in front, each optimized for a specific client type: Envoy with gRPC-Web filter for browsers, a lightweight REST/JSON gateway (e.g., gRPC-gateway, Kong, or custom) for IoT/edge devices that cannot handle HTTP/2, and native gRPC for mobile/desktop. A service mesh (e.g., Istio with proxyless gRPC or sidecar Envoy) manages internal routing, mTLS, and observability.

### Pros
1. **Optimized for each client type:** Each gateway can be tuned for its specific client profile. For example, IoT/edge gateways can use HTTP/1.1 with small JSON payloads, while mobile clients get the full benefit of binary Protobuf and HTTP/2 multiplexing.
2. **Resilience and isolation:** A failure or misconfiguration in one gateway (e.g., the REST gateway) does not affect other client types. Each gateway can be scaled independently based on demand patterns.
3. **Future-proofing:** New client types can be added by implementing a new gateway without modifying the core gRPC service. This is valuable for emerging IoT protocols or future browser capabilities.

### Cons
1. **Significant infrastructure complexity:** Multiple gateways mean multiple deployments, configurations, and monitoring dashboards. The operational overhead can be substantial, especially for small teams.
2. **Contract fragmentation risk:** Each gateway may introduce subtle differences in behavior (e.g., error formatting, timeout handling, authentication). Maintaining consistency across all gateways requires disciplined API governance.
3. **Higher latency for multi-hop paths:** Requests that pass through multiple layers (e.g., browser → Envoy → gateway → gRPC service) incur additional latency at each hop. For low-latency requirements, this can be problematic.

### Trade-off Analysis

| Dimension | Assessment |
|-----------|-----------|
| **Scalability** | Excellent. Each gateway can be scaled independently. The internal gRPC service benefits from client-side load balancing (e.g., round-robin with headless Kubernetes services, as [Datadog does](https://www.datadoghq.com/blog/grpc-at-datadog)). Service mesh integration (e.g., [Istio proxyless gRPC](https://istio.io/latest/blog/2021/proxyless-grpc) or [Cloud Service Mesh proxyless](https://docs.cloud.google.com/service-mesh/docs/service-routing/proxyless-overview)) can offload traffic management from the application. |
| **Developer Productivity** | Low to Medium. Multiple gateways increase the surface area for configuration, testing, and debugging. Each gateway has its own DSL (Envoy YAML, gRPC-gateway annotations, custom adapters). The core gRPC service is shared, which is a productivity win, but the gateway layer adds significant overhead. |
| **Infrastructure Cost** | High. Multiple gateways mean more containers, more CPU/memory, and potentially more cloud costs. The [Istio sidecar proxy cost analysis](https://www.solo.io/blog/how-ambient-mesh-delivers-advanced-resource-and-cost-savings) shows that sidecar proxies can cost ~$2,376,000/year for 15,000 pods (0.6 vCPU per proxy). Proxyless gRPC can reduce this cost, but the gateway layer remains. |
| **Ease of Client Integration** | Very high. Each client type has a gateway purpose-built for its needs. Browsers get REST/gRPC-Web, IoT/edge gets lightweight HTTP, mobile gets native gRPC. The integration path is clear and optimized for each client. |

**Sources:** [Datadog blog on gRPC load balancing](https://www.datadoghq.com/blog/grpc-at-datadog), [Istio proxyless gRPC blog](https://istio.io/latest/blog/2021/proxyless-grpc), [Google Cloud proxyless service mesh](https://docs.cloud.google.com/service-mesh/docs/service-routing/proxyless-overview), [Solo.io ambient mesh cost analysis](https://www.solo.io/blog/how-ambient-mesh-delivers-advanced-resource-and-cost-savings), [Envoy gRPC features](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/other_protocols/grpc)

---

## Cross-Cutting Concerns

### Backward Compatibility and Versioning

All options benefit from Protobuf's built-in forward/backward compatibility. Key practices (from [Earthly's guide](https://earthly.dev/blog/backward-and-forward-compatibility) and [Protocol Buffers documentation](https://protobuf.dev/overview)):

- **Never reuse a field number.** Use the `reserved` keyword to prevent accidental reuse.
- **Never change the type of an existing field.** If you need a different type, add a new field and deprecate the old one.
- **Package-based versioning** (e.g., `api.v1`, `api.v2`) is the recommended approach for breaking changes ([Eclipse Velocitas style guide](https://eclipse.dev/velocitas/docs/concepts/development_model/val/grpc_style_guide)).
- **Semantic versioning** for the `.proto` package: encode the major version in the package name, but do not expose minor or patch versions on the wire.
- **Deprecation lifecycle:** Mark fields as `deprecated = true` in the `.proto` file, monitor usage, then remove after a well-communicated sunset period ([OneUptime versioning guide](https://oneuptime.com/blog/post/2026-01-08-grpc-api-versioning/view)).

For the hybrid architecture (Option 4), versioning is more complex because each gateway may need to support multiple API versions simultaneously. A version-aware routing layer (e.g., in Envoy or a service mesh) is recommended.

### IoT and Edge Device Optimization

For low-bandwidth, constrained IoT/edge devices:

- **Protobuf binary payloads** are typically 3–10× smaller than equivalent JSON. Benchmarks show Protobuf payloads are ~10× smaller than JSON, reducing bandwidth costs and transmission time ([RAPIDSEA blog](https://www.rapidseasuite.com/blog/grpc-in-modern-iot-architectures-enabling-fast-secure-and-scalable-communication), [APISIX gRPC guide](https://apisix.apache.org/learning-center/what-is-grpc)).
- Keep field numbers low (1–15) for frequently used fields to minimize wire encoding size ([Earthly guide](https://earthly.dev/blog/backward-and-forward-compatibility)).
- Use **unary RPCs** for simple telemetry bursts and **server-streaming** for config updates. Avoid client-streaming and bidirectional streaming on severely constrained devices.
- **HTTP/2 connection overhead** can be a concern for devices that connect infrequently. The initial connection latency for gRPC can be higher than MQTT or CoAP ([Medium comparison](https://medium.com/@naeemulhaq/optimizing-real-time-edge-to-cloud-data-pipelines-a-technical-comparison-of-mqtt-websockets-and-96bcfdf6c26a)). For such devices, consider using the REST/JSON transcoding path (Option 2) or a lightweight protocol like MQTT at the edge, with gRPC for edge-to-cloud communication.
- **ThingsBoard Edge** uses persistent bidirectional gRPC streaming for edge-to-cloud communication, demonstrating that gRPC can work well for always-on edge gateways ([ThingsBoard gRPC protocol docs](https://thingsboard.io/docs/edge/pe/reference/architecture/grpc)).
- **gRPC's strong interface contracts** reduce integration ambiguity and support automated code generation for IoT firmware, which is critical for long-lived deployments ([RAPIDSEA blog](https://www.rapidseasuite.com/blog/grpc-in-modern-iot-architectures-enabling-fast-secure-and-scalable-communication)).

### Client-Side Load Balancing and Service Mesh

For scalability and reliability:

- **gRPC client-side load balancing** (round-robin) with Kubernetes headless services is a proven approach used by Datadog at scale ([Datadog blog](https://www.datadoghq.com/blog/grpc-at-datadog)). It eliminates the need for intermediate load balancers.
- **Proxyless gRPC service mesh** (e.g., Istio with xDS) allows gRPC clients to receive traffic management configuration directly from the control plane, reducing the overhead of sidecar proxies ([Istio proxyless gRPC blog](https://istio.io/latest/blog/2021/proxyless-grpc), [Google Cloud proxyless service mesh](https://docs.cloud.google.com/service-mesh/docs/service-routing/proxyless-overview)).
- **Envoy as a sidecar** provides advanced traffic management (circuit breaking, retries, traffic splitting) but adds CPU/memory overhead. The [Solo.io ambient mesh analysis](https://www.solo.io/blog/how-ambient-mesh-delivers-advanced-resource-and-cost-savings) estimates 0.6 vCPU per Envoy proxy at 1000 req/s, which can be significant at scale.
- For IoT/edge, client-side load balancing may not be applicable (devices typically connect to a fixed endpoint). Instead, use DNS-based or anycast routing at the edge.

---

## Summary Decision Matrix

| Criteria | Option 1: gRPC-Web + Envoy | Option 2: gRPC + REST Transcoding | Option 3: Connect Protocol | Option 4: Hybrid Gateways |
|----------|---------------------------|-----------------------------------|---------------------------|---------------------------|
| **Browser Support** | Good (unary + server-stream only) | Excellent (full REST) | Excellent (full streaming via Connect protocol) | Excellent (customizable per client) |
| **Mobile/Desktop Support** | Excellent (native gRPC) | Excellent (native gRPC) | Excellent (gRPC compatible) | Excellent (native gRPC) |
| **IoT/Edge Support** | Good (binary, but HTTP/2 overhead) | Good (REST/JSON path available) | Medium (language support limits) | Excellent (optimized path per device) |
| **Streaming (Browser)** | Server-stream only | No streaming | Full streaming (Connect protocol) | Depends on gateway |
| **Infrastructure Complexity** | Medium (Envoy required) | Medium (Envoy required) | Low (no proxy) | High (multiple gateways) |
| **Infrastructure Cost** | Moderate | Moderate | Low | High |
| **Developer Productivity** | High (single `.proto`) | High (single `.proto` + annotations) | Very High (no proxy, debuggable) | Low (multiple gateways to maintain) |
| **Backward Compatibility** | Excellent (Protobuf) | Excellent (Protobuf + annotations) | Excellent (Protobuf, multi-protocol) | Good (requires gateway coordination) |
| **Debugging Ease** | Low (binary traffic) | High (human-readable JSON) | High (curl-debuggable) | Depends on gateway |

---

## Recommendation Context

- **For most teams with heterogeneous clients**, **Option 3 (Connect)** offers the best balance of simplicity, developer productivity, and client support. The elimination of the proxy is a significant operational win, and the multi-protocol support allows gradual migration from gRPC-Web.
- **If your IoT/edge devices are severely constrained** (e.g., sub-100 KB RAM, infrequent connections), **Option 2 (gRPC + REST Transcoding)** provides a lightweight REST/JSON fallback that can be cached by CDNs, while still allowing native gRPC for capable clients.
- **If you already have a substantial investment in Envoy** (e.g., Istio service mesh), **Option 1 (gRPC-Web + Envoy)** is the natural choice. It's well-documented, battle-tested, and integrates seamlessly with service mesh observability.
- **If you are building a large-scale platform with diverse client requirements**, **Option 4 (Hybrid Gateways)** provides the most flexibility but comes with the highest operational cost. Use this only if you have the team size and operational maturity to manage multiple gateway types.

---

## References

1. gRPC-Web Official Documentation and State of the Project — https://grpc.io/blog/state-of-grpc-web
2. Envoy gRPC-JSON Transcoder Filter Documentation — https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/grpc_json_transcoder_filter
3. Envoy gRPC Overview — https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/other_protocols/grpc
4. Connect Protocol Official Documentation — https://connectrpc.com/docs/introduction
5. Buf Blog: Connect-Web Announcement — https://buf.build/blog/connect-web-protobuf-grpc-in-the-browser
6. Kreya: gRPC-Web Under the Hood (Deep Dive) — https://kreya.app/blog/grpc-web-deep-dive
7. gRPC vs REST 2026 Performance Comparison — https://tech-insider.org/grpc-vs-rest-2026
8. Datadog: Lessons from Running a Large gRPC Mesh — https://www.datadoghq.com/blog/grpc-at-datadog
9. Protocol Buffers Official Documentation (Overview) — https://protobuf.dev/overview
10. Earthly Blog: Protocol Buffers Backward and Forward Compatibility — https://earthly.dev/blog/backward-and-forward-compatibility
11. Eclipse Velocitas gRPC Interface Style Guide — https://eclipse.dev/velocitas/docs/concepts/development_model/val/grpc_style_guide
12. OneUptime: How to Version gRPC APIs Without Breaking Clients — https://oneuptime.com/blog/post/2026-01-08-grpc-api-versioning/view
13. Microsoft Learn: Versioning gRPC Services — https://learn.microsoft.com/en-us/aspnet/core/grpc/versioning?view=aspnetcore-10.0
14. RAPIDSEA: gRPC in Modern IoT Architectures — https://www.rapidseasuite.com/blog/grpc-in-modern-iot-architectures-enabling-fast-secure-and-scalable-communication
15. Medium: Optimizing Real-Time Edge-to-Cloud Data Pipelines (MQTT, WebSockets, gRPC) — https://medium.com/@naeemulhaq/optimizing-real-time-edge-to-cloud-data-pipelines-a-technical-comparison-of-mqtt-websockets-and-96bcfdf6c26a
16. ThingsBoard Edge: gRPC Synchronization Protocol — https://thingsboard.io/docs/edge/pe/reference/architecture/grpc
17. APISIX: What is gRPC? Protocol Buffers, Performance & API Gateway Integration — https://apisix.apache.org/learning-center/what-is-grpc
18. Istio Blog: gRPC Proxyless Service Mesh — https://istio.io/latest/blog/2021/proxyless-grpc
19. Google Cloud: Proxyless gRPC Service Mesh Overview — https://docs.cloud.google.com/service-mesh/docs/service-routing/proxyless-overview
20. Solo.io: Cut Service Mesh Costs by 92% with Ambient Mesh — https://www.solo.io/blog/how-ambient-mesh-delivers-advanced-resource-and-cost-savings
21. BytesizeGo: Complete Guide to gRPC Load Balancing — https://www.bytesizego.com/blog/grpc-load-balancing
22. Red Hat Blog: gRPC-to-REST Transcoding with OpenShift and Service Mesh — https://www.redhat.com/en/blog/grpc-to-rest-transcoding-with-openshift-and-service-mesh
23. .NET Blog: Announcing gRPC JSON Transcoding for .NET — https://devblogs.microsoft.com/dotnet/announcing-grpc-json-transcoding-for-dotnet
24. DEV Community: Browser Client to gRPC Server Routing Options — https://dev.to/stevenacoffman/browser-client-to-grpc-server-routing-options-connect-grpc-web-grpc-gateway-and-more-52cm
25. Envoy Proxy Homepage and Features — https://www.envoyproxy.io
26. Envoy-dev: gRPC Latency Hunting in Envoy — https://groups.google.com/g/envoy-dev/c/55j2PF18K1g
27. Levo.ai: What Is gRPC API? Features, Examples, and Use Cases — https://www.levo.ai/resources/blogs/grpc-api
28. grpc.io: gRPC in the Browser (Postman blog) — https://grpc.io/blog/postman-grpcweb
29. Gravitee: gRPC vs. gRPC-Web: Key Differences Explained — https://www.gravitee.io/blog/understanding-grpc-web
30. Zuplo: gRPC API Gateway Guide — https://zuplo.com/learning-center/grpc-api-gateway-guide


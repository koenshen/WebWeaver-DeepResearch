

# A Comprehensive Research Report: Google's A2A Protocol vs. Anthropic's MCP Protocol

## 1. Introduction

The rapid evolution of AI agents has created a pressing need for standardized communication protocols. Two major open standards have emerged to address this challenge: **Anthropic's Model Context Protocol (MCP)**, introduced in November 2024, and **Google's Agent-to-Agent (A2A) Protocol**, announced in April 2025. While both aim to enable interoperable AI systems, they operate at fundamentally different layers of the AI stack and solve complementary problems. This report provides a detailed explanation of the differences and connections between A2A and MCP, elaborates on the innovative aspects of A2A, and examines the specific problems it is designed to address.

## 2. Overview of the Model Context Protocol (MCP)

### 2.1 What is MCP?

The Model Context Protocol (MCP) is an open standard and open-source framework introduced by Anthropic in November 2024. It standardizes the way AI systems—particularly large language models (LLMs)—integrate with and share data from external tools, data sources, and services. MCP is often described as a **"USB-C port for AI applications"** —a universal adapter that allows AI models to connect to any compliant data source or tool through a single, standardized interface [[1]](https://www.anthropic.com/news/model-context-protocol) [[2]](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro).

### 2.2 MCP Architecture

MCP follows a **client-host-server architecture**:

- **Hosts**: LLM applications (e.g., Claude, ChatGPT, VS Code) that initiate connections.
- **Clients**: Connectors within the host application that manage communication with MCP servers.
- **Servers**: Services that provide context, data, and capabilities (tools, resources, prompts) to the LLM.

Communication occurs over **JSON-RPC 2.0**, with support for stateful sessions and capability negotiation. The protocol defines three core server primitives:
- **Tools**: Executable actions the model can invoke.
- **Resources**: Data and state (e.g., documents, database records).
- **Prompts**: Reusable templates that guide model behavior for specific tasks [[3]](https://modelcontextprotocol.io/specification/2026-07-28) [[4]](https://codilime.com/blog/model-context-protocol-explained).

### 2.3 MCP Design Principles

MCP is designed to solve the problem of **information silos and fragmented integrations**. Before MCP, every new data source required custom connector code. MCP replaces this with a single protocol, enabling developers to "build once, integrate everywhere." Key design principles include:
- **Universal standard** for connecting AI to data.
- **Security and two-way connections** between data and AI tools.
- **Composability** through modular server implementations.
- **Ecosystem breadth**—supported by major AI providers including OpenAI, Anthropic, and Microsoft, and tools like VS Code, Cursor, and Replit [[5]](https://en.wikipedia.org/wiki/Model_Context_Protocol) [[6]](https://www.itential.com/resource/blog/mcp-101-understanding-the-model-context-protocol).

## 3. Overview of the Agent-to-Agent (A2A) Protocol

### 3.1 What is A2A?

The Agent-to-Agent (A2A) protocol is an open standard released by Google on April 9, 2025, at Google Cloud Next. It defines how autonomous AI agents from different vendors, frameworks, and platforms can **discover each other, delegate tasks, and coordinate work** without exposing their internal implementations. In June 2025, Google contributed the protocol to the **Linux Foundation**, ensuring vendor-neutral, community-driven governance [[7]](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability) [[8]](https://github.com/a2aproject/A2A).

### 3.2 A2A Architecture

A2A uses a **client-remote (peer-to-peer) agent model**:

- **Client Agent**: Formulates and communicates tasks to remote agents.
- **Remote Agent (Server)**: Receives tasks, processes them, and returns results (artifacts) with status updates.

The protocol is built on **existing web standards**:
- **Transport**: JSON-RPC 2.0 over HTTPS, Server-Sent Events (SSE) for streaming, and push notifications via webhooks.
- **Discovery**: Agents publish an **Agent Card** at `/.well-known/agent-card.json`—a JSON metadata file describing the agent's name, description, capabilities, supported modalities, authentication requirements, and endpoint URL.
- **Task Lifecycle**: A defined set of states: *Submitted, Working, Input-Required, Completed, Failed, Canceled, Rejected*.
- **Content**: Messages and artifacts contain **Parts**—typed content units (`TextPart`, `FilePart`, `DataPart`) that enable modality-agnostic data exchange [[9]](https://www.ibm.com/think/topics/agent2agent-protocol) [[10]](https://atlan.com/know/google-a2a-protocol).

### 3.3 A2A Design Principles

Google designed A2A with five key principles [[7]](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability):

1. **Embrace agentic capabilities**: Agents collaborate in their natural, unstructured modalities without being limited to being treated as "tools."
2. **Build on existing standards**: HTTP, SSE, JSON-RPC make it easy to integrate with existing IT stacks.
3. **Secure by default**: Enterprise-grade authentication and authorization, with parity to OpenAPI's security schemes (API keys, OAuth 2.0, OpenID Connect).
4. **Support for long-running tasks**: Flexible support for tasks ranging from quick operations to hours-long research, with real-time feedback and state updates.
5. **Modality agnostic**: Support for text, audio, video, and other streaming modalities.

## 4. Key Differences Between A2A and MCP

| Dimension | MCP (Model Context Protocol) | A2A (Agent-to-Agent Protocol) |
|---|---|---|
| **Primary Purpose** | Connect AI models to external tools, data sources, and APIs (agent-to-tool) | Enable autonomous agents to discover, delegate tasks, and collaborate (agent-to-agent) |
| **Architectural Model** | Client-host-server (hub-and-spoke); LLM-centric | Client-remote (peer-to-peer); agent-to-agent |
| **Communication Pattern** | Structured, synchronous, stateful JSON-RPC sessions | Conversational, asynchronous, with streaming (SSE) and push notifications |
| **Interaction Surface** | **Vertical**: Model accesses tools/data directly | **Horizontal**: Agents coordinate across organizational and vendor boundaries |
| **Discovery Mechanism** | Capability negotiation via MCP primitives (tools, resources, prompts) | Agent Cards (JSON metadata files) published at well-known URLs |
| **LLM Assumption** | MCP server typically relies on the caller's LLM to interpret and drive interaction | Assumes the remote peer is LLM-enabled and autonomous |
| **Content Types** | JSON-RPC messages with extensible method definitions | Explicitly defined Parts: `TextPart`, `FilePart`, `DataPart` |
| **Task Management** | Not a primary focus; tools are invoked per-request | Full task lifecycle with defined states (7 states) and long-running support |
| **Origin** | Anthropic (November 2024) | Google (April 2025); now under Linux Foundation |
| **Primary Use Case** | Single-agent applications needing tool access (e.g., Claude + databases) | Multi-agent systems requiring cross-platform coordination (e.g., Salesforce agent + ServiceNow agent) |

### 4.1 Deeper Architectural Distinctions

The fundamental difference is captured succinctly by the industry: **MCP is how agents use tools; A2A is how agents talk to each other** [[11]](https://www.merge.dev/blog/mcp-vs-a2a) [[12]](https://auth0.com/blog/mcp-vs-a2a).

- **MCP** is a **vertical protocol**: it connects a single AI model downward to data sources and tools. It's analogous to a USB-C port—a standardized way to plug peripherals into a computer.
- **A2A** is a **horizontal protocol**: it connects multiple AI agents sideways, enabling them to delegate tasks, exchange information, and coordinate workflows. It's analogous to a network router that directs traffic between autonomous nodes [[13]](https://atlan.com/know/mcp/mcp-vs-a2a-protocol).

A Cisco blog post provides a useful network engineer's mental model: **MCP is like Layer 2 (data link layer)**—it provides detailed visibility and direct access to resources but does not scale indefinitely. **A2A is like Layer 3 (network layer)**—it aggregates higher-level capability information and provides routing between agentic networks [[14]](https://blogs.cisco.com/ai/mcp-and-a2a-a-network-engineers-mental-model-for-agentic-ai).

### 4.2 Where the LLM Sits

A key technical difference noted in community discussions is the location of the LLM. In MCP, the MCP server is typically not LLM-enabled; it serves tools and data, and the client-side LLM (in the host application) interprets and drives the interaction. In A2A, the remote agent is assumed to be LLM-enabled—it is an autonomous agent that can reason, make decisions, and communicate in natural language [[15]](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/1108).

## 5. Connections Between A2A and MCP: Complementary, Not Competitive

### 5.1 The Complementary Stack

Google has explicitly stated that **A2A complements MCP** [[7]](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability). The two protocols solve different problems at different layers of the same multi-agent system and are designed to be used together:

- **MCP** provides the "muscle" for individual agents—giving them access to tools, databases, APIs, and context.
- **A2A** provides the "nervous system"—enabling agents to communicate, coordinate, and hand off work to each other.

### 5.2 How They Work Together in Practice

A typical enterprise multi-agent workflow might use both protocols in a layered architecture [[16]](https://www.cybage.com/blog/mastering-google-s-a2a-protocol-the-complete-guide-to-agent-to-agent-communication) [[17]](https://dev.to/pockit_tools/mcp-vs-a2a-the-complete-guide-to-ai-agent-protocols-in-2026-30li):

1. An **orchestrator agent** uses **A2A** to delegate a subtask to a **specialist agent** (e.g., an inventory agent).
2. That specialist agent then uses **MCP** to query its own tools and data sources (e.g., a PostgreSQL database, a CRM API).
3. The specialist agent returns results to the orchestrator via **A2A**.

**Example: Retail Supply Chain**  
An inventory agent uses MCP to check stock levels in a database. When it detects low stock, it uses A2A to communicate with external supplier agents to place orders. The supplier agents, in turn, may use MCP to access their own internal systems [[9]](https://www.ibm.com/think/topics/agent2agent-protocol).

**Example: Code Review Pipeline**  
An orchestrator agent uses A2A to assign a code review task to a security-specialist agent. That agent uses MCP to access the GitHub API, SonarQube, and a vulnerability database, then reports findings back via A2A [[17]](https://dev.to/pockit_tools/mcp-vs-a2a-the-complete-guide-to-ai-agent-protocols-in-2026-30li).

### 5.3 Blended Architectures

The boundaries can blur. In some architectures:
- Each agent in an A2A system may use MCP internally to call its own tools.
- A single MCP-powered agent might spin up temporary sub-agents (using frameworks like LangGraph or AutoGen) to handle subtasks—essentially implementing an A2A-like pattern within an MCP context [[12]](https://auth0.com/blog/mcp-vs-a2a).

### 5.4 Industry Consensus

The overwhelming industry consensus is that **MCP and A2A are not competing standards** but complementary building blocks. An article on Medium by one of the A2A protocol's authors explicitly states: "Anthropic's MCP and Google's A2A are not competing protocols; **A2A ❤️ MCP**. They solve different, complementary, but essential problems in the multi-agent systems space" [[18]](https://dr-arsanjani.medium.com/complementary-protocols-for-agentic-systems-understanding-googles-a2a-anthropic-s-mcp-47f5e66b6486).

## 6. Innovative Aspects of the A2A Protocol

### 6.1 Agent Cards: A Standardized Discovery Mechanism

A2A's **Agent Card** system is a significant innovation. Published at a well-known URL (`/.well-known/agent-card.json`), each Agent Card is a JSON document that acts as a "business card" or "LinkedIn profile" for an AI agent. It contains:
- Agent name, description, and version
- Service endpoint URL
- Supported modalities (text, audio, video, files)
- Authentication requirements (aligned with OpenAPI security schemes)
- Capability flags (streaming, push notification support)

This enables **dynamic, runtime discovery**—a client agent can discover capable remote agents without prior knowledge of their existence, enabling truly plug-and-play multi-agent ecosystems [[10]](https://atlan.com/know/google-a2a-protocol) [[9]](https://www.ibm.com/think/topics/agent2agent-protocol).

### 6.2 Full Task Lifecycle Management

A2A introduces a comprehensive **task lifecycle** with seven defined states:

| State | Description |
|---|---|
| `Submitted` | Task received by the remote agent |
| `Working` | Remote agent is actively processing |
| `Input-Required` | Agent needs more information from the client |
| `Completed` | Task finished successfully with artifacts |
| `Failed` | Task ended with an error |
| `Canceled` | Client canceled before completion |
| `Rejected` | Agent refused the task |

This lifecycle, combined with support for **Server-Sent Events (SSE)** for real-time streaming and **push notifications** via webhooks, enables robust handling of both short-lived and long-running tasks (hours or days), including those requiring human-in-the-loop intervention [[10]](https://atlan.com/know/google-a2a-protocol) [[9]](https://www.ibm.com/think/topics/agent2agent-protocol).

### 6.3 Agent Opacity and Privacy

A2A treats agents as **opaque** entities. Agents can collaborate without sharing internal memory, proprietary logic, specific tool implementations, or underlying frameworks. This is a crucial innovation for enterprise adoption because it:
- Preserves **intellectual property** and trade secrets.
- Enhances **security** by limiting the attack surface.
- Allows agents built with different frameworks (Google ADK, LangGraph, BeeAI, etc.) to interoperate without exposing internals [[8]](https://github.com/a2aproject/A2A) [[9]](https://www.ibm.com/think/topics/agent2agent-protocol).

### 6.4 Modality Agnosticism with Structured Parts

A2A's **Parts** system (`TextPart`, `FilePart`, `DataPart`) enables rich, multi-modal data exchange. This is a forward-looking design that recognizes the agentic world is not limited to text. The protocol supports:
- **Text** (plain text, markdown)
- **Files** (documents, images, spreadsheets)
- **Structured JSON data** (database records, API responses)
- **Audio and video streaming** (planned/evolving)

The **User Experience (UX) negotiation** capability allows agents to negotiate the correct content format and UI capabilities (e.g., iframes, video, web forms) for the end-user, enabling rich, interactive experiences [[7]](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability).

### 6.5 Enterprise-Grade Security Built on Open Standards

A2A is designed **secure by default**, supporting:
- **Authentication**: API keys, OAuth 2.0, OpenID Connect Discovery—aligned with OpenAPI security schemes.
- **Authorization**: The remote agent handles access control after authentication.
- **Transport security**: HTTPS for all communications.
- **v0.3 enhancement**: Signable security cards for additional trust verification.

This allows A2A to integrate with existing enterprise identity infrastructure without requiring new authentication systems [[7]](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability) [[19]](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade).

### 6.6 Linux Foundation Governance

The transfer of A2A to the **Linux Foundation** in June 2025 was a critical innovation in governance. It ensures:
- **Vendor-neutral**, community-driven development.
- **Reduced lock-in risk** compared to single-vendor-controlled specifications.
- **Open contribution** from any organization or individual.
- Long-term stability and industry-wide adoption [[8]](https://github.com/a2aproject/A2A) [[20]](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents).

## 7. Specific Problems A2A is Designed to Address

### 7.1 The Agent Fragmentation Problem

Before A2A, enterprise teams building multi-agent systems faced a severe fragmentation problem:
- Agents from one vendor could not reliably hand off work to agents from another vendor.
- Each framework had its own internal messaging format and task model.
- There was no common discovery mechanism.
- Every new agent pair required custom, bespoke integration code.

A **Salesforce agent** could not delegate a subtask to a **ServiceNow agent** without custom glue code. A **Google Vertex AI agent** could not coordinate with an **AWS Bedrock agent** without a hand-rolled bridge. A2A replaces this one-off integration effort with a single open standard [[10]](https://atlan.com/know/google-a2a-protocol) [[21]](https://galileo.ai/blog/google-agent2agent-a2a-protocol-guide).

### 7.2 The Integration Complexity Crisis

Industry data indicates that **20–40% of engineering resources** in AI projects are consumed by integration maintenance. Without standardized protocols, integration complexity grows quadratically while engineering capacity remains linear. A2A directly addresses this by providing a standardized communication layer that eliminates the need for custom integrations between every pair of agents [[21]](https://galileo.ai/blog/google-agent2agent-a2a-protocol-guide).

### 7.3 Vendor Lock-in and Ecosystem Lock-in

Organizations face significant risk when locked into a single AI vendor's agent ecosystem. Analysts have identified **ecosystem lock-in** as a critical generative AI blind spot. A2A's open, vendor-neutral standard (governed by the Linux Foundation) enables:
- Multi-vendor agent deployments.
- Flexibility to choose best-of-breed agents for specific tasks.
- Negotiating leverage with vendors.
- Future-proofing investments against vendor strategy changes [[21]](https://galileo.ai/blog/google-agent2agent-a2a-protocol-guide).

### 7.4 Lack of Standardized Agent Discovery

Prior to A2A, there was no standard way for an agent to discover what another agent could do. A2A's **Agent Card** system solves this by providing a machine-readable, universally accessible metadata file that enables agents to:
- Dynamically discover suitable remote agents.
- Understand their capabilities, modalities, and authentication requirements.
- Determine the optimal agent for a given task at runtime [[10]](https://atlan.com/know/google-a2a-protocol) [[9]](https://www.ibm.com/think/topics/agent2agent-protocol).

### 7.5 Inability to Handle Long-Running, Asynchronous Tasks

Many enterprise workflows involve tasks that take hours or days, require human approval, or span multiple steps. Traditional API models (synchronous request-response) are inadequate for:
- Supply chain coordination.
- Document review and approval workflows.
- Complex research and analysis.
- Multi-step compliance checks.

A2A's **task lifecycle with SSE streaming and webhook notifications** provides the infrastructure needed for these asynchronous, long-running, and human-in-the-loop workflows [[10]](https://atlan.com/know/google-a2a-protocol) [[9]](https://www.ibm.com/think/topics/agent2agent-protocol).

### 7.6 Multi-Modal Collaboration Constraints

The agentic world is not limited to text. Agents need to exchange images, files, structured data, and eventually audio and video. A2A's **Parts** system and **modality-agnostic** design directly address the problem of limited content types in earlier integration approaches [[7]](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability).

## 8. Real-World Use Cases and Adoption

A2A has already seen significant adoption across industries:

- **PayPal**: Deployed A2A in production for merchant-facing workflows, where a sales agent uses A2A to locate and authenticate a payment agent via its Agent Card and delegate invoice creation [[10]](https://atlan.com/know/google-a2a-protocol).
- **Tyson Foods & Gordon Food Service**: Pioneering collaborative A2A systems to drive sales and reduce supply chain friction, creating real-time channels for agents to share product data and leads [[19]](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade).
- **Adobe**: Leveraging A2A to make distributed agents interoperable across the enterprise ecosystem, streamlining content creation and multi-system workflows [[19]](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade).
- **S&P Global**: Adopted A2A as the protocol for inter-agent communication, enhancing interoperability, scalability, and future-readiness [[19]](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade).
- **ServiceNow**: Using A2A within its AI Agent Fabric to connect customer, partner, and ServiceNow agents for faster decisions and fewer handoffs [[19]](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade).
- **Twilio**: Implementing latency-aware agent selection by extending A2A to broadcast agent latency, enabling intelligent task routing [[19]](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade).

The protocol has support from over **150 organizations**, spanning every major hyperscaler, leading technology providers, and multinational customers [[19]](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade).

## 9. Conclusion

A2A and MCP are not competing protocols but **complementary layers** in the emerging stack for enterprise AI systems:

- **MCP** solves the problem of **how individual agents access tools and data**—it is a vertical, model-to-tool protocol.
- **A2A** solves the problem of **how agents discover, delegate, and coordinate**—it is a horizontal, agent-to-agent protocol.

A2A's key innovations—Agent Cards for discovery, a full task lifecycle with streaming, agent opacity for privacy, modality agnosticism, enterprise-grade security, and Linux Foundation governance—directly address the fragmentation, integration complexity, vendor lock-in, and coordination challenges that have hindered the deployment of multi-agent systems at scale.

The most likely future for enterprise AI architecture is one where **both protocols are used together**: A2A routes tasks between agents, and MCP equips each agent with the tools and context it needs to execute those tasks. As the line between tools and agents continues to blur, these protocols may converge, but for now, they form the two essential pillars of interoperable, scalable, and secure multi-agent systems.

## 10. References

1. Anthropic. "Introducing the Model Context Protocol." November 2024. https://www.anthropic.com/news/model-context-protocol
2. Model Context Protocol. "Getting Started." https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro
3. Model Context Protocol. "Specification (Latest)." https://modelcontextprotocol.io/specification/2026-07-28
4. CodiLime. "Model Context Protocol (MCP) Explained: A Practical Guide." https://codilime.com/blog/model-context-protocol-explained
5. Wikipedia. "Model Context Protocol." https://en.wikipedia.org/wiki/Model_Context_Protocol
6. Itential. "MCP 101: Understanding the Model Context Protocol." https://www.itential.com/resource/blog/mcp-101-understanding-the-model-context-protocol
7. Google Developers Blog. "Announcing the Agent2Agent Protocol (A2A)." April 9, 2025. https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability
8. A2A Project (GitHub). "Agent2Agent (A2A) Protocol." https://github.com/a2aproject/A2A
9. IBM. "What is A2A protocol (Agent2Agent)?" https://www.ibm.com/think/topics/agent2agent-protocol
10. Atlan. "Google A2A Protocol: How Agent-to-Agent Coordination Works." https://atlan.com/know/google-a2a-protocol
11. Merge.dev. "A2A vs MCP: How They Overlap and Differ." https://www.merge.dev/blog/mcp-vs-a2a
12. Auth0. "MCP vs A2A: A Guide to AI Agent Communication Protocols." https://auth0.com/blog/mcp-vs-a2a
13. Atlan. "MCP vs A2A Protocol: Architecture, Differences and When to Use." https://atlan.com/know/mcp/mcp-vs-a2a-protocol
14. Cisco Blogs. "MCP and A2A: A Network Engineer's Mental Model for Agentic AI." https://blogs.cisco.com/ai/mcp-and-a2a-a-network-engineers-mental-model-for-agentic-ai
15. GitHub Discussion (MCP Repository). "Comparing with Google's Agent2Agent (A2A) Protocol." https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/1108
16. Cybage. "Mastering Google's A2A Protocol: The Complete Guide to Agent-to-Agent Communication." https://www.cybage.com/blog/mastering-google-s-a2a-protocol-the-complete-guide-to-agent-to-agent-communication
17. Dev.to. "MCP vs A2A: The Complete Guide to AI Agent Protocols in 2026." https://dev.to/pockit_tools/mcp-vs-a2a-the-complete-guide-to-ai-agent-protocols-in-2026-30li
18. Medium (Dr. Arsanjani). "Complementary Protocols for Agentic Systems: Understanding Google's A2A & Anthropic's MCP." https://dr-arsanjani.medium.com/complementary-protocols-for-agentic-systems-understanding-googles-a2a-anthropic-s-mcp-47f5e66b6486
19. Google Cloud Blog. "Agent2Agent Protocol (A2A) is Getting an Upgrade." https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade
20. Linux Foundation. "Linux Foundation Launches the Agent2Agent Protocol Project." June 23, 2025. https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents
21. Galileo AI. "Google's Agent2Agent Protocol Explained." https://galileo.ai/blog/google-agent2agent-a2a-protocol-guide
22. OneReach.ai. "MCP vs A2A: Protocols for Multi-Agent Collaboration 2026." https://onereach.ai/blog/guide-choosing-mcp-vs-a2a-protocols
23. Solo.io. "What Is Agent2Agent Protocol (A2A)?" https://www.solo.io/topics/ai-infrastructure/what-is-a2a
24. Salesforce. "Agent2Agent Protocol: The Standard for AI Agent Interoperability." https://www.salesforce.com/agentforce/ai-agents/agent2agent-protocol
25. K21 Academy. "Agentic AI Protocols Comparison: MCP vs A2A vs ACP vs ANP." https://k21academy.com/agentic-ai/agentic-ai-protocols-comparison
26. TrueFoundry. "MCP vs A2A: Compare Single-Agent & Multi-Agent Protocols." https://www.truefoundry.com/blog/mcp-vs-a2a


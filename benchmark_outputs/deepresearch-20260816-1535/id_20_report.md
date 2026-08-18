
# Anthropic Streamable HTTP 传输层：工程实现方案深度研究报告

## 摘要

Anthropic 于 2025 年 3 月 26 日正式发布 MCP 规范修订版（v2025-03-26），将 Streamable HTTP 确立为 MCP 协议的首选远程传输层，并逐步废弃原有的 HTTP+SSE 传输机制。这一变革并非简单的 API 升级，而是对 AI 代理与外部工具间通信模型的一次根本性重构。本文档基于官方规范、社区实现及工程实践，全面剖析 Streamable HTTP 的实现方案、技术细节与架构哲学。

---

## 1. 背景与动机

### 1.1 HTTP+SSE 的固有缺陷

在 MCP 的早期版本（2024-11-05）中，客户端与服务器通过**两个独立通道**通信：
- **HTTP 请求/响应通道**：客户端通过标准 HTTP POST 向服务器发送消息。
- **SSE 事件流通道**：服务器通过专门的 `/sse` 端点向客户端推送消息。

此设计引发了以下关键问题：

- **强制长连接**：服务器必须为每个客户端维护一个长时间运行的 SSE 连接。在 1000 并发用户压力下，SSE 方案需维持上千活跃 TCP 连接，大量消耗服务器文件描述符与内存资源（约 80KB/连接）。
- **基础设施兼容性差**：企业防火墙、负载均衡器、CDN 等中间设备对长时间 SSE 长连接的兼容性不足。企业防火墙环境下 SSE 连接中断率高达 15%~30%，因安全设备常将长空闲连接判定为僵尸网络活动。
- **粘性会话（Sticky Session）强制要求**：即使是无状态通信场景，HTTP+SSE 也强制要求客户端与服务器之间维持粘性会话连接，client 和 server 端实现均非常沉重。
- **断线后状态丢失**：SSE 连接断开后所有会话状态丢失，客户端必须重新建立连接并初始化整个会话。重连虽内置，但无法恢复断点上下文。
- **高并发下性能退化严重**：100 并发时 SSE 平均延迟 18ms，但并发增至 1000 时延迟飙升至 1511ms。

### 1.2 Streamable HTTP 的设计目标

Streamable HTTP 的设计目标可概括为：

1. **统一端点**：将所有通信整合到单一 HTTP 端点（通常为 `/mcp`），消除多通道复杂性。
2. **按需流式传输**：服务器根据请求类型灵活选择返回标准 HTTP 响应或升级为 SSE 流式传输。
3. **无状态优先**：支持完全无状态的服务器实现，使 MCP 服务可部署在 Serverless 平台（如 AWS Lambda），自动获得弹性扩缩能力。
4. **基础设施友好**：标准 HTTP 语义使其可无缝集成到 API 网关、服务网格、负载均衡器和 CDN 中。
5. **断点续传与容错**：通过 SSE 事件 ID 和显式 Session ID 实现有状态恢复。

---

## 2. 核心架构设计

### 2.1 统一端点模型

Streamable HTTP 最核心的改变是：**移除了专用 SSE 端点 `/sse`，所有通信通过单一 MCP 端点完成**。

```
// 旧模式（HTTP+SSE）
- GET  /sse           ← SSE 事件流（服务器→客户端）
- POST /messages?sessionId=xxx  ← 客户端消息（客户端→服务器）

// 新模式（Streamable HTTP）
- POST /mcp           ← 客户端发送 JSON-RPC 消息
- GET  /mcp           ← 客户端监听服务器推送
```

该端点**必须同时支持 HTTP POST 和 GET 方法**。

### 2.2 消息发送流程

#### 2.2.1 客户端→服务器（POST）

客户端发送 JSON-RPC 消息时遵循以下规则：

1. **HTTP POST 到 MCP 端点**，请求体为 JSON-RPC 请求、通知或响应（单个对象，不支持批量数组）。
2. **必须包含 `Accept` 头**，列出 `application/json` 和 `text/event-stream` 作为支持的内容类型。
3. **服务器处理**：
   - 若输入为 JSON-RPC **响应或通知**：服务器返回 **HTTP 202 Accepted**（无响应体）。
   - 若输入为 JSON-RPC **请求**：服务器返回 **`Content-Type: application/json`**（同步结果）或 **`Content-Type: text/event-stream`**（启动 SSE 流）。
4. **SSE 流行为**（v2025-11-25 规范）：
   - 服务器应立即发送一个包含事件 ID 和空 `data` 字段的 SSE 事件，以"预热"客户端重连能力。
   - 服务器可在发送 ID 事件后随时关闭底层 TCP 连接（不终止 SSE 流），客户端应通过重连"轮询"流。
   - 关闭连接前，服务器应发送 SSE `retry` 字段，客户端必须尊重该字段指定的重试间隔。
   - 流中最终应包含针对每个请求的 JSON-RPC 响应。
   - 服务器可在响应之前发送 JSON-RPC 请求和通知（这些消息应与原始请求相关）。
   - 响应发送完毕后，服务器应终止 SSE 流。

#### 2.2.2 服务器→客户端（GET）

客户端可通过 HTTP GET 到 MCP 端点，打开一个独立的 SSE 流以接收服务器主动推送的消息：

1. **必须包含 `Accept` 头**，列出 `text/event-stream`。
2. 服务器返回 `Content-Type: text/event-stream` 或 **HTTP 405 Method Not Allowed**。
3. 此流中的消息应与客户端并发 POST 请求中的消息无关联。
4. 服务器不得在此流上发送 JSON-RPC 响应，除非是恢复某个之前的 POST 请求流。

### 2.3 会话管理

Streamable HTTP 支持可选的**有状态会话**，通过 `Mcp-Session-Id`（v2025-03-26）或 `MCP-Session-Id`（v2025-11-25）HTTP 头部实现：

- **会话创建**：服务器在初始化（`InitializeResult`）响应中通过 `MCP-Session-Id` 头部分配会话 ID。ID 应全局唯一且加密安全（如 UUID、JWT、加密哈希）。
- **会话使用**：客户端在后续所有请求中必须携带该头部。
- **会话终止**：
  - 服务器可随时终止会话，之后对含该 ID 的请求返回 **HTTP 404 Not Found**。
  - 客户端收到 404 后必须发送新的 `InitializeRequest`（不带旧 Session ID）重新建会话。
  - 客户端应发送 **HTTP DELETE** 到 MCP 端点以显式终止会话。服务器可返回 **HTTP 405 Method Not Allowed** 拒绝此操作。

### 2.4 断点续传与消息重投

这是 Streamable HTTP 工程实现中的关键可靠性机制：

- **事件 ID 分配**：服务器可为其 SSE 事件附加 `id` 字段。ID 必须在同一会话（或同一客户端）的所有流中全局唯一，并应编码足够信息以标识源流。
- **断线恢复**：客户端断线后，通过 HTTP GET 发送 `Last-Event-ID` 头部到 MCP 端点，指示其收到的最新事件 ID。
- **服务器行为**：服务器使用该 ID 从断点处重放消息，并恢复流。恢复机制不依赖于原始流是通过 POST 还是 GET 发起的。

### 2.5 多连接支持

- 客户端可同时维持多个 SSE 流。
- 服务器必须确保每条消息仅在一个流上发送，不得广播至多个流。

### 2.6 协议版本协商

自 v2025-11-25 起，客户端必须在所有后续请求中包含 `MCP-Protocol-Version` 头部：
```
MCP-Protocol-Version: 2025-11-25
```
版本号应为初始化阶段协商的结果。若未收到此头部，服务器默认假设版本为 `2025-03-26`。

---

## 3. 关键工程特性

### 3.1 连接动态升级机制

```
客户端 POST /mcp （标准 HTTP 请求）
  │
  ├── 服务器返回 200 + Content-Type: application/json
  │   └── 同步模式：简单请求立即返回结果
  │
  └── 服务器返回 200 + Content-Type: text/event-stream
      └── 异步模式：自动升级为 SSE 流式传输
```

这种**协商式流化**是 Streamable HTTP 的核心创新：避免了 SSE 必需的长连接预先建立，服务器可根据请求特性按需决定传输模式。

### 3.2 短时流设计

与 SSE 的持久长连接不同，Streamable HTTP 采用**短时流（Short-lived Streaming）**设计：

- 单个请求-响应周期通常控制在 30~60 秒内。
- 企业防火墙超时阈值通常为 30~60 秒，因此短时流使中断率从 SSE 的 15%~30% 降至 1% 以下。
- 服务器可在发送事件 ID 后主动关闭 TCP 连接，客户端通过轮询重连维持流。

### 3.3 无状态优先架构

Streamable HTTP 采纳**无状态优先（Stateless First）**原则：

- 90% 以上的 MCP 服务可能都是无状态的。
- 无状态模式下无需粘性会话，请求可在服务器集群中任意路由。
- 需要状态时，通过 Session ID 和外部存储（如 Redis）实现会话状态共享。
- 无状态设计使服务部署密度提升 3 倍以上，可部署在 Serverless 平台实现零负载时缩容到零。

---

## 4. 性能对比数据

| 维度 | SSE | Streamable HTTP |
|------|-----|-----------------|
| 100 并发延迟 | 18ms | 75ms（初始握手开销） |
| 1000 并发延迟 | 1511ms | 7.5ms |
| 内存消耗/连接 | ~80KB | ≤5KB/请求 |
| TCP 连接数（1000 并发） | 上千活跃连接 | 数十连接（复用） |
| 企业防火墙中断率 | 15%~30% | <1% |
| 客户端代码量 | 基准 | 减少 40%~60% |
| 水平扩展 | 需粘性会话 | 线性扩展 |

> 数据来源：腾讯云开发者社区的实际测试数据。

---

## 5. 实现代码示例

### 5.1 服务器端（TypeScript，使用官方 SDK）

```typescript
import express from "express";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";

const server = new McpServer({
  name: "my-streamable-server",
  version: "1.0.0"
});

// 注册工具、资源、提示词...

const app = express();
app.use(express.json());

app.all('/mcp', async (req, res) => {
  const transport = new StreamableHTTPServerTransport(req, res);
  await server.connect(transport);
});

app.listen(3000);
```

### 5.2 客户端（TypeScript）

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

const transport = new StreamableHTTPClientTransport(new URL("http://localhost:3000/mcp"));
const client = new Client({
  name: "my-client",
  version: "1.0.0"
});

await client.connect(transport);
```

### 5.3 客户端兼容性检测（Streamable HTTP 与 SSE 双模式）

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
import { SSEClientTransport } from "@modelcontextprotocol/sdk/client/sse.js";

let client;
const baseUrl = new URL(url);

try {
  // 首先尝试 Streamable HTTP
  client = new Client({ name: 'streamable-http-client', version: '1.0.0' });
  const transport = new StreamableHTTPClientTransport(baseUrl);
  await client.connect(transport);
  console.log("使用 Streamable HTTP 传输连接成功");
} catch (error) {
  // 失败时回退到 SSE
  console.log("Streamable HTTP 连接失败，回退到 SSE 传输");
  client = new Client({ name: 'sse-client', version: '1.0.0' });
  const sseTransport = new SSEClientTransport(baseUrl);
  await client.connect(sseTransport);
}
```

### 5.4 Python 客户端示例（使用 aiohttp）

```python
import aiohttp
import json

class StreamableHTTPClient:
    def __init__(self, url: str, headers: dict = None):
        self.url = url
        self.headers = headers or {}
    
    async def send(self, message: dict):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(
                self.url,
                json=message,
                headers={'Content-Type': 'application/json'}
            ) as response:
                if response.status == 200:
                    content_type = response.headers.get('Content-Type', '')
                    if 'text/event-stream' in content_type:
                        # 处理 SSE 流
                        async for line in response.content:
                            print(f"SSE: {line}")
                    else:
                        return await response.json()
                else:
                    raise Exception(f'HTTP error: {response.status}')
```

---

## 6. 安全机制

### 6.1 Origin 验证

服务器**必须**验证所有传入请求的 `Origin` 头部，以防止 DNS 重绑定攻击：

- 若 `Origin` 存在且无效，服务器**必须**返回 **HTTP 403 Forbidden**。
- 响应体可包含一个无 `id` 的 JSON-RPC 错误响应。

### 6.2 本地绑定建议

当在本地运行时，服务器**应**仅绑定到 `127.0.0.1`，而非 `0.0.0.0`。

### 6.3 认证

服务器**应**对所有连接实施适当的身份验证机制（如 Bearer Token、OAuth 2.1）。

---

## 7. 版本演进

| 版本 | 日期 | 关键变更 |
|------|------|----------|
| 2024-11-05 | 2024-11 | 初始 MCP 规范，使用 HTTP+SSE 传输 |
| 2025-03-26 | 2025-03-26 | 引入 Streamable HTTP，取代 SSE 为首选传输 |
| 2025-11-25 | 2025-11 | 强化 SSE 流行为（预热事件、轮询重连）；新增 `MCP-Protocol-Version` 头部要求；细化事件 ID 和重连规范 |
| 2026-07-28 | 2026-07-28 | 新增 `Mcp-Method` 和 `Mcp-Name` 头部要求，便于负载均衡器路由 |

---

## 8. 参考资料

1. MCP 官方规范 - Streamable HTTP 传输（v2025-03-26）
   https://modelcontextprotocol.io/specification/2025-03-26/basic/transports

2. MCP 官方规范 - Streamable HTTP 传输（v2025-11-25）
   https://modelcontextprotocol.io/specification/2025-11-25/basic/transports

3. MCP 官方规范 - Streamable HTTP 传输（v2026-07-28）
   https://modelcontextprotocol.io/specification/2026-07-28/basic/transports

4. MCP 规范 2026-07-28 发布候选说明
   https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate

5. MCP Streamable HTTP 示例实现（Python + TypeScript）— GitHub
   https://github.com/invariantlabs-ai/mcp-streamable-http

6. 官方 MCP Python SDK 仓库
   https://github.com/modelcontextprotocol/python-sdk

7. MCP 协议演进：从 SSE 到 Streamable HTTP 的技术革命 — 腾讯云开发者社区
   https://cloud.tencent.com/developer/article/2556166

8. MCP 协议重大升级，Spring AI Alibaba 联合 Higress 发布 Streamable HTTP 实现方案
   https://java2ai.com/blog/spring-ai-alibaba-mcp-streamable-http

9. Why MCP Deprecated SSE and Went with Streamable HTTP — fka.dev
   https://blog.fka.dev/blog/2025-06-06-why-mcp-deprecated-sse-and-go-with-streamable-http

10. Why MCP's Move Away from Server-Sent Events Simplifies Security — Auth0
    https://auth0.com/blog/mcp-streamable-http

11. A Visual Guide to MCP's Streamable HTTP Transport — Medium / The AI Language
    https://medium.com/the-ai-language/a-visual-guide-to-mcps-streamable-http-transport-6dc18fe751ad

12. Spring AI 官方文档 - Streamable-HTTP MCP Servers
    https://docs.spring.io/spring-ai/reference/api/mcp/mcp-streamable-http-server-boot-starter-docs.html

13. MCP 协议：为什么 Streamable HTTP 是最佳选择？— UML 组织
    http://www.uml.org.cn/ai/202505064.asp

14. MCP 协议：为什么 Streamable HTTP 是最佳选择？— 掘金
    https://juejin.cn/post/7497891111924957193

15. HTTP Streamable 凭什么让 Anthropic 果断抛弃 SSE？— CNode
    https://cnodejs.org/topic/683eb4480412ab6062d3948e

16. SSE vs Streamable HTTP: Why MCP Switched Transport Protocols — BrightData
    https://brightdata.com/blog/ai/sse-vs-streamable-http

17. 理论+代码讲解 Streamable HTTP MCP 服务器原理 — CSDN
    https://blog.csdn.net/weixin_42782643/article/details/148060906

18. MCP 传输层：Stdio vs Streamable HTTP — TrueFoundry
    https://www.truefoundry.com/blog/mcp-stdio-vs-streamable-http-enterprise

19. Migrate Your Claude Connector from SSE to Streamable HTTP — Sunpeak AI
    https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http

20. Anthropic 官方博客 - Introducing the Model Context Protocol
    https://www.anthropic.com/news/model-context-protocol

21. Anthropic 官方博客 - Donating MCP and Establishing the Agentic AI Foundation
    https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation

22. GitHub 讨论：Streamable HTTP 是否需要 HTTP/2？
    https://github.com/orgs/modelcontextprotocol/discussions/598

23. GitHub Issue：Claude Code 支持 Streamable HTTP MCP 服务器
    https://github.com/anthropics/claude-code/issues/1387

24. GitHub Issue：Claude Agent SDK 缺少 Accept 头导致 406
    https://github.com/anthropics/claude-agent-sdk-typescript/issues/202

25. MCP Course #10 - Visual Overview of Streamable HTTP Server & Client Interaction — YouTube
    https://www.youtube.com/watch?v=sNFcx-jUnvg


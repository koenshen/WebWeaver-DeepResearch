
# Designing a Highly Available, Horizontally Scalable Chat Application for Millions of Concurrent Users

## 1. Introduction

Modern chat applications (WhatsApp, Discord, Telegram) serve billions of users and trillions of messages. This report presents a comprehensive architecture for a chat system that must handle **millions of concurrent users** while providing **exactly-once delivery**, **typing indicators**, **message history**, **media sharing**, **one-to-one and group chats**, and **end-to-end encryption (E2EE)**. The design is intended for junior developers who want to understand the trade-offs behind real-world, production-grade messaging systems.

---

## 2. Core Architecture Components

A highly scalable chat system is decomposed into several loosely coupled layers, each of which can scale independently.

### 2.1 Messaging Layer (Real-Time Delivery)

The messaging layer is responsible for establishing persistent connections, routing messages between clients, and pushing events (new messages, typing indicators, presence updates) in real time.

**Key Patterns:**

- **WebSocket Gateway Fleet:** Clients maintain persistent WebSocket connections to a pool of gateway servers. Each gateway handles thousands of concurrent connections, using lightweight threads or event loops (e.g., Erlang processes, Node.js event loop, Java NIO).  
  *Reference:* WhatsApp uses Erlang’s BEAM VM to manage millions of concurrent processes per server [^whatsapp-architecture].

- **Pub/Sub Backplane for Cross-Server Communication:** When a message is sent to a user connected to a different gateway, the message must be forwarded. A **pub/sub message broker** (Redis Pub/Sub, RabbitMQ, or Kafka) acts as a backplane: each gateway subscribes to channels (e.g., per-user or per-conversation) and publishes messages that are fanned out to all relevant gateways.  
  *Reference:* Ably and many production systems use this pattern to decouple connection management from message routing [^ably-websocket].

- **Connection Registry:** A distributed hash map (e.g., Redis Hash or a dedicated lookup service) maps `user_id → gateway_id`. This allows any gateway to quickly determine which gateway holds the WebSocket connection for a given recipient.  
  *Reference:* Discord’s real-time gateway uses a similar registry for presence and message routing.

- **Typing Indicators & Presence:** These are ephemeral, high-churn events. They are best handled in-memory with short TTLs. When a user types, the gateway publishes a `typing:{conversation_id}` event to Redis Pub/Sub; other gateways receive it and push it to connected clients. The state is not persisted to durable storage.  
  *Reference:* A production typing indicator system using Redis Pub/Sub achieves ~10–15ms total latency across servers [^typing-indicator].

### 2.2 Storage Layer

The storage layer is responsible for durable message history, user profiles, conversation metadata, and media metadata.

**Key Patterns:**

- **Message Store (Write-Optimized, Time-Series):** Messages are append-only with high write throughput. A **wide-column NoSQL database** (Cassandra, ScyllaDB, or DynamoDB) is the natural fit because of its ability to scale horizontally, handle high write loads, and model time-series data efficiently.  
  *Reference:* Discord stores trillions of messages in Cassandra / ScyllaDB [^discord-cassandra].

- **Conversation Metadata & User Profiles (Relational):** For structured data with strong consistency needs (user accounts, group membership, permissions), a **relational database** (PostgreSQL, MySQL) with read replicas is appropriate. WhatsApp uses MySQL for group metadata [^whatsapp-architecture].

- **Media Blob Store:** Images, videos, and files are stored in an **object store** (S3, GCS, Azure Blob) with a CDN for fast global delivery. The storage layer keeps only metadata (URL, size, type) and the encryption key (if E2EE is used).

### 2.3 Real-Time Event Handling & Data Services

- **Data Services Layer:** Discord’s architecture introduces a **data service** layer between the API monolith and the database. These services are stateless, written in a high-performance language (Rust, Go), and provide **request coalescing** (deduplicating concurrent reads for the same row) and **consistent hash-based routing** (all requests for a given channel go to the same service instance). This reduces load on the database and improves tail latency.  
  *Reference:* Discord’s data services in Rust reduced p99 read latency from 40–125ms to 15ms [^discord-data-services].

- **Stream Processing:** For non-real-time tasks such as indexing messages for search, generating analytics, or fanning out group messages asynchronously, a **distributed streaming platform** (Kafka) is used. Kafka provides **exactly-once semantics** when combined with transactional producers and consumers.  
  *Reference:* Confluent documents Kafka’s exactly-once delivery via idempotent producers and transactions [^kafka-exactly-once].

---

## 3. Scalability Mechanisms

### 3.1 Sharding / Partitioning

**Database Sharding:**

- **Cassandra/ScyllaDB Architecture:** Data is automatically partitioned by a partition key. For messages, the partition key is typically `(channel_id, bucket)`, where `bucket` is a time window (e.g., a 10-day period). This ensures that all messages in a channel within a given time window co-locate on a few nodes, making range scans (loading history) fast.  
  *Reference:* Discord found that keeping partitions under 100–200 MB avoids hot spots and compaction issues [^discord-cassandra].

- **DynamoDB:** Uses partition key (e.g., `conversation_id`) and sort key (e.g., `message_id` or `timestamp`). Single-table design with GSIs enables querying by user.  
  *Reference:* AWS documentation recommends designing schemas based on access patterns, using vertical partitioning for large conversations [^dynamodb-chat].

- **Relational Sharding:** PostgreSQL can be sharded using tools like Citus, but this adds complexity and is less commonly used for high-write message stores.

**Key Trade-Off: Partition Size vs. Scatter-Gather**

| Strategy | Pros | Cons |
|----------|------|------|
| Single partition per channel (e.g., `channel_id`) | Simple reads for history | Hot partitions, large partitions degrade performance |
| Time-based bucketing (e.g., `channel_id + day`) | Balanced partitions, easy TTL | Requires multi-partition queries for cross-time-range reads |
| Multi-bucket (e.g., `channel_id + day + bucket_num`) | Highest write throughput, ideal for hot channels | Scatter-gather reads, complex pagination |

*Reference:* The Last Pickle’s time-series data modeling guide [^cassandra-time-series].

### 3.2 Load Balancing

- **WebSocket Load Balancing:** Because WebSocket connections are stateful (long-lived, session-bound), **sticky sessions** (session affinity) are required. Common strategies:
  - **IP Hash** (e.g., NGINX `ip_hash`): Simple, but fragile if users roam networks.
  - **Cookie-based stickiness** (e.g., HAProxy cookie insertion): More robust.
  - **Application-level routing:** The load balancer reads a session ID from a custom header or cookie.

  *Reference:* Ably explains that sticky sessions are essential for WebSockets, but should be combined with a pub/sub backplane to avoid connection state becoming a single point of failure [^ably-websocket].

- **API Load Balancing:** Standard HTTP(S) load balancers (NLB, ALB, HAProxy, NGINX) with round-robin or least-connections distribute REST API calls.

### 3.3 Horizontal Scaling

- **Gateway Fleet:** Add more WebSocket gateway servers behind a load balancer. Each gateway registers itself in the connection registry.
- **Data Services:** Stateless services scale horizontally behind a consistent hash ring (e.g., using a hash of `channel_id` to route to the correct instance).
- **Database:** Add nodes to the Cassandra/ScyllaDB cluster; automatic rebalancing redistributes data.
- **Kafka:** Add partitions and brokers to increase throughput.

---

## 4. High Availability & Fault Tolerance

### 4.1 Redundancy & Replication

- **Database Replication:** Cassandra and ScyllaDB use configurable replication factors (e.g., RF=3) across availability zones. In the event of a node failure, reads and writes are served by remaining replicas.  
  *Reference:* Discord’s ScyllaDB cluster runs with RF=3 across multiple AWS AZs [^discord-cassandra].

- **Kafka Replication:** Topics are replicated across brokers. A controller broker handles leader election if a broker fails.

- **Gateway Failover:** If a gateway server fails, clients reconnect via the load balancer and are routed to a healthy gateway. The connection registry is updated.

### 4.2 Exactly-Once Delivery

Achieving **exactly-once delivery** in a distributed, high-throughput chat system is difficult. The most pragmatic approach is **at-least-once delivery with idempotent deduplication**, which presents to the user as exactly-once.

**Key Techniques:**

1. **Client-Generated Message ID (`client_msg_id`):** Each message is assigned a unique, monotonic ID by the sender. The server deduplicates by this ID before persisting.

2. **Idempotent Writes:** The message store uses `client_msg_id` as part of the primary key. If the same ID is inserted twice, the second write is a no-op (or overwrites with the same data).

3. **Transactional Offset Management (Kafka):** For stream processing, Kafka’s **transactional API** ensures that offsets are committed atomically with output data. This prevents duplicates when a consumer crashes and restarts.  
   *Reference:* Kafka’s exactly-once semantics rely on idempotent producers and transactions, as documented by Confluent [^kafka-exactly-once].

4. **Deduplication in the Data Service:** Discord’s request coalescing ensures that concurrent reads for the same message are served from a single database query, reducing duplicates.

**Important Caveat:** True end-to-end exactly-once delivery across heterogeneous systems (WebSocket gateway → Kafka → Database → push notification) is extremely expensive. Most production systems (WhatsApp, Discord) accept **at-least-once with dedup**, which gives the user an exactly-once experience without the complexity of distributed transactions.

### 4.3 Offline Message Handling

- Messages are persisted in the message store before the sender receives an acknowledgment.
- When a recipient comes online, they perform a **sync** operation: the client sends the last known `server_seq` (a monotonic sequence number per conversation), and the server returns all messages with a higher sequence.
- This pattern is used by WhatsApp and described in system design interviews [^bytebytego-chat].

### 4.4 Graceful Degradation

- If the database is under load, ephemeral features (typing indicators, presence) can be degraded or sampled.
- If Redis Pub/Sub is down, gateways can fall back to direct HTTP polling or a secondary backplane.
- Rate limiting at the gateway and API layers protects against DDoS and misbehaving clients.

---

## 5. Security & Encryption Design

### 5.1 Encryption in Transit

- **TLS 1.3** is mandatory for all client-server and server-server communication.
- WebSocket connections use `wss://` (TLS over WebSocket).
- Inter-service communication (gRPC, HTTP) uses mutual TLS (mTLS) in a service mesh.

### 5.2 Encryption at Rest

- **Message Store:** Data is encrypted at rest using AES-256. In Cassandra/ScyllaDB, transparent data encryption (TDE) can be enabled at the OS or database level.
- **Media Store:** Object stores (S3, GCS) provide server-side encryption (SSE-S3 or SSE-KMS).
- **Backups:** Encrypted with separate keys.

### 5.3 End-to-End Encryption (E2EE)

E2EE is a **desirable** feature, meaning the server never has access to plaintext message content. The **Signal Protocol** is the de facto standard, used by Signal, WhatsApp, and Google Messages.

**Signal Protocol Architecture:**

1. **Key Exchange (X3DH):** When two users first communicate, they exchange **identity keys**, **signed prekeys**, and **one-time prekeys** via a server-side key directory. The X3DH protocol establishes a shared secret without the server learning the keys.
2. **Double Ratchet Algorithm:** After the initial key exchange, each message derives a new encryption key using a ratchet mechanism. This provides **forward secrecy** (compromise of a current key does not expose past messages) and **post-compromise security** (future messages become secure again after a compromise).
3. **Group Chats:** Signal’s group protocol uses a **sender key** that is distributed to all group members via pairwise encrypted channels. This avoids expensive per-recipient encryption for each message.

*Reference:* Signal’s technical specifications provide the complete details [^signal-protocol].

**Server Role in E2EE:**
- The server stores **encrypted blobs** (ciphertext) and metadata (sender, recipient, timestamp).
- The server cannot read the message content.
- For media sharing, the media file is encrypted on the client with a symmetric key, and the key is sent as part of the encrypted message payload.
- The server’s key directory must be secured against tampering; public keys are signed by the user’s identity key.

**Trade-Offs:**
- E2EE prevents server-side content analysis (spam, malware scanning, indexing).
- Group chat fan-out becomes more complex because each message must be encrypted once per recipient (or use a sender key).
- Search over message history cannot be done server-side; clients must do local search.

### 5.4 Authentication & Authorization

- **JWT-based authentication** for API calls.
- **WebSocket authentication** occurs during the handshake (token in the query string or first message).
- **Rate limiting** and **API keys** for internal services.

---

## 6. Database Selection Comparison

The choice of database depends on the access pattern, consistency requirements, and operational complexity. A **polyglot persistence** approach is common.

| Feature | Relational (PostgreSQL / MySQL) | Wide-Column NoSQL (Cassandra / ScyllaDB) | Document NoSQL (DynamoDB) | Distributed Streaming (Kafka) |
|---------|--------------------------------|------------------------------------------|---------------------------|-------------------------------|
| **Best For** | User profiles, group metadata, permissions | Message history (time-series, high write) | Variable schema, serverless scaling | Event sourcing, async fan-out, cross-datacenter replication |
| **Scalability** | Vertical + read replicas; sharding with Citus (complex) | Horizontal by default; linear scalability via partition key | Horizontal; auto-scaling, but hot partitions possible | Horizontal via partition count; high throughput |
| **Latency** | Low for indexed queries; can degrade under high write | Low for writes; reads can be expensive (multiple SSTables) | Single-digit ms for reads/writes within a partition | Sub-ms for publish; depends on consumer lag |
| **Consistency** | Strong ACID (serializable) | Tunable (eventual to strong) | Eventually consistent (strong optional via DynamoDB Transactions) | At-least-once / exactly-once with configurable acks |
| **Write Throughput** | Limited by single node; replicas help reads | Very high (append-only, LSM trees) | Very high (auto-scales) | Very high (partitioned) |
| **Read Patterns** | Flexible SQL joins, aggregations | Must be query-driven; no joins; denormalize | Must be access-pattern driven; single-table design | Sequential consumption; replay from offset |
| **Operational Complexity** | Low to medium (mature tooling) | High (compaction, repair, tuning) | Low (fully managed on AWS) | Medium (need to manage brokers, ZooKeeper/KRaft) |
| **Cost** | Moderate (licensing, hardware) | Moderate to high (many nodes, SSDs) | Pay-per-request (can be expensive for high throughput) | Moderate (broker nodes, storage) |

**Justification for the Recommended Design:**

- **Messages:** Use **ScyllaDB** (or Cassandra) due to its ability to handle **high write throughput** (append-only), **time-series data model** with bucketing, and **horizontal scalability**. Discord’s migration from Cassandra to ScyllaDB reduced p99 latencies from 40–125ms to 15ms for reads and from 5–70ms to 5ms for writes [^discord-cassandra]. ScyllaDB’s **shard-per-core architecture** avoids Java GC pauses and provides consistent latency.
- **User & Group Metadata:** Use **PostgreSQL** with read replicas. This data is low-volume, requires strong consistency (e.g., ensuring a user cannot be added to a group that doesn’t exist), and benefits from relational integrity.
- **Ephemeral State (Typing, Presence):** Use **Redis** (in-memory data store) with TTL-based expiry. No persistence needed.
- **Event Streaming & Async Processing:** Use **Kafka** for exactly-once stream processing, indexing messages into Elasticsearch, and fan-out of group messages to subscribers. Kafka’s **exactly-once semantics** (idempotent producers + transactions) ensure reliable processing [^kafka-exactly-once].
- **Media Storage:** Use **S3 / GCS** with CDN for low-latency access.

---

## 7. End-to-End Architecture Diagram (Textual)

```
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│   Client A   │       │   Client B   │       │   Client C   │
│  (WebSocket) │       │  (WebSocket) │       │  (WebSocket) │
└──────┬───────┘       └──────┬───────┘       └──────┬───────┘
       │                      │                      │
       │                      │                      │
       ▼                      ▼                      ▼
┌──────────────────────────────────────────────────────────────┐
│                  Load Balancer (Sticky Sessions)              │
│         (NGINX / HAProxy / AWS NLB with IP Hash)             │
└──────────────────────────────────────────────────────────────┘
       │                      │                      │
       ▼                      ▼                      ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Gateway 1   │     │  Gateway 2   │     │  Gateway 3   │
│  (WebSocket) │     │  (WebSocket) │     │  (WebSocket) │
└──────┬───────┘     └──────┬───────┘     └──────┬───────┘
       │                      │                      │
       │      ┌───────────────┴────────────────┐     │
       │      │  Redis Pub/Sub (Backplane)      │     │
       │      │  + Connection Registry (Hash)   │     │
       │      └───────────────┬────────────────┘     │
       │                      │                      │
       ▼                      ▼                      ▼
┌──────────────────────────────────────────────────────────────┐
│                    Data Services (Rust / Go)                  │
│   - Request coalescing                                       │
│   - Consistent hash routing (by channel_id)                  │
│   - gRPC endpoints                                           │
└──────────────────────────────────────────────────────────────┘
       │                      │                      │
       ▼                      ▼                      ▼
┌──────────────────────────────────────────────────────────────┐
│                    Message Store (ScyllaDB)                   │
│    Partition key: (channel_id, bucket)                       │
│    Clustering: message_id (timeuuid) DESC                    │
│    Replication factor: 3 (across AZs)                        │
└──────────────────────────────────────────────────────────────┘
       │                      │                      │
       ▼                      ▼                      ▼
┌──────────────────────────────────────────────────────────────┐
│                    User Metadata (PostgreSQL)                 │
│                    Media Blob Store (S3 + CDN)               │
│                    Stream Processing (Kafka)                  │
│                    Search Index (Elasticsearch)               │
└──────────────────────────────────────────────────────────────┘
```

---

## 8. Summary of Trade-Offs and Key Decisions

| Aspect | Decision | Rationale |
|--------|----------|-----------|
| **Message Delivery Guarantee** | At-least-once with idempotent dedup (presents as exactly-once) | True exactly-once across heterogeneous systems is prohibitively expensive; dedup by `client_msg_id` is practical and proven [^bytebytego-chat]. |
| **Message Store** | ScyllaDB (or Cassandra) | Write-optimized, horizontally scalable, time-series bucketing, proven at trillion-message scale [^discord-cassandra]. |
| **User Metadata** | PostgreSQL | Strong consistency, relational integrity, mature tooling, low volume. |
| **Ephemeral State** | Redis (in-memory, TTL) | Sub-millisecond latency, no persistence needed, natural expiry. |
| **Real-Time Communication** | WebSocket + Redis Pub/Sub | Persistent connections, server-push, decoupled gateways [^ably-websocket]. |
| **E2EE** | Signal Protocol (X3DH + Double Ratchet) | Industry standard, forward secrecy, post-compromise security [^signal-protocol]. |
| **Load Balancing** | Sticky sessions (IP hash / cookie) | WebSocket connections must stay on the same gateway [^ably-websocket]. |
| **Async Processing** | Kafka with exactly-once semantics | Reliable fan-out, indexing, and cross-DC replication [^kafka-exactly-once]. |

---

## 9. References

1. WhatsApp Architecture (Erlang, BEAM, WebSocket, XMPP) – *Technical Explore*  
   https://www.technicalexplore.com/tech/unveiling-the-architecture-behind-whatsapp-a-deep-dive-into-the-worlds-most-popular-messaging-platform

2. Discord How Discord Stores Trillions of Messages (Cassandra → ScyllaDB, Data Services in Rust) – *Discord Blog*  
   https://discord.com/blog/how-discord-stores-trillions-of-messages

3. WebSocket Architecture Best Practices (Pub/Sub, Sticky Sessions, Backpressure) – *Ably*  
   https://ably.com/topic/websocket-architecture-best-practices

4. Exactly-Once Semantics in Apache Kafka – *Confluent Documentation*  
   https://docs.confluent.io/kafka/design/delivery-semantics.html

5. Signal Protocol Specification – *Signal Foundation*  
   https://signal.org/docs

6. Cassandra Time Series Data Modeling (Bucketing, Partition Key Design) – *The Last Pickle*  
   https://thelastpickle.com/blog/2017/08/02/time-series-data-modeling-massive-scale.html

7. Building a Scalable Real-Time Typing Indicator System (Redis Pub/Sub, WebSocket) – *Medium (Ramesh)*  
   https://medium.com/@ramesh200212/building-a-scalable-real-time-typing-indicator-system-a-deep-dive-into-distributed-architecture-5f14b331c4ab

8. DynamoDB Chat Data Model (Single-Table Design, Access Patterns) – *AWS Database Blog*  
   https://aws.amazon.com/blogs/database/amazon-dynamodb-data-models-for-generative-ai-chatbots

9. ScyllaDB vs. Apache Cassandra (Latency Comparison, Discord Case Study) – *ScyllaDB*  
   https://www.scylladb.com/compare/scylladb-vs-apache-cassandra

10. System Design: Design a Chat System (ByteByteGo) – *bytebytego.com*  
    https://bytebytego.com/courses/system-design-interview/design-a-chat-system

11. Load Balancing WebSockets (Sticky Sessions, IP Hash, Cookie-Based) – *Ably*  
    https://ably.com/topic/when-and-how-to-load-balance-websockets-at-scale

12. Kafka Exactly-Once Semantics (Idempotent Producers, Transactions) – *Confluent Blog*  
    https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it

13. End-to-End Encryption (E2EE) Definition – *IBM*  
    https://www.ibm.com/think/topics/end-to-end-encryption

14. WhatsApp Erlang Architecture (Concurrency, Mnesia, Scaling) – *Scale With Chintan*  
    https://scalewithchintan.com/blog/whatsapp-erlang-architecture-2-billion-users

15. Chat Architecture Reliable Message Ordering – *Ably*  
    https://ably.com/blog/chat-architecture-reliable-message-ordering

---

*This report is intended as an educational resource for junior developers. The design decisions reflect a balance of proven patterns from large-scale production systems and the theoretical trade-offs described in the literature.*

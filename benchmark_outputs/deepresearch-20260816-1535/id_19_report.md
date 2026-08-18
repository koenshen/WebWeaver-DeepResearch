
# Prometheus 高流失率（高基数）的深层影响与系统性解决方案——深度研究报告

## 摘要

Prometheus 的“高流失率”（High Churn Rate）是指时间序列的标签组合在短时间内频繁变化或大量新增，导致活跃序列数急剧膨胀的现象。它在技术层面表现为**高基数（High Cardinality）**，是 Prometheus 生产环境中最为棘手的性能瓶颈之一。本报告从影响、系统性解决方案、以及主流云厂商的现有方案三个维度，进行了深入的调研与分析。

---

## 一、高流失率（高基数）的核心影响

高流失率直接导致 Prometheus 实例中活跃时间序列（Active Series）数量激增，对系统稳定性、资源消耗、查询性能、成本以及运维效率带来全方位冲击。

### 1.1 系统稳定性风险

- **内存溢出（OOM）与崩溃**：Prometheus 将最近两小时的数据保存在内存的 Head Block 中。当序列数量持续增长（如 Pod 频繁重建导致 `pod_name` 标签不断变化），Head Block 无法压缩，内存占用单调递增，最终导致 OOM 被杀。
  - 来源：[Prometheus At Scale: Taming High Cardinality (2026)](https://alexandre-vazquez.com/prometheus-scalability)
- **查询引发级联超时**：高基数指标在查询时需要扫描大量倒排索引，可能触发 Prometheus 的查询超时，甚至拖垮整个实例。
  - 来源：[Prometheus性能调优-什么是高基数问题以及如何解决?](https://www.cnblogs.com/east4ming/p/17242749.html)

### 1.2 存储与计算资源膨胀

- **磁盘与 IO 爆炸**：每个唯一的标签组合都对应一条独立的时间序列，存储和 IO 开销呈指数级增长。例如，`http_request_duration_seconds_bucket` 指标若带有 `instance`（100个）、`le`（10个）、`url`（400个）、`method`（5个）标签，理论序列数可达 200 万。
  - 来源：[Prometheus性能调优-什么是高基数问题以及如何解决? - 腾讯云](https://cloud.tencent.com/developer/article/2183170)
- **CPU 占用飙升**：倒排索引的维护和查询在序列数激增时成为 CPU 瓶颈。`rate(prometheus_tsdb_head_series_created_total[5m])` 持续高于 50,000/分钟即视为预警。
  - 来源：[Prometheus At Scale: Taming High Cardinality (2026)](https://alexandre-vazquez.com/prometheus-scalability)

### 1.3 查询性能严重退化

- **仪表板加载失败**：Grafana Dashboard 的查询一旦涉及高基数指标，可能因数据量过大而超时或加载空白。
  - 来源：[Prometheus性能调优-什么是高基数问题以及如何解决?](https://www.cnblogs.com/east4ming/p/17242749.html)
- **告警失效**：Alerting Rule 因查询超时无法评估，导致生产故障无法被感知。
  - 来源：[Prometheus At Scale: Taming High Cardinality (2026)](https://alexandre-vazquez.com/prometheus-scalability)

### 1.4 商业成本激增

- **SaaS 按量计费**：多数云厂商和可观测 SaaS 产品按活跃序列数或每分钟摄入样本数计费。高流失率导致账单迅速攀升。例如，Amazon Managed Prometheus 的成本优化案例显示，优化前每日成本 39.96 美元，优化后降至 14.3 美元，降幅达 64%。
  - 来源：[优化 Amazon EKS 集群的 Amazon Managed Service for Prometheus 成本](https://aws.amazon.com/cn/blogs/china/taking-control-of-amp-spending-on-amazon-eks-clusters-strategies-for-cost-optimization)
- **自建资源成本**：即使自建，也需要更高的硬件配置和运维投入。

### 1.5 运维噪音与警报疲劳

- **海量告警干扰**：高基数产生的冗余数据会触发大量无意义的告警，SRE 团队疲于应对，反而延误根因分析。
  - 来源：[Prometheus性能调优-什么是高基数问题以及如何解决?](https://www.cnblogs.com/east4ming/p/17242749.html)

---

## 二、系统性解决方案

高流失率问题没有银弹，需要从**指标体系设计、采集链路治理、存储架构选型、查询优化**四个层面构建分层防御体系。

### 2.1 指标体系设计：源头治理

#### 2.1.1 禁止使用高基数标签

- **不可枚举的标签**：`user_id`、`order_id`、`trace_id`、`session_id`、`email`、`IP` 等值域无界的标签绝不能出现在 Prometheus 指标中。
  - 来源：[何为 Prometheus 高基数？为何有时会有高基数峰值？](https://flashcat.cloud/blog/what-are-cardinality-spikes-and-why-do-they-matter)
- **标签归一化**：路径类标签需做归一化处理，如 `/api/user/123/profile` → `/api/user/:id/profile`。
  - 来源：[减少写入量以降低 Prometheus 指标成本 - 阿里云](https://www.alibabacloud.com/help/zh/cms/cloudmonitor-1-0/product-overview/usage-analysis-and-cost-optimization-guide)

#### 2.1.2 合理设计数据模型

- 避免将多个高基数标签组合在同一指标中。例如，10 万个设备、100 个地区、10 种设备类型，若建模在一个指标中，理论序列数可达 1 亿；按实际查询模式拆分为多个指标后，可减少 10 倍。
  - 来源：[时序数据高基问题揭秘：根因分析与解决之道 | Greptime](https://greptime.cn/blogs/2024-03-03-cardinality)

### 2.2 采集链路治理：层层过滤

#### 2.2.1 优先在 Exporter 侧关闭 Collector

- 在指标源头（如 `node_exporter` 的 `--collector.disable-defaults`）关闭无用 Collector，避免指标进入抓取流程。
  - 来源：[优化实践：Prometheus 性能和高基数问题](https://flashcat.cloud/blog/prometheus-performance-and-cardinality-in-practice)

#### 2.2.2 使用 `metric_relabel_configs` 丢弃高基数标签/指标

- 在抓取完成后、入库之前，通过 `metric_relabel_configs` 丢弃不必要的标签或高基数指标。例如：

  ```yaml
  metric_relabel_configs:
  - source_labels: [__name__]
    regex: "etcd_request_duration_seconds_bucket"
    action: drop
  ```

- 来源：[Prometheus性能调优-什么是高基数问题以及如何解决?](https://www.cnblogs.com/east4ming/p/17242749.html)

#### 2.2.3 设置 `sample_limit` 与 `scrape_interval`

- 为每个 target 设置 `sample_limit`，防止单个目标产生过多样本导致系统过载。
- 增大全局 `scrape_interval`（如从 15s 调整为 1m），降低数据摄入速率。
  - 来源：[Prometheus性能调优-什么是高基数问题以及如何解决? - 腾讯云](https://cloud.tencent.com/developer/article/2183170)

#### 2.2.4 使用 `write_relabel_configs` 在 Remote Write 阶段过滤

- 在将数据写入远端存储（如 Thanos、Mimir、VictoriaMetrics）时，通过 `write_relabel_configs` 进行二次过滤，并添加 `external_labels` 以区分 HA 副本。
  - 来源：[Prometheus性能调优-什么是高基数问题以及如何解决?](https://www.cnblogs.com/east4ming/p/17242749.html)

### 2.3 预聚合与 Recording Rules

- 对于必须保留的高基数指标，使用 Recording Rule 预聚合（如 `sum by (namespace, job)`），将聚合结果存入新指标，然后丢弃原始高基数指标。
  - 来源：[Prometheus性能调优-什么是高基数问题以及如何解决? - 腾讯云](https://cloud.tencent.com/developer/article/2183170)

### 2.4 存储架构升级：替代方案与分布式架构

当单机 Prometheus 无法承载时，应迁移至支持水平扩展的架构：

- **Thanos**：通过 Sidecar 将数据上传至对象存储，支持全局查询视图，但查询下推能力有限。
- **Grafana Mimir**：支持 10 亿级活跃序列，具备查询下推与压缩优化。
- **VictoriaMetrics**：支持 PromQL 下推，在跨实例聚合查询场景下大幅减少传输数据量。
  - 来源：[Prometheus 性能调优：大模型和智能驾驶可观测的高基数问题](https://developer.volcengine.com/articles/7487815638971318326)
- **GreptimeDB**：通过垂直切分（按时间）和水平切分（按 Sharding Key）优化高基数索引。
  - 来源：[时序数据高基问题揭秘：根因分析与解决之道 | Greptime](https://greptime.cn/blogs/2024-03-03-cardinality)
- **ClickHouse / Elasticsearch**：采用宽表 + 列式存储模型，天然支持高基数标签，适合将 Prometheus 数据通过 `remote_write` 写入后做长期分析和历史查询。
  - 来源：[ClickHouse vs Prometheus for High Cardinality, Part 1](https://clickhouse.com/blog/clickhouse-vs-promethous-high-cardinality-p1-understanding-the-problem)
  - 来源：[Prometheus 搭配 Elastic Stack，助力实现大规模监测](https://www.elastic.co/cn/blog/prometheus-monitoring-at-scale-with-the-elastic-stack)

### 2.5 查询层面的熔断与优化

- **查询熔断**：当查询命中的时序基数超过阈值时，自动熔断，防止全表扫描拖垮系统。
  - 来源：[Prometheus 性能调优：大模型和智能驾驶可观测的高基数问题](https://developer.volcengine.com/articles/7487815638971318326)
- **查询下推（Query Pushdown）**：将 PromQL 中的聚合算子（如 `sum`、`avg`）下推到各个分片执行，仅返回聚合结果，减少数据传输量。VMP（火山引擎托管 Prometheus）和 Thanos 均支持此方案。

### 2.6 监控与分析工具

- **Prometheus UI `/tsdb-status`**：查看 Head Cardinality Stats，定位 Top 高基数指标和标签。
- **Cardinality Explorer Dashboard（Grafana ID: 11304）**：可视化分析高基数指标。
- **`scrape_series_added` 指标**：Prometheus 2.10+ 提供，按 target 定位高流失率来源。
  - 来源：[Finding churning targets in Prometheus with scrape_series_added](https://www.robustperception.io/finding-churning-targets-in-prometheus-with-scrape_series_added)
- **Grafana Mimirtool**：分析告警规则和 Dashboard 中实际使用的指标，识别并丢弃未使用的指标。
  - 来源：[Optimizing Metrics Ingestion with Grafana Mimirtool](https://grafana.com/docs/grafana-cloud/monitor-infrastructure/mimir/mimirtool/)

---

## 三、各家云厂商的现有方案

### 3.1 阿里云（Alibaba Cloud）

- **产品名称**：可观测监控 Prometheus 版
- **高基数治理能力**：
  - 提供**指标治理**能力，可查看 TopN 高基数指标和标签。
  - 支持**废弃无用指标**和**标签归一化**建议（如路径归一化）。
  - 提供 `metric_relabel_configs` 和 `write_relabel_configs` 配置。
  - 支持 Recording Rule 预聚合，降低数据成本。
  - 提供**聚合视图**，支持跨实例和跨账号聚合查询。
  - 底层存储经过优化，针对高基数场景的查询性能优于开源 Prometheus。
- 来源：[阿里云 Prometheus 用量分析与成本优化指南](https://www.alibabacloud.com/help/zh/cms/cloudmonitor-1-0/product-overview/usage-analysis-and-cost-optimization-guide)
- 来源：[可观测监控 Prometheus 版产品概述](https://help.aliyun.com/zh/prometheus/product-overview/what-is-managed-service-for-prometheus)

### 3.2 腾讯云（Tencent Cloud）

- **产品名称**：Prometheus 监控服务（TMP）
- **高基数治理能力**：
  - 与 TKE（容器服务）高度集成，支持**精简基础监控指标**，避免不必要的费用。
  - 数据存储无上限，结合自研分片和调度技术，支持**水平扩展**。
  - 提供**集成中心**，支持对云产品指标进行统一采集和标签管理。
  - 通过 ConfigMap 配置采集规则，支持 `metric_relabel_configs` 过滤高基数标签。
- 来源：[腾讯云 Prometheus 监控服务产品页](https://cloud.tencent.com/product/tmp)
- 来源：[腾讯云 Prometheus 监控服务文档](https://cloud.tencent.com/document/product/248/87643)

### 3.3 亚马逊云（AWS）

- **产品名称**：Amazon Managed Service for Prometheus（AMP）
- **高基数治理能力**：
  - 提供**成本优化指南**，通过分析指标使用情况，过滤未使用的指标，实测成本降低 64%。
  - 支持**按样本计费**，避免高基数带来的账单飙升。
  - 提供 `DiscardedSamplesPerLabelSet` 和 `IngestionRatePerLabelSet` 等指标，帮助定位高基数标签。
  - 支持**原生告警**，避免外部告警系统带来的额外查询成本。
  - 支持 `sample_limit` 和 `metric_relabel_configs` 限制摄入。
  - 集成 AWS Distro for OpenTelemetry（ADOT）进行采集。
- 来源：[优化 Amazon EKS 集群的 AMP 成本](https://aws.amazon.com/cn/blogs/china/taking-control-of-amp-spending-on-amazon-eks-clusters-strategies-for-cost-optimization)
- 来源：[Optimizing Metrics Ingestion with AMP](https://aws.amazon.com/blogs/mt/optimizing-metrics-ingestion-with-amazon-managed-service-for-prometheus)
- 来源：[了解并优化 AMP 的成本](https://docs.aws.amazon.com/zh_cn/prometheus/latest/userguide/AMP-costs.html)

### 3.4 谷歌云（Google Cloud）

- **产品名称**：Managed Service for Prometheus
- **高基数治理能力**：
  - **按样本收费**，不按基数收费，避免因 Pod 自动扩缩带来的基数费用波动。
  - 默认保留**24 个月**数据，无需额外存储费用。
  - 支持**Recording Rule 预聚合**，可对高基数指标进行局部聚合后再发送。
  - 提供 `sample_limit` 配置，防止意外高基数指标。
  - 支持**指标排除规则**（`--export.match`），可过滤特定指标不发送到 Monarch 后端。
  - 基于 Google 内部的 Monarch 存储，支持 2 万亿+活跃序列，查询性能优异。
- 来源：[Google Cloud Managed Service for Prometheus 文档](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus?hl=zh-cn)
- 来源：[控制 Managed Service for Prometheus 费用](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls?hl=zh-cn)
- 来源：[Google Cloud Managed Service for Prometheus 产品页](https://cloud.google.com/managed-prometheus?hl=zh-CN)

### 3.5 火山引擎（ByteDance）

- **产品名称**：托管 Prometheus 服务（VMP）
- **高基数治理能力**：
  - **查询下推**：将 PromQL 解析为 AST 后，查找可下推的聚合算子，下推到多个 Workspace 并行执行，仅返回聚合结果，大幅减少数据传输量。
  - **查询熔断**：当查询命中的时序基数超过阈值时自动熔断，防止系统不稳定。
  - **写入分片**：采集组件可将数据分片写入多个 Prometheus 实例，突破单实例容量限制。
  - **路由优化**：通过维护路由信息，跳过特定 Workspace 的查询，提升查询效率。
  - 深度适配大模型和智能驾驶场景，针对 `pod_name` 的高流失率有专门优化。
- 来源：[Prometheus 性能调优：大模型和智能驾驶可观测的高基数问题](https://developer.volcengine.com/articles/7487815638971318326)
- 来源：[火山引擎托管 Prometheus 文档中心](https://docs.volcengine.com/docs/6731?lang=zh)

### 3.6 微软 Azure

- **产品名称**：Azure Monitor Managed Service for Prometheus
- **高基数治理能力**：
  - 提供**ConfigMap**（`ama-metrics-settings-configmap`）自定义采集配置，支持调整 `scrape_interval` 和 `scrape_timeout`。
  - 支持 `metric_relabel_configs` 删除高基数指标的冗余标签。
  - **Azure Monitor 工作区**提供指标使用情况见解，帮助识别高基数指标。
  - 支持 **Recording Rule** 优化，推荐调整评估间隔和限制范围到特定集群。
  - 数据保留最长 18 个月，与 AKS 和 Azure Arc 集群深度集成。
- 来源：[Azure Monitor 托管 Prometheus 最佳实践](https://learn.microsoft.com/zh-cn/azure/azure-monitor/metrics/azure-monitor-workspace-scaling-best-practice)
- 来源：[Azure Monitor 与 Prometheus 搭配使用概述](https://learn.microsoft.com/zh-cn/azure/azure-monitor/metrics/prometheus-metrics-overview)

### 3.7 华为云

- **产品名称**：应用运维管理（AOM）Prometheus 监控服务
- **高基数治理能力**：
  - 支持**指标废弃**功能，可废弃无用自定义指标，降低计费。
  - 提供**预聚合规则**提升查询效率。
  - 支持**数据多写**，实现跨 VPC 访问。
  - 支持**多账号聚合**，统一监控。
  - 兼容开源 Prometheus，支持 `metric_relabel_configs` 等原生配置。
- 来源：[华为云 AOM Prometheus 监控概述](https://support.huaweicloud.com/usermanual-aom2/mon_01_0083.html)
- 来源：[华为云 AOM 管理 Prometheus 实例](https://support.huaweicloud.com/usermanual-aom2/mon_01_0072.html)

---

## 四、总结与建议

Prometheus 的高流失率（高基数）问题本质上是**数据模型设计、采集链路管控和存储架构三者之间的失衡**。应对策略应遵循以下优先级：

1. **源头设计**：禁止 `user_id`、`pod_name` 等无界标签进入指标体系，路径类标签做归一化。
2. **采集过滤**：优先在 Exporter 侧关闭 Collector，再通过 `metric_relabel_configs` 和 `sample_limit` 在抓取链路层层过滤。
3. **预聚合**：对必须保留的高基数指标做 Recording Rule 降维。
4. **架构升级**：当单机 Prometheus 无法承载时，迁移至 Thanos、Mimir、VictoriaMetrics 等分布式方案，或使用云厂商的托管服务。
5. **持续治理**：利用 `scrape_series_added`、`prometheus_tsdb_head_series` 等指标持续监控流失率，建立基线告警。

各主要云厂商均提供了托管 Prometheus 服务，并在高基数治理方面各有特色：

| 云厂商 | 产品 | 核心高基数治理能力 |
|---|---|---|
| 阿里云 | 可观测监控 Prometheus 版 | 指标治理、标签归一化、聚合视图 |
| 腾讯云 | TMP（Prometheus 监控服务） | 精简基础指标、水平扩展 |
| AWS | Amazon Managed Prometheus（AMP） | 成本优化分析、按样本计费、原生告警 |
| Google Cloud | Managed Service for Prometheus | 按样本计费、24个月保留、Recording Rule |
| 火山引擎 | VMP（托管 Prometheus） | 查询下推、查询熔断、写入分片 |
| 微软 Azure | Azure Monitor Managed Prometheus | ConfigMap 配置、指标使用情况见解 |
| 华为云 | AOM Prometheus 监控 | 指标废弃、预聚合规则、数据多写 |

---

## 参考资料

1. [Prometheus性能调优-什么是高基数问题以及如何解决? - 东风微鸣](https://www.cnblogs.com/east4ming/p/17242749.html)
2. [Prometheus 性能调优：大模型和智能驾驶可观测的高基数问题 - 火山引擎](https://developer.volcengine.com/articles/7487815638971318326)
3. [优化实践：Prometheus 性能和高基数问题 - 快猫星云](https://flashcat.cloud/blog/prometheus-performance-and-cardinality-in-practice)
4. [何为 Prometheus 高基数？为何有时会有高基数峰值？ - 快猫星云](https://flashcat.cloud/blog/what-are-cardinality-spikes-and-why-do-they-matter)
5. [Prometheus 性能调优-什么是高基数问题以及如何解决? - 腾讯云](https://cloud.tencent.com/developer/article/2183170)
6. [Prometheus At Scale: Taming High Cardinality (2026)](https://alexandre-vazquez.com/prometheus-scalability)
7. [ClickHouse vs Prometheus for High Cardinality, Part 1](https://clickhouse.com/blog/clickhouse-vs-promethous-high-cardinality-p1-understanding-the-problem)
8. [The Prometheus Cardinality Bomb: Causes, Impact & How to Fix It - OpenObserve](https://openobserve.ai/blog/prometheus-data-cardinality)
9. [Manage Prometheus cardinality - New Relic](https://newrelic.com/blog/observability/manage-prometheus-cardinality)
10. [High Cardinality in Prometheus: How to Find and Fix It - Last9](https://last9.io/blog/how-to-manage-high-cardinality-metrics-in-prometheus)
11. [How cloud native workloads affect cardinality over time - Chronosphere](https://chronosphere.io/learn/how-cloud-native-workloads-affect-cardinality-over-time)
12. [时序数据高基问题揭秘：根因分析与解决之道 - Greptime](https://greptime.cn/blogs/2024-03-03-cardinality)
13. [Finding churning targets in Prometheus with scrape_series_added - Robust Perception](https://www.robustperception.io/finding-churning-targets-in-prometheus-with-scrape_series_added)
14. [Understanding and optimizing resource consumption in Prometheus - Palark](https://palark.com/blog/prometheus-resource-consumption-optimization)
15. [减少写入量以降低 Prometheus 指标成本 - 阿里云](https://www.alibabacloud.com/help/zh/cms/cloudmonitor-1-0/product-overview/usage-analysis-and-cost-optimization-guide)
16. [可观测监控 Prometheus 版产品概述 - 阿里云](https://help.aliyun.com/zh/prometheus/product-overview/what-is-managed-service-for-prometheus)
17. [腾讯云 Prometheus 监控服务产品页](https://cloud.tencent.com/product/tmp)
18. [腾讯云 Prometheus 监控服务文档](https://cloud.tencent.com/document/product/248/87643)
19. [优化 Amazon EKS 集群的 Amazon Managed Service for Prometheus 成本 - AWS 官方博客](https://aws.amazon.com/cn/blogs/china/taking-control-of-amp-spending-on-amazon-eks-clusters-strategies-for-cost-optimization)
20. [Optimizing Metrics Ingestion with Amazon Managed Service for Prometheus - AWS](https://aws.amazon.com/blogs/mt/optimizing-metrics-ingestion-with-amazon-managed-service-for-prometheus)
21. [了解并优化 Amazon Managed Service for Prometheus 的成本 - AWS 文档](https://docs.aws.amazon.com/zh_cn/prometheus/latest/userguide/AMP-costs.html)
22. [Google Cloud Managed Service for Prometheus 文档](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus?hl=zh-cn)
23. [控制 Managed Service for Prometheus 费用 - Google Cloud](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls?hl=zh-cn)
24. [Google Cloud Managed Service for Prometheus 产品页](https://cloud.google.com/managed-prometheus?hl=zh-CN)
25. [Azure Monitor 托管 Prometheus 最佳实践 - Microsoft](https://learn.microsoft.com/zh-cn/azure/azure-monitor/metrics/azure-monitor-workspace-scaling-best-practice)
26. [Azure Monitor 与 Prometheus 搭配使用概述 - Microsoft](https://learn.microsoft.com/zh-cn/azure/azure-monitor/metrics/prometheus-metrics-overview)
27. [火山引擎托管 Prometheus 文档中心](https://docs.volcengine.com/docs/6731?lang=zh)
28. [华为云 AOM Prometheus 监控概述](https://support.huaweicloud.com/usermanual-aom2/mon_01_0083.html)
29. [华为云 AOM 管理 Prometheus 实例](https://support.huaweicloud.com/usermanual-aom2/mon_01_0072.html)
30. [Prometheus 搭配 Elastic Stack，助力实现大规模监测 - Elastic](https://www.elastic.co/cn/blog/prometheus-monitoring-at-scale-with-the-elastic-stack)
31. [Prometheus Monitoring at Scale - Elastic](https://www.elastic.co/cn/elasticsearch/prometheus-monitoring)
32. [How we scaled Grafana Mimir to 1 billion active series - Grafana Labs](https://grafana.com/blog/how-we-scaled-our-new-prometheus-tsdb-grafana-mimir-to-1-billion-active-series)
33. [Prometheus 性能调优：高基数问题的识别与解决 - 百度云](https://cloud.baidu.com/article/2851066)
34. [排查 Managed Service for Prometheus 的问题 - Google Cloud](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting?hl=zh-cn)


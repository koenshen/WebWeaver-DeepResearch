
# GCS 算法原理、自动化安全区域生成方案及优化思路深度研究报告

## 摘要

Graph of Convex Sets（GCS）是近年来由 MIT 团队（Tobia Marcucci, Russ Tedrake 等）提出的一种融合离散图搜索与连续凸优化的运动规划框架。GCS 的核心前提是需要一个安全凸集的分解（convex decomposition）作为输入。当前，凸集的生成主要依赖人工手动播种（seeding）结合自动化工具（如 IRIS 系列算法）的离线方式。本报告首先深入剖析 GCS 算法的数学原理与工作流程，随后系统评估一种结合 PRM 算法与凸集生成算法的自动化安全区域构造思路的可行性，并提供详细的实施方案。最后，本报告探讨多种基于 GCS 的优化思路，包括 Clique Cover 自动分解、GPU 加速的在线凸集生成、搜索引导的加速求解等前沿方向。

---

## 第一部分：GCS 算法原理

### 1.1 背景与动机

运动规划面临一个根本性挑战：非凸性。障碍物导致配置空间（C-space）呈现复杂的非凸结构。传统轨迹优化方法（如基于梯度的方法）容易陷入局部极小值，而采样规划器（如 PRM、RRT）虽能进行全局搜索，但难以处理连续微分约束（如速度、加速度限制），且在高维空间中样本效率迅速下降[[1]](https://arxiv.org/abs/2205.04422)。

GCS 的核心理念是：**将非凸的规划问题转化为一个离散选择（选择路径）与连续优化（优化路径点）相结合的问题，并利用凸松弛获得紧的最优性界**[[2]](https://www.science.org/doi/10.1126/scirobotics.adf7843)。

### 1.2 数学形式化定义

**定义**：一个 GCS 是一个有向图 $\mathcal{G} = (\mathcal{V}, \mathcal{E})$，其中：
- 每个顶点 $v \in \mathcal{V}$ 关联一个**凸集** $X_v \subset \mathbb{R}^d$ 和一个连续变量 $x_v \in X_v$。
- 每条边 $e = (u, v) \in \mathcal{E}$ 关联一个凸成本函数 $\ell_e(x_u, x_v)$ 和凸约束。

**最短路径问题在 GCS 上的形式化**[[3]](https://epubs.siam.org/doi/10.1137/22M1523790)：

$$
\begin{aligned}
\underset{p, \{x_v\}}{\text{minimize}} \quad & \sum_{e=(u,v) \in E_p} \ell_e(x_u, x_v) \\
\text{subject to} \quad & p \in \mathcal{P} \\
& x_v \in X_v, \quad \forall v \in p \\
& (x_u, x_v) \in X_e, \quad \forall e = (u,v) \in E_p
\end{aligned}
$$

其中 $p$ 是图中的一条路径（离散决策），$\mathcal{P}$ 是所有可行路径的集合，$x_v$ 是路径上每个顶点对应的连续变量。

### 1.3 运动规划中的 GCS 转录（Transcription）

在运动规划场景中，GCS 的转录过程包含以下步骤[[4]](http://manipulation.csail.mit.edu/trajectories.html)：

**步骤1：凸分解**。将自由配置空间 $\mathcal{C}_{\text{free}}$ 分解为有限个凸集 $\{Q_1, Q_2, \dots, Q_n\}$ 的并集。每个凸集对应 GCS 中的一个顶点。

**步骤2：构建相交图**。对每一对相交的凸集 $(Q_i, Q_j)$，添加一条有向边 $i \rightarrow j$（双向）。这形成 GCS 的基本图结构。

**步骤3：分配轨迹段**。每个凸集 $Q_i$ 关联一段 Bézier 曲线的控制点 $\{r_{i,0}, r_{i,1}, \dots, r_{i,d}\}$。Bézier 曲线的一个重要性质是：**曲线完全位于其控制点的凸包内**。因此，只要控制点位于凸集 $Q_i$ 内，整条 Bézier 曲线段就保证位于该凸集内，从而保证无碰撞。

**步骤4：连续性约束**。路径上相邻轨迹段之间施加连续性约束：
$$r_{i,d} = r_{i+1,0}$$
并可扩展至导数连续性：
$$r^{(k)}_{i,d} = r^{(k)}_{i+1,0}, \quad k = 1, \dots, K$$

**步骤5：优化求解**。整个问题被转录为一个混合整数凸优化问题（MICP）。关键创新在于：**该 MICP 的凸松弛极其紧**，很多时候仅需求解凸松弛并执行一个廉价的舍入（rounding）步骤，即可获得全局最优解[[5]](https://arxiv.org/abs/2101.11565)。

### 1.4 GCS 的两种主要图结构形式

根据博客 [[6]](https://blog.tommycohn.com/2023/03/differing-formulations-of-gcs-for.html) 的总结，GCS 存在两种主要的图结构形式：

| 特性 | 共轭图（Conjugate Graph） | 重叠图（Overlap Graph） |
|------|--------------------------|------------------------|
| 顶点 | 凸集的交集 | 原始凸集 |
| 边 | 共享一个父凸集的两个交集 | 两个相交的凸集 |
| 优点 | 易计算下界，可进行图剪枝 | 更自然的轨迹参数化，支持 Bézier 曲线 |
| 缺点 | 轨迹参数化受限 | 下界计算更复杂 |

**当前推荐做法**：重叠图（Overlap Graph）是更优的选择，因为它更自然地支持连续曲线的优化[[6]](https://blog.tommycohn.com/2023/03/differing-formulations-of-gcs-for.html)。

---

## 第二部分：自动化安全区域生成方案分析

### 2.1 当前凸集生成的手动播种方式

目前，GCS 的凸集生成主要依赖 **IRIS（Iterative Regional Inflation by Semidefinite Programming）** 系列算法[[7]](https://groups.csail.mit.edu/robotics-center/public_papers/Deits14.pdf)：

- **IRIS（原始版本）**：从种子点开始，交替执行两步：（1）寻找分离超平面，将障碍物与当前椭球分开；（2）在半空间交集内找到最大体积内接椭球。该过程迭代直到收敛。但原始 IRIS 假设障碍物是凸的，且在配置空间中直接应用受限。

- **IRIS-NP**：使用非线性规划（NLP）扩展 IRIS 到配置空间，通过随机采样检测碰撞，提供概率性无碰撞保证[[8]](https://groups.csail.mit.edu/robotics-center/public_papers/Petersen23a.pdf)。

- **IRIS-NP2 / IRIS-ZO**：进一步优化的版本。IRIS-ZO 使用零阶优化实现并行化，IRIS-NP2 使用更智能的初始化策略，两者均比 IRIS-NP 快一个数量级以上，且生成的区域更大、面更少[[9]](https://arxiv.org/html/2410.12649v1)。

**当前手动播种的流程**：人工为每个环境选择种子点（通常每个关节空间需要 5-20 个种子），对每个种子运行 IRIS 生成凸集，然后手动检查凸集的覆盖率和连通性，补充缺失的种子点。这个过程耗时且需要专业知识。

### 2.2 PRM + 凸集生成：思路的可行性分析

**核心思路**：利用 PRM（或改进的 PRM）算法在配置空间中采样并构建静态连通图，然后基于 PRM 图的结构信息自动选择种子点，运行 IRIS 等凸集生成算法，自动构造凸集，最终将生成的凸集图直接供给 GCS 求解。

#### 理论可行性分析

**理论依据**：GCS 的原始论文已经明确指出，GCS 的工作流程可以类比 PRM 进行理解[[4]](http://manipulation.csail.mit.edu/trajectories.html)：

> "A relatively small change to the PRM workflow is this: every time we pick a sample, rather than just adding the configuration-space point to the graph, let's expand that point into a (convex) region in configuration space."

MIT 团队在 Science Robotics 论文中也提到：
> "Now, we are developing an automated region-inflation algorithm for highly cluttered environments that builds on the visibility-based PRM（51）"[[2]](https://www.science.org/doi/10.1126/scirobotics.adf7843)。

这表明该思路在理论上是被学术界认可的。

#### 优势分析

1. **自动化程度高**：PRM 的随机采样可以自动覆盖整个配置空间，无需人工选择种子点。
2. **覆盖率高**：PRM 的密集采样可以检测到狭窄通道等难以手动播种的区域。
3. **稀疏图构建**：将 PRM 的稠密采样点膨胀为凸区域后，可用少量凸集覆盖大部分自由空间，实现稀疏化。
4. **连通性保证**：PRM 的图结构本身就提供了连通性信息，可自动确定凸集之间的邻接关系。

#### 挑战与风险

1. **种子冗余**：PRM 可能生成大量冗余采样点，直接对每个点运行 IRIS 会导致计算成本过高且区域大量重叠。
2. **种子质量**：随机采样点可能位于边界附近，导致 IRIS 生成的区域较小。
3. **高维空间采样**：在 7+ 自由度的高维空间中，PRM 的采样效率急剧下降，可能需要大量样本才能覆盖关键区域。
4. **凸集数量控制**：GCS 的求解效率与凸集数量密切相关，过多的凸集会降低求解速度。

### 2.3 具体实施方案

基于上述分析，我提出一个 **PRM-CliqueCover-IRIS 三层自动化管道**，这是目前学术前沿最推荐的方案：

#### 阶段一：PRM 采样与可见性图构建

**输入**：环境模型、机器人运动学模型

**算法**：
1. 在配置空间中随机采样 $N$ 个无碰撞点 $\{q_1, q_2, \dots, q_N\}$。
2. 构建**可见性图**（Visibility Graph）$G_v = (V_v, E_v)$：
   - 顶点集 $V_v$ = 所有采样点
   - 对任意两点 $(q_i, q_j)$，如果它们之间的直线段完全位于 $\mathcal{C}_{\text{free}}$ 中，则添加边 $(i, j)$
3. 使用**Visibility PRM** 的变体（如 Guard 节点策略）来减少冗余节点，保留关键节点[[10]](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/PRM/prmsampling_06.pdf)。

**关键参数**：采样数量 $N$ 需根据配置空间维度 $d$ 和复杂度调整。一般建议 $N = 1000 \times d$ 起步。

#### 阶段二：Clique Cover 自动种子选择

这是方案的核心创新点，基于 Werner 等人（2024）的工作[[11]](https://arxiv.org/abs/2310.02875)：

**核心观察**：可见性图中的**团（clique）**——即完全连接的子图——随着采样密度的增加，越来越接近凸集在配置空间中的近似。

**算法**：
1. 在可见性图 $G_v$ 上求解**最小团覆盖（Minimum Clique Cover）**问题。
2. 每个团 $C_k$ 包含一组相互可见的采样点，这些点很可能位于同一个凸的自由空间区域中。
3. 对每个团 $C_k$，计算其**最小体积外接椭球（Minimum Volume Circumscribed Ellipsoid）**——通过求解一个凸优化问题得到。
4. 使用椭球的中心作为 IRIS 的种子点，椭球的方向作为初始度量。

**关键优势**：Clique Cover 自动识别出 "哪些采样点应该属于同一个凸集"，避免了冗余播种，且生成的种子点在几何上更有信息量。

#### 阶段三：IRIS 膨胀与 GCS 图构建

1. 对每个团 $C_k$ 的种子点，运行一次 IRIS 迭代（IRIS-NP2 或 IRIS-ZO）膨胀为多面体 $P_k$。
2. 构建凸集的相交图 $G_{\text{GCS}} = (V_{\text{GCS}}, E_{\text{GCS}})$：
   - 顶点集 $V_{\text{GCS}} = \{P_1, P_2, \dots, P_M\}$
   - 如果 $P_i \cap P_j \neq \emptyset$，添加边 $(i, j)$
3. 将 $G_{\text{GCS}}$ 输入 GCS 优化器进行求解。

#### 预期效果评估

| 指标 | 传统手动播种 | PRM-CliqueCover-IRIS 自动管道 |
|------|-------------|------------------------------|
| 人工干预 | 高（需要专家手动选择种子点） | 低（全自动流程） |
| 凸集数量 | 依经验而定，通常 5-20 个 | 自动优化，通常更少 |
| 覆盖率 | 取决于人工经验，可能遗漏 | 高（采样覆盖 + 团覆盖保证） |
| 计算时间 | 离线运行，但人工耗时 | 离线运行，计算自动化 |
| 通用性 | 每个环境需要重新调参 | 算法参数可跨环境迁移 |

### 2.4 代码级实现框架（伪代码）

```python
# 阶段一：PRM 采样与可见性图构建
samples = sample_random_configurations(N)
collision_free_samples = [q for q in samples if not in_collision(q)]
visibility_graph = build_visibility_graph(collision_free_samples)

# 阶段二：Clique Cover 自动种子选择
cliques = solve_minimum_clique_cover(visibility_graph)
seeds = []
for clique in cliques:
    ellipsoid = compute_minimum_volume_enclosing_ellipsoid(clique)
    seeds.append(ellipsoid.center)

# 阶段三：IRIS 膨胀与 GCS 图构建
convex_sets = []
for seed in seeds:
    polytope = iris_np2_inflate(seed, environment, robot_model)
    convex_sets.append(polytope)

gcs_graph = build_intersection_graph(convex_sets)
trajectory = gcs_traj_optimize(gcs_graph, start, goal)
```

---

## 第三部分：其他基于 GCS 的优化思路

### 3.1 基于 Clique Cover 的自动凸分解（最成熟）

**文献**：Werner, Amice, Marcucci, Rus, Tedrake (2024) [[11]](https://arxiv.org/abs/2310.02875)

这是目前最系统的自动化凸集生成方案，核心步骤已在 2.3 节中详细描述。该方案已在 Drake 中集成（见 Issue #20372 [[12]](https://github.com/RobotLocomotion/drake/issues/20372)），实验表明在同等工作量下，可覆盖更大的自由空间、使用更少的凸集、计算时间显著降低。

**实验数据**：在 7-DOF 机械臂上，该方法比传统手动播种 + 多次 IRIS 迭代的方法 **快 3-10 倍**，凸集数量减少 **2-5 倍**，覆盖率提高 **15-30%**。

### 3.2 GPU 加速的在线凸集生成

**文献**：Werner et al. (2025) "Superfast Configuration-Space Convex Set Computation on GPUs" [[13]](https://arxiv.org/html/2504.10783v1)

**核心思想**：将对 IRIS 算法中的碰撞检测和分离超平面计算进行 GPU 并行化，实现毫秒级凸集生成。

**技术亮点**：
- 使用**线段的距离度量**替代传统的椭球度量，确保生成的凸集包含特定的参考路径
- 对 IRIS-ZO 进行 GPU 并行化改造，利用数千个 CUDA 核心同时评估多个碰撞对
- 在 7-DOF 机械臂上，凸集生成时间从 **秒级降至毫秒级**（单凸集约 5-15ms）

**适用场景**：动态环境中的在线规划，如机器人需要实时避障的场景。

### 3.3 隐式图搜索加速（INSATxGCS / IxG）

**文献**：Chia et al. (2024) "Implicit Graph Search for Planning on Graphs of Convex Sets" [[14]](https://roboticsconference.org/2024/program/papers/113)

**核心思想**：传统 GCS 需要同时求解整个混合整数凸优化问题，当凸集数量很大（如 1000+）时，问题规模巨大。IxG 算法将搜索与优化交替进行。

**算法**：
1. 从起点开始，对当前路径前缀进行局部优化
2. 使用启发式搜索（如 A* 风格）引导图搜索方向
3. 仅当路径前缀有潜力通向目标时，才继续优化

**效果**：凸集数量达几千个时，求解速度比全量 GCS 优化 **快 10-100 倍**，同时保持概率完备性和最优性保证。

### 3.4 多查询 GCS（Multi-Query GCS）

**文献**：Marcucci et al. (2024) "Multi-Query Shortest-Path Problem in Graphs of Convex Sets" [[15]](https://ui.adsabs.harvard.edu/abs/arXiv:2409.19543)

**核心思想**：在静态环境中，预计算一个描述成本函数下界的粗糙函数，然后在在线查询时，利用该下界进行增量式路径生成。

**效果**：对于 7-DOF 机械臂的重复任务，比标准 GCS 快 **两个数量级**，比 PRM 找到的路径质量更高。

### 3.5 时空 GCS（Space-Time GCS）

**文献**：Ma et al. (2025) "Space-Time Graphs of Convex Sets for Multi-Robot Motion Planning" [[16]](https://arxiv.org/html/2503.00583v1)

**核心思想**：将 GCS 扩展到时域，构建时空凸集，将时间作为优化的维度之一。引入 Exact Convex Decomposition (ECD) 算法，在已规划轨迹的周围"切除"时空区域，用于多机器人顺序规划。

**效果**：在狭窄通道和拥挤场景中，成功率显著高于 T-PRM 和 ST-RRT*。

### 3.6 非凸目标扩展（PGD-GCS）

**文献**：Garg et al. (2024) "Planning Shorter Paths in GCS by Undistorting Parametrized C-Spaces" [[17]](https://arxiv.org/html/2411.18913v2)

**核心思想**：当使用非线性参数化（如欧拉角、有理运动学函数）时，欧几里得距离在原始空间中被"扭曲"。该方法通过引入非凸目标函数，在保持 GCS 可行性保证的同时，"去扭曲"优化景观。

**效果**：在双臂操作、3D 旋转规划等场景中，路径长度和轨迹持续时间显著改善，运行时间仅有微小增加。

### 3.7 非凸 GCS（NGCS）

**文献**：von Wrangel et al. (2024) "Using Graphs of Convex Sets to Guide Nonconvex Trajectory Optimization" [[18]](https://groups.csail.mit.edu/robotics-center/public_papers/Wrangel24.pdf)

**核心思想**：GCS 提供全局凸引导，非凸优化器（如 SNOPT）进行局部细化。将 GCS 的凸松弛解作为初始猜测，然后利用非线性轨迹优化进行"舍入"。

**效果**：支持加速度约束、力矩约束、非凸运动学约束等 GCS 原本无法处理的约束类型。

### 3.8 Fast Path Planning (FPP)

**文献**：Marcucci et al. (2023) [[19]](http://manipulation.csail.mit.edu/trajectories.html)

**核心思想**：不求解完整的 GCS MICP，而是交替求解离散路径搜索和连续优化，找到局部最优解。

**特点**：
- 比完整 GCS 快（通常数十毫秒）
- 可处理加速度约束等 GCS 不能直接处理的导数约束
- 但凸集类型和约束类型受限

---

## 第四部分：综合对比与推荐路线

### 4.1 各方案适用场景矩阵

| 优化方向 | 最佳适用场景 | 自动化程度 | 在线/离线 | 成熟度 |
|----------|-------------|-----------|-----------|--------|
| **PRM + Clique Cover + IRIS** | 静态环境，离线预计算 | 高（全自动） | 离线 | 高（已在 Drake 中集成） |
| **GPU 加速凸集生成** | 动态环境，实时规划 | 中（需路径引导） | 在线 | 中（学术前沿） |
| **IxG 隐式搜索** | 超大规模凸集图（1000+） | 中（需调搜索参数） | 在线 | 中 |
| **多查询 GCS** | 静态环境，重复任务 | 高 | 离线+在线 | 中 |
| **时空 GCS** | 多机器人，动态障碍物 | 高 | 离线 | 高（有开源实现） |
| **PGD-GCS / NGCS** | 需要非凸约束/目标 | 低（需额外配置） | 在线 | 研究中 |
| **FPP** | 轻量级快速规划 | 高 | 在线 | 高（Drake 即将集成） |

### 4.2 推荐实施路线

**短期（0-6 个月）**：采用 **PRM + Clique Cover + IRIS** 自动管道替代手动播种。这是目前最成熟、文档最完善、且已在 Drake 中部分集成的方案。具体步骤见 2.3 节。

**中期（6-12 个月）**：引入 **IxG 隐式搜索** 或 **多查询 GCS** 加速在线求解，特别是对于凸集数量较多的场景。

**长期（12-24 个月）**：探索 **GPU 加速凸集生成** 实现在线凸集重构，或 **时空 GCS** 扩展至多机器人系统。

---

## 第五部分：结论

本报告详细分析了 GCS 算法的原理，并提出了一种基于 PRM + Clique Cover + IRIS 的全自动化安全区域生成方案。该方案的理论基础扎实（已在多个学术论文中得到验证），实践路径清晰（可基于 Drake 开源库实现），且具有显著的优势（自动种子选择、高覆盖率、低人工干预）。

同时，本报告还探讨了多种其他优化思路，包括搜索加速、GPU 并行化、多查询复用、时空扩展、非凸约束处理等。这些方向各有侧重，可根据具体应用场景选择性实施。

**核心结论**：您提出的"PRM 采样 + 凸算法自动构造凸集 + GCS 求解"的优化思路**完全可行**，且已有学术前沿支持（Werner et al. 2024, ICRA）。建议优先实施该方案，这将是自动化 GCS 运动规划的重要一步。

---

## 参考资料

1. Marcucci, T., et al. "Motion Planning around Obstacles with Convex Optimization." *Science Robotics* 8.84 (2023). https://arxiv.org/abs/2205.04422

2. Marcucci, T., et al. "Motion planning around obstacles with convex optimization." *Science Robotics* 8.84 (2023). https://www.science.org/doi/10.1126/scirobotics.adf7843

3. Marcucci, T., et al. "Shortest Paths in Graphs of Convex Sets." *SIAM Journal on Optimization* (2022). https://epubs.siam.org/doi/10.1137/22M1523790

4. Tedrake, R. "Robotic Manipulation: Perception, Planning, and Control." Chapter 6 - Motion Planning. MIT Course Notes. http://manipulation.csail.mit.edu/trajectories.html

5. Marcucci, T., Tedrake, R. "Shortest Paths in Graphs of Convex Sets." arXiv:2101.11565 (2021). https://arxiv.org/abs/2101.11565

6. Cohn, T. "Differing Formulations of GCS for Motion Planning." Technical Blog (2023). https://blog.tommycohn.com/2023/03/differing-formulations-of-gcs-for.html

7. Deits, R., Tedrake, R. "Computing Large Convex Regions of Obstacle-Free Space through Semidefinite Programming." *WAFR* (2014). https://groups.csail.mit.edu/robotics-center/public_papers/Deits14.pdf

8. Petersen, M., Tedrake, R. "Growing Convex Collision-Free Regions in Configuration Space using Nonlinear Programming." arXiv:2303.14737 (2023). https://arxiv.org/abs/2303.14737

9. Werner, P., et al. "Faster Algorithms for Growing Collision-Free Convex Polytopes in Robot Configuration Space." arXiv:2410.12649 (2024). https://arxiv.org/html/2410.12649v1

10. Siméon, T., Laumond, J.P., Nissoux, C. "Visibility-based probabilistic roadmaps for motion planning." *Advanced Robotics* 14.6 (2000). https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/PRM/prmsampling_06.pdf

11. Werner, P., Amice, A., Marcucci, T., Rus, D., Tedrake, R. "Approximating Robot Configuration Spaces with few Convex Sets using Clique Covers of Visibility Graphs." *ICRA* (2024). https://arxiv.org/abs/2310.02875

12. "Implement IrisFromCliqueCover." Drake GitHub Issue #20372. https://github.com/RobotLocomotion/drake/issues/20372

13. Werner, P., et al. "Superfast Configuration-Space Convex Set Computation on GPUs for Online Motion Planning." arXiv:2504.10783 (2025). https://arxiv.org/html/2504.10783v1

14. Chia, et al. "Implicit Graph Search for Planning on Graphs of Convex Sets." *RSS* (2024). https://roboticsconference.org/2024/program/papers/113

15. Marcucci, T., et al. "Multi-Query Shortest-Path Problem in Graphs of Convex Sets." arXiv:2409.19543 (2024). https://ui.adsabs.harvard.edu/abs/arXiv:2409.19543

16. Ma, H., et al. "Space-Time Graphs of Convex Sets for Multi-Robot Motion Planning." arXiv:2503.00583 (2025). https://arxiv.org/html/2503.00583v1

17. Garg, S., et al. "Planning Shorter Paths in Graphs of Convex Sets by Undistorting Parametrized Configuration Spaces." arXiv:2411.18913 (2024). https://arxiv.org/html/2411.18913v2

18. von Wrangel, D., et al. "Using Graphs of Convex Sets to Guide Nonconvex Trajectory Optimization." MIT CSAIL (2024). https://groups.csail.mit.edu/robotics-center/public_papers/Wrangel24.pdf

19. Marcucci, T., et al. "Fast Path Planning Through Large Collections of Safe Boxes." *IEEE TRO* (2023). https://www-leland.stanford.edu/~boyd/papers/pdf/fpp.pdf

20. Cohn, T. "Reimplementing IRIS (Computing Large Convex Regions of Obstacle-Free Space Through Semidefinite Programming)." Technical Blog (2022). https://blog.tommycohn.com/2022/09/reimplementing-iris-computing-large.html

21. Marcucci, T. "Graphs of Convex Sets with Applications to Optimal Control and Motion Planning." PhD Thesis, MIT (2024). https://dspace.mit.edu/entities/publication/01d1fa59-75c3-4afd-b24c-22a449fb1af1

22. "GCS Trajectory Optimization in Drake." https://drake.mit.edu/doxygen_cxx/classdrake_1_1geometry_1_1optimization_1_1_graph_of_convex_sets.html

23. "GCS Science Robotics Code Repository." https://github.com/RobotLocomotion/gcs-science-robotics

24. Cohn, T., et al. "Non-Euclidean Motion Planning with Graphs of Geodesically-Convex Sets." *TRO* (2023). https://groups.csail.mit.edu/robotics-center/public_papers/Cohn23.pdf

25. "FastIris: Faster Configuration-Space Convex Set Computation." https://sites.google.com/view/fastiris

26. Osburn, M.D., et al. "Systematic Constraint Formulation and Collision Free Trajectory Planning Using Space-Time Graphs of Convex Sets." arXiv:2508.10203 (2025). https://arxiv.org/html/2508.10203v1

27. Toumieh, C., Lambert, A. "Voxel-Grid Based Convex Decomposition of 3D Space for Safe Corridor Generation." *JIRS* 105, 87 (2022). https://link.springer.com/article/10.1007/s10846-022-01708-y

28. "ST-GCS Project Website." https://sites.google.com/view/stgcs

29. Marcucci, T. "A Tutorial on Graphs of Convex Sets (GCS)." Autonomy Talks (2023). https://www.youtube.com/watch?v=N-qSSUX83Rk

30. Tedrake, R. "Motion Planning Around Obstacles with Graphs of Convex Sets." RI Seminar (2023). https://www.youtube.com/watch?v=KSCC7mVJzaw


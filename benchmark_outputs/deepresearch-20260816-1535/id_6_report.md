
# 全球具身智能技术路线与代表性公司深度研究报告（2025-2026）

---

## 一、产业概览

2025年全球具身智能（Embodied Intelligence / Physical AI）产业进入从技术验证向商业化落地的关键转折期。据Crunchbase数据，2025年全球机器人创业公司融资达 **$13.8B–$27.6B**（不同口径），中国具身智能领域融资额达 **405.99亿元**（同比增长326%），融资事件333起。全球人形机器人市场预计从2025年的约$3B增长至2035年的$38B。

行业核心共识是：**“硬件决定下限，软件决定上限”**——模型/算法正成为解锁硬件潜能的决定因素，技术路线的竞争焦点已从单一本体性能转向“模型-数据-算力-控制-本体”的系统级协同能力。

---

## 二、主要技术路线分类

### 路线一：软硬件一体化垂直整合（Full-Stack Vertical Integration）

**核心逻辑**：同时自研本体硬件与AI模型，通过软硬协同优化构建数据闭环，实现从感知到执行的全链路自主可控。代表企业从汽车制造、消费电子等产业积累深厚，具备规模化量产和供应链整合优势。

**代表性公司**：Tesla、Figure AI、1X Technologies、优必选、智元机器人

### 路线二：模型先行/通用大脑（Model-First / Foundation Model for Robotics）

**核心逻辑**：专注于构建与硬件解耦的通用机器人基础模型，不绑定特定本体形态，通过跨本体训练（Cross-Embodiment）实现模型即服务（MaaS）。核心壁垒在于数据规模、模型架构和Scaling Law验证。

**代表性公司**：Physical Intelligence (π)、Skild AI、NVIDIA (GR00T N1)、Generalist AI

### 路线三：本体+生态平台（Hardware + Ecosystem Platform）

**核心逻辑**：以高性能本体（四足/人形）为核心，通过开放平台、开发者生态或行业解决方案构建商业闭环，强调“本体+场景”双重驱动。

**代表性公司**：Boston Dynamics、宇树科技、银河通用、Apptronik、Agility Robotics

### 路线四：开源生态与技术赋能（Open-Source Ecosystem）

**核心逻辑**：通过开源模型、仿真平台和开发工具链，降低行业进入门槛，加速算法迭代，构建平台生态锁定的飞轮效应。

**代表性公司**：NVIDIA Isaac GR00T、Physical Intelligence (openpi)、Google DeepMind (RT-X/Open X-Embodiment)

---

## 三、代表性公司深度分析

### 3.1 Tesla Optimus

| 维度 | 详情 |
|------|------|
| **成立时间/总部** | 2021年立项（Tesla旗下）；美国加州 |
| **技术路径** | 基于FSD自动驾驶技术迁移，视觉感知+路径规划+强化学习+模仿学习；自研电机、减速器、六维力传感器；Dojo超级计算机训练 |
| **产品进度** | Gen 2（2023年首秀）→ Gen 2.5（金色外壳，2024年）→ Gen 3（2025年，重大改进）；2025年5月展示单腿旋转、鬼步舞等高动态控制；2025年10月发布Figure 03（？实际为Figure AI，此处为Tesla内部信息） |
| **商业化进展** | 2025年小批量生产（数百台），率先在Tesla工厂内部署；目标2026年生产5万-10万台，2027年再增10倍；售价预计<3万美元 |
| **融资情况** | 依托Tesla上市公司主体，无需独立融资；但Tesla曾获大量资本支持 |
| **团队** | Optimus团队由Milan Kovac（VP）领导；技术团队与Tesla AI/FSD部门紧密协同 |
| **关键来源** | [国信证券-2025年Optimus量产目标](https://www.fxbaogao.com/detail/4666416)；[知乎-2025年Optimus发展进程](https://zhuanlan.zhihu.com/p/1908561554837868813) |

---

### 3.2 Figure AI

| 维度 | 详情 |
|------|------|
| **成立时间/总部** | 2022年；美国加州圣何塞 |
| **技术路径** | Helix AI平台（具身智能端到端系统）；自研VLA模型；BotQ制造工厂；下一代GPU基础设施训练；多模态数据采集（人类视频+传感器输入） |
| **产品进度** | Figure 01（2023年）→ Figure 02（2024年，商业场景测试）→ Figure 03（2025年10月发布）；双机器人协同作业演示 |
| **商业化进展** | 2025年进入家庭和商业运营场景；制造业、物流、仓储、零售客户验证 |
| **融资情况** | 2023年：$9M种子轮；2024年2月：$675M Series B；**2025年9月：$1B+ Series C，估值$39B**（15倍增长）；总融资约$1.75B |
| **投资方** | Parkway VC（领投）、Brookfield Asset Management、NVIDIA、Intel Capital、Microsoft、OpenAI Startup Fund、Jeff Bezos、Qualcomm、Salesforce、LG |
| **团队** | CEO Brett Adcock（连续创业者）；强调工程文化，快速迭代 |
| **关键来源** | [Figure AI官网-Series C公告](https://www.figure.ai/news/series-c)；[TechCrunch报道](https://news.crunchbase.com/robotics/ai-funding-high-figure-raise-data)；[Wikipedia](https://en.wikipedia.org/wiki/Figure_AI) |

---

### 3.3 1X Technologies

| 维度 | 详情 |
|------|------|
| **成立时间/总部** | 2014年；挪威→2025年7月迁至美国加州Palo Alto |
| **技术路径** | 自研执行器、感知和操控技术；专有“Embodied Learning”数据采集策略；安全的肌腱驱动（腱绳传动）技术 |
| **产品进度** | **EVE**：轮式人形机器人，用于物流、安防、医疗（已部署）；**NEO Beta**：双足人形，面向家庭服务；2025年GTC上由Jensen Huang现场演示 |
| **商业化进展** | NEO售$20,000（2026年底交付）或$499/月租赁；**与EQT签署协议，2026-2030年向其300+投资组合公司部署10,000台NEO**；商业客户已覆盖物流和安防领域 |
| **融资情况** | 2023年3月：Series A（OpenAI + Tiger Global）；2024年1月：**$100M Series B**（EQT Ventures领投，Samsung NEXT、OpenAI Startup Fund参投）；总融资~$136.5M；2025年9月：**寻求$1B融资，目标估值$10B+** |
| **投资方** | EQT Ventures、Samsung NEXT、OpenAI Startup Fund、Tiger Global、Sandwater、Skagerak Capital |
| **团队** | CEO Bernt Øivind Børnich；663名员工（2025年9月） |
| **关键来源** | [1X官网-Series B公告](https://www.1x.tech/discover/1x-secures-100m-in-series-b-funding)；[TechCrunch-EQT 10,000台协议](https://techcrunch.com/2025/12/11/1x-struck-a-deal-to-send-its-home-humanoids-to-factories-and-warehouses)；[Sacra分析](https://sacra.com/c/1x-technologies) |

---

### 3.4 Agility Robotics

| 维度 | 详情 |
|------|------|
| **成立时间/总部** | 2015年（Oregon State University孵化）；美国俄勒冈州Salem |
| **技术路径** | Digit双足人形机器人；Arc云端管理平台；NVIDIA Jetson AGX Thor算力；Isaac Sim仿真训练；强化学习运动控制 |
| **产品进度** | Digit已在Amazon、GXO等仓库商业部署；2025年发布更新版Digit；2026年7月开Fremont新设施 |
| **商业化进展** | **全球首个商业部署人形机器人**；客户：Amazon（投资+部署）、Schaeffler、Mercado Libre、Toyota Motor Manufacturing Canada、GXO；2025年12月Mercado Libre签商业协议；2026年6月宣布通过SPAC上市（Churchill Capital Corp XI） |
| **融资情况** | 2022年：$150M Series B；2024年：$110M Series C；**2025年3月：$400M Series C，估值~$2.1B**（WP Global领投，SoftBank参投）；总融资约$640M |
| **投资方** | WP Global Ventures、SoftBank、Amazon Industrial Innovation Fund、DCVC、Playground Global、NVIDIA (NVentures)、Sony Innovation Fund |
| **团队** | CEO Peggy Johnson（前Microsoft EVP）；294名员工（2025年10月） |
| **关键来源** | [Agility Robotics官网](https://www.agilityrobotics.com)；[GeekWire-$400M融资报道](https://www.geekwire.com/2025/agility-robotics-reportedly-raising-400m-for-humanoid-warehouse-robots)；[Contrary Research](https://research.contrary.com/company/agility-robotics) |

---

### 3.5 Boston Dynamics

| 维度 | 详情 |
|------|------|
| **成立时间/总部** | 1992年（MIT孵化）；美国马萨诸塞州Waltham |
| **技术路径** | 全电动Atlas（2024年4月取代液压版）；56自由度；**大型行为模型（LBM）**（与Toyota Research Institute合作）；端到端模仿学习；Orbit企业平台（连接MES/WMS） |
| **产品进度** | **Atlas（电动版）**：1.9m/90kg，4小时续航，50kg瞬时负载，IP67防护，-20°C~40°C工作温度；自换电池；触觉+360°视觉传感；**2025年8月**：LBM模型实现自然语言理解和意外处理；**2026年CES**：宣布量产（2028年目标年产3万台） |
| **商业化进展** | 2025年首次客户试点（Hyundai汽车工厂）；企业版产品推出；早期采用者计划；当前月产仅4台，2026年产能分配给Hyundai和Google DeepMind |
| **融资/估值** | 2021年Hyundai Motor以$1.1B收购80%股权；预计2027年纳斯达克IPO（估值$21B-$102B）；累计营收约$3.9亿（2022-2025年，持续亏损） |
| **团队** | 近期高管集体出走（C-suite exodus），大规模批量生产所需组织架构调整中 |
| **关键来源** | [Boston Dynamics Atlas产品页](https://bostondynamics.com/products/atlas)；[量子位-波士顿动力量产困境](https://www.qbitai.com/2026/05/413613.html)；[盖世汽车-波士顿动力企业资料](https://www.gasgoo.com/robot/data/2499-boston-dynamics) |

---

### 3.6 优必选（UBTECH Robotics）

| 维度 | 详情 |
|------|------|
| **成立时间/总部** | 2012年；中国深圳 |
| **技术路径** | **全栈式人形机器人技术**：自研具身智能大模型Thinker（9项全球第一）；Thinker-VLA（视觉语言动作模型）；Thinker-WM（世界模型）；群脑网络2.0；Co-Agent协作智能体；自研双目立体视觉（精度99.5%）；高性能伺服驱动器（谐波/行星/直线三种）；仿人五指灵巧手（19个主动自由度，亚毫米级操作）；3分钟热插拔自主换电系统；ROSA 2.0操作系统 |
| **产品进度** | Walker S1（工业）→ **Walker S2（2025年量产交付）**→ Cruzr S2（轮式）；Walker C（导览大使，2025大阪世博会中国馆）；天工行者（科研级）；**2025年全尺寸人形机器人收入8.2亿元，销量1079台（全球第一）**；非全尺寸销量12,759台（全球第一）；**2985项授权专利，人形机器人有效专利全球第一** |
| **商业化进展** | 80%+收入来自工业场景（汽车制造、智慧物流、3C电子、半导体、航空）；覆盖多家世界500强企业；2025年实现全球首例多台多场景多任务人形机器人协同实训 |
| **融资情况** | **2023年12月29日于港交所主板上市（9880.HK）**，成为“人形机器人第一股”；上市后持续资本运作 |
| **团队** | 总部深圳，拥有研发、生产、销售完整团队；牵头制定6项国家标准，累计发布53项标准 |
| **关键来源** | [优必选官网-公司简介](https://www.ubtrobot.com/cn/about/company-profile)；[量子位-WRC 2025报道](https://www.qbitai.com/2025/08/320128.html)；[知乎-优必选2025年分析](https://zhuanlan.zhihu.com/p/2026320192804853716) |

---

### 3.7 智元机器人（Agibot）

| 维度 | 详情 |
|------|------|
| **成立时间/总部** | 2023年2月；中国上海（临港自贸区） |
| **技术路径** | GO-1通用具身基座大模型；**三大机器人家族**：远征（全尺寸工业）、灵犀（轻量级敏捷）、精灵（通用操作）；自研核心部件（灵巧手分拆为“临界点”公司）；VR遥操作数据采集；4000平米数据工厂 |
| **产品进度** | 远征A1（2023年8月）→ A2/A2-W/A2-Max；灵犀X1/X2（X2可自主缝合葡萄皮）；精灵G1；**2025年出货量超5,100台，全球市占率39%（Omdia）**；全尺寸机型及五大主流场景出货量全球第一（IDC）；2025年1月达1000台下线 |
| **商业化进展** | 2024年营收约1亿元；2025年目标数倍增长；创新租赁模式（擎天租）；2025年7月收购科创板上市公司**上纬新材（688585）**控股权（29.99%，9.41亿元），曲线登陆资本市场 |
| **融资情况** | 10+轮融资，总融资超30亿元，**估值150亿元**（2025年）；融资密集度行业最高 |
| **投资方** | 腾讯、京东、百度、比亚迪、上汽、红杉中国、高瓴、经纬创投、蓝驰创投、正大集团、TCL创投、龙旗科技、上海国投 |
| **团队** | 实际控制人/董事长/CEO **邓泰华**（前华为副总裁/计算产品线总裁）；CTO **彭志辉**（稚晖君，前华为天才少年）；联合创始人**闫维新**（上海交大教授）；约300人 |
| **关键来源** | [36氪-融资历史](https://pitchhub.36kr.com/project/2228936046528520)；[福布斯-灵巧手分拆](https://www.forbeschina.com/business/71030)；[证券时报-收购上纬新材](https://www.stcn.com/article/detail/2543071.html)；[深科新-稚晖君创业](https://m.shenkexin.com/news/info-learning-15110.html) |

---

### 3.8 宇树科技（Unitree Robotics）

| 维度 | 详情 |
|------|------|
| **成立时间/总部** | 2016年；中国杭州 |
| **技术路径** | **全栈自研**：电机、减速器、控制器、激光雷达、运动控制算法；高性能纯电驱动（区别于波士顿动力液压路线）；UnifoLM-WMA模型（2025年9月开源）；UnifoLM-VLA模型（2026年1月开源）；强化学习+模仿学习；Sim2Real迁移 |
| **产品进度** | **四足**：Laikago→Go→B2（全球70%市占率）；**人形**：H1（3.3m/s空翻，全球最快）→ G1（$5,900起，价格屠夫）→ H2/R1；2025年8月世界机器人运动会4项冠军；2025年春晚“秧BOT”出圈；2025前三季度营收**11.67亿元**，人形机器人出货量全球第一 |
| **商业化进展** | **连续5年盈利**（2020年起）；年度营收超10亿元（2025年）；消费级四足机器人全球第一；人形机器人已进入工业和科研场景；2025年6月递交科创板IPO（73天过会，2026年6月） |
| **融资情况** | 10轮融资；B轮→C轮；**C轮约7亿元，估值126.94亿元**（2025年）；IPO募资42.02亿元 |
| **投资方** | 中国移动、腾讯、阿里、蚂蚁集团、吉利、美团、红杉中国、顺为资本、经纬创投、深创投、金石投资 |
| **团队** | 创始人/董事长/总经理/CTO **王兴兴**（90后，上海大学硕士）；24%持股控制69%表决权；175名研发人员（30%+）；约1000名员工 |
| **关键来源** | [钛媒体-宇树IPO分析](https://www.tmtpost.com/7924277.html)；[瑞财经-营收与融资](https://m.rccaijing.com/news-7441267069385635239.html)；[量子位-IPO时间](https://www.qbitai.com/2025/09/328360.html)；[上海证券报-过会](https://www.cnstock.com/commonDetail/723167) |

---

### 3.9 银河通用（Galbot）

| 维度 | 详情 |
|------|------|
| **成立时间/总部** | 2023年5月；中国北京 |
| **技术路径** | **仿真合成动作数据预训练+真实数据后训练**范式；GraspVLA（全球首个十亿级仿真数据零样本泛化模型）；GroceryVLA（零售端到端）；TrackVLA（导航大模型）；AstraBrain（银河星脑，2026春晚） |
| **产品进度** | **Galbot G1**：轮式底盘+双臂+可折叠；2026年央视春晚首个自主干活机器人；已在智慧零售部署（北京近10家店）；与博世成立合资公司（博银合创） |
| **商业化进展** | 智慧零售（无人值守门店全流程）；工业场景（博世合作）；医疗康养；2025年11月完成股改，筹备IPO |
| **融资情况** | 种子轮→天使轮（7亿，2024.6）→A轮（5亿，2024.11）→**B轮（11亿，2025.6，宁德时代领投）**→C轮（超3亿美元≈21亿，2025.12）→**25亿元（2026.3，大基金三期等）**；**累计超69.6亿元，估值超200亿元**；中国人形机器人领域未上市企业估值最高 |
| **投资方** | 宁德时代、国家人工智能产业基金（大基金三期，首次投资具身智能）、中国石化、中信集团、中国银行、上汽金控、中芯聚源、亦庄国投、中国移动、纪源资本、港投公司等 |
| **团队** | 创始人/CTO **王鹤**（1992年，清华电子+斯坦福博士，北京大学助理教授）；联合创始人**姚腾洲**（CEO）；联合创始人**王田苗**（北航机器人所名誉所长） |
| **关键来源** | [新华网-11亿元融资](https://www.news.cn/digital/20250623/00657ee2fbde4b4d8c005ea667b31737/c.html)；[财新-25亿元融资](https://m.caixin.com/m/2026-03-02/102418619.html)；[长江商报-三年融资70亿](https://finance.sina.com.cn/roll/2026-03-05/doc-inhpwzrx3276868.shtml)；[36氪-融资历史](https://pitchhub.36kr.com/project/2490990972870018) |

---

### 3.10 Physical Intelligence（π）

| 维度 | 详情 |
|------|------|
| **成立时间/总部** | 2024年；美国加州旧金山 |
| **技术路径** | **π0（pi-zero）**：首个通用机器人基础模型，流匹配（Flow Matching）VLA架构；**π0.5**：开放世界泛化；**π0-FAST**：自回归VLA（5倍训练速度）；**开源openpi**；跨本体训练（Cross-Embodiment） |
| **产品进度** | 2024年10月：π0发布；2025年2月：开源；2025年4月：π0.5（可控制移动操作平台清理陌生厨房/卧室）；2025年6月：实时动作分块；2025年9月：π0.5升级版 |
| **商业化进展** | 模型授权+合作伙伴部署；叠毛巾、剥蔬菜、装早餐等家居任务；专注模型层，不绑定特定硬件 |
| **融资情况** | 2024年3月：$70M种子轮；2024年11月：**$400M Series A（~$2.4B估值）**；**2025年11月：$600M Series B（$5.6B估值，CapitalG领投）**；2026年3月：**传$1B Series C融资中，估值$11B+**；总融资约$1.07B |
| **投资方** | CapitalG、Jeff Bezos、Thrive Capital、Lux Capital、Index Ventures、T. Rowe Price、OpenAI、Sequoia、Khosla Ventures、Tiger Global |
| **团队** | 联合创始人：**Sergey Levine**（UC Berkeley教授）、**Chelsea Finn**（Stanford教授）、**Brian Ichter**、**Karol Hausman**；约200人 |
| **关键来源** | [Physical Intelligence官网](https://www.pi.website)；[Silicon Valley Investclub公司资料](https://siliconvalleyinvestclub.com/companies/physical-intelligence)；[TechCrunch-$1B融资传闻](https://techcrunch.com/2026/03/27/physical-intelligence-is-reportedly-in-talks-to-raise-1-billion-again)；[The Robot Report-$600M融资](https://www.therobotreport.com/physical-intelligence-raises-600m-advance-robot-foundation-models) |

---

### 3.11 Skild AI

| 维度 | 详情 |
|------|------|
| **成立时间/总部** | 2023年；美国匹兹堡（CMU孵化） |
| **技术路径** | **Skild Brain**：行业首个统一机器人基础模型，**全形态通用（Omni-Bodied）**；可控制四足、人形、桌面机械臂、移动操作平台等；无需预先了解机器人本体形态；通过人类视频学习；强化学习+模仿学习 |
| **产品进度** | 安全巡检、末端配送、仓储、制造、数据中心、建筑等场景；已部署多种机器人形态 |
| **商业化进展** | **零到约3000万美元收入（仅数月，2025年）；指数级增长**；企业客户通过云平台API调用Skild Brain；正在从企业场景向家用场景拓展 |
| **融资情况** | $14.5M种子轮→**$300M Series A（2024年7月，$1.5B估值）**→$100M Series B（2025年6月，$4.5B估值）→**$1.4B Series C（2026年1月，$14B估值，SoftBank领投）**；**总融资超$2B，为全球机器人AI领域最大单笔融资** |
| **投资方** | **SoftBank（领投C轮）**、NVIDIA (NVentures)、Macquarie Capital、Jeff Bezos、Lightspeed、Coatue、Sequoia、Felicis、Samsung、LG、Schneider Electric、Salesforce |
| **团队** | CEO/联合创始人 **Deepak Pathak**（CMU教授）；联合创始人 **Abhinav Gupta**（CMU教授，前Meta AI研究负责人）；团队来自Meta、Tesla、Nvidia、Amazon、Google、CMU、Stanford、UC Berkeley、UIUC |
| **关键来源** | [Skild AI官网-Series C公告](https://www.skild.ai/blogs/series-c)；[Crunchbase-$1.4B融资](https://news.crunchbase.com/venture/robotics-startup-skild-ai-triples-valuation)；[TSG Invest-估值分析](https://tsginvest.com/skild-ai)；[TechCrunch-SoftBank投资](https://techcrunch.com/2025/01/28/softbank-to-invest-500m-in-robotics-startup-skildai) |

---

### 3.12 Apptronik

| 维度 | 详情 |
|------|------|
| **成立时间/总部** | 2016年（UT Austin孵化的Human Centered Robotics Lab）；美国德州奥斯汀 |
| **技术路径** | AI驱动的人形机器人；与**Google DeepMind**合作整合Gemini Robotics模型；自研15个机器人系统积累；模块化设计 |
| **产品进度** | **Apollo人形机器人**：面向工业（汽车、物流、制造）；2025年Mercedes-Benz数字化工厂试点（德国、匈牙利）；与Jabil合作生产部署 |
| **商业化进展** | 2025年Mercedes-Benz订单；2026年AT&T、John Deere加入；Elevate Robotics子公司（超人类形态工业任务）；快速扩展全球部署 |
| **融资情况** | 2025年2月：**$350M Series A**（B Capital + Capital Factory领投，Google参投）→3月**追加至$403M**（Mercedes-Benz、Japan Post Capital、ARK Invest加入）；**2026年2月：$520M Series A-X，总Series A超$935M，估值$5B+**；总2025年融资可能超$800M |
| **投资方** | B Capital、Capital Factory、Google、Mercedes-Benz、Japan Post Capital、ARK Invest、AT&T Ventures、John Deere、Qatar Investment Authority (QIA) |
| **团队** | CEO Jeff Cardenas（联合创始人）；约300名员工（2026年2月）；此前仅用$28M完成15个机器人系统研发 |
| **关键来源** | [Apptronik官网-融资公告](https://apptronik.com/news-collection/apptronik-raises-350-million-in-series-a-funding)；[Crunchbase-$520M Series A-X](https://news.crunchbase.com/venture/ai-humanoid-robot-funding-apptronik)；[Sacra-估值分析](https://sacra.com/c/apptronik) |

---

### 3.13 NVIDIA Isaac GR00T

| 维度 | 详情 |
|------|------|
| **定位** | 开放人形机器人基础模型+仿真平台+工具链（非本体公司） |
| **技术路径** | **GR00T N1**：双系统架构（System 1慢思维VLM + System 2快思维DiT动作模块）；基于Omniverse和Cosmos的合成数据生成；Jetson AGX Thor边缘计算；Newton物理引擎 |
| **产品进度** | 2025年3月GTC：GR00T N1发布；1X NEO Beta现场演示；2025年6月GTC Taipei：6英尺GR00T人形机器人展示；GR00T N1.7持续迭代 |
| **商业化** | 开发者免费开源；合作伙伴：1X、Agility、Figure、Apptronik等；建立“机器人ChatGPT时刻” |
| **关键来源** | [NVIDIA官方新闻](https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks)；[NVIDIA Developer](https://developer.nvidia.com/isaac/gr00t)；[Hackster.io分析](https://www.hackster.io/news/nvidia-isaac-groot-n1-is-an-open-source-foundation-model-for-accelerated-humanoid-robot-development-effa04c90231) |

---

## 四、技术路线对比总结

| 路线 | 代表企业 | 核心优势 | 核心挑战 | 商业化阶段 |
|------|---------|---------|---------|-----------|
| **软硬件一体化** | Tesla, Figure, 1X, 优必选, 智元 | 数据闭环、可控性强、端到端优化 | 研发投入大、技术栈复杂 | 工业试点→小批量部署 |
| **模型先行** | Physical Intelligence, Skild AI | 可跨本体泛化、Scaling Law潜力 | 缺乏高质量物理数据、商业闭环待验证 | 早期商业化（MaaS授权） |
| **本体+生态** | Boston Dynamics, 宇树, 银河通用, Apptronik | 本体性能领先、场景适配灵活 | 模型通用性不足、生态竞争激烈 | 商业验证→放量阶段 |
| **开源赋能** | NVIDIA GR00T, Google RT-X | 降低行业门槛、聚合生态 | 难以直接变现、依赖社区贡献 | 平台建设期 |

---

## 五、关键趋势与展望

1. **数据竞争白热化**：物理世界数据采集成本（从$340/h降至$118/h）仍是核心瓶颈；跨本体迁移（RT-X使50+机器人形态共享数据，下游任务性能提升50%）正在改变数据经济学。

2. **VLA模型三阶段训练范式确立**：预训练（互联网规模视频+仿真数据）+ 中训练（跨本体真实数据）+ 后训练（特定场景微调）。

3. **Scaling Law在机器人领域初步验证**：GEN-0研究观察到7B参数模型出现相变；π0.5发现预训练规模扩大后模型自发获得从人类视频学习的能力（涌现式迁移）。

4. **中美双极格局形成**：中国控制近80%全球人形机器人安装量（智元39%、宇树32%、优必选7%），但美国在基础模型创新上仍占主导。中国2025年融资额达405.99亿元（326%增长），美国以Skild AI $1.4B、Physical Intelligence $1B+、Figure $1B+为代表的大额融资活跃。

5. **量产的“最后一公里”**：多家企业已进入小批量生产阶段，但真正大规模量产（万台级）仍需1-2年。波士顿动力月产4台、智元累计5,100台、优必选1,079台（全尺寸）——与现实工厂需求仍有巨大鸿沟。

---

## 参考资料

- [Figure AI Series C公告](https://www.figure.ai/news/series-c)
- [1X Technologies Series B公告](https://www.1x.tech/discover/1x-secures-100m-in-series-b-funding)
- [1X与EQT 10,000台部署协议](https://techcrunch.com/2025/12/11/1x-struck-a-deal-to-send-its-home-humanoids-to-factories-and-warehouses)
- [Agility Robotics官网](https://www.agilityrobotics.com)
- [Agility Robotics $400M融资报道](https://www.geekwire.com/2025/agility-robotics-reportedly-raising-400m-for-humanoid-warehouse-robots)
- [Boston Dynamics Atlas产品页](https://bostondynamics.com/products/atlas)
- [波士顿动力高管出走与量产分析](https://www.qbitai.com/2026/05/413613.html)
- [优必选官网-公司简介](https://www.ubtrobot.com/cn/about/company-profile)
- [优必选WRC 2025报道](https://www.qbitai.com/2025/08/320128.html)
- [智元机器人36氪融资信息](https://pitchhub.36kr.com/project/2228936046528520)
- [智元机器人灵巧手分拆-福布斯](https://www.forbeschina.com/business/71030)
- [智元机器人收购上纬新材-证券时报](https://www.stcn.com/article/detail/2543071.html)
- [宇树科技IPO深度分析-钛媒体](https://www.tmtpost.com/7924277.html)
- [宇树科技营收与融资-瑞财经](https://m.rccaijing.com/news-7441267069385635239.html)
- [宇树科技IPO过会-上海证券报](https://www.cnstock.com/commonDetail/723167)
- [银河通用11亿元融资-新华网](https://www.news.cn/digital/20250623/00657ee2fbde4b4d8c005ea667b31737/c.html)
- [银河通用25亿元融资-财新](https://m.caixin.com/m/2026-03-02/102418619.html)
- [银河通用三年融资分析-长江商报](https://finance.sina.com.cn/roll/2026-03-05/doc-inhpwzrx3276868.shtml)
- [Physical Intelligence官网](https://www.pi.website)
- [Physical Intelligence公司资料-Silicon Valley Investclub](https://siliconvalleyinvestclub.com/companies/physical-intelligence)
- [Physical Intelligence $1B融资传闻-TechCrunch](https://techcrunch.com/2026/03/27/physical-intelligence-is-reportedly-in-talks-to-raise-1-billion-again)
- [Skild AI Series C公告](https://www.skild.ai/blogs/series-c)
- [Skild AI $1.4B融资-Crunchbase](https://news.crunchbase.com/venture/robotics-startup-skild-ai-triples-valuation)
- [Skild AI估值分析-TSG Invest](https://tsginvest.com/skild-ai)
- [Apptronik $350M Series A公告](https://apptronik.com/news-collection/apptronik-raises-350-million-in-series-a-funding)
- [Apptronik $520M Series A-X-Crunchbase](https://news.crunchbase.com/venture/ai-humanoid-robot-funding-apptronik)
- [NVIDIA Isaac GR00T N1官方新闻](https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks)
- [NVIDIA Isaac GR00T开发者页面](https://developer.nvidia.com/isaac/gr00t)
- [Tesla Optimus 2025年量产目标-国信证券](https://www.fxbaogao.com/detail/4666416)
- [Tesla Optimus发展进程详解-知乎](https://zhuanlan.zhihu.com/p/1908561554837868813)
- [具身智能数据市场深度研究报告-知乎](https://zhuanlan.zhihu.com/p/2037175382634452800)
- [IDC 2026年具身智能十大技术趋势](https://www.idc.com/resource-center/blog/%E6%A8%A1%E5%9E%8B%E9%A9%B1%E5%8A%A8%EF%BC%8C%E8%BD%AF%E4%BB%B6%E5%AE%9A%E4%B9%89%EF%BC%8C%E7%A1%AC%E4%BB%B6%E9%87%8D%E6%9E%84-idc-%E8%A7%A3%E8%AF%BB-2026%E5%B9%B4%E5%85%B7%E8%BA%AB%E6%99%BA%E8%83%BD)
- [2025年具身智能行业深度-EET China](https://www.eet-china.com/mp/a413338.html)
- [2025年人形机器人走到哪一步了？- YouTube硅谷科技评论](https://www.youtube.com/watch?v=qs0ovkaacls)
- [Top 50 Investor-Favored AI & Embodied AI Companies-36Kr](https://eu.36kr.com/en/p/3899597215745664)
- [Robotics Funding Surges to $27.6B in 2025-LinkedIn](https://www.linkedin.com/posts/tech-funding-news_7-robotics-startups-to-watch-according-to-activity-7460976711543799808--Rcu)
- [Embodied AI Market Report 2025-MarketsandMarkets](https://www.marketsandmarkets.com/ResearchInsight/embodied-ai-market.asp)
- [深圳市具身智能机器人技术创新与产业发展行动计划](https://stic.sz.gov.cn/xxgk/tzgg/content/post_12052515.html)
- [2025具身智能机器人十大发展趋势-央视新闻](https://news.cctv.com/2025/08/08/ARTI1v4BmYbTiCDuSTJ4rdoj250808.shtml)


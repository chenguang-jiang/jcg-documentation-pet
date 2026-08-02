# Dawn Pet 流程图解指南

把抽象的流程、状态机、时序、决策，翻译成 Dawn Pet 一连串认真又笨拙的物理动作，用稀疏抖动细线箭头串成一张可读的图。**流程图解不是把 mermaid 涂黑**，而是让每个节点"演"出来。

## 何时用流程图解

| 内容 | 推荐形式 | 理由 |
|---|---|---|
| 3–5 个节点的主线流程、想给文章配一张"有温度"的流程封面 | **流程图解** | 一眼看懂走向，又有角色叙事 |
| 单个动作 / 单个概念 / 头像 | 单张配图 / 头像 | 不需要连接关系 |
| 节点 > 6、含精确数值 / 表格 / 代码 / 多泳道并发 | **mermaid**（精确）+ 流程图解（封面，可选） | Dawn Pet 图塞不下精确信息，硬塞会乱 |
| 既要精确又要好看 | **mermaid 画精确流程，Dawn Pet 图画意境封面**，两者并存 | 见下文"与 mermaid 协作" |

> 流程图解的目标是**让人愿意看、记得住走向**，不是替代精确图。节点一多就交给 mermaid。

## 核心思想：节点 = 动作，连接 = 细线，标签 = 节点下的手写短词

- **每个节点**是一个 mini 场景：同一个 Dawn Pet 在做一件对应这个节点语义的事。
- **节点之间**用稀疏、略抖的细黑线箭头连接，箭头方向 = 流程方向。
- **每个节点下方**允许一行手写体短词标签（这是流程图**唯一**允许的文字，且必须在角色**之外**、节点正下方，绝不写在角色身上）。
- 整张图仍是纯白底、纯黑角色、唯一橙红肚标；箭头和标签用细黑线/手写黑字，**不引入第二颜色**（橙红只留在肚标，必要时可用一个极小橙红点标记"当前/关键节点"，但默认不用）。

## 节点语义 → Dawn Pet 动作映射表

把流程节点的"意思"查表翻译成动作。同一张图里所有 Dawn Pet 必须看起来是**同一个角色**（同样的矮胖黑团、两只错位白眼、短肢扁脚、橙红肚标），只是动作和道具不同。

| 流程语义 | Dawn Pet 的动作 | 道具（稀疏细线） |
|---|---|---|
| 开始 / 触发 | 认真按一个 oversized 大按钮 | 大按钮 |
| 发送 / 请求 | 把一封信 / 纸飞机用力扔出去 | 信封 / 纸飞机 |
| 接收 | 慌忙伸手接住飞来的箱子 | 飞来的箱子 |
| 处理 / 计算 | 对着一摞纸认真敲大键盘 / 拨算盘 | 键盘 / 算盘 |
| 等待 / 异步 | 抱箱子站着盯沙漏，或坐地上等 | 沙漏 |
| 校验 / 验证 | 拿放大镜检查箱子 / 用尺子量 | 放大镜 / 尺子 |
| 授权 / 同意 | 在一张大纸上按手印 / 盖大章 | 纸 + 印章 |
| 连接 / 对接 | 把两个大插头对接 / 缠一团电缆 | 插头 / 电缆 |
| 传输 / 搬运 | 抱一摞文件摇摇晃晃地走 | 文件摞 |
| 存储 / 写入 | 把箱子推进一个大柜子 / 抽屉 | 柜子 |
| 读取 / 查询 | 从大柜子里掏东西 / 翻一本大书 | 柜子 / 书 |
| 分支 / 判断 | 站岔路口，左右各一个箱子，认真看 | 路牌 / 两箱子 |
| 成功 / 完成 | 把箱子稳稳放好，站定（无嘴，靠站姿） | 细线画的小对勾旗 |
| 失败 / 错误 | 被箱子压倒 / 箱子散架一地 | 散架的箱子 |
| 重试 | 从地上爬起来，再搬同一个箱子 | 同上 |
| 循环 | 绕着一个箱子转圈推 | 箱子 |
| 合并 / 汇总 | 把几个小箱子堆成一个大箱子 | 多个箱子 |
| 通知 / 告警 | 举一个大铃铛 / 大喇叭 | 铃铛 / 喇叭 |

> 表里没有的语义，按"认真 + 笨拙 + 一个 oversized 道具"的原则现编一个物理动作，**不要**画抽象符号（齿轮、云朵、数据库圆柱体等写实图标都禁止——它们破坏手绘白底语言）。

## 布局模式

| 模式 | 结构 | 适用 | 节点上限 |
|---|---|---|---|
| **横向流水线** linear | 一行 3–5 格，从左到右，水平箭头 | 主线顺序流程（最常用） | 5 |
| **漫画分格** comic | 1×3 或 2×2，细线格框，按阅读顺序箭头 | 有"起承转合"的故事化流程 | 4 |
| **循环 / 状态** loop | 3–4 个 Dawn Pet 围成一圈，弧形箭头首尾相接 | 状态机、轮询、重试循环 | 4 |
| **分支** branch | 顶部一个 Dawn Pet（判断），下方分两条路各一个 Dawn Pet | 是/否、成功/失败二分 | 3（1+2） |

- 节点之间留**明显空隙**放箭头，不重叠、不挤。
- 一张图**只选一种布局**，不要混排。
- 阅读顺序默认左上→右下；分支模式默认上→下。

## 连接与箭头规则

- 箭头用**稀疏、略抖的细黑线**，箭头头部小而清晰，方向无歧义。
- 箭头**尽量不交叉**；分支模式的两条路用一左一右分开，不交叉。
- 一条箭头只连两个节点；不要从一个节点拉出三四条线造成蜘蛛网。
- 循环模式的回环箭头走外圈弧线，不穿过角色。

## 标签规则（流程图唯一允许的文字）

- 每个节点**正下方**一行手写体短词：中文 ≤ 4 字，英文 ≤ 2 词。
- 标签描述**节点语义**（"发起授权""校验""成功"），不描述 Dawn Pet 的动作。
- 标签在角色**之外**，绝不压在黑团上、绝不画进肚标或脸。
- 除节点标签外，**不放**标题、图例、边框、水印、序号圆圈。

## 节点数量与留白

- 单张图节点 **3–5 个**为甜区；6 个是硬上限，超过就拆成两张图或改用 mermaid。
- 节点越多，每个 Dawn Pet 画得越小、越简，道具越省，**留白优先于细节**。
- 宁可少画一个节点、把走向画清楚，也不要塞满。

## 与 mermaid 协作（推荐模式）

技术文章里，精确流程和可爱配图各司其职：

1. 用 **mermaid** 画精确的 `flowchart` / `sequenceDiagram` / `stateDiagram`，承载全部节点、条件、字段。
2. 用 **Dawn Pet 流程图解**画一张 3–5 节点的"主线意境图"当章节封面或摘要配图，让人先建立直觉。
3. 两张图**节点命名对齐**（意境图的标签 ⊂ mermaid 的节点名），读者能对应上。

> 例：Enode 授权流程的 mermaid 有 8 个节点，Dawn Pet 意境图只挑 4 个主线节点——"发起连接 → 用户登录授权 → 发现设备 → 开始读取"——每个配一个动作。

## 不适合 Dawn Pet 画的流程（诚实边界）

- 节点 > 6 的复杂流程。
- 需要精确数值、百分比、表格、代码片段、接口字段。
- 多泳道并发时序（谁先谁后靠时间轴对齐的）。
- 需要严格图例 / 颜色编码区分多类对象。
- 这些**用 mermaid**；Dawn Pet 图最多当封面，不冒充精确图。

## 完整示例：用户授权流程（横向流水线，4 节点）

节点：发起连接 → 登录授权 → 校验通过 → 开始读取。

```text
Use case: illustration-story
Asset type: 16:9 horizontal flow diagram (4 nodes, linear layout)

Input images:
- Image 1 is the exact Dawn Pet identity reference. Every node must show the
  SAME Dawn Pet (identical pear-shaped black body, two uneven white dot eyes,
  short limbs, flat feet, tiny orange-red belly mark). Only the action and the
  thin-line prop change between nodes.

Primary request:
Draw a left-to-right 4-node flow diagram on a pure white background. Each node
is the same Dawn Pet doing one action; connect nodes with sparse, slightly
wobbly thin black arrows pointing right. Under each node, one short handwritten
label in black, placed OUTSIDE the character.

Node 1 (label "发起连接"): Dawn Pet seriously pressing one oversized button.
Node 2 (label "登录授权"): the same Dawn Pet pressing a hand-stamp onto a big
  sheet of paper.
Node 3 (label "校验通过"): the same Dawn Pet inspecting a box with a magnifier,
  standing settled.
Node 4 (label "开始读取"): the same Dawn Pet waddling while carrying a stack of
  papers.

Character invariants (every node): one short wide solid-black pear body; head
and torso fused, no neck; exactly two small uneven white dot eyes, no mouth;
very short rounded arms, short legs, oversized flat feet; one tiny flat
orange-red semicircle low on the belly.

Style: minimalist hand-drawn black-ink cartoon, pure white background, generous
whitespace between nodes. Props and arrows drawn only with sparse, slightly
wobbly thin black lines. No second color except the belly mark.

Constraints: no text on the character, no title, no legend, no border, no
watermark, no numbered circles, no realistic icons (gears, clouds, db
cylinders). No 3D, gloss, gradient, shading. Arrows must not cross. Keep each
Dawn Pet clearly the same character.
```

## 局部迭代句式（流程图解专用）

- `Keep the layout and all other nodes unchanged. Make the arrow between node 2 and node 3 point the other way.`
- `Keep every Dawn Pet identical. Replace node 3's action with the same character inspecting a box with a ruler.`
- `Keep the characters and arrows unchanged. Move each handwritten label to sit clearly below its node, outside the black body.`
- `Keep the flow unchanged. Remove node 4 and reconnect so the diagram has three nodes with more whitespace.`

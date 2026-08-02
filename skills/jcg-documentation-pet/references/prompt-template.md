# Dawn Pet 提示词模板

## 主模板

```text
Use case: illustration-story
Asset type: {identity sheet / 16:9 editorial scene / avatar}

Input images:
- Image 1 is the exact Dawn Pet identity reference. Preserve its silhouette, eyes, belly mark, short limbs, and deadpan clumsy personality.
- Any other image is pose, prop, or composition reference only. Never replace the identity from Image 1.

Primary request:
Show the same Dawn Pet {action or scene}.

Character invariants:
- One short, wide, softly asymmetric pear-and-dumpling solid-black body.
- Head and torso are one continuous shape; no neck, separate head, narrow waist, or ant-like anatomy.
- Exactly two small, slightly uneven white dot eyes in the upper third; no mouth or pupils.
- Very short rounded arms, short sturdy legs, and slightly oversized flat black feet.
- One tiny flat orange-red semicircle centered low on the belly.

Personality and action:
Dawn Pet is completely serious, patient, slightly slow, and adorably incompetent. Make the humor come from {specific physical action or predicament}, not from a cute facial expression.

Style:
Minimalist hand-drawn black-ink cartoon on a pure white background. The character is a solid black mass with a subtly handmade edge. Draw the main prop with sparse, slightly wobbly, clearly visible thin black lines. Use generous whitespace.

Composition:
{one character / up to three separated poses}. One clear action and one main prop. Keep the character as the visual focus. Default 16:9 for editorial scenes.

Palette:
Pure black, pure white, and only one tiny orange-red belly accent. No gray, shading, texture, gradients, or extra colors.

Constraints:
No robot parts, horns, ears, antennae, bird features, separate head, long limbs, clothing, mouth, eyebrows, blush, text, labels, logos, borders, or watermark. No 3D, glossy rendering, polished corporate vector style, dense infographic, or busy background.
```

## 动作设定图示例

```text
Create a three-pose character sheet of the exact same Dawn Pet: standing still, waddling while carrying one oversized cardboard box, and sitting down after the box slips. Keep all three figures identical in body shape, eyes, limb length, feet, and orange-red belly mark. Separate each pose with generous white space.
```

## 正文配图示例

```text
Show the same Dawn Pet seriously trying to push an oversized folder across a clean white page. The folder is drawn only with sparse hand-drawn black lines. The pet leans forward with tiny arms and flat feet slipping slightly backward. Keep the face blank and mouthless.
```

## 局部迭代句式

- `Keep everything else unchanged. Make the body shorter and wider, with the head and torso fused into one continuous black mass.`
- `Keep the silhouette unchanged. Restore exactly two small uneven white dot eyes and remove the mouth.`
- `Keep the character unchanged. Shorten and thicken the legs, and make the feet flatter and slightly larger.`
- `Keep the scene unchanged. Simplify the prop to sparse, slightly wobbly black lines and increase the surrounding white space.`

## 流程图解模板

画流程 / 状态 / 决策图时用这个模板。先把每个流程节点查 [flow-diagram.md](flow-diagram.md) 的“节点语义 → 动作映射表”翻译成动作，再填入 `{nodes}`。

```text
Use case: illustration-story
Asset type: 16:9 flow diagram ({layout: linear / comic / loop / branch}, {N} nodes)

Input images:
- Image 1 is the exact Dawn Pet identity reference. Every node must show the
  SAME Dawn Pet (identical pear-shaped black body, two uneven white dot eyes,
  short limbs, flat feet, tiny orange-red belly mark). Only the action and the
  thin-line prop change between nodes.

Primary request:
Draw a {N}-node flow diagram on a pure white background using a {layout}
layout. Each node is the same Dawn Pet doing one action. Connect nodes with
sparse, slightly wobbly thin black arrows following the flow direction; arrows
must not cross. Under each node, one short handwritten label in black, placed
OUTSIDE the character.

Nodes (action per node, from the semantic→action mapping table):
{node 1 (label "..."): same Dawn Pet <action> with <thin-line prop>}
{node 2 (label "..."): ...}
{...up to 5 nodes...}

Character invariants (every node): one short wide solid-black pear body; head
and torso fused, no neck; exactly two small uneven white dot eyes, no mouth;
very short rounded arms, short legs, oversized flat feet; one tiny flat
orange-red semicircle low on the belly.

Style: minimalist hand-drawn black-ink cartoon, pure white background,
generous whitespace between nodes. Props and arrows only with sparse, slightly
wobbly thin black lines. No second color except the belly mark.

Constraints: no text on the character, no title, no legend, no border, no
watermark, no numbered circles, no realistic icons (gears, clouds, db
cylinders). No 3D, gloss, gradient, shading. Keep every Dawn Pet clearly the
same character.
```

> 节点 > 6、含精确数值 / 表格 / 代码 / 多泳道并发的流程，不要用本模板——改用 mermaid，本模板最多画 3–5 节点的主线意境封面。


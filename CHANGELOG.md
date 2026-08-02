# Changelog

All notable changes to this project are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Flow-diagram asset type: render processes / state machines / decisions as a
  sequence of Dawn Pet actions connected by thin-line arrows, driven by a
  semantic→action mapping table (`references/flow-diagram.md`).
- Flow-diagram sections in `visual-system.md`, `prompt-template.md` (template),
  and `qa-checklist.md` (consistency checklist).
- `SKILL.md` routes flow / state / decision content to the flow-diagram
  workflow and documents the mermaid-collaboration pattern.
- Contract test for `flow-diagram.md` (22 assertions total).
- Auto asset-type routing: `SKILL.md` now discriminates the asset type from
  content structure (ordered steps / arrows / branches / loops) instead of
  waiting for the user to name it, declares the decision in one line before
  drawing, and falls back to mermaid automatically; `flow-diagram.md` gains
  structural recognition signals. Guarded by `test_auto_routing`
  (23 assertions total).

## [0.1.0] - 2026-07-30

### Added
- `jcg-documentation-pet` Codex Skill: generate and edit a consistent clumsy
  black mascot character "Dawn Pet" for DawnVibe documentation, with strict
  identity invariants.
- `SKILL.md`: complete workflow — identity lock, personality expression, asset
  type selection, generation and delivery instructions.
- `references/identity.md`: immutable character features (silhouette, face,
  limbs, belly mark, visual material, personality, prohibited variations).
- `references/visual-system.md`: color palette, line style, composition rules
  for avatars, pose sheets, and editorial scenes.
- `references/prompt-template.md`: ready-to-use prompt templates with character
  invariants, style constraints, and iteration phrases.
- `references/qa-checklist.md`: post-generation checklist covering identity
  consistency, style, failure signals, and fix order.
- `assets/identity/dawn-pet-anchor.png`: the single official identity anchor
  image (three poses: standing, carrying box, sitting).
- `agents/openai.yaml`: Codex agent config with implicit invocation.
- Contract tests (`tests/test_skill_contract.py`) — 20 assertions.
- GitHub Actions CI (`.github/workflows/test.yml`).
- Bilingual README (English / 简体中文) with hero SVG.

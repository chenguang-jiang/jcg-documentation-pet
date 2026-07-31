#!/usr/bin/env python3
"""Contract tests for jcg-documentation-pet skill."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = ROOT.parents[1]
SKILL_MD = (ROOT / "SKILL.md").read_text(encoding="utf-8")


class TestSkillContract(unittest.TestCase):

    def test_frontmatter_name(self) -> None:
        self.assertIn("name: jcg-documentation-pet", SKILL_MD)

    def test_frontmatter_description(self) -> None:
        self.assertIn("description:", SKILL_MD)
        self.assertIn("Dawn Pet", SKILL_MD)

    def test_identity_section(self) -> None:
        self.assertIn("锁定身份", SKILL_MD)

    def test_personality_section(self) -> None:
        self.assertIn("表达性格", SKILL_MD)

    def test_asset_types(self) -> None:
        for t in ("头像", "动作设定图", "正文场景配图", "局部编辑"):
            self.assertIn(t, SKILL_MD)

    def test_anchor_reference(self) -> None:
        self.assertIn("dawn-pet-anchor.png", SKILL_MD)

    def test_reference_links(self) -> None:
        for ref in ("identity.md", "visual-system.md", "prompt-template.md", "qa-checklist.md"):
            self.assertIn(ref, SKILL_MD)

    def test_generation_workflow(self) -> None:
        self.assertIn("生成与交付", SKILL_MD)

    def test_identity_md(self) -> None:
        text = (ROOT / "references" / "identity.md").read_text(encoding="utf-8")
        self.assertIn("不可变特征", text)
        self.assertIn("禁止变化", text)

    def test_visual_system_md(self) -> None:
        text = (ROOT / "references" / "visual-system.md").read_text(encoding="utf-8")
        self.assertIn("色彩", text)
        self.assertIn("构图", text)

    def test_prompt_template_md(self) -> None:
        text = (ROOT / "references" / "prompt-template.md").read_text(encoding="utf-8")
        self.assertIn("Character invariants", text)
        self.assertIn("Constraints", text)

    def test_qa_checklist_md(self) -> None:
        text = (ROOT / "references" / "qa-checklist.md").read_text(encoding="utf-8")
        self.assertIn("身份一致性", text)
        self.assertIn("修正顺序", text)

    def test_anchor_image_exists(self) -> None:
        anchor = ROOT / "assets" / "identity" / "dawn-pet-anchor.png"
        self.assertTrue(anchor.is_file(), f"Missing anchor image: {anchor}")
        self.assertGreater(anchor.stat().st_size, 1000, "Anchor image too small")

    def test_yaml_exists(self) -> None:
        self.assertTrue((ROOT / "agents" / "openai.yaml").is_file())

    def test_yaml_display_name(self) -> None:
        text = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("Dawn Pet", text)

    def test_repo_readme_english(self) -> None:
        text = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("jcg-documentation-pet", text)

    def test_repo_readme_chinese(self) -> None:
        self.assertTrue((REPO_ROOT / "README.zh-CN.md").is_file())

    def test_repo_license(self) -> None:
        self.assertTrue((REPO_ROOT / "LICENSE").is_file())

    def test_repo_changelog(self) -> None:
        self.assertTrue((REPO_ROOT / "CHANGELOG.md").is_file())

    def test_repo_ci_workflow(self) -> None:
        self.assertTrue((REPO_ROOT / ".github" / "workflows" / "test.yml").is_file())

    def test_repo_hero_svg(self) -> None:
        hero = REPO_ROOT / "assets" / "readme" / "hero.svg"
        self.assertTrue(hero.is_file())
        self.assertIn("<svg", hero.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main(verbosity=2)

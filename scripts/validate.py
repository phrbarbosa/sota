#!/usr/bin/env python3
"""Check repo conventions and relative links. Standard library only.

The Agent Skills spec itself is checked by skills-ref in CI. Lists every error, and exits 1 if there is any.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "sota"
errors: list[str] = []


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append("SKILL.md: no frontmatter")
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if line and not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            fields[key] = value.strip()
    return fields


def check_skill() -> dict[str, str]:
    text = (SKILL / "SKILL.md").read_text()
    fields = frontmatter(text)
    name = fields.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append(f"SKILL.md: invalid name {name!r}")
    if name != SKILL.name:
        errors.append(f"SKILL.md: name {name!r} differs from directory {SKILL.name!r}")
    if not 1 <= len(fields.get("description", "")) <= 1024:
        errors.append(f"SKILL.md: description has {len(fields.get('description', ''))} chars, limit 1024")
    if len(fields.get("compatibility", "")) > 500:
        errors.append("SKILL.md: compatibility over 500 chars")
    if len(text.splitlines()) > 500:
        errors.append("SKILL.md: over 500 lines")
    return fields


def check_references() -> None:
    refs = SKILL / "references"
    on_disk = {p.name for p in refs.glob("*.md")}
    text = (SKILL / "SKILL.md").read_text()
    named = set(re.findall(r"references/([\w-]+\.md)", text))
    for missing in sorted(named - on_disk):
        errors.append(f"SKILL.md names references/{missing}, which does not exist")
    for orphan in sorted(on_disk - named):
        errors.append(f"references/{orphan} is not listed in SKILL.md")
    for path in refs.glob("*.md"):
        for mention in re.findall(r"`([a-z-]+\.md)`", path.read_text()):
            if mention not in on_disk:
                errors.append(f"references/{path.name} mentions {mention}, which does not exist")


def check_markdown_links() -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or "results" in path.parts:
            continue
        for target in re.findall(r"\]\((?!https?://|#)([^)#]+)", path.read_text()):
            if not (path.parent / target).exists():
                errors.append(f"{path.relative_to(ROOT)}: broken link {target}")


def check_manifests(fields: dict[str, str]) -> None:
    try:
        plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
        market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    except (OSError, ValueError) as exc:
        errors.append(f"manifest: {exc}")
        return
    if plugin["name"] != market["plugins"][0]["name"]:
        errors.append("plugin.json and marketplace.json name different plugins")
    skill_text = (SKILL / "SKILL.md").read_text()
    version = re.search(r'version: "([^"]+)"', skill_text).group(1)
    if plugin.get("version") != version:
        errors.append(f"version mismatch: plugin.json {plugin.get('version')}, SKILL.md {version}")
    if f"## {version}" not in (ROOT / "CHANGELOG.md").read_text():
        errors.append(f"CHANGELOG.md has no entry for {version}")


def check_placeholders() -> None:
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".json"} and ".git" not in path.parts:
            if "results" in path.parts:
                continue
            if re.search(r"<you>|<your name>|TODO|FIXME", path.read_text()):
                errors.append(f"{path.relative_to(ROOT)}: unresolved placeholder")


def check_translations() -> None:
    """The two READMEs must link to each other and carry the same sources, numbers, headings and table rows."""
    pt = (ROOT / "README.md").read_text()
    en = (ROOT / "README.en.md").read_text()
    if "(README.en.md)" not in pt or "(README.md)" not in en:
        errors.append("README.md and README.en.md must link to each other")
    for label, pattern in (("headings", r"^#{2,3} "), ("table rows", r"^\|")):
        count_pt = len(re.findall(pattern, pt, re.M))
        count_en = len(re.findall(pattern, en, re.M))
        if count_pt != count_en:
            errors.append(f"READMEs differ in {label}: pt {count_pt}, en {count_en}")
    arxiv_pt = set(re.findall(r"arxiv\.org/abs/[\d.]+", pt))
    arxiv_en = set(re.findall(r"arxiv\.org/abs/[\d.]+", en))
    if arxiv_pt != arxiv_en:
        errors.append(f"READMEs cite different sources: {sorted(arxiv_pt ^ arxiv_en)}")
    numbers_pt, numbers_en = readme_numbers(pt), readme_numbers(en)
    if numbers_pt != numbers_en:
        diff = (numbers_pt - numbers_en) + (numbers_en - numbers_pt)
        errors.append(f"READMEs differ in numbers: {sorted(diff)}")


def readme_numbers(text: str) -> Counter:
    """Every number in prose, ignoring links and separators, so 7,24 and 7.24 compare equal."""
    text = re.sub(r"\]\([^)]*\)", "]", text)
    return Counter(re.sub(r"[.,]", "", n) for n in re.findall(r"\d[\d.,]*\d|\d", text))


def check_anchors() -> None:
    """Links inside a page must land on one of that page's own headings."""
    for name in ("README.md", "README.en.md"):
        text = (ROOT / name).read_text()
        slugs = set()
        for heading in re.findall(r"^#{1,6} (.+)$", text, re.M):
            slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
            slugs.add(slug)
        for anchor in re.findall(r"\]\(#([^)]+)\)", text):
            if anchor not in slugs:
                errors.append(f"{name}: anchor #{anchor} matches no heading")


def main() -> int:
    fields = check_skill()
    check_references()
    check_markdown_links()
    check_manifests(fields)
    check_placeholders()
    check_translations()
    check_anchors()
    for error in errors:
        print(f"error: {error}")
    print(f"{'FAILED' if errors else 'OK'}: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

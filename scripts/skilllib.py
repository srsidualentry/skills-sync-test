"""Shared parsing for SKILL.md files. SKILL.md is the source of truth."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
CATALOG = ROOT / "catalog.json"


def split_list(value):
    return [v.strip() for v in value.split(",") if v.strip()]


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("missing frontmatter")
    top, meta, in_meta = {}, {}, False
    for line in m.group(1).split("\n"):
        if line.startswith("metadata:"):
            in_meta = True
            continue
        if in_meta and line.startswith("  "):
            k, _, v = line.strip().partition(":")
            meta[k.strip()] = v.strip()
        elif ":" in line:
            in_meta = False
            k, _, v = line.partition(":")
            top[k.strip()] = v.strip()
    return top, meta, m.group(2)


def section(body, heading):
    m = re.search(r"^## " + re.escape(heading) + r"\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return m.group(1).strip() if m else None


def bullets(text):
    return [l[2:].strip() for l in text.split("\n") if l.startswith("- ")]


def numbered(text):
    return [re.sub(r"^\d+\.\s*", "", l).strip() for l in text.split("\n") if re.match(r"^\d+\.\s", l)]


def load_skill(path):
    top, meta, body = parse_frontmatter(Path(path).read_text())
    return {
        "name": top.get("name", ""),
        "title": meta.get("title", ""),
        "description": top.get("description", ""),
        "area": meta.get("area", ""),
        "access": meta.get("access", ""),
        "surface": split_list(meta.get("surface", "")),
        "requires": split_list(meta.get("requires", "")),
        "tools": split_list(meta.get("tools", "")),
        "example_prompt": meta.get("example_prompt", ""),
        "when": bullets(section(body, "When to use") or ""),
        "steps": numbered(section(body, "Steps") or ""),
    }


def all_skill_files():
    return sorted(SKILLS_DIR.glob("*/SKILL.md"))


def build_catalog_text():
    import json
    skills = [load_skill(p) for p in all_skill_files()]
    return json.dumps({"skills": skills}, indent=2, ensure_ascii=False) + "\n"

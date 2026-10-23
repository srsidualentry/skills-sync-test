#!/usr/bin/env python3
"""Exits non-zero if any skill or catalog.json is invalid or stale."""
import re
import sys

from skilllib import CATALOG, all_skill_files, build_catalog_text, parse_frontmatter, section

REAL_TOOLS = {
    "search_records", "get_record_detail", "get_record_by_number", "get_record_history",
    "get_related_records", "search_entities", "list_companies", "save_entity", "save_record",
    "get_contract_detail", "preview_contract_schedule", "create_contract",
    "preview_fixed_asset_schedule", "create_fixed_asset", "list_bank_match_suggestions",
}
REQUIRED_TOP = ["name", "description"]
REQUIRED_META = ["title", "area", "access", "surface", "example_prompt"]
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
errors = []


def err(skill, msg):
    errors.append(f"{skill}: {msg}")


for path in all_skill_files():
    folder = path.parent.name
    text = path.read_text()
    try:
        top, meta, body = parse_frontmatter(text)
    except ValueError as e:
        err(folder, str(e))
        continue
    if top.get("name") != folder:
        err(folder, f"folder name differs from frontmatter name '{top.get('name')}'")
    for k in REQUIRED_TOP:
        if not top.get(k):
            err(folder, f"missing field {k}")
    for k in REQUIRED_META:
        if not meta.get(k):
            err(folder, f"missing field metadata.{k}")
    for k in ("requires", "tools"):
        if k not in meta:
            err(folder, f"missing field metadata.{k} (may be empty)")
    for t in [x.strip() for x in meta.get("tools", "").split(",") if x.strip()]:
        if t not in REAL_TOOLS:
            err(folder, f"unknown tool '{t}'")
    if meta.get("access") not in ("read-only", "read-write"):
        err(folder, f"access must be read-only or read-write, got '{meta.get('access')}'")
    for h in ("When to use", "Steps"):
        if not section(body, h):
            err(folder, f"missing section '{h}'")
    if EMAIL.search(text):
        err(folder, "contains an email address")
    if chr(0x2014) in text or chr(0x2013) in text:
        err(folder, "contains an em or en dash")

if not CATALOG.exists() or CATALOG.read_text() != build_catalog_text():
    errors.append("catalog.json is stale: run scripts/build_catalog.py")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok: {len(all_skill_files())} skills valid, catalog.json up to date")

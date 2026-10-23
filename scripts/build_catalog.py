#!/usr/bin/env python3
"""Reads every SKILL.md and writes catalog.json. Never edit catalog.json by hand."""
from skilllib import CATALOG, build_catalog_text

CATALOG.write_text(build_catalog_text())
print(f"wrote {CATALOG.name}")

#!/usr/bin/env python3
"""Reads every SKILL.md and writes catalog.json and the README catalog table.
Never edit either by hand."""
from skilllib import CATALOG, README, build_catalog_text, readme_with_catalog

CATALOG.write_text(build_catalog_text())
README.write_text(readme_with_catalog())
print(f"wrote {CATALOG.name} and the README catalog table")

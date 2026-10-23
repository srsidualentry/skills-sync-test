# Repository architecture

## Layout

```
skills/<name>/SKILL.md   one folder per skill, flat layout, names start with dualentry-
catalog.json             generated from the SKILL.md files
README.md                the catalog table is generated between the catalog markers
scripts/                 build_catalog.py, validate.py, skilllib.py
.github/workflows/       validate.yml
docs/                    these guides
```

## Source of truth

`SKILL.md` is the source of truth. `catalog.json` and the README catalog table are generated from it.
Never edit either of them by hand.

## The edit loop

1. Edit `skills/<name>/SKILL.md`.
2. Run `python3 scripts/build_catalog.py`.
3. Run `python3 scripts/validate.py`.
4. Commit the skill, `catalog.json` and `README.md` together, then push.

## Validation

`scripts/validate.py` fails if a folder name differs from the frontmatter name, a name does not start
with `dualentry-`, a required field is missing, a tool is not a known DualEntry MCP tool, access is not
`read-only` or `read-write`, a "When to use" or "Steps" section is missing, the text contains an email
address or an em or en dash, or `catalog.json` or the README table is stale.

A GitHub Action runs both scripts on every push and fails if a generated file changed.

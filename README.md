# skills-sync-test

Throwaway test repo: skills live here as `skills/<name>/SKILL.md`, and a landing page reads `catalog.json` from the raw GitHub URL.

`SKILL.md` is the source of truth. Never edit `catalog.json` by hand.

## Edit loop

1. Edit `skills/<name>/SKILL.md`
2. `python3 scripts/build_catalog.py`
3. `python3 scripts/validate.py`
4. `git push`

The GitHub Action repeats steps 2 and 3 and fails if `catalog.json` changed.

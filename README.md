# DualEntry Skills

[![Agent Skills Spec](https://img.shields.io/badge/Agent%20Skills-Specification-blue)](https://agentskills.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**DualEntry skills for AI agents.**

> Status: prototype. This catalog is a working test of publishing DualEntry skills.

---

Skills are portable instruction sets that teach compatible agents how to work in
[DualEntry](https://www.dualentry.com): payables, receivables, revenue, and close. They pair with
DualEntry's agent tools through an MCP connection, and work across clients that support the
[Agent Skills specification](https://agentskills.io).

Each skill is a plain `SKILL.md` file. Long-form guides for installation, connecting to DualEntry,
safety, and troubleshooting live in [`docs/`](docs/).

---

## Quickstart

Install skills with the [`skills` CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add srsidualentry/skills-sync-test
```

Install a specific skill without prompts:

```bash
npx skills add srsidualentry/skills-sync-test --skill <skill-name> --yes
```

Target a specific agent:

```bash
npx skills add srsidualentry/skills-sync-test --skill <skill-name> --agent <agent-name>
```

List the skills in this repository without installing anything:

```bash
npx skills add srsidualentry/skills-sync-test --list
```

Keep installed skills up to date with `npx skills update`.

### Connect your agent to DualEntry

Skills contain instructions only. To read DualEntry data, your agent also needs an authenticated
connection to DualEntry's MCP tools. See [`docs/authentication.md`](docs/authentication.md).

## Skill catalog

All skills are read-only and use the DualEntry MCP surface.

<!-- catalog:start -->

| Skill | Area | What it does |
|---|---|---|
| [`dualentry-intercompany-gl-report`](skills/dualentry-intercompany-gl-report/SKILL.md) | Close | Excel report of posted intercompany GL activity. |
| [`dualentry-bills-due-soon`](skills/dualentry-bills-due-soon/SKILL.md) | Payables | Unpaid bills due within the next N days. |
| [`dualentry-latest-posted-bill`](skills/dualentry-latest-posted-bill/SKILL.md) | Payables | Find the most recent posted bill, optionally for a vendor or entity. |
| [`dualentry-unpaid-bills-list`](skills/dualentry-unpaid-bills-list/SKILL.md) | Payables | List unpaid bills as of a date, largest first. |
| [`dualentry-ar-latest-overdue-invoice`](skills/dualentry-ar-latest-overdue-invoice/SKILL.md) | Receivables | Find the most recent posted, unpaid overdue invoice. |
| [`dualentry-ar-overdue-invoices`](skills/dualentry-ar-overdue-invoices/SKILL.md) | Receivables | List posted, unpaid, overdue invoices. |
| [`dualentry-ar-pending-approval`](skills/dualentry-ar-pending-approval/SKILL.md) | Receivables | List invoices pending approval. |
| [`dualentry-contracts-upcoming-start`](skills/dualentry-contracts-upcoming-start/SKILL.md) | Revenue | List contracts starting in the next N days. |
| [`dualentry-deferred-revenue-by-entity`](skills/dualentry-deferred-revenue-by-entity/SKILL.md) | Revenue | Deferred revenue at a date by entity, consolidated. |
| [`dualentry-implementation-invoice-dates`](skills/dualentry-implementation-invoice-dates/SKILL.md) | Revenue | Upcoming invoices for the implementation module. |

<!-- catalog:end -->

## About this repository

- Skills live under `skills/` in a flat layout: `skills/<name>/SKILL.md`. Every name starts with `dualentry-`.
- `SKILL.md` is the source of truth. `catalog.json` and the catalog table above are generated from it
  by `scripts/build_catalog.py`. Never edit them by hand.
- CI runs `scripts/validate.py` on every push and fails if a skill is invalid or a generated file is stale.
- See [`PRODUCT.md`](PRODUCT.md) for a map of DualEntry areas and which skill to load for a task.
- See [`docs/repository-architecture.md`](docs/repository-architecture.md) for the layout and edit loop.
- See [`CHANGELOG.md`](CHANGELOG.md) for release history.
- Found a problem in a skill? Open an issue in this repository.

## License

[MIT](LICENSE)

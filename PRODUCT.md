# DualEntry: Product Reference for AI Agents

A map of the DualEntry areas these skills cover, the records they read, and which skill to load for a task. Read this to orient; load a skill from [`README.md`](README.md) to act.

## The tool surface

These skills use DualEntry's MCP tools, such as `search_records`, `get_record_detail` and `get_contract_detail`. Each skill lists the tools it expects in its `tools` frontmatter field. Every skill in this catalog is read-only.

## Areas, records, and skills

| Area | What it covers | Records involved | Load |
|---|---|---|---|
| Payables | Unpaid and upcoming vendor bills, and the latest posted bill | bills, vendors | `dualentry-unpaid-bills-list`, `dualentry-bills-due-soon`, `dualentry-latest-posted-bill` |
| Receivables | Overdue invoices and invoices waiting for approval | invoices, customers | `dualentry-ar-overdue-invoices`, `dualentry-ar-latest-overdue-invoice`, `dualentry-ar-pending-approval` |
| Revenue | Upcoming contracts, invoices for the implementation module, and deferred revenue by entity | contracts, performance obligations, invoices, entities | `dualentry-contracts-upcoming-start`, `dualentry-implementation-invoice-dates`, `dualentry-deferred-revenue-by-entity` |
| Close | Posted intercompany general ledger activity | journal entries, companies | `dualentry-intercompany-gl-report` |

## Choosing a skill

- Match the task to the area above, then load the skill whose "What it does" fits.
- Each skill states its defaults (for example, the date range, scope and sort order). Use them unless the user says otherwise.
- Each skill is read-only. Do not use one of these skills to change data.

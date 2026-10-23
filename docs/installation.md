# Installation

## Install with the Skills CLI

Install every skill in this repository:

```bash
npx skills add srsidualentry/skills-sync-test
```

Install one skill without prompts:

```bash
npx skills add srsidualentry/skills-sync-test --skill dualentry-ar-pending-approval --yes
```

Target a specific agent (repeat `--agent` for several):

```bash
npx skills add srsidualentry/skills-sync-test --skill dualentry-ar-pending-approval --agent claude-code
```

List the available skills without installing:

```bash
npx skills add srsidualentry/skills-sync-test --list
```

Update installed skills:

```bash
npx skills update
```

See the [`skills` CLI](https://github.com/vercel-labs/skills) for the current list of supported agents.

## Choose a tool connection

Installing a skill only copies instructions. To read DualEntry data, connect your agent to DualEntry
as described in [Authentication](authentication.md).

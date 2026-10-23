# Safety and permissions

## What the skills instruct

- Every skill in this catalog is read-only. Each one declares `access: read-only` in its frontmatter,
  and the validator rejects any value other than `read-only` or `read-write`.
- Skills tell an agent which records to look up and how to present them. They do not tell an agent
  to create, change or delete records.
- Each skill lists the MCP tools it expects. The validator rejects tool names that are not on the
  known list.

## What DualEntry enforces

To be confirmed. This section will describe how DualEntry limits what a connected agent can see and do.

## Data accuracy

- Skills are instructions, not data. Figures come from the records an agent reads in DualEntry.
- Review results before acting on them, and check any figure that matters against the source record.

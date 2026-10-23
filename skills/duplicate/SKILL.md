---
name: duplicate
description: List invoices pending approval.
metadata:
  title: Duplicate
  area: Receivables
  access: read-only
  surface: MCP
  requires:
  tools: search_records
  example_prompt: Which invoices are pending approval?
---

# Duplicate

## When to use

- Seeing how many invoices are waiting for approval
- Getting links to each invoice that needs a decision

## Defaults

Defaults if I don't say otherwise:
- Scope: all invoices currently pending approval, no date filter, current organization only.

## Steps

1. Return all invoices pending approval.
2. Show count, plus invoice number with link for each.
Rules: no fabricated numbers, statuses or links.

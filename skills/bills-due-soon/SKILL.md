---
name: bills-due-soon
description: Unpaid bills due within the next N days.
metadata:
  title: Bills Due Soon SYNC EDIT
  area: Payables
  access: read-only
  surface: MCP
  requires:
  tools: search_records
  example_prompt: Which bills are due in the next 10 days?
---

# Bills Due Soon SYNC EDIT

## When to use

- Planning cash outflow for the next few days
- Finding bills with an early-payment discount about to expire

## Defaults

Defaults if I don't say otherwise:
- Window: from today through the next 10 days, by due date.
- Scope: all companies I have access to.
- Sort: due date, earliest first.

## Steps

1. List unpaid bills due in the window.
2. Include vendor, amount, due date, early-payment discount available.
3. Sum total cash outflow.

---
name: dualentry-unpaid-bills-list
description: List unpaid bills as of a date, largest first.
metadata:
  title: Unpaid Bills List
  area: Payables
  access: read-only
  surface: MCP
  requires:
  tools: search_records, get_record_detail
  example_prompt: List my unpaid bills, largest first.
---

# Unpaid Bills List

## When to use

- Seeing which vendor bills are still unpaid as of a date
- Ranking open payables by amount

## Defaults

Defaults if I don't say otherwise:
- As-of date: today.
- Scope: all companies I have access to.
- Sort: amount, largest first.

## Steps

1. Return all unpaid bills as of the date: vendor, bill number, amount, currency, due date.
2. Sort by amount descending.

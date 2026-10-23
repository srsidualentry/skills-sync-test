---
name: dualentry-ar-latest-overdue-invoice
description: Find the most recent posted, unpaid overdue invoice.
metadata:
  title: Latest Overdue Invoice
  area: Receivables
  access: read-only
  surface: MCP
  requires:
  tools: search_records, get_record_detail
  example_prompt: What is the latest overdue invoice?
---

# Latest Overdue Invoice

## When to use

- Finding the single most recent posted, unpaid overdue invoice
- Checking one overdue invoice quickly without a full report

## Defaults

Defaults if I don't say otherwise:
- Overdue as of: today.
- Exclusions: none.

## Steps

1. Return the most recent posted, unpaid overdue invoice that is not excluded.
2. Show invoice ID, customer, due date, days overdue, outstanding balance, status.

---
name: ar-overdue-invoices
description: List posted, unpaid, overdue invoices.
metadata:
  title: AR Overdue Invoices
  area: Receivables
  access: read-only
  surface: MCP
  requires:
  tools: search_records
  example_prompt: Show my top 10 overdue invoices from last month.
---

# AR Overdue Invoices

## When to use

- Reviewing the largest posted, unpaid invoices that are past due
- Preparing collections follow-up for a month or a days-overdue threshold

## Defaults

Defaults if I don't say otherwise:
- Due-date range: the most recently completed calendar month. If I give a minimum days overdue instead (for example 30), use that and ignore the range.
- Days past due: calculated as of today.
- Top N: 10.
- Scope: all companies.
- Sort: invoice amount, largest first.

## Steps

1. Filter posted, unpaid invoices by the range.
2. Sort by amount descending and take the top N.
3. Show invoice number with link, amount and currency, due date, days past due, and the total.

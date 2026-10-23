---
name: dualentry-latest-posted-bill
description: Find the most recent posted bill, optionally for a vendor or entity.
metadata:
  title: Latest Posted Bill
  area: Payables
  access: read-only
  surface: MCP
  requires:
  tools: search_records, get_record_detail
  example_prompt: What is the latest posted bill?
---

# Latest Posted Bill

## When to use

- Finding the most recent posted bill, for any vendor or one you name
- Looking up a bill by vendor or entity without giving a date

## Defaults

Defaults if I don't say otherwise:
- Vendor: any vendor.
- Entity: all entities.
- Date range: none; take the most recent posted bill of all time.
If I name a vendor or entity, limit to it. Never ask me for them.

## Steps

1. Return the latest posted bill: number, vendor, date, currency, company, expense account, total.

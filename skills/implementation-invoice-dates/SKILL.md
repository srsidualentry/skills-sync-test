---
name: implementation-invoice-dates
description: Upcoming invoices for the implementation module.
metadata:
  title: Implementation Invoice Dates
  area: Revenue
  access: read-only
  surface: MCP
  requires:
  tools: search_records
  example_prompt: When are the next implementation invoices going out?
---

# Implementation Invoice Dates

## When to use

- Finding upcoming invoices that include the Implementation module
- Getting the dates those invoices will go out

## Defaults

Defaults if I don't say otherwise:
- Window: from today through the next 2 months.
- Module: Implementation.
- Notification: none. Only send a Slack message if I ask, and then ask me for the recipient.

## Steps

1. List invoices to be sent with that module in the window, with their dates.
2. Return the dates.

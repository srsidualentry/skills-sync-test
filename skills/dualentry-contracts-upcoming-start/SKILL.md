---
name: dualentry-contracts-upcoming-start
description: List contracts starting in the next N days.
metadata:
  title: Contracts Upcoming Start
  area: Revenue
  access: read-only
  surface: MCP
  requires:
  tools: search_records, get_contract_detail
  example_prompt: Which contracts start in the next 90 days?
---

# Contracts Upcoming Start

## When to use

- Listing contracts about to start, by recognition start or first invoice date
- Spotting contracts where the first invoice comes before recognition starts

## Defaults

Defaults if I don't say otherwise:
- Window: from today through the next 90 days.
- Date tested: recognition start date or scheduled first invoice date, either one.
- Scope: all companies.

## Steps

1. Find contracts with a performance obligation where either date falls in the window.
2. Show customer, contract ID, obligation, modules, value, first invoice date, recognition start.
3. Sort by first invoice date. Flag when first invoice precedes recognition start.

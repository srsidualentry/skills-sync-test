---
name: intercompany-gl-report
description: Excel report of posted intercompany GL activity.
metadata:
  title: Intercompany GL Report
  area: Close
  access: read-only
  surface: MCP
  requires:
  tools: 
  example_prompt: Give me the intercompany general ledger report for the last 30 days.
---

# Intercompany GL Report

## When to use

- Producing an Excel report of posted intercompany ledger activity
- Supporting intercompany review during close

## Defaults

Defaults if I don't say otherwise:
- Period: the last 30 days.
- Companies: all companies.
- Status: posted activity only.
- Format: Excel (.xlsx). CSV or PDF if I ask.

## Steps

1. Pull posted intercompany activity from ledger data (not Report Center).
2. Columns: posting date, JE number, account, memo, debit, credit, source company, counterparty company, currency.
3. File name: Intercompany General Ledger Report.

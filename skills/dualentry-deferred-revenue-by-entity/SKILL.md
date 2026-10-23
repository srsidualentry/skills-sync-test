---
name: dualentry-deferred-revenue-by-entity
description: Deferred revenue at a date by entity, consolidated.
metadata:
  title: Deferred Revenue by Entity
  area: Revenue
  access: read-only
  surface: MCP
  requires:
  tools: 
  example_prompt: What is deferred revenue by entity at month end?
---

# Deferred Revenue by Entity

## When to use

- Reporting deferred revenue at a date, split by entity
- Consolidating deferred revenue into the parent reporting currency

## Defaults

Defaults if I don't say otherwise:
- As-of date: the last day of the most recently completed month.
- Currency: each entity's own currency, plus a consolidated total in the parent entity's reporting currency. Use another currency only if I name one.
- Entities: all.

## Steps

1. By entity, split implementation from subscription.
2. Consolidate into the target currency.

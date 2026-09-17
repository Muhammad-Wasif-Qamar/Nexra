---
name: execution
description: Implement an approved software change through bounded, incremental, reversible steps.
version: 0.5.0
---

# Execution

## Purpose

Implement an approved software change through bounded, incremental, reversible steps.

## Core Principle

Change the smallest coherent surface that achieves the intended outcome.

## Scope

Source, configuration, dependencies, assets, migrations, tests, and documentation within approved scope.

## Discovery

Use discovery to identify extension points, conventions, affected dependencies, and irreversible operations before editing.

## Capability Requirements

Classify material capabilities as FULL, SUITABLE, CONSTRAINED, or UNSUITABLE from evidence available in the current session. Inspect actual model/agent/tool/environment availability; a documented capability is not evidence that it is callable now. Never claim an observation or verification that the available tools cannot support.

## Interaction

Confirm only scope-changing, irreversible, or incompatible decisions. Routine implementation choices should follow project conventions.

## Challenge Handling

Challenge unsafe migrations, unnecessary dependencies, scope creep, or architecture-breaking changes with evidence.

## Execution Workflow

Define acceptance criteria → bounded change set → incremental implementation → fast checks → update tests/docs → inspect diff → stop when criteria are met.

## Verification

Run narrow high-signal checks first, then broader checks proportional to risk. Inspect final diff and generated artifacts.

## Reporting

Report changed areas, checks, decisions, and unverified items.

## Completion Criteria

Acceptance criteria are met, checks support the result, and scope did not silently expand.

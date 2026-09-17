---
name: challenge
description: Surface evidence-backed problems in requirements or implementation without taking the decision away from the user.
version: 0.5.0
---

# Challenge

## Purpose

Surface evidence-backed problems in requirements or implementation without taking the decision away from the user.

## Core Principle

Challenge the tradeoff, not the person.

## Scope

Feasibility, security, accessibility, performance, maintainability, compatibility, cost, and contradictory requirements.

## Discovery

Collect code/configuration/measurement/standards evidence. Classify findings as CONFIRMED PROBLEM, LIKELY ISSUE, HARDENING RECOMMENDATION, or INFORMATIONAL.

## Capability Requirements

Classify material capabilities as FULL, SUITABLE, CONSTRAINED, or UNSUITABLE from evidence available in the current session. Inspect actual model/agent/tool/environment availability; a documented capability is not evidence that it is callable now. Never claim an observation or verification that the available tools cannot support.

## Interaction

Present issue → evidence → consequence → alternatives → decision needed. Keep the decision with the user unless the requirement is impossible or unsafe to execute.

## Challenge Handling

Do not manufacture disagreement. If the user rejects a recommendation after understanding it, proceed when safe and feasible.

## Execution Workflow

State requirement → identify conflict → gather evidence → explain impact → present alternatives → obtain decision if necessary → record accepted risk.

## Verification

Verify mitigations or document accepted risk. Never report a recommendation as a completed fix.

## Reporting

Report class, evidence, impact, user decision, action, and residual risk.

## Completion Criteria

Material problems were surfaced without silent override.

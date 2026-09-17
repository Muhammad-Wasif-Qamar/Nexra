---
name: interaction
description: Resolve user decisions and ambiguities that cannot be discovered, safely defaulted, or inferred from explicit intent.
version: 0.5.0
---

# Interaction

## Purpose

Resolve user decisions and ambiguities that cannot be discovered, safely defaulted, or inferred from explicit intent.

## Core Principle

Discover before asking; ask before silently deciding.

## Scope

Questions, preferences, ambiguity, intent, authority, irreversible choices, and progressive clarification.

## Discovery

Separate discoverable facts, explicit constraints, subjective preferences, genuine ambiguity, and costly/irreversible decisions. Use existing project conventions for low-risk defaults.

## Capability Requirements

Classify material capabilities as FULL, SUITABLE, CONSTRAINED, or UNSUITABLE from evidence available in the current session. Inspect actual model/agent/tool/environment availability; a documented capability is not evidence that it is callable now. Never claim an observation or verification that the available tools cannot support.

## Interaction

Batch high-value questions, explain why an answer matters, and prefer concrete options when appropriate. Do not interview the user about discoverable facts.

## Challenge Handling

Do not treat subjective preference as an error. Challenge only when a concrete feasibility, accessibility, security, performance, or maintainability issue exists; use the challenge skill for that reasoning.

## Execution Workflow

Identify outcome → discover → default safely where possible → ask blocking/high-impact questions → confirm irreversible decisions → stop reopening settled choices.

## Verification

Verify that decisions were reflected and that no redundant questions were asked.

## Reporting

Report material decisions and assumptions, not a transcript.

## Completion Criteria

Questions were necessary and user authority was preserved.

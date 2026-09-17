---
name: verification
description: Collect evidence that an implementation satisfies its requested outcome and relevant quality constraints.
version: 0.5.0
---

# Verification

## Purpose

Collect evidence that an implementation satisfies its requested outcome and relevant quality constraints.

## Core Principle

Verification depth must match the claim.

## Scope

Behavior, integration, builds, visual output, accessibility, performance, security, and regression checks as applicable.

## Discovery

Map each acceptance criterion to an evidence method and identify unavailable methods before making claims.

## Capability Requirements

Classify material capabilities as FULL, SUITABLE, CONSTRAINED, or UNSUITABLE from evidence available in the current session. Inspect actual model/agent/tool/environment availability; a documented capability is not evidence that it is callable now. Never claim an observation or verification that the available tools cannot support.

## Interaction

Ask the user for validation only for subjective criteria or unavailable observations; do not outsource testable facts.

## Challenge Handling

Narrow claims such as secure, pixel-perfect, production-ready, or fully tested when evidence cannot support them.

## Execution Workflow

Extract criteria → choose evidence → run cheap/high-signal checks → runtime/integration checks → inspect regressions → classify pass/fail/blocked/N/A → form evidence-bounded completion.

## Verification

Use reproducible commands/observations. Distinguish environment failures from product failures.

## Reporting

Report criterion → method → result → limitation.

## Completion Criteria

Every material criterion has evidence or an explicit verification gap.

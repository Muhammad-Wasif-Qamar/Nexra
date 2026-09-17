---
name: capability-assessment
description: Determine whether the current model, agent, tools, environment, and project can reliably support the requested outcome.
version: 0.5.0
---

# Capability Assessment

## Purpose

Determine whether the current model, agent, tools, environment, and project can reliably support the requested outcome.

## Core Principle

Assess before depending; capability means availability plus adequacy for this task.

## Scope

Model reasoning/coding/context/vision; agent filesystem, terminal, browser, MCP and subagents; environment runtime/network/GPU; project constraints.

## Discovery

Translate the request into observable capability requirements, inspect what is actually callable, and assign FULL/SUITABLE/CONSTRAINED/UNSUITABLE. Record evidence and limitations.

## Capability Requirements

Classify material capabilities as FULL, SUITABLE, CONSTRAINED, or UNSUITABLE from evidence available in the current session. Inspect actual model/agent/tool/environment availability; a documented capability is not evidence that it is callable now. Never claim an observation or verification that the available tools cannot support.

## Interaction

Tell the user when a limitation changes the deliverable. Prefer safe alternatives over asking the user to compensate for missing capabilities.

## Challenge Handling

Challenge requirements that depend on unavailable capabilities or evidence. Offer lower-fidelity alternatives and let the user decide when tradeoffs are material.

## Execution Workflow

Assess requirements → inspect availability → evaluate adequacy → select workflow → re-check after environment changes → pass limitations to execution and verification.

## Verification

Verification claims must be bounded by capability. No browser means no claim of visual inspection; no runtime means no claim of runtime success.

## Reporting

Report capability state, evidence, impact, and selected fallback.

## Completion Criteria

Every material capability is classified and the workflow is compatible with the result.

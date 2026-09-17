---
name: project-discovery
description: Establish relevant facts about an existing software project before planning or modifying it.
version: 0.5.0
---

# Project Discovery

## Purpose

Establish relevant facts about an existing software project before planning or modifying it.

## Core Principle

Discover before asking; evidence outranks assumptions.

## Scope

Repository structure, stack, architecture, conventions, environment, dependencies, constraints, and unknowns relevant to the requested change.

## Discovery

Inspect package manifests, entry points, routes, source boundaries, configs, tests, docs, and version-control state. Classify facts as observed, verified, inferred, or unknown. Trace only the smallest useful surface and stop when more inspection will not change the plan.

## Capability Requirements

Classify material capabilities as FULL, SUITABLE, CONSTRAINED, or UNSUITABLE from evidence available in the current session. Inspect actual model/agent/tool/environment availability; a documented capability is not evidence that it is callable now. Never claim an observation or verification that the available tools cannot support.

## Interaction

Ask only for material information that cannot be discovered or safely defaulted. If the request conflicts with observed architecture, explain the conflict and ask whether the intent is migration or modification.

## Challenge Handling

Challenge incompatible requirements, destructive implications, missing prerequisites, or infeasible outcomes using evidence. Do not challenge taste.

## Execution Workflow

Define outcome → map affected files → identify conventions → establish constraints → record unknowns → decide whether user input is needed → hand evidence to the next stage. Discovery itself must not silently become redesign.

## Verification

Verify important facts with inspection or safe commands; do not call unrun commands verified.

## Reporting

Report stack, relevant architecture, conventions, constraints, unknowns, and necessary questions.

## Completion Criteria

Material project facts are established and no unnecessary implementation occurred.

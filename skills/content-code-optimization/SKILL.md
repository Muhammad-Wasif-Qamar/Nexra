---
name: content-code-optimization
description: Improve content clarity and code efficiency while preserving correctness, intent, accessibility, and maintainability.
version: 0.5.0
---

# Content + Code Optimization

## Purpose

Improve content clarity and code efficiency while preserving correctness, intent, accessibility, and maintainability.

## Core Principle

Optimize measurable outcomes without sacrificing meaning or maintainability for vanity metrics.

## Scope

Content quality and code efficiency are separate dimensions that may interact; avoid word-count rewrites and micro-optimizations without evidence.

## Discovery

Content: inspect purpose, headings, CTA hierarchy, duplication, metadata, terminology, reading level. Code: inspect hot paths, bundles, rendering, network, data access, dependencies, repeated work, lifecycle, dead code. Establish baselines.

## Capability Requirements

Classify material capabilities as FULL, SUITABLE, CONSTRAINED, or UNSUITABLE from evidence available in the current session. Inspect actual model/agent/tool/environment availability; a documented capability is not evidence that it is callable now. Never claim an observation or verification that the available tools cannot support.

## Interaction

Ask about brand/legal wording/audience only when material and unknown.

## Challenge Handling

Challenge optimization that harms clarity, accessibility, semantics, correctness, caching, or maintainability.

## Execution Workflow

Baseline → separate content/code issues → rank by impact/evidence → smallest high-impact changes → remove duplication/unnecessary work → re-measure → review content after structure changes.

## Verification

Use before/after measurements for measurable performance. Verify links, headings, metadata, tests, rendered behavior, and regressions.

## Reporting

Report content changes separately from code/performance changes and include evidence/tradeoffs.

## Completion Criteria

Quality improves or the limitation is explicit; meaning/correctness remain intact.

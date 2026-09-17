---
name: 3d-web-design
description: Design interactive 3D web experiences with scene, camera, asset, interaction, accessibility, and performance discipline.
version: 0.5.0
---

# 3D Web Design

## Purpose

Design interactive 3D web experiences with scene, camera, asset, interaction, accessibility, and performance discipline.

## Core Principle

Treat 3D as an interactive system with a budget, not decoration.

## Scope

WebGL/WebGPU scenes, cameras, meshes, materials, lighting, assets, loading, interaction, fallbacks, and DOM integration.

## Discovery

Inspect renderer, scene graph, camera, asset formats, texture sizes, device targets, loading pipeline, and existing UI integration. Establish a performance budget before adding effects.

## Capability Requirements

Classify material capabilities as FULL, SUITABLE, CONSTRAINED, or UNSUITABLE from evidence available in the current session. Inspect actual model/agent/tool/environment availability; a documented capability is not evidence that it is callable now. Never claim an observation or verification that the available tools cannot support.

## Interaction

Ask about device targets or visual direction only when material and not inferable.

## Challenge Handling

Challenge unbounded assets/effects, blocking loads, inaccessible controls, or 3D that is unnecessary for the outcome.

## Execution Workflow

Spatial goal → device/performance budget → renderer architecture → camera/world/lighting → assets → loading/fallback → UI integration → reduced-motion/low-capability path → profiling.

## Verification

Verify initialization, failures, resize, input, cleanup, fallbacks, and measurable render cost. Do not claim cross-device GPU performance without representative tests.

## Reporting

Report renderer assumptions, asset changes, budget, interaction, fallback, verification.

## Completion Criteria

Purpose, budget, loading/fallback, interaction, accessibility, and performance constraints are addressed.

---
name: scroll-world-flyby
description: Build a continuous spatial web journey where scroll or equivalent progress drives camera movement, scene transitions, depth, and narrative.
version: 0.5.0
---

# Scroll World / Fly-by Animation

## Purpose

Build a continuous spatial web journey where scroll or equivalent progress drives camera movement, scene transitions, depth, and narrative.

## Core Principle

Scroll World and Fly-by are one discipline: navigation through a spatial scene whose camera and composition evolve with progress.

## Scope

Camera paths, waypoints, scene choreography, progress mapping, depth/parallax, transitions, section synchronization, input, reduced motion, and performance.

## Discovery

Inspect scroll container, renderer, camera, scene graph, sections, assets, triggers, and layout. Establish a normalized timeline and its coordinate system.

## Capability Requirements

Classify material capabilities as FULL, SUITABLE, CONSTRAINED, or UNSUITABLE from evidence available in the current session. Inspect actual model/agent/tool/environment availability; a documented capability is not evidence that it is callable now. Never claim an observation or verification that the available tools cannot support.

## Interaction

Ask for narrative waypoints or journey intent only when content does not establish them.

## Challenge Handling

Challenge scroll hijacking, excessive speed/rotation, disorientation, long forced-scroll sections, hidden content, and expensive per-frame work.

## Execution Workflow

Define route/waypoints → normalize progress → map ranges to camera/target/visibility → bounded interpolation/easing → coherent parallax → prevent clipping/discontinuity → preserve user control → fallback → test forward/reverse/rapid/touch/keyboard/resize.

## Verification

Verify progress math, waypoint boundaries, camera bounds, cleanup, resize, reduced motion, and reverse navigation. Browser testing is required for claims about continuity, jank, or spatial comfort.

## Reporting

Report timeline, camera mapping, input model, performance evidence, fallback, and visual verification.

## Completion Criteria

One coherent spatial system exists; progress is deterministic; users retain control; fallback/accessibility paths exist.

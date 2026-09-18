---
name: scroll-world-flyby
description: Design and implement scroll-driven spatial experiences where scrolling controls camera movement, scene transitions, depth, and cinematic progression through a 3D or simulated 3D world.
version: 0.1.0
---

# Scroll World / Fly-by

## Purpose

The Scroll World / Fly-by skill guides the design and implementation of experiences where the user's scroll position controls movement through a visual world.

This includes:

- cinematic website journeys;
- 3D fly-throughs;
- spatial storytelling;
- camera journeys;
- scroll-controlled scenes;
- section-to-section world transitions;
- parallax environments;
- simulated 3D journeys;
- WebGL-based scroll experiences.

The objective is not simply:

> "Make the page scroll with animations."

The objective is:

> **Map meaningful user progress to a coherent spatial and visual journey.**

---

# Core Principle

## Scroll Is a Progress Signal

Treat scroll position as a progression value.

Conceptually:

```text
scroll position
      ↓
normalized progress
      ↓
scene state
      ↓
camera / object / environment changes
```

Do not attach unrelated animations directly to arbitrary scroll events.

The current scroll position should correspond to a predictable state of the experience.

---

# Spatial Continuity

A conventional animated page may use:

```text
scroll
↓
fade section
↓
fade next section
```

A scroll world instead creates continuity:

```text
scroll
↓
move through space
↓
approach object
↓
transition environment
↓
continue journey
↓
arrive at next scene
```

The defining characteristic is spatial continuity.

A page does not become a scroll world merely because it contains several scroll-triggered animations.

---

# Scope

This skill covers:

- scroll progress;
- normalized timelines;
- local scene progress;
- camera paths;
- camera orientation;
- camera targets;
- camera waypoints;
- scene sequencing;
- scene states;
- spatial transitions;
- parallax;
- depth;
- object choreography;
- section synchronization;
- pinned scenes;
- 3D/WebGL integration;
- simulated 3D;
- responsive behavior;
- touch scrolling;
- accessibility;
- reduced motion;
- performance;
- asset loading;
- fallback behavior;
- runtime verification.

Use `3d-web-design` for general 3D rendering architecture.

Use `animation-design` for general motion principles.

Use `ui-ux-design` for broader interaction, layout, hierarchy, and accessibility decisions.

---

# Before Implementation

Inspect the existing project before choosing an implementation strategy.

Determine:

- frontend framework;
- rendering architecture;
- existing animation libraries;
- existing scroll libraries;
- 3D libraries;
- canvas components;
- routing;
- page sections;
- responsive breakpoints;
- asset structure;
- existing camera systems;
- existing scene systems;
- performance conventions;
- accessibility conventions.

Look for existing technologies such as:

- CSS transforms;
- Web Animations API;
- Framer Motion;
- GSAP;
- ScrollTrigger;
- Three.js;
- React Three Fiber;
- Babylon.js;
- WebGL;
- Intersection Observer;
- native scroll APIs.

Do not introduce another animation or scroll framework without justification.

---

# Discover Before Asking

Determine from the project:

- framework;
- rendering architecture;
- existing scroll utilities;
- existing animation system;
- available 3D assets;
- existing page structure;
- responsive strategy;
- browser support expectations;
- accessibility implementation.

Do not ask the user for information that the repository already provides.

Ask only when the information represents a genuine user decision or cannot reasonably be discovered.

---

# Determine the Experience Type

Identify which experience is actually required.

Possible types:

```text
2D PARALLAX
Layered depth illusion.

CAMERA JOURNEY
Camera moves through a predefined path.

OBJECT JOURNEY
Objects move while the camera remains relatively stable.

SECTION WORLD
Each page section represents a different scene.

CINEMATIC SEQUENCE
Scroll controls a directed visual sequence.

EXPLORATION
User has greater control over spatial movement.
```

Do not build a full 3D world when layered 2D motion provides the same result.

---

# Determine the Spatial Model

Before implementation, determine whether the experience is:

```text
REAL 3D
Actual geometry, camera, lighting and depth.

SIMULATED 3D
2D assets combined with perspective, scale and parallax.

HYBRID
A real 3D subject surrounded by 2D or DOM-based content.
```

Do not assume that "cinematic" means "WebGL."

---

# Challenge Unnecessary Complexity

Challenge implementation assumptions when there is a substantive reason.

Examples:

- WebGL is unnecessary;
- CSS transforms can provide the requested effect;
- a static image communicates the same concept;
- dozens of large assets are loaded for a simple journey;
- multiple animation libraries are introduced;
- scroll locking interferes with navigation;
- mobile performance is likely to degrade;
- the visual effect obscures content.

A challenge should identify:

```text
OBSERVATION
↓
CONSEQUENCE
↓
ALTERNATIVE
↓
USER DECISION
```

Do not challenge subjective aesthetic preferences simply because another aesthetic is possible.

---

# User Intent

Determine:

```text
What should the user experience?
What should scrolling communicate?
What information should appear at each stage?
What should the user remember?
What is the destination of the journey?
```

A technically impressive camera journey without a clear purpose is not automatically a successful experience.

---

# Spatial Story Structure

Before coding a complex world, define the journey.

Example:

```text
SCENE 01
Introduction
    ↓
SCENE 02
Approach
    ↓
SCENE 03
Product reveal
    ↓
SCENE 04
Feature exploration
    ↓
SCENE 05
Call to action
```

Each scene should have a purpose.

For each scene, identify:

- what the user sees;
- what the camera is doing;
- what objects are doing;
- what content is visible;
- what changes from the previous scene;
- what the user should understand;
- how the scene ends.

---

# Scene Definition

A scene can define:

```text
id
start progress
end progress
camera state
object state
environment state
content state
transition
purpose
```

Example:

```javascript
{
  id: "product-reveal",
  start: 0.20,
  end: 0.35,
  camera: {
    position: [...],
    target: [...]
  },
  objects: {
    product: {
      position: [...],
      rotation: [...],
      scale: [...]
    }
  }
}
```

The exact representation depends on the project's architecture.

Do not create an elaborate scene configuration framework for a two-scene page unless the complexity is justified.

---

# Scene Boundaries

A scene should have a clear beginning and end.

Example:

```text
0.00 → 0.20
INTRO

0.20 → 0.40
APPROACH

0.40 → 0.60
REVEAL

0.60 → 0.80
DETAIL

0.80 → 1.00
CTA
```

Avoid overlapping scene ownership unless the overlap is intentional.

If two systems independently control the same camera property, the final state can become difficult to predict.

---

# Normalized Progress

Normalize scroll progress where possible:

```text
0.0 → beginning
0.5 → middle
1.0 → end
```

Conceptually:

```javascript
progress = clamp(
  scrollPosition / scrollRange,
  0,
  1
);
```

A normalized timeline reduces dependence on a particular viewport height or document pixel length.

---

# Local Scene Progress

For a scene spanning:

```text
0.25 → 0.50
```

derive local progress:

```text
0.25 → 0
0.50 → 1
```

Conceptually:

```javascript
localProgress =
  (globalProgress - sceneStart) /
  (sceneEnd - sceneStart);
```

Clamp the result to:

```text
0 → 1
```

This allows each scene to define its own animation independently.

---

# Normalized Timeline

A complex experience should have an understandable normalized timeline.

Example:

```text
GLOBAL TIMELINE

0.00 ───────── 0.15
INTRODUCTION

0.15 ───────── 0.35
APPROACH

0.35 ───────── 0.55
PRIMARY REVEAL

0.55 ───────── 0.75
FEATURE JOURNEY

0.75 ───────── 1.00
CONCLUSION
```

Avoid scattered values such as:

```javascript
if (scrollY > 421) ...
if (scrollY > 913) ...
if (scrollY > 1482) ...
```

Prefer a central timeline representation where practical.

---

# Waypoints

Complex camera journeys should use explicit waypoints rather than arbitrary camera values scattered throughout components.

A waypoint can define:

```text
progress
position
target
optional rotation
optional field of view
optional scene state
```

Example:

```javascript
const waypoints = [
  {
    progress: 0.00,
    position: [0, 1, 8],
    target: [0, 0, 0]
  },
  {
    progress: 0.35,
    position: [2, 2, 5],
    target: [0, 1, 0]
  },
  {
    progress: 0.70,
    position: [-2, 3, 3],
    target: [1, 0, 0]
  },
  {
    progress: 1.00,
    position: [0, 2, 7],
    target: [0, 0, 0]
  }
];
```

Waypoints make the intended journey explicit and easier to tune.

---

# Mapping Functions

Do not assume all properties should move linearly.

Use appropriate mappings for:

- position;
- rotation;
- scale;
- opacity;
- camera movement;
- lighting;
- environment transitions.

Conceptually:

```text
scroll progress
↓
mapping function
↓
property value
```

Possible mappings include:

- linear;
- ease-in;
- ease-out;
- ease-in-out;
- clamped interpolation;
- piecewise interpolation;
- curve interpolation.

---

# Easing

Camera motion can feel mechanical when mapped directly to linear scroll.

Use easing when appropriate.

However, do not introduce easing everywhere.

Excessive smoothing can create perceived input lag:

```text
user scrolls
↓
camera reacts later
↓
user perceives lag
```

The user should generally understand why the scene is currently in its state.

---

# Scrubbing

A scrubbed animation means:

```text
scroll forward
→ animation moves forward

scroll backward
→ animation reverses
```

This creates a direct relationship between user progress and scene state.

For cinematic experiences, this is often more coherent than triggering independent one-shot animations.

---

# Reversibility

Users can scroll backward.

The experience should remain correct when progress changes:

```text
0.70 → 0.60 → 0.45 → 0.20
```

Do not assume users only travel forward.

Whenever practical, derive visual state from current progress rather than depending entirely on historical callbacks.

---

# Fast Scrolling

Fast scrolling can skip intermediate positions.

Do not depend on every intermediate frame or threshold being visited.

For continuous animation:

```text
current progress
→ calculate current state
```

For one-shot events:

```text
detect meaningful threshold crossing
→ execute event safely
```

The experience should remain valid even when users rapidly scroll or drag the scrollbar.

---

# Camera Paths

A camera path should define:

- origin;
- destination;
- intermediate points;
- orientation;
- progress range;
- constraints;
- focal target.

Common journey types include:

```text
approach
orbit
rise
descend
pass through
pull back
reveal
follow
```

Each movement should communicate something.

Do not move the camera simply because movement looks impressive.

---

# Camera Position

Camera movement should communicate spatial progression.

Examples:

```text
camera moves forward
→ user approaches subject

camera moves upward
→ environment is revealed

camera pulls backward
→ context becomes visible

camera passes object
→ journey progresses

camera orbits
→ object inspection
```

---

# Camera Target

Moving the camera position without controlling what it looks at can produce unstable composition.

When appropriate, explicitly define:

```text
camera position
+
camera target
```

The target may remain fixed during a simple approach or move independently during a more complex journey.

---

# Camera Path Interpolation

For simple journeys:

```text
linear interpolation
```

may be sufficient.

For complex journeys:

```text
curve / spline interpolation
```

may provide smoother movement.

Do not use splines solely because they are technically sophisticated.

---

# Camera Continuity

Avoid abrupt discontinuities such as:

```text
scene A camera
→ instant scene B camera
```

unless the jump is intentionally designed.

Prefer:

```text
scene A
↓
transition
↓
scene B
```

when continuity is part of the experience.

---

# Camera Orientation

Camera position and orientation should be treated as related but independently controllable concerns.

Possible strategies include:

```text
look-at target
quaternion orientation
Euler rotation
curve tangent
```

Use the approach that matches the rendering architecture.

Avoid mixing multiple orientation systems without a clear ownership model.

---

# Field of View

Field of view influences perceived speed and spatial scale.

Conceptually:

```text
narrow FOV
→ compressed spatial appearance

wide FOV
→ stronger sense of speed and depth
```

Use FOV changes sparingly.

Large changes can produce discomfort or make spatial relationships difficult to understand.

---

# Object Choreography

Objects can:

- enter;
- exit;
- rotate;
- scale;
- move;
- separate;
- assemble;
- reveal information;
- change material or lighting state.

Coordinate these changes with the camera.

A camera and object should not independently compete for visual attention.

---

# Motion Hierarchy

When several things move simultaneously, establish a hierarchy.

A useful order is:

```text
PRIMARY
Camera / major spatial movement

SECONDARY
Primary object movement

TERTIARY
Environment / background movement

MICRO
Particles / decorative effects
```

The most important movement should remain visually dominant.

---

# Depth

Depth can be created using:

```text
foreground
midground
background
```

with different movement rates.

This creates parallax.

In a real 3D scene, depth comes from actual spatial relationships.

In simulated 3D, depth may be communicated through:

- scale;
- perspective;
- blur;
- parallax;
- occlusion;
- lighting;
- shadows.

---

# Parallax

Parallax should support spatial hierarchy.

Example:

```text
foreground → moves more
midground → moderate movement
background → moves less
```

Do not exaggerate movement until the scene becomes visually unstable.

---

# Simulated 3D

A convincing fly-by does not always require real 3D.

Possible techniques:

- layered images;
- CSS transforms;
- scale;
- blur;
- perspective;
- depth-based parallax;
- masks;
- gradients.

Use these when they satisfy the intended experience.

---

# Real 3D

Real 3D is more appropriate when users need:

- true perspective;
- object inspection;
- free camera movement;
- volumetric environments;
- real lighting;
- complex spatial interaction.

Use `3d-web-design` for rendering architecture.

---

# Hybrid Worlds

A hybrid experience can combine:

```text
3D subject
+
DOM text
+
2D background
+
scroll-driven camera
```

A useful ownership model is:

```text
3D layer
→ visual subject

DOM layer
→ semantic content

scroll controller
→ shared progress
```

---

# Scene Transitions

Transitions may use:

- camera travel;
- object movement;
- environmental changes;
- lighting changes;
- fog;
- color changes;
- scale;
- depth;
- opacity.

Avoid stacking every transition technique at once.

A transition should have a dominant mechanism.

---

# Transition Hierarchy

When possible:

```text
spatial continuity
    ↓
camera movement
    ↓
object movement
    ↓
environmental transition
    ↓
micro-effects
```

Do not use visual effects to compensate for poor spatial structure.

---

# Content Synchronization

Important content should be synchronized with scene progression.

Example:

```text
0.00–0.20
Hero

0.20–0.40
Product reveal

0.40–0.60
Feature 01

0.60–0.80
Feature 02

0.80–1.00
CTA
```

Content should not appear so briefly that users cannot read or understand it.

---

# Text in a Scroll World

Text must remain readable while the world moves.

Consider:

- contrast;
- position;
- duration;
- motion;
- hierarchy;
- background complexity;
- responsive layout.

Do not place critical text where camera movement makes it unreadable.

Determine whether text should:

```text
move with the world
```

or:

```text
remain fixed in the interface
```

These communicate different relationships.

---

# Navigation

Do not allow scroll choreography to destroy normal navigation.

Users should still be able to:

- navigate sections;
- use links;
- reach the footer;
- use keyboard navigation;
- use browser controls.

---

# Scroll Hijacking

Avoid aggressive scroll hijacking.

Do not replace normal browser scrolling with custom behavior unless the experience genuinely requires it.

Prefer:

```text
native scroll
+
scroll-linked visual state
```

when possible.

---

# Input Independence

Scroll is not the only input method.

Consider:

- mouse wheel;
- trackpad;
- touch;
- keyboard;
- scrollbar dragging;
- reduced-motion preferences.

Do not assume identical behavior across all devices.

---

# Touch Scrolling

Do not interfere unnecessarily with native touch scrolling.

Avoid:

- preventing default touch behavior without justification;
- trapping the user inside a scene;
- requiring precise gestures for basic navigation;
- assuming wheel-event semantics apply to touch.

---

# Mobile

Mobile scroll experiences require separate consideration.

Possible changes:

```text
desktop 3D journey
↓
simplified mobile journey
```

Possible reductions:

- fewer objects;
- fewer particles;
- fewer post-processing effects;
- shorter camera travel;
- lower asset quality;
- static sections;
- simplified parallax.

Do not simply scale desktop values down.

---

# Responsive Camera

A camera path that looks correct at:

```text
1440 × 900
```

may fail at:

```text
390 × 844
```

Potential problems include:

- subject leaving the frame;
- text overlapping objects;
- excessive perspective;
- insufficient focal space;
- unreadable content.

Use responsive scene parameters when necessary.

---

# Reduced Motion

Respect:

```text
prefers-reduced-motion
```

for substantial motion.

Possible behavior:

```text
full fly-through
↓
reduced camera movement
↓
simplified transitions
↓
static or lightly animated scenes
```

The page should remain understandable without cinematic motion.

---

# Accessibility

The visual journey should not be the only mechanism for communicating content.

Important information should remain available through semantic HTML.

Consider:

- headings;
- landmarks;
- links;
- buttons;
- keyboard navigation;
- focus behavior;
- text alternatives;
- reduced motion;
- readable contrast.

---

# SEO

Important textual content should not exist exclusively inside a WebGL canvas.

Use ordinary HTML for:

- headings;
- descriptions;
- links;
- CTA content;
- meaningful page text.

Use the SEO skill for broader search optimization.

---

# Asset Strategy

Identify assets as:

```text
critical
important
decorative
optional
```

This helps determine loading priority.

---

# Asset Budget

Establish practical limits for:

- model size;
- texture size;
- number of assets;
- initial download;
- total scene memory;
- compressed transfer size.

Do not load every scene's assets during initial page load without justification.

---

# Lazy Loading

Load assets according to their role in the journey.

Possible strategy:

```text
initial scene
↓
load next scene
↓
transition
↓
load following scene
```

Avoid visible loading gaps.

---

# Preloading

Preload assets when the user is likely to reach them soon.

Balance:

```text
loading ahead
vs
unnecessary bandwidth
```

---

# Asset Disposal

If scenes are dynamically unloaded, release resources that are no longer needed.

Consider:

- geometries;
- textures;
- materials;
- render targets;
- animation resources;
- event listeners;
- DOM references.

See `3d-web-design` for detailed 3D resource lifecycle practices.

---

# Rendering Strategy

Determine whether the world requires:

```text
continuous rendering
```

or:

```text
render-on-demand
```

Do not render continuously when nothing visual changes unless the architecture requires it.

---

# Draw Calls

Large worlds can become expensive because of draw calls.

Consider:

- instancing;
- material reuse;
- batching;
- visibility control;
- scene partitioning.

Do not optimize blindly. Measure when performance is important.

---

# Visibility

Only render what contributes meaningfully to the current scene where practical.

Possible techniques:

- frustum culling;
- scene activation;
- distance-based visibility;
- LOD;
- object pooling.

---

# Post-Processing

Use post-processing carefully.

Common effects include:

- bloom;
- depth of field;
- motion blur;
- fog;
- color grading.

Every effect can add rendering cost.

Use effects to reinforce the scene, not to compensate for weak composition.

---

# Loading Experience

The loading state is part of the experience.

Possible states:

```text
INITIALIZING
LOADING
READY
DEGRADED
FAILED
```

Do not leave the user staring at an empty canvas without explanation.

---

# Progressive Scene Loading

For large worlds, consider:

```text
Scene A
↓
prepare Scene B
↓
Scene B becomes active
↓
prepare Scene C
```

Do not unload the current scene before the next scene is sufficiently ready if doing so would expose a visible gap.

---

# State Management

Avoid storing every frame's visual state in a global application state system unless required.

High-frequency animation state should generally remain close to the rendering or animation system.

---

# Component Boundaries

For complex experiences, separate responsibilities where useful:

```text
scene definition
camera
objects
scroll controller
UI
loading
fallback
performance controls
```

Avoid one giant component containing the entire world.

Do not split a small experience into dozens of components solely for architectural appearance.

---

# Data-Driven Scenes

For multiple scenes, consider representing scene configuration as data.

Conceptually:

```javascript
const scenes = [
  {
    id: "intro",
    start: 0,
    end: 0.2
  },
  {
    id: "product",
    start: 0.2,
    end: 0.5
  }
];
```

Benefits include:

- easier timeline tuning;
- clearer scene ownership;
- simpler testing;
- easier reordering;
- reduced scattered constants.

---

# State Ownership

Define which system owns each value.

Example:

```text
scroll controller
→ global progress

scene timeline
→ local scene progress

camera controller
→ camera transform

scene controller
→ active scene

UI
→ semantic content
```

Avoid multiple systems writing to the same camera or object transform.

---

# Deterministic Visual State

Whenever practical, visual state should be derivable from current progress.

Conceptually:

```text
progress = 0.62
↓
scene state = known
↓
camera = known
↓
objects = known
```

This makes:

- reverse scrolling;
- refresh;
- deep linking;
- testing;
- debugging

more reliable.

---

# Routing

If the experience spans multiple routes, determine whether scroll progress is:

```text
route-local
```

or:

```text
global
```

Do not let animation state leak unexpectedly between pages.

---

# Scroll Position Restoration

Consider:

- refresh;
- back navigation;
- deep links;
- restored scroll positions.

The scene should be able to reconstruct the corresponding visual state.

---

# SSR and Hydration

In SSR applications, browser-only APIs and WebGL initialization may need to occur client-side.

Avoid accessing browser-only APIs during server rendering without appropriate handling.

Watch for hydration mismatches caused by client-only scene state.

---

# Browser Capability

Possible limitations include:

- WebGL availability;
- GPU performance;
- memory;
- browser restrictions;
- mobile hardware;
- embedded webviews.

If the experience depends on a capability that may be absent, provide a fallback.

Do not claim universal support without evidence.

---

# Fallback Strategy

Possible fallback levels:

```text
FULL
Full interactive 3D experience.

REDUCED
Simplified effects and fewer assets.

STATIC
Static or lightly animated representation.

CONTENT
Semantic content without the cinematic layer.
```

The fallback should preserve the purpose of the page.

---

# Failure Handling

Handle:

- asset failures;
- WebGL failures;
- unsupported browsers;
- runtime exceptions;
- incomplete scene data;
- loading timeouts;
- unavailable textures;
- renderer initialization failures.

Do not allow one decorative effect to prevent the rest of the page from functioning.

---

# Verification

Verify separately:

```text
SCROLL BEHAVIOR
CAMERA BEHAVIOR
SCENE TRANSITIONS
CONTENT SYNCHRONIZATION
RESPONSIVENESS
ACCESSIBILITY
PERFORMANCE
FALLBACK
```

Do not treat successful compilation as proof that the experience works.

---

# Scroll Verification

Test:

- scrolling forward;
- scrolling backward;
- slow scrolling;
- fast scrolling;
- scrollbar dragging;
- trackpad scrolling;
- touch scrolling.

Check whether progress remains stable and whether visual state corresponds to current position.

---

# Camera Verification

Verify:

- camera starts in the intended location;
- camera follows the intended path;
- camera targets remain correct;
- subject framing is intentional;
- transitions do not jump unexpectedly;
- FOV changes are controlled;
- camera does not clip through important geometry;
- camera does not expose unintended empty space.

---

# Waypoint Verification

When waypoints are used, inspect each important waypoint.

For example:

```text
WAYPOINT 01
progress 0.00

WAYPOINT 02
progress 0.25

WAYPOINT 03
progress 0.50

WAYPOINT 04
progress 0.75

WAYPOINT 05
progress 1.00
```

Verify:

- positions;
- targets;
- orientation;
- scene ownership;
- transition continuity.

Do not only test the beginning and end.

---

# Scene Transition Verification

Check:

```text
scene A
↓
transition
↓
scene B
```

for:

- continuity;
- object visibility;
- camera continuity;
- content timing;
- loading state;
- unexpected flashes;
- overlapping animations.

Verify both forward and reverse movement.

---

# Accessibility Verification

Check:

- semantic headings;
- keyboard reachability;
- visible focus;
- CTA accessibility;
- reduced-motion behavior;
- text alternatives;
- contrast;
- non-canvas content;
- navigation.

Verify that important information remains available when motion is disabled.

---

# Performance Verification

When performance is a requirement, measure:

- frame time;
- rendering cost;
- asset transfer;
- memory;
- scene initialization;
- mobile behavior;
- CPU usage where available;
- GPU workload where measurable.

Do not claim:

```text
60 FPS
smooth
optimized
fast
```

without evidence when those claims matter.

---

# Visual Verification

When visual inspection is available, verify:

- camera composition;
- transition continuity;
- object positioning;
- text readability;
- depth;
- parallax;
- section timing;
- mobile layout;
- loading states;
- fallback states.

If visual inspection is unavailable:

```text
Visual verification: UNVERIFIED.
```

Do not claim that a cinematic sequence looks correct without seeing it.

---

# Evidence

Verification should produce evidence.

Useful evidence includes:

```text
automated test output
browser inspection
screenshots
recordings
performance measurements
network traces
console output
manual interaction results
```

Do not replace evidence with confidence.

---

# Challenge Examples

## Full 3D for Simple Parallax

Request:

> Make five background layers move at different speeds using a full WebGL engine.

Challenge:

```text
Observation:
The requested effect consists primarily of layered depth movement.

Concern:
A WebGL renderer may introduce unnecessary complexity and runtime cost.

Alternative:
Use layered assets with CSS transforms or a lightweight animation system
unless true 3D interaction is required.
```

The user retains the final decision.

---

## Huge Initial Asset

Request:

> Load every 3D environment at page startup.

Challenge:

```text
Observation:
Multiple environments create a large initial asset set.

Concern:
Initial transfer and GPU memory may become unnecessarily large.

Alternative:
Load the first environment immediately and progressively prepare
subsequent scenes.
```

---

## Excessive Scroll Locking

Request:

> Lock the page until the entire animation finishes.

Challenge:

```text
Observation:
The requested interaction prevents normal scrolling behavior.

Concern:
Users may lose navigation control and have difficulty reaching content.

Alternative:
Use a pinned scene while preserving normal document scrolling.
```

---

## Too Many Simultaneous Motions

Request:

> While the camera moves forward, rotate the model, scale it, move the background, animate particles, change lighting, and blur the scene.

Challenge:

```text
Observation:
Multiple visual systems change simultaneously.

Concern:
The focal hierarchy may become unclear.

Alternative:
Make the camera and primary subject the dominant motion, then introduce
secondary effects only where they support the scene.
```

---

# Anti-Patterns

## Random Scroll Animations

Adding unrelated animations because scroll events are available.

## Scroll Hijacking

Replacing browser scrolling with custom behavior unnecessarily.

## Camera Chaos

Changing position, rotation, FOV, and target independently without a coherent spatial plan.

## No Scene Structure

Hard-coding hundreds of scroll thresholds throughout components.

## One Giant Timeline

Creating an unmaintainable animation timeline containing every object and transition.

## Scattered Thresholds

Using unrelated pixel values throughout the application without a documented relationship.

## Desktop-Only Experience

Assuming mouse wheel behavior applies to mobile.

## Motion Without Meaning

Animating elements without improving communication or experience.

## WebGL by Default

Using a 3D engine when CSS or ordinary animation would accomplish the same result.

## Giant Initial Payload

Loading the entire world before meaningful content appears.

## No Reduced-Motion Path

Making the experience inaccessible or uncomfortable for users who request reduced motion.

## Canvas-Only Content

Putting critical information exclusively inside the rendered scene.

## Event-Dependent Visual State

Making the final visual state depend on which scroll callbacks happened to execute.

## Multiple Scroll Sources

Using several independent systems to calculate scroll progress.

## Multiple Camera Owners

Allowing several components or systems to write to the same camera transform without coordination.

## Giant Component

Putting the entire experience into one component.

## Unverified Cinematic Claims

Claiming that camera paths, transitions, responsiveness, or performance are correct without appropriate verification.

---

# Example: Basic Fly-Through

```text
page scroll
    ↓
normalize progress
    ↓
calculate local scene progress
    ↓
interpolate camera
    ↓
interpolate object transforms
    ↓
update scene
    ↓
render
```

---

# Example: Waypoint-Based Journey

```text
WAYPOINT 01
0.00
Starting position

        ↓

WAYPOINT 02
0.25
Approach subject

        ↓

WAYPOINT 03
0.50
Reveal subject

        ↓

WAYPOINT 04
0.75
Move into environment

        ↓

WAYPOINT 05
1.00
Final composition
```

---

# Example: Multi-Scene Journey

```text
SCENE 01
0.00 → 0.20
Intro

SCENE 02
0.20 → 0.45
Camera approaches product

SCENE 03
0.45 → 0.70
Product rotates and features appear

SCENE 04
0.70 → 0.90
Camera pulls into environment

SCENE 05
0.90 → 1.00
CTA
```

---

# Example: Responsive Degradation

Desktop:

```text
full 3D environment
camera travel
particles
lighting effects
```

Mobile:

```text
simplified environment
shorter camera travel
fewer particles
reduced effects
```

Reduced motion:

```text
static scenes
minimal transitions
normal document navigation
```

All three should communicate the same underlying content.

---

# Example: Hybrid Implementation

```text
DOM
├── heading
├── description
├── CTA
└── navigation

CANVAS
├── 3D product
├── environment
└── lighting

SCROLL CONTROLLER
└── normalized progress
```

---

# Example: Progressive Loading

```text
INITIAL LOAD
    ↓
load critical assets
    ↓
render first scene
    ↓
prepare next scene
    ↓
transition
    ↓
activate next scene
    ↓
prepare following scene
```

---

# Example: Reduced Motion

Normal:

```text
scroll
↓
camera moves
↓
objects move
↓
environment transitions
```

Reduced motion:

```text
scroll
↓
scene changes
↓
minimal or no camera movement
↓
content remains visible
```

---

# Example: Failure Fallback

If WebGL fails:

```text
WebGL unavailable
      ↓
disable cinematic renderer
      ↓
retain semantic content
      ↓
show static representation where available
      ↓
keep navigation functional
```

---

# Completion Criteria

The Scroll World / Fly-by skill is complete when:

- [ ] the purpose of the spatial journey is understood;
- [ ] existing animation and rendering architecture was inspected;
- [ ] the simplest suitable implementation approach was selected;
- [ ] unnecessary WebGL or framework complexity was challenged;
- [ ] the experience is structured into meaningful scenes;
- [ ] scene ownership is clear;
- [ ] scroll progress is normalized or otherwise predictably represented;
- [ ] local scene progress is handled correctly;
- [ ] a normalized timeline exists for complex journeys;
- [ ] camera movement is intentional;
- [ ] camera targets are intentional;
- [ ] camera waypoints are coherent where needed;
- [ ] camera interpolation is predictable;
- [ ] scene transitions are coherent;
- [ ] object choreography supports the camera journey;
- [ ] motion hierarchy is clear;
- [ ] depth and parallax support spatial understanding;
- [ ] content is synchronized with scene progression;
- [ ] text remains readable;
- [ ] normal navigation remains usable;
- [ ] scroll hijacking is avoided unless justified;
- [ ] reverse scrolling works;
- [ ] fast scrolling does not break the experience;
- [ ] touch behavior is considered;
- [ ] keyboard navigation remains usable;
- [ ] mobile behavior is considered;
- [ ] responsive camera composition is handled where necessary;
- [ ] reduced motion is supported where appropriate;
- [ ] important content is available outside the canvas;
- [ ] assets are loaded appropriately;
- [ ] unnecessary rendering work is avoided;
- [ ] resource disposal is handled where required;
- [ ] failures have a usable fallback where practical;
- [ ] SSR/client boundaries are handled where relevant;
- [ ] scroll position restoration is considered;
- [ ] scroll behavior is tested in both directions;
- [ ] camera waypoints are verified;
- [ ] scene transitions are verified;
- [ ] accessibility is verified;
- [ ] visual verification is performed when available;
- [ ] performance claims are evidence-based;
- [ ] unverified behavior is explicitly reported.

The goal is not:

> **"Make scrolling control a bunch of animations."**

The goal is:

> **"Turn user progress into a coherent spatial journey without sacrificing usability, accessibility, performance, or user control."**

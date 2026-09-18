---
name: 3d-web-design
description: Design and implement performant, responsive, interactive 3D web experiences with appropriate rendering architecture, asset handling, interaction, accessibility, and graceful degradation.
version: 0.1.0
---

# 3D Web Design

## Purpose

The 3D Web Design skill guides an agent in designing and implementing 3D experiences for the web.

The objective is not simply to place a 3D model on a webpage.

A successful 3D web experience must balance:

- visual quality;
- user interaction;
- performance;
- loading behavior;
- responsiveness;
- accessibility;
- device capabilities;
- maintainability.

3D should serve the product or experience rather than become an unnecessary technical dependency.

---

# Core Principle

## Use 3D When It Provides Real Value

3D is justified when it meaningfully improves:

- spatial understanding;
- product visualization;
- storytelling;
- immersion;
- interaction;
- navigation;
- visual communication.

Do not introduce WebGL or a 3D engine merely because it looks impressive.

---

# Scope

This skill covers:

- WebGL-based experiences;
- Three.js;
- React Three Fiber;
- Babylon.js;
- 3D model viewers;
- product configurators;
- interactive scenes;
- camera systems;
- lighting;
- materials;
- textures;
- 3D assets;
- scene composition;
- interaction;
- responsive 3D;
- loading;
- performance;
- fallbacks.

For specialized scroll-driven worlds or fly-through experiences, use:

```text
scroll-world-flyby
```

in addition to this skill.

---

# Before Implementing 3D

Inspect:

- existing rendering libraries;
- existing canvas components;
- asset directories;
- model formats;
- shader usage;
- texture pipeline;
- camera architecture;
- animation system;
- responsive system;
- performance constraints.

Do not introduce a second 3D framework into an existing project without a reason.

---

# Discover Before Asking

Inspect the repository for:

- Three.js;
- React Three Fiber;
- Babylon.js;
- WebGL utilities;
- `.glb`;
- `.gltf`;
- `.fbx`;
- `.obj`;
- texture assets;
- HDR/environment maps;
- existing canvas components.

Determine what already exists before asking the user.

---

# Determine the 3D Requirement

Clarify what role 3D plays.

Possible roles:

```text
PRODUCT VIEWER
Inspect and rotate an object.

CONFIGURATOR
Change properties of a 3D object.

ENVIRONMENT
Explore a 3D space.

HERO
Provide visual storytelling.

DATA VISUALIZATION
Represent spatial data.

NAVIGATION
Move through a virtual environment.

CINEMATIC
Deliver a controlled visual sequence.
```

The implementation strategy depends heavily on this role.

---

# 3D Complexity

Estimate scene complexity before implementation.

Consider:

- number of objects;
- polygon count;
- material count;
- texture resolution;
- texture count;
- lighting complexity;
- shadows;
- post-processing;
- animation;
- particle count;
- physics;
- interaction.

Do not treat every 3D scene as equivalent.

---

# Rendering Architecture

Choose the simplest suitable architecture.

Possible approaches:

```text
CSS 3D
↓
Canvas/WebGL
↓
Three.js
↓
React Three Fiber
↓
Babylon.js
```

Use CSS 3D when the effect is simple enough.

Use WebGL when true 3D rendering is required.

---

# Framework Selection

If the project already uses a framework:

- follow its integration patterns;
- reuse existing rendering abstractions;
- avoid unnecessary framework changes.

For React projects, React Three Fiber may be appropriate when the project benefits from declarative React integration.

For non-React projects, use an architecture appropriate to the existing stack.

Do not select technology solely from personal preference.

---

# Scene Structure

A 3D scene should have clear ownership.

Typical structure:

```text
Scene
├── Camera
├── Lighting
├── Environment
├── Main Objects
├── Effects
└── Interaction Layer
```

Keep scene responsibilities understandable.

---

# Camera

The camera is part of the experience.

Determine:

- perspective or orthographic projection;
- position;
- target;
- field of view;
- movement;
- limits;
- responsive behavior.

Do not allow camera movement to become disorienting.

---

# Perspective vs Orthographic

Perspective is generally useful for:

- realistic spatial scenes;
- environments;
- cinematic experiences;
- product presentation with depth.

Orthographic can be useful for:

- diagrams;
- technical visualization;
- controlled object presentation.

Choose based on the visual requirement.

---

# Camera Controls

Camera controls should define:

- rotation limits;
- zoom limits;
- pan limits;
- damping;
- interaction modality.

Avoid allowing unrestricted camera movement unless exploration is explicitly desired.

---

# Camera Orientation

Users should maintain spatial orientation.

Avoid:

- sudden unexplained camera jumps;
- extreme FOV changes;
- uncontrolled rotations;
- disorienting transitions.

For cinematic movement, use intentional sequencing.

---

# Lighting

Lighting should support:

- object readability;
- depth;
- hierarchy;
- atmosphere.

Consider:

```text
key light
fill light
rim light
environment light
ambient contribution
```

The exact setup depends on the scene.

---

# Real-Time Shadows

Shadows can improve depth but can be expensive.

Consider:

- shadow map resolution;
- number of shadow-casting lights;
- number of shadow receivers;
- device performance.

Do not enable high-resolution shadows everywhere by default.

---

# Materials

Use materials appropriate to the visual requirement.

Consider:

- physically based rendering;
- roughness;
- metalness;
- normal maps;
- environment reflections;
- transparency.

Avoid unnecessary shader complexity.

---

# Textures

Texture quality affects both visual quality and memory.

Consider:

- dimensions;
- compression;
- format;
- mipmaps;
- reuse;
- loading size.

Do not use a 4K texture for a tiny object.

---

# Texture Memory

Large textures can consume significant GPU memory.

A scene with many large textures can fail on constrained devices even when polygon counts are modest.

Optimize texture memory alongside geometry.

---

# 3D Asset Formats

Prefer efficient web-compatible formats when possible.

For many web workflows:

```text
GLB / glTF
```

is a strong default because it can package geometry, materials, and related assets efficiently.

Do not convert assets blindly; inspect the existing pipeline first.

---

# Asset Optimization

Before shipping an asset, consider:

- polygon reduction;
- mesh compression;
- texture compression;
- unused material removal;
- unused animation removal;
- duplicate asset elimination.

Do not reduce quality beyond what the visual requirement permits.

---

# Asset Loading

Large 3D assets should generally not block the entire application unnecessarily.

Consider:

```text
initial UI
↓
loading state
↓
asset loading
↓
scene initialization
↓
interactive state
```

Provide useful feedback where loading takes noticeable time.

---

# Progressive Loading

For complex scenes, consider:

- low-detail placeholder;
- staged asset loading;
- prioritized assets;
- lazy loading;
- level of detail.

Do not load every asset immediately if only a small portion is initially visible.

---

# Loading Failure

Handle:

- missing model;
- failed texture;
- network failure;
- unsupported format;
- initialization error.

The page should remain understandable when 3D fails.

---

# Graceful Degradation

A 3D feature should have an appropriate fallback when possible.

Examples:

```text
3D viewer
↓
static product image
```

or:

```text
interactive 3D hero
↓
static hero composition
```

The fallback depends on the product requirement.

---

# Device Capability

Consider that users may have:

- high-end desktop GPUs;
- integrated graphics;
- mobile GPUs;
- old devices;
- battery-constrained devices.

Do not assume the development machine represents the target population.

---

# Capability Detection

Where appropriate, detect:

- WebGL availability;
- renderer limitations;
- reduced-motion preference;
- device constraints;
- asset support.

Do not build complicated device detection without a demonstrated need.

---

# Responsive 3D

Responsive 3D may require more than resizing the canvas.

Consider changing:

- camera position;
- field of view;
- object scale;
- scene composition;
- interaction;
- effect complexity;
- asset quality.

---

# Mobile 3D

Mobile devices often have tighter:

- GPU limits;
- memory limits;
- thermal limits;
- battery constraints.

Consider simplified scenes and reduced effects.

---

# Device Pixel Ratio

Very high pixel ratios increase rendering cost.

Consider limiting effective pixel ratio for performance-sensitive scenes.

Do not blindly render at maximum device pixel ratio.

---

# Render Loop

Understand what causes frames to render.

Possible models:

```text
continuous rendering
```

or:

```text
on-demand rendering
```

Use continuous rendering when the scene genuinely requires it.

Use on-demand rendering where the scene is mostly static.

---

# Continuous Rendering

Continuous rendering may be required for:

- animation;
- physics;
- dynamic lighting;
- interactive scenes.

But it also consumes resources.

Do not keep a full render loop running for a static model when unnecessary.

---

# Animation

For 3D animation:

- define animation ownership;
- manage lifecycle;
- avoid unnecessary updates;
- clean up animation mixers/resources;
- respect reduced motion where applicable.

For complex scroll-driven animation, use the Scroll World/Fly-by skill.

---

# Interaction

3D interaction may include:

- pointer;
- touch;
- drag;
- zoom;
- rotation;
- hover;
- click;
- keyboard.

Choose interaction based on the actual task.

---

# Pointer Interaction

Raycasting and pointer interaction can become expensive in large scenes.

Limit interactive targets where possible.

Do not raycast every object if only a few objects can be selected.

---

# Touch Interaction

Touch controls need deliberate handling.

Consider:

- drag conflicts with page scrolling;
- pinch-to-zoom;
- touch target size;
- accidental activation.

Do not simply reuse desktop pointer behavior unchanged.

---

# Keyboard Interaction

Important 3D interactions should not depend exclusively on pointer input.

Where practical, provide:

- keyboard access;
- alternative controls;
- accessible descriptions;
- equivalent actions.

---

# Hover in 3D

Hover is unavailable on touch devices.

If hover reveals important information, provide an alternative interaction.

---

# Object Selection

Selected objects should have clear feedback.

Possible signals:

- outline;
- highlight;
- material change;
- label;
- camera movement.

Do not rely only on subtle visual changes.

---

# Labels and Annotations

For complex 3D scenes, labels can improve comprehension.

Consider:

- readability;
- occlusion;
- responsive behavior;
- interaction;
- screen-reader alternatives.

Do not cover the scene with unnecessary labels.

---

# Physics

Physics engines can add significant complexity.

Use physics when the interaction genuinely requires physical behavior.

Do not add physics merely to make an object move.

---

# Particle Systems

Particles can create atmosphere but may become expensive.

Consider:

- particle count;
- update frequency;
- transparency;
- overdraw;
- mobile performance.

Use them intentionally.

---

# Post-Processing

Effects such as:

- bloom;
- depth of field;
- motion blur;
- chromatic aberration;
- ambient occlusion

can increase rendering cost.

Use only effects that materially improve the intended experience.

---

# Transparency and Overdraw

Transparent materials can be expensive because of overdraw and sorting.

Use transparency only when required.

Optimize transparent layers on constrained devices.

---

# Shaders

Custom shaders provide control but increase complexity.

Before writing a custom shader:

- determine whether a built-in material works;
- determine whether an existing shader utility exists;
- consider maintenance;
- consider compatibility.

Do not introduce shader complexity for a trivial visual effect.

---

# WebGL Context Loss

Long-running or resource-intensive WebGL applications should consider context loss.

Where practical, provide a recoverable experience.

Do not assume the WebGL context will remain available forever.

---

# Resource Cleanup

When a 3D component is removed:

- dispose geometries;
- dispose materials;
- release textures;
- remove listeners;
- stop animation loops;
- dispose controls;
- clean up renderers where appropriate.

Memory leaks are particularly costly in 3D applications.

---

# Scene Disposal

Disposal should follow ownership.

Do not dispose a resource still used by another scene or component.

Shared resources require explicit ownership rules.

---

# Memory Management

Monitor:

- GPU memory;
- texture memory;
- geometry;
- render targets;
- post-processing buffers.

Large scenes can fail from memory pressure even when CPU usage appears acceptable.

---

# Render Targets

Render targets can consume significant GPU memory.

Create only those required for:

- post-processing;
- reflections;
- shadows;
- off-screen rendering.

Dispose them appropriately.

---

# 3D and UI Integration

A 3D canvas should coexist cleanly with UI.

Consider:

```text
3D layer
+
UI layer
+
interaction boundaries
```

Define pointer-event ownership carefully.

---

# Canvas Sizing

Ensure canvas dimensions track the intended layout.

Avoid:

- stretched rendering;
- incorrect aspect ratio;
- blurry output;
- unnecessary full-page rendering.

---

# Aspect Ratio

Update camera projection when the viewport changes.

For perspective cameras, aspect ratio affects visual composition.

A stale projection can cause distorted or cropped scenes.

---

# Resize Handling

Handle:

- viewport resize;
- orientation changes;
- container size changes.

Prefer observing the actual rendering container when appropriate rather than assuming the entire window defines the scene.

---

# Accessibility

3D interfaces can create accessibility challenges.

Consider providing:

- descriptive text;
- alternative representations;
- keyboard interaction;
- reduced-motion behavior;
- meaningful labels;
- non-3D fallback.

Do not assume that a visually impressive 3D scene is accessible by default.

---

# Reduced Motion

For significant camera movement, rotation, zoom, or animated objects:

```text
prefers-reduced-motion
```

should influence behavior where appropriate.

Possible behavior:

```text
full cinematic motion
↓
reduced transition
↓
static state
```

---

# SEO and 3D

Important textual content should not exist only inside the 3D canvas.

If a 3D scene communicates important information, provide meaningful HTML content where appropriate.

Do not expect search engines or assistive technologies to interpret arbitrary WebGL content as ordinary page content.

---

# 3D and SEO

Use the SEO skill for:

- headings;
- metadata;
- semantic content;
- structured data;
- crawlable text.

The 3D scene should enhance the page rather than become the only representation of important information.

---

# 3D and Animation

Use Animation Design for:

- motion principles;
- easing;
- transition behavior;
- reduced motion;
- interaction feedback.

This skill focuses on the 3D rendering and scene architecture.

---

# 3D and Scroll World/Fly-by

Use Scroll World/Fly-by when the experience includes:

- camera travel through a world;
- scene sequencing;
- scroll-controlled progression;
- spatial storytelling;
- fly-through transitions.

Do not duplicate that specialized methodology here.

---

# Performance Strategy

For performance-sensitive scenes, optimize in this order:

```text
Remove unnecessary work
↓
Reduce asset cost
↓
Reduce rendering complexity
↓
Reduce effects
↓
Measure
↓
Tune
```

Do not immediately optimize arbitrary code without evidence.

---

# Performance Budget

For significant 3D experiences, establish practical budgets for:

```text
asset size
texture memory
polygon/triangle count
draw calls
render resolution
loading time
frame time
```

Exact budgets depend on the target audience and hardware.

---

# Draw Calls

Many small objects/materials can increase draw calls.

Possible strategies:

- instancing;
- material reuse;
- batching;
- merging compatible geometry.

Do not merge objects if doing so breaks required interaction or animation.

---

# Instancing

Instancing is useful when many objects share:

- geometry;
- material;
- behavior.

Examples:

```text
particles
trees
repeated products
crowds
stars
```

Use it where repeated rendering is actually a bottleneck.

---

# Level of Detail

LOD can reduce complexity based on distance.

Use it when:

- scenes are large;
- camera distance varies significantly;
- geometry cost matters.

Do not add LOD machinery to a tiny scene without justification.

---

# Culling

Use frustum or visibility culling where appropriate.

Do not spend significant CPU work implementing custom culling unless the scene requires it.

---

# Performance Measurement

When performance matters, measure:

- frame time;
- FPS where meaningful;
- draw calls;
- triangle count;
- memory;
- load time;
- asset transfer size.

Avoid relying solely on subjective smoothness.

---

# Testing

For 3D experiences, test:

- scene initialization;
- asset loading;
- interaction;
- resize;
- cleanup;
- fallback;
- error handling;
- relevant devices/browsers.

Where automated testing cannot validate visual behavior, supplement it with runtime/visual inspection.

---

# Browser Testing

When browser access exists, inspect:

- console errors;
- WebGL errors;
- network requests;
- asset failures;
- frame behavior;
- layout;
- interaction.

---

# Device Testing

For significant experiences, representative device testing is valuable.

Consider:

```text
desktop
mobile
integrated GPU
high-performance GPU
```

The exact matrix should reflect the target audience.

---

# Verification

3D verification should distinguish:

```text
code correctness
runtime correctness
visual correctness
performance correctness
```

These are separate claims.

---

# Visual Verification

When visual inspection is available, verify:

- composition;
- camera;
- lighting;
- materials;
- model appearance;
- interaction;
- responsive layout.

If unavailable:

```text
Visual verification: UNVERIFIED.
```

---

# Performance Verification

Do not claim:

```text
smooth
fast
60 FPS
low memory
```

without appropriate evidence when these are important requirements.

---

# Failure Modes

Consider:

```text
WebGL unavailable
asset fails
texture fails
shader fails
context lost
device too slow
memory pressure
network slow
canvas sizing error
```

The interface should fail gracefully where practical.

---

# Challenge Conditions

Challenge a 3D requirement when there is evidence of:

- unnecessary complexity;
- severe performance cost;
- excessive asset size;
- accessibility conflict;
- unsupported device assumptions;
- unnecessary dependencies;
- visual complexity that harms usability.

Example:

> Load a 500 MB model on the homepage.

Challenge:

```text
Concern:
The asset size may create unacceptable loading and mobile performance costs.

Alternative:
Use an optimized web asset and progressively load higher-detail geometry.
```

---

# Do Not Challenge Aesthetic Preference

Do not challenge:

```text
"I want a dark 3D scene."
"I prefer glossy materials."
"I want a dramatic camera."
```

merely because another aesthetic is possible.

Challenge when the preference creates a substantive technical or usability issue.

---

# Anti-Patterns

## 3D for Decoration

Using WebGL without a meaningful product or communication benefit.

---

## Framework Duplication

Introducing another 3D framework when the project already has an appropriate one.

---

## Maximum Quality Everywhere

Using maximum textures, shadows, effects, and pixel ratio on every device.

---

## Giant Assets

Shipping unoptimized models and textures.

---

## Permanent Render Loop

Continuously rendering a static scene without need.

---

## No Fallback

Allowing 3D failure to produce a broken page.

---

## Desktop-Only Interaction

Designing interaction exclusively around mouse controls.

---

## Canvas-Only Content

Putting important content exclusively inside WebGL.

---

## No Cleanup

Leaving geometries, textures, listeners, or animation loops alive after unmount.

---

## Performance by Guess

Calling a scene performant without measurement when performance is a requirement.

---

# Example: Product Viewer

Request:

> Add a 3D product viewer.

Process:

```text
Inspect existing rendering stack
↓
Inspect available product assets
↓
Optimize model/textures
↓
Create scene
↓
Configure camera
↓
Add controlled rotation/zoom
↓
Add loading/failure state
↓
Add responsive behavior
↓
Add fallback
↓
Verify runtime and visual behavior
```

---

# Example: 3D Hero

Request:

> Add a 3D hero to the homepage.

First determine:

```text
Does 3D improve the hero's communication?
What content must remain readable?
What happens on mobile?
What is the loading budget?
What happens if WebGL is unavailable?
```

Do not automatically replace the entire hero with a canvas.

---

# Example: Static Scene

A product is displayed in a mostly static 3D scene.

Prefer:

```text
on-demand rendering
```

if continuous rendering is unnecessary.

Do not run a permanent animation loop simply because a 3D renderer exists.

---

# Example: Many Repeated Objects

A scene contains hundreds of identical objects.

Consider:

```text
instancing
```

before creating hundreds of independent meshes.

---

# Completion Criteria

The 3D Web Design skill is complete when:

- [ ] the purpose of 3D is understood;
- [ ] existing rendering architecture was inspected;
- [ ] appropriate rendering technology was selected;
- [ ] scene structure is coherent;
- [ ] camera behavior is intentional;
- [ ] assets are appropriately optimized;
- [ ] loading behavior is handled;
- [ ] failure/fallback behavior is considered;
- [ ] responsive behavior is implemented;
- [ ] interaction is appropriate to input modality;
- [ ] accessibility is considered;
- [ ] reduced motion is considered;
- [ ] resources are cleaned up;
- [ ] performance implications are considered;
- [ ] performance is measured when required;
- [ ] visual verification is performed when required and available;
- [ ] unverified visual/performance claims are explicitly reported.

The goal is not:

> **"Put 3D on the website."**

The goal is:

> **"Use 3D when it provides meaningful value, and implement it in a way that remains usable, responsive, maintainable, and performant."**
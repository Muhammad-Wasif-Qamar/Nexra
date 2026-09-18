---
name: animation-design
description: Design and implement purposeful, performant, accessible, and coherent motion for interfaces and web experiences.
version: 0.1.0
---

# Animation Design

## Purpose

The Animation Design skill guides an agent in designing and implementing motion that improves:

- comprehension;
- continuity;
- feedback;
- hierarchy;
- orientation;
- perceived responsiveness;
- visual storytelling.

Animation should have a purpose.

The objective is not to maximize the amount of motion.

---

# Core Principle

## Motion Should Communicate Something

A useful animation should help the user understand one or more of:

```text
What changed?
Where did it come from?
Where did it go?
What can I interact with?
What is happening?
What should I notice?
What happens next?
```

If removing an animation does not reduce clarity, feedback, continuity, or intentional visual expression, question whether it is necessary.

---

# Scope

This skill covers:

- transitions;
- micro-interactions;
- page transitions;
- entrance/exit animations;
- hover states;
- press states;
- loading animations;
- feedback animations;
- scroll-triggered motion;
- parallax;
- camera movement;
- timeline-based animation;
- choreographed sequences;
- responsive motion;
- reduced-motion behavior;
- animation performance.

It does not replace:

- UI/UX Design;
- 3D Web Design;
- Scroll World / Fly-by;
- performance optimization;
- accessibility-specific analysis.

Use those skills when their specialized concerns are relevant.

---

# Before Animating

First inspect:

- existing animation libraries;
- existing motion utilities;
- CSS transitions;
- animation tokens;
- component conventions;
- reduced-motion handling;
- rendering architecture;
- current performance constraints.

Do not introduce a new animation system before inspecting what already exists.

---

# Discover Before Asking

Determine from the project:

- framework;
- rendering model;
- existing animation library;
- supported browsers;
- responsive system;
- existing motion patterns;
- component architecture.

Ask the user only for information that cannot reasonably be discovered.

---

# Animation Intent

Identify the role of the motion.

Common roles:

```text
FEEDBACK
Confirms an interaction.

TRANSITION
Connects one state to another.

ORIENTATION
Shows spatial or navigational relationship.

HIERARCHY
Draws attention to important content.

STATUS
Communicates loading, success, failure, or progress.

STORYTELLING
Creates intentional visual progression.

DELIGHT
Adds personality without compromising usability.
```

A single animation can have multiple roles.

---

# Animation Hierarchy

Not every element should move equally.

Consider:

```text
Primary event
↓
Supporting motion
↓
Ambient motion
```

Important motion should remain distinguishable from decorative motion.

---

# Timing

Animation timing should reflect:

- interaction speed;
- distance;
- visual complexity;
- importance;
- expected user attention.

Very short animations may feel abrupt.

Very long animations may feel slow.

Do not select durations arbitrarily when an existing system defines them.

---

# Duration Consistency

Related interactions should have related timing.

For example:

```text
button feedback
< component transition
< page transition
```

The exact values depend on the product.

Consistency is generally more important than a universal numeric rule.

---

# Easing

Use easing to communicate physical or conceptual behavior.

Common patterns:

```text
ease-out
```

for elements entering or settling.

```text
ease-in
```

for elements leaving.

```text
ease-in-out
```

for movement between stable states.

Do not apply the same easing curve to every animation automatically.

---

# Motion Distance

Movement should generally be proportional to the relationship being communicated.

Small UI changes should not travel huge distances.

Large spatial transitions can justify larger movement.

---

# Direction

Motion direction should support spatial understanding.

For example:

```text
panel opens from right
→
content appears to originate from right
```

Directional consistency helps users construct a mental model.

---

# Continuity

Use motion to preserve continuity when:

```text
state A
↓
state B
```

would otherwise feel disconnected.

Examples:

- expanding a card;
- opening a modal;
- changing tabs;
- navigating between related views.

---

# Micro-Interactions

Micro-interactions can communicate:

- hover;
- press;
- selection;
- completion;
- validation;
- focus;
- drag state.

Keep them subtle enough not to interfere with the primary task.

---

# Hover

Hover animation should:

- respond quickly;
- communicate interactivity;
- avoid excessive movement;
- not be the only indication of an action.

Remember that hover does not exist on many touch devices.

---

# Press

Press feedback should communicate that the interaction was received.

Possible signals:

- small scale change;
- color transition;
- shadow change;
- state transition.

Do not create excessive movement for a simple button press.

---

# Focus

Focus must remain visible and understandable.

Do not remove focus indicators merely because a hover animation exists.

Motion should support focus, not replace accessibility semantics.

---

# Loading Animation

Loading motion should communicate ongoing work.

Consider:

- expected duration;
- whether progress is measurable;
- whether a skeleton is more informative;
- whether the user can cancel;
- whether repeated animations become distracting.

Do not animate a loading indicator indefinitely after the operation has completed.

---

# Success Animation

Success motion should provide clear confirmation without distracting from the next action.

Examples:

- checkmark transition;
- subtle highlight;
- status change;
- progress completion.

---

# Error Animation

Error motion can attract attention, but should not rely on motion alone.

Consider:

- clear text;
- color/state;
- focus;
- accessible announcement.

Avoid aggressive shaking that can be distracting or uncomfortable.

---

# Page Transitions

Page transitions should preserve orientation.

Consider:

- whether pages are spatially related;
- whether navigation is immediate;
- whether transition duration delays task completion;
- whether the transition can be interrupted.

Do not animate every route change by default.

---

# Interruptibility

Animations should generally tolerate interruption.

For interactive interfaces:

```text
start
↓
user changes mind
↓
reverse/cancel/settle
```

Avoid animations that lock the user into unnecessary sequences.

---

# State Transitions

Prefer animating meaningful state changes rather than continuously animating static elements.

Example:

```text
collapsed
→
expanded
```

is often useful.

```text
card
→
permanent floating movement
```

may add little value.

---

# Scroll-Driven Animation

Scroll-driven motion should connect animation progress to user-controlled scrolling.

Consider:

- scroll progress;
- page length;
- frame/timeline mapping;
- interruption;
- reverse scrolling;
- responsive behavior;
- reduced motion;
- performance.

Do not assume every scroll interaction needs parallax.

---

# Scroll vs Time

Choose the appropriate driver.

Use:

```text
scroll
```

when animation should represent spatial reading or progression.

Use:

```text
time
```

when the animation represents an autonomous event.

Use:

```text
interaction
```

when motion should respond directly to user action.

---

# Parallax

Parallax can establish depth.

Use carefully.

Potential problems include:

- excessive movement;
- motion sickness;
- performance cost;
- loss of content alignment;
- mobile usability.

Parallax should reinforce hierarchy rather than become the entire experience.

---

# Staggering

Staggering can help communicate grouping.

Example:

```text
item 1
↓
item 2
↓
item 3
```

Avoid excessive stagger delays that make the interface feel slow.

---

# Choreography

Complex sequences should define:

```text
trigger
↓
primary event
↓
supporting event
↓
settled state
```

Do not create a collection of unrelated animations and call it choreography.

---

# Animation State Machine

Complex motion benefits from explicit states.

Example:

```text
IDLE
↓
ENTERING
↓
ACTIVE
↓
EXITING
↓
IDLE
```

This can prevent:

- conflicting animations;
- race conditions;
- stuck states;
- inconsistent cleanup.

---

# Animation Ownership

Determine which layer owns motion.

Possible ownership:

```text
component
page
layout
scene
global navigation
```

Avoid multiple layers independently controlling the same property.

---

# Avoid Competing Controllers

If two systems manipulate:

```text
transform
opacity
position
scale
```

they may produce conflicts.

Define ownership clearly.

---

# CSS vs JavaScript

Prefer the simplest appropriate mechanism.

Use CSS when:

- transitions are simple;
- states are declarative;
- no complex runtime control is needed.

Use JavaScript/framework animation when:

- animation depends on application state;
- sequencing is complex;
- physics/interpolation is required;
- timeline control is required.

Do not use JavaScript for a simple CSS transition without a reason.

---

# Animation Libraries

Before adding a library:

1. inspect existing dependencies;
2. determine whether current tools are sufficient;
3. assess bundle/runtime cost;
4. assess compatibility;
5. assess maintenance;
6. consider whether the new abstraction will be reused.

Do not add a library for one trivial fade.

---

# Transform and Opacity

Where appropriate, prefer properties that can be efficiently animated.

Common candidates:

```text
transform
opacity
```

Avoid expensive layout-triggering animation when an equivalent composited approach is possible.

This is guidance, not a universal rule.

---

# Layout Animation

Animating:

```text
width
height
top
left
```

can cause layout work.

Sometimes layout animation is necessary.

When it is not necessary, consider:

```text
transform
opacity
```

instead.

Measure when performance is important.

---

# Rendering Performance

Watch for:

- excessive DOM updates;
- unnecessary React/Vue/etc. renders;
- large animated layers;
- expensive filters;
- blur;
- shadows;
- continuous canvas rendering;
- excessive particle counts;
- unnecessary layout recalculation.

Do not optimize purely by assumption.

---

# Continuous Animation

Continuous motion is more expensive and more visually demanding than event-driven motion.

Question continuous animation when it:

- consumes CPU/GPU;
- distracts from content;
- drains battery;
- causes accessibility problems.

Prefer event-driven motion when it communicates the same thing.

---

# GPU Considerations

GPU acceleration is not automatically free.

Large layers, filters, textures, and 3D scenes can increase:

- memory usage;
- power consumption;
- thermal load.

Do not blindly add `will-change` or force GPU layers everywhere.

---

# `will-change`

Use `will-change` only when there is a meaningful performance reason.

Avoid applying it globally to many elements.

---

# Motion and Responsiveness

Animation should adapt to viewport constraints.

Consider:

- shorter travel distance on mobile;
- simplified sequences;
- fewer simultaneous elements;
- different camera behavior;
- reduced decorative motion.

Do not assume desktop motion maps directly to mobile.

---

# Reduced Motion

Respect:

```css
@media (prefers-reduced-motion: reduce)
```

where applicable.

Reduced-motion behavior can include:

- removing decorative motion;
- shortening transitions;
- disabling parallax;
- replacing animated transitions with instant state changes;
- retaining essential feedback without large movement.

---

# Reduced Motion Is Not Always Zero Motion

Some motion communicates state or orientation.

Where appropriate, preserve essential state feedback while reducing unnecessary movement.

The exact behavior depends on the interface.

---

# Motion Sensitivity

Avoid:

- rapid flashing;
- aggressive shaking;
- uncontrolled camera movement;
- excessive zoom;
- rapid perspective changes.

Motion should remain comfortable for the intended audience.

---

# Accessibility

Motion must not be the sole communication mechanism.

If animation communicates:

```text
success
error
selection
progress
```

provide another signal where appropriate.

---

# Input Modality

Consider:

```text
mouse
touch
keyboard
pen
screen reader
```

An interaction designed around hover alone is incomplete.

---

# Animation and UX

Animation should never compensate for poor information architecture.

If users cannot understand:

```text
what happened
```

without watching a long animation, the UI has a communication problem.

---

# Animation and Branding

Motion can contribute to brand identity through:

- timing;
- easing;
- rhythm;
- spatial language;
- transition style.

Brand motion should remain usable.

Do not prioritize brand expression over interaction clarity.

---

# Motion Language

For products with significant animation, define a consistent motion language.

Possible dimensions:

```text
duration
easing
distance
scale
direction
opacity
stagger
```

Reuse the language across related components.

---

# Motion Tokens

If the project uses design tokens, motion can be represented as tokens.

Example:

```text
duration-fast
duration-normal
duration-slow

ease-standard
ease-emphasized

distance-small
distance-medium
distance-large
```

Use the project's actual naming conventions.

---

# Animation Architecture

For larger motion systems, separate:

```text
motion definition
trigger
state
rendering
accessibility behavior
```

This improves maintainability.

---

# Animation Cleanup

When animations finish or components unmount:

- remove listeners;
- cancel timers;
- cancel animation frames;
- release resources;
- stop observers;
- prevent stale callbacks.

Animation bugs often arise from incomplete lifecycle cleanup.

---

# Event Listeners

Scroll, resize, pointer, and animation listeners should be managed correctly.

Avoid:

```text
listener added on every render
```

without appropriate cleanup.

---

# RequestAnimationFrame

Use `requestAnimationFrame` appropriately for frame-based browser animation.

Avoid uncontrolled loops.

A loop should have:

```text
start condition
update
stop condition
cleanup
```

---

# Scroll Performance

Avoid expensive work on every scroll event when possible.

Consider:

- passive listeners;
- throttling;
- requestAnimationFrame;
- intersection observers;
- CSS scroll-linked animation where appropriate.

Use the simplest solution that satisfies the requirement.

---

# Intersection Observation

Intersection-based animation is useful for:

- reveal-on-scroll;
- lazy activation;
- entering viewport effects.

Do not use heavy scroll calculations when visibility is all that matters.

---

# Animation Failure States

Consider what happens when:

- assets fail;
- JavaScript fails;
- animation library fails;
- user disables motion;
- device is slow;
- viewport changes;
- component unmounts mid-animation.

The underlying interface should remain usable.

---

# Graceful Degradation

Animation should enhance the interface rather than become a hard dependency for basic usability.

Example:

```text
Animation available:
rich transition.

Animation unavailable:
instant but functional state change.
```

---

# 3D and Advanced Motion

When motion controls:

- 3D camera;
- WebGL scene;
- spatial world;
- fly-through;
- cinematic sequence;

use the specialized 3D Web Design or Scroll World/Fly-by skill in addition to this skill.

Do not duplicate specialized methodology here.

---

# Challenging Animation Requirements

Challenge when there is evidence of:

- severe performance impact;
- accessibility conflict;
- confusing motion;
- unnecessary dependency complexity;
- interaction blocking;
- excessive animation;
- impossible timing requirements.

Example:

> Animate every card continuously.

Response:

```text
Concern:
Continuous animation across all cards may increase rendering cost and visual distraction.

Alternative:
Use motion on entry/interaction and keep resting cards static.
```

The user retains the decision.

---

# Do Not Challenge Taste

Do not challenge purely subjective preferences such as:

```text
"I want slower animations."
"I like subtle bounce."
"I want a cinematic transition."
```

unless there is a substantive consequence.

---

# Verification

Animation verification should evaluate:

- trigger;
- timing;
- state transitions;
- interruption;
- responsive behavior;
- reduced-motion behavior;
- visual result;
- performance where relevant.

---

# Visual Verification

If the task is visually sensitive and browser/visual inspection is available:

- inspect the animation;
- verify timing and composition;
- inspect different viewport sizes;
- check intermediate states where relevant.

If visual inspection is unavailable:

```text
Visual verification: UNVERIFIED.
```

Do not claim the animation looks correct.

---

# Performance Verification

For performance-sensitive motion, measure where possible.

Possible evidence:

- frame rate;
- frame time;
- CPU/GPU utilization;
- browser performance traces;
- memory usage;
- long tasks.

Do not claim:

```text
60 FPS
```

without evidence.

---

# Animation Checklist

### Intent

- [ ] Animation has a defined purpose.
- [ ] Motion supports the user's task.
- [ ] Decorative motion is not overwhelming.

### Timing

- [ ] Duration is appropriate.
- [ ] Easing is coherent.
- [ ] Related transitions use consistent timing.

### Interaction

- [ ] Trigger is clear.
- [ ] Motion can be interrupted where appropriate.
- [ ] State transitions are coherent.
- [ ] Focus behavior remains correct.

### Responsive

- [ ] Mobile behavior considered.
- [ ] Desktop behavior considered.
- [ ] Motion does not cause overflow.

### Accessibility

- [ ] Reduced-motion behavior considered.
- [ ] Motion is not the only communication mechanism.
- [ ] Rapid/flashing motion is avoided.

### Performance

- [ ] Expensive properties were considered.
- [ ] Continuous loops are justified.
- [ ] Event listeners are managed.
- [ ] Animation cleanup exists.
- [ ] Performance was measured where required.

### Engineering

- [ ] Existing animation system was inspected.
- [ ] Unnecessary dependencies were avoided.
- [ ] Animation ownership is clear.
- [ ] No unrelated animation architecture was introduced.

---

# Anti-Patterns

## Animation Everywhere

Moving every component simply because motion is available.

---

## Infinite Decoration

Continuous animation with no meaningful communication.

---

## Blocking Animation

Forcing users to wait for unnecessary transitions.

---

## Hover-Only Interaction

Using hover as the only way to reveal functionality.

---

## No Reduced Motion

Ignoring user motion preferences.

---

## JavaScript for Everything

Using complex runtime animation for simple state transitions.

---

## Library Explosion

Adding multiple animation libraries for isolated effects.

---

## Competing Controllers

Multiple systems independently controlling the same visual property.

---

## Unbounded Animation Loop

Starting animation loops without a clear stop and cleanup mechanism.

---

## Performance by Assumption

Claiming an animation is performant without measurement when measurement is required.

---

## Decorative Compensation

Using animation to hide weak UX or unclear information architecture.

---

# Example: Button Interaction

Request:

> Make the button feel more responsive.

Implementation:

```text
hover → subtle transition
press → immediate pressed state
focus → visible focus indicator
disabled → no misleading interaction animation
```

Do not add a large bounce animation unless the product context calls for it.

---

# Example: Page Transition

Request:

> Add smooth transitions between pages.

Process:

```text
Inspect routing system
↓
Inspect existing animation system
↓
Determine whether route transitions are supported
↓
Define enter/exit behavior
↓
Avoid delaying navigation unnecessarily
↓
Support reduced motion
↓
Verify visually and functionally
```

---

# Example: Scroll Animation

Request:

> Make the hero respond to scrolling.

Determine:

```text
What should move?
What should remain fixed?
What represents scroll progress?
What happens when scrolling reverses?
What happens on mobile?
What happens with reduced motion?
```

Do not automatically add parallax to every element.

---

# Example: Complex Sequence

Request:

> Create a cinematic landing animation.

Plan:

```text
Initial state
↓
Hero enters
↓
Primary content appears
↓
Supporting elements settle
↓
User interaction becomes available
```

Avoid blocking interaction longer than necessary.

---

# Completion Criteria

The Animation Design skill is complete when:

- [ ] animation purpose is defined;
- [ ] existing motion architecture was inspected;
- [ ] timing and easing are coherent;
- [ ] interaction states are handled;
- [ ] animation ownership is clear;
- [ ] responsive behavior is considered;
- [ ] reduced-motion behavior is considered;
- [ ] accessibility is considered;
- [ ] performance implications are considered;
- [ ] cleanup is implemented;
- [ ] unnecessary dependencies are avoided;
- [ ] visual verification is performed when required and available;
- [ ] unverified visual/performance claims are explicitly identified.

The goal is not:

> **"Add more animation."**

The goal is:

> **"Use motion to make interaction, state, hierarchy, and spatial relationships clearer without compromising usability or performance."**
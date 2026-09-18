---
name: ui-ux-design
description: Design and implement usable, coherent, accessible, responsive, and visually intentional user interfaces based on user goals, project context, and existing design systems.
version: 0.1.0
---

# UI/UX Design

## Purpose

The UI/UX Design skill guides an agent in designing and implementing interfaces that are:

- understandable;
- usable;
- visually coherent;
- responsive;
- accessible;
- consistent with the product's purpose;
- consistent with the existing project where appropriate.

The goal is not to make an interface merely "look good."

The goal is to create an interface that helps users accomplish the intended task with appropriate visual hierarchy, interaction design, feedback, and information architecture.

---

# Core Principle

## Design for the User's Task

A UI decision should be connected to:

```text
User
↓
Goal
↓
Information
↓
Action
↓
Feedback
↓
Outcome
```

Do not optimize visual appearance while ignoring the user's actual task.

---

# Scope

This skill covers:

- interface structure;
- information architecture;
- visual hierarchy;
- layout;
- typography;
- color;
- spacing;
- component design;
- interaction patterns;
- responsive behavior;
- accessibility;
- states;
- feedback;
- navigation;
- forms;
- buttons and controls;
- cards;
- dialogs;
- dashboards;
- landing pages;
- application interfaces;
- design-system usage.

This skill does not replace:

- accessibility-specific analysis;
- security analysis;
- performance optimization;
- animation design;
- 3D design;
- SEO;
- content strategy.

Those concerns should be integrated where relevant and delegated to specialized skills when available.

---

# Before Designing

Do not immediately start designing.

First understand:

- what is being built;
- who uses it;
- what users need to accomplish;
- where the interface exists in the product;
- existing design conventions;
- existing components;
- existing responsive behavior;
- technical constraints;
- available visual references;
- explicit user preferences.

Use Project Discovery before asking the user for information that can be discovered from the repository.

---

# Design Context

Determine as much as possible about:

```text
PRODUCT
What the product does.

USER
Who uses the interface.

TASK
What the user needs to accomplish.

CONTEXT
Where and when the interface is used.

PLATFORM
Web, mobile, desktop, embedded, etc.

DEVICE
Relevant viewport/device constraints.

BRAND
Existing visual identity.

SYSTEM
Existing components/design tokens.

TECHNOLOGY
Framework and UI implementation constraints.
```

---

# Discover Before Asking

Inspect the project for:

- existing component libraries;
- design tokens;
- theme files;
- CSS variables;
- Tailwind configuration;
- typography;
- color definitions;
- spacing scales;
- existing layouts;
- reusable components;
- responsive breakpoints;
- icon systems;
- existing pages;
- accessibility conventions.

Do not ask:

> What colors do you use?

if the project already defines its color system.

---

# Existing Design System

If a design system exists:

1. identify it;
2. understand its tokens;
3. reuse its components;
4. preserve established conventions;
5. extend it only when necessary.

Do not create a second design system inside an existing application without justification.

---

# No Existing Design System

If no meaningful design system exists, establish a lightweight system appropriate to the task.

Consider:

```text
colors
typography
spacing
radius
shadows
borders
breakpoints
component states
```

Keep the system proportional to the project.

A small website does not require a 200-token design system.

---

# User Intent

Separate:

```text
What the user explicitly requested
```

from:

```text
What the interface needs to accomplish
```

Example:

User:

> Make the dashboard more modern.

The agent should determine what "modern" means in context rather than arbitrarily applying a visual trend.

Potential dimensions include:

- typography;
- spacing;
- hierarchy;
- interaction;
- density;
- color;
- component consistency;
- motion.

If the decision is subjective and materially affects the result, ask a targeted question or present a small set of options.

---

# Subjective vs Objective Decisions

Some decisions can be inferred from evidence.

Examples:

```text
Existing primary color → discoverable.
Existing spacing scale → discoverable.
Existing breakpoint → discoverable.
Required keyboard access → accessibility requirement.
Preferred visual style → potentially subjective.
Brand personality → potentially subjective.
```

Do not turn subjective preferences into technical facts.

---

# Visual Hierarchy

Every interface should communicate relative importance.

Consider:

```text
Primary action
↓
Secondary action
↓
Supporting information
↓
Optional information
```

Use:

- size;
- position;
- contrast;
- whitespace;
- typography;
- grouping;
- alignment

to establish hierarchy.

Do not make every element visually prominent.

---

# Information Architecture

Before styling complex interfaces, determine:

- what information exists;
- how it is grouped;
- what users need first;
- what users need later;
- how users navigate between sections;
- what actions belong together.

A visually polished interface with poor information architecture remains difficult to use.

---

# Layout

Choose layout based on content and task.

Common structures:

- single-column;
- split layout;
- grid;
- sidebar;
- top navigation;
- dashboard;
- content/detail;
- master/detail;
- wizard;
- modal workflow.

Do not select a layout solely because it is visually fashionable.

---

# Alignment

Use consistent alignment relationships.

Consider:

- page margins;
- content columns;
- headings;
- controls;
- cards;
- tables;
- navigation.

Alignment should make relationships obvious.

---

# Spacing

Use a consistent spacing system.

Avoid arbitrary values unless required by the design.

Prefer relationships such as:

```text
section spacing
>
component spacing
>
internal spacing
>
text spacing
```

Spacing should communicate grouping and hierarchy.

---

# Typography

Typography should establish:

- hierarchy;
- readability;
- emphasis;
- scanning structure.

Consider:

- font family;
- font size;
- weight;
- line height;
- letter spacing;
- text width.

Avoid excessive font sizes or weights.

---

# Text Width

Long lines reduce readability.

For text-heavy interfaces, constrain line length appropriately.

Do not force every layout into maximum-width containers when the content type does not require it.

---

# Color

Use color intentionally.

A basic semantic system may include:

```text
primary
secondary
background
surface
text
muted
border
success
warning
error
info
```

Color should communicate hierarchy and state rather than decorate every component.

---

# Contrast

Ensure important content remains distinguishable.

Check:

- body text;
- labels;
- buttons;
- links;
- form controls;
- error states;
- disabled states;
- overlays.

Do not rely on color alone to communicate meaning.

---

# Components

Prefer reusable components when the project architecture supports them.

Examples:

```text
Button
Input
Select
Card
Modal
Navbar
Sidebar
Tabs
Toast
Dropdown
Table
Pagination
```

Reuse should reduce inconsistency without creating unnecessary abstraction.

---

# Component Abstraction

Do not abstract prematurely.

A component is a good candidate for reuse when:

- the pattern repeats;
- behavior is shared;
- styling is shared;
- accessibility behavior is shared;
- maintenance benefits from centralization.

Avoid creating components for every `<div>`.

---

# Component States

Interactive components should consider relevant states.

For example:

```text
default
hover
focus
active
disabled
loading
success
error
selected
empty
```

Not every component needs every state.

---

# Buttons

Buttons should communicate:

- what action occurs;
- importance of the action;
- whether the action is available;
- current state.

Use clear action labels.

Prefer:

```text
Save changes
Create project
Continue
```

over vague labels such as:

```text
Submit
Click here
Okay
```

when a more specific label is possible.

---

# Links vs Buttons

Use semantic controls.

Use:

```text
link
```

for navigation.

Use:

```text
button
```

for actions.

Do not use clickable `<div>` elements when semantic controls are available.

---

# Forms

Forms should provide:

- clear labels;
- appropriate input types;
- validation;
- useful error messages;
- clear submission behavior;
- understandable required fields;
- appropriate focus handling.

Avoid making users guess what went wrong.

---

# Form Validation

Validation should distinguish:

```text
missing input
invalid format
invalid value
server-side rejection
```

Messages should explain how to correct the problem.

Avoid:

```text
Invalid input.
```

when a more actionable message is possible.

---

# Error States

Design errors intentionally.

An error state should communicate:

```text
what happened
+
what the user can do
```

Example:

```text
Unable to load projects.
Try again.
```

Do not leave users with blank screens or unexplained failures.

---

# Loading States

Loading states should reflect expected duration.

Possible approaches:

- inline progress;
- skeleton;
- spinner;
- disabled action;
- optimistic update.

Avoid unnecessary loading indicators for operations that complete nearly instantly.

---

# Empty States

An empty state should distinguish:

```text
no data yet
```

from:

```text
failed to load
```

A useful empty state may provide:

- explanation;
- next action;
- relevant guidance.

---

# Success Feedback

Users should know when important actions succeed.

Examples:

- inline confirmation;
- toast;
- state change;
- redirect;
- updated content.

Avoid excessive success notifications for trivial interactions.

---

# Navigation

Navigation should reflect the information architecture.

Consider:

- current location;
- hierarchy;
- primary destinations;
- secondary destinations;
- mobile behavior;
- keyboard access.

Do not hide essential navigation behind unnecessarily complex interactions.

---

# Responsive Design

Design for supported viewport classes rather than one fixed screen.

Consider:

```text
mobile
tablet
desktop
large desktop
```

Use the project's established breakpoints where possible.

---

# Responsive Behavior

Elements may:

- resize;
- reflow;
- stack;
- collapse;
- scroll;
- hide;
- transform into another control.

Choose behavior based on importance and usability.

Do not simply shrink desktop UI until it technically fits.

---

# Mobile Interfaces

On smaller screens:

- prioritize essential content;
- maintain usable touch targets;
- avoid excessive horizontal scrolling;
- preserve readable text;
- simplify navigation where appropriate.

Do not assume desktop interaction patterns transfer directly to mobile.

---

# Accessibility

Accessibility is part of UI quality.

Consider:

- semantic HTML;
- keyboard navigation;
- focus visibility;
- accessible names;
- labels;
- headings;
- contrast;
- reduced motion;
- screen-reader semantics;
- touch target size.

Do not rely solely on automated accessibility tools.

---

# Keyboard Interaction

Interactive elements should generally be reachable and usable with the keyboard.

Check:

- tab order;
- focus visibility;
- Enter/Space behavior;
- Escape behavior for dismissible overlays;
- focus restoration.

Avoid creating keyboard traps.

---

# Focus

Focus should be intentionally managed for:

- dialogs;
- menus;
- forms;
- navigation;
- dynamic content.

When opening a modal, focus should move appropriately.

When closing it, focus should generally return to the triggering context.

---

# Semantic Structure

Use appropriate HTML elements.

Prefer:

```html
button
a
nav
main
header
footer
section
form
label
```

over generic containers when semantics apply.

---

# Screen Readers

Do not use ARIA to compensate for incorrect HTML when semantic HTML solves the problem.

Prefer:

```html
<button>
```

over:

```html
<div role="button">
```

when possible.

---

# Reduced Motion

If the interface contains significant motion, consider:

```text
prefers-reduced-motion
```

Respect users who request reduced motion.

The Animation Design skill handles deeper motion design.

---

# Interaction Design

Good interaction should communicate:

```text
possible
→
action
→
feedback
→
result
```

Users should understand:

- what can be interacted with;
- what happened after interaction;
- what state the system is currently in.

---

# Feedback Timing

Feedback should occur close enough to the action that the relationship is obvious.

Avoid:

- delayed unexplained notifications;
- feedback that disappears too quickly;
- feedback unrelated to the action.

---

# Progressive Disclosure

Do not expose every option immediately when doing so creates unnecessary complexity.

Use progressive disclosure when:

- advanced options are uncommon;
- information is secondary;
- workflows are complex.

Do not hide important information merely to make the interface look simpler.

---

# Modals

Use modals for focused interruptions.

Good use cases:

- confirmation;
- focused form;
- important decision;
- contextual workflow.

Avoid using modals for ordinary navigation or large application flows when a dedicated page is clearer.

---

# Confirmation Dialogs

Confirmation should be proportional to consequence.

High-impact destructive actions may require confirmation.

Low-risk actions generally should not create unnecessary friction.

Use specific language:

```text
Delete project?
This will permanently remove the project and its data.
```

rather than:

```text
Are you sure?
```

---

# Destructive Actions

Make destructive actions distinguishable.

Consider:

- explicit labels;
- confirmation;
- undo;
- warnings;
- consequences.

Do not make destructive actions visually or interactively indistinguishable from ordinary actions.

---

# Search

Search interfaces should clarify:

- what is searchable;
- whether results are live or submitted;
- what filters apply;
- what happens when no results exist.

For large datasets, consider:

- debouncing;
- pagination;
- result counts;
- filters;
- sorting.

The implementation should follow project architecture and performance constraints.

---

# Tables

Tables should support scanning.

Consider:

- column hierarchy;
- alignment;
- density;
- responsive behavior;
- sorting;
- filtering;
- pagination;
- empty states;
- loading;
- errors.

Do not force complex tables into unusable mobile layouts.

---

# Cards

Cards should represent meaningful content groupings.

Avoid excessive cardification where every piece of information becomes a separate bordered box.

Use whitespace and hierarchy when borders are unnecessary.

---

# Dashboards

Dashboards should prioritize:

```text
important metrics
↓
current state
↓
actionable information
↓
secondary detail
```

Avoid filling the dashboard with metrics merely because data is available.

---

# Landing Pages

Landing pages should establish:

```text
value proposition
↓
supporting evidence
↓
primary action
↓
additional information
↓
secondary actions
```

Do not sacrifice clarity for visual effects.

---

# Design References

If the user provides:

- screenshots;
- design files;
- websites;
- mockups;
- component references;

treat them as evidence of desired direction.

Do not blindly copy unrelated patterns from references.

Extract relevant properties such as:

- spacing;
- hierarchy;
- typography;
- composition;
- interaction;
- motion;
- density.

---

# Design from a Screenshot

When reproducing a screenshot:

Inspect:

- overall composition;
- grid;
- spacing;
- typography;
- colors;
- borders;
- shadows;
- imagery;
- responsive implications.

Do not claim pixel-perfect reproduction without appropriate visual verification.

---

# Brand Consistency

If brand assets exist, inspect and reuse:

- logos;
- colors;
- typography;
- imagery;
- iconography;
- tone.

Do not replace established branding merely because another style is fashionable.

---

# Visual Trends

Trends can be useful, but they are not requirements.

Examples:

- glassmorphism;
- gradients;
- oversized typography;
- brutalism;
- minimalism;
- 3D;
- animated backgrounds.

Use a trend only when it supports the product's context.

---

# Avoid Decoration-First Design

Do not add:

- gradients;
- shadows;
- blur;
- animations;
- decorative icons;
- floating elements

without a purpose.

Visual complexity should not obscure interaction or information hierarchy.

---

# Design Tradeoffs

UI decisions often involve tradeoffs.

Examples:

```text
visual density vs readability
animation vs performance
customization vs consistency
minimalism vs discoverability
decoration vs clarity
flexibility vs simplicity
```

When a tradeoff materially affects the user's goal, surface it.

Do not silently optimize for the agent's preferred aesthetic.

---

# User Preferences

Subjective preferences belong to the user.

Examples:

```text
"Use rounded cards."
"Make the interface darker."
"Use slower transitions."
"Keep the typography oversized."
```

Do not challenge a preference merely because it differs from the agent's taste.

Challenge when there is a substantive issue such as:

- accessibility;
- usability;
- performance;
- maintainability;
- contradiction with requirements.

---

# Challenging UI Requirements

A UI requirement should be challenged when there is evidence of a material problem.

Examples:

```text
"Hide the navigation on desktop."

Potential issue:
Users may lose access to core destinations.
```

```text
"Use tiny gray text everywhere."

Potential issue:
Readability and contrast may suffer.
```

```text
"Animate every component continuously."

Potential issue:
Performance and cognitive load.
```

The user retains the final decision.

---

# UI Performance

Consider:

- image size;
- asset loading;
- layout shifts;
- excessive DOM complexity;
- unnecessary re-renders;
- animation cost;
- large component trees.

Do not optimize prematurely.

Measure when performance is a stated requirement or there is evidence of a problem.

---

# Images

Use appropriately sized images.

Consider:

- intrinsic dimensions;
- responsive sizing;
- lazy loading;
- modern formats;
- loading priority;
- alt text.

Do not load enormous assets for small UI elements.

---

# Icons

Prefer a consistent icon system.

Do not mix unrelated icon styles without a reason.

Icons should support comprehension rather than replace necessary labels.

---

# Motion

Motion should communicate:

- state changes;
- hierarchy;
- continuity;
- spatial relationships;
- feedback.

For advanced motion work, use the Animation Design skill.

---

# UI Implementation Discipline

When implementing a design:

1. inspect existing UI architecture;
2. identify reusable components;
3. establish or reuse tokens;
4. implement structure;
5. implement styling;
6. implement interaction;
7. implement responsive behavior;
8. implement accessibility;
9. verify visually and functionally.

Do not start by adding decorative styling before understanding structure.

---

# Visual Verification

UI changes should be visually inspected when browser/visual capability is available.

Check:

- spacing;
- alignment;
- typography;
- overflow;
- hierarchy;
- interaction states;
- responsive layouts;
- loading/error/empty states.

If visual inspection is unavailable, report:

```text
Visual verification: UNVERIFIED
```

Do not claim that the UI "looks correct."

---

# UI Review Checklist

Before considering a UI task complete:

### Structure

- [ ] Information hierarchy is clear.
- [ ] Layout supports the user's task.
- [ ] Navigation is understandable.

### Visual

- [ ] Typography is coherent.
- [ ] Spacing is consistent.
- [ ] Colors are intentional.
- [ ] Components are visually consistent.

### Interaction

- [ ] Interactive elements communicate their state.
- [ ] Feedback exists for important actions.
- [ ] Error states are understandable.
- [ ] Loading states are appropriate.

### Responsive

- [ ] Supported viewport classes are considered.
- [ ] Content does not overflow unexpectedly.
- [ ] Mobile interactions remain usable.

### Accessibility

- [ ] Semantic elements are used.
- [ ] Keyboard interaction works where relevant.
- [ ] Focus behavior is appropriate.
- [ ] Labels and accessible names exist.
- [ ] Contrast is considered.
- [ ] Motion preferences are considered.

### Engineering

- [ ] Existing components were reused where appropriate.
- [ ] No unnecessary dependency was introduced.
- [ ] No unrelated refactor was performed.
- [ ] Relevant tests/checks pass.

---

# Anti-Patterns

## Decoration Before Structure

Making an interface visually impressive before establishing hierarchy.

---

## Screenshot Worship

Copying a reference without understanding the user's actual needs.

---

## One-Viewport Design

Optimizing only for the developer's current screen.

---

## Component Explosion

Creating excessive abstractions that make the code harder to understand.

---

## Design-System Replacement

Replacing an existing design system unnecessarily.

---

## Accessibility Afterthought

Implementing the visual interface first and treating accessibility as optional cleanup.

---

## Motion Everywhere

Adding animation to every element without considering usability or performance.

---

## Color as Meaning

Communicating state using color alone.

---

## Generic Error Messages

Showing errors without telling users what happened or what to do.

---

## Fake Interactivity

Making elements look clickable when they are not, or making non-semantic elements behave like controls without proper accessibility.

---

# Example: Existing Project

User:

> Make the dashboard look more premium.

Correct process:

```text
Inspect project
↓
Identify existing design system
↓
Inspect dashboard structure
↓
Determine current visual limitations
↓
Identify what "premium" should mean in context
↓
Ask only if subjective decisions materially affect the design
↓
Plan changes
↓
Implement
↓
Verify visually
```

Do not immediately replace the entire design system.

---

# Example: Existing Component

User:

> Add a new button to the settings page.

If an existing Button component exists:

```text
Reuse Button.
```

Do not create:

```text
SettingsButton
```

unless there is a meaningful behavioral or architectural reason.

---

# Example: Accessibility Conflict

User:

> Make the text extremely light gray on white.

If contrast becomes inadequate:

```text
Challenge:
The requested contrast may make important text difficult to read.

Alternative:
Use a darker muted tone while preserving the intended visual hierarchy.
```

The user decides after understanding the tradeoff.

---

# Example: Responsive Conflict

User:

> Keep the entire desktop navigation exactly the same on mobile.

If the navigation becomes unusable:

```text
Challenge:
The desktop navigation does not fit the mobile interaction constraints.

Options:
- collapse into a menu;
- use a compact navigation;
- preserve the current structure with horizontal scrolling.

```

Do not silently choose one if the decision materially affects the product.

---

# Example: User Preference

User:

> I want very rounded cards.

If there is no substantive usability or technical problem:

```text
Implement the rounded cards.
```

Do not challenge aesthetic preference merely because it is subjective.

---

# Completion Criteria

The UI/UX Design skill is complete when:

- [ ] user goal is understood;
- [ ] relevant project UI conventions were inspected;
- [ ] existing design system/components were considered;
- [ ] information hierarchy is coherent;
- [ ] layout supports the intended task;
- [ ] visual hierarchy is intentional;
- [ ] interaction states are considered;
- [ ] responsive behavior is considered;
- [ ] accessibility is considered;
- [ ] user preferences were respected;
- [ ] substantive UI problems were surfaced rather than silently ignored;
- [ ] implementation follows project conventions;
- [ ] relevant checks were performed;
- [ ] visual verification was performed when required and available;
- [ ] unverified visual behavior is explicitly reported.

The goal is not:

> **"Make the interface beautiful."**

The goal is:

> **"Make the interface understandable, usable, coherent, and appropriate for the user's task."**
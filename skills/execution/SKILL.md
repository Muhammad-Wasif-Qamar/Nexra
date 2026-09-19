---
name: execution
description: Convert an approved task and bounded plan into controlled implementation changes while preserving project conventions, minimizing unrelated modifications, and maintaining a clear record of what was changed.
version: 0.1.0
---

# Execution

## Purpose

Execution defines how Nexra turns an understood and approved task into actual project changes.

Execution begins only after enough discovery, capability assessment, interaction, and planning has occurred to make implementation meaningful.

The objective is:

- implement the requested outcome;
- preserve existing project behavior where it is not intentionally changed;
- make the smallest coherent change that satisfies the requirement;
- avoid unrelated refactoring;
- validate risky increments;
- maintain awareness of assumptions and decisions;
- leave a clear, inspectable final diff.

Execution is not the same as verification.

Changing code does not prove that the requested outcome works.

---

# Core Principle

## Execute the Bounded Change

Every implementation should have a bounded scope.

The agent should know:

- what it is changing;
- why it is changing it;
- what it should not change;
- which constraints apply;
- what evidence will be required afterward.

Avoid turning a focused task into an uncontrolled cleanup operation.

---

# Execution Inputs

Execution should normally receive:

```text
requested outcome
discovered project facts
capability states
user decisions
accepted assumptions
acceptance criteria
bounded change set
verification requirements
```

If critical information is missing, return to the appropriate earlier stage rather than guessing.

---

# Execution Lifecycle

Use an adaptive workflow:

```text
Understand
↓
Bound
↓
Plan
↓
Prepare
↓
Implement
↓
Inspect
↓
Validate incrementally
↓
Review final diff
↓
Hand off to verification
```

The exact depth depends on task complexity.

---

# Execution Readiness

Before making changes, determine:

- the target area is known;
- the requested behavior is sufficiently understood;
- relevant constraints are known;
- required capabilities are available;
- necessary user decisions are resolved;
- the change scope is bounded;
- the intended verification method is known.

Do not require a formal checklist for trivial edits.

For significant work, make these conditions explicit.

---

# Bounded Change Set

A bounded change set identifies:

```text
TARGET
What should change.

SCOPE
Which parts of the project may change.

EXCLUSIONS
What should remain untouched.

DEPENDENCIES
What related files/components may need modification.

CONSTRAINTS
What must remain true.

ACCEPTANCE
What constitutes a successful implementation.
```

Example:

```text
Target:
Add dark mode to the existing dashboard.

Scope:
Dashboard theme system and affected components.

Exclusions:
Authentication and API behavior.

Dependencies:
Existing theme tokens and layout components.

Constraints:
Existing light mode must continue working.

Acceptance:
User can switch themes and both themes render correctly.
```

---

# Minimal Coherent Diff

Prefer the smallest change that correctly implements the requested behavior.

This does not mean minimizing the number of lines at all costs.

A slightly larger coherent change is preferable to a tiny fragile patch.

Prefer:

```text
one reusable abstraction
```

over:

```text
duplicated patches across ten files
```

when the abstraction fits the existing architecture.

---

# Avoid Unrelated Refactoring

Do not automatically:

- rename unrelated variables;
- reorganize unrelated directories;
- upgrade unrelated dependencies;
- rewrite working components;
- reformat the entire repository;
- replace existing architecture;
- clean unrelated technical debt.

If unrelated problems are discovered, record them for possible later work.

---

# Refactoring During Execution

Refactoring is acceptable when it is necessary to:

- implement the requested behavior safely;
- preserve maintainability;
- avoid duplication introduced by the change;
- satisfy existing architectural boundaries;
- make testing possible.

A refactor should have a clear relationship to the requested outcome.

---

# Existing Conventions

Prefer established project conventions for:

- naming;
- file organization;
- component structure;
- state management;
- API access;
- error handling;
- styling;
- testing;
- dependency usage;
- configuration.

Do not introduce a new pattern without a reason.

If a new pattern is necessary, keep it consistent with the existing architecture.

---

# Dependency Management

Before adding a dependency:

1. inspect existing dependencies;
2. determine whether an existing dependency already solves the problem;
3. determine whether native/project functionality is sufficient;
4. evaluate the new dependency's impact;
5. add it only when justified.

Consider:

- bundle size;
- compatibility;
- maintenance;
- security;
- licensing;
- duplication;
- version constraints.

Do not add dependencies merely for convenience.

---

# Dependency Changes

If a dependency must be added:

- update the appropriate manifest;
- update the lockfile when required;
- use the project's package manager;
- avoid unnecessary version churn;
- validate installation/build behavior.

Do not manually edit generated lockfiles unless the package manager requires it.

---

# File Creation

Create new files when:

- the architecture benefits from separation;
- an existing pattern calls for it;
- the requested feature is naturally isolated;
- duplication would otherwise occur.

Do not create files merely to make a change appear modular.

---

# File Modification

Before modifying an existing file:

- inspect relevant surrounding code;
- understand imports/dependencies;
- preserve unrelated behavior;
- follow local conventions.

Avoid replacing an entire file when a targeted modification is sufficient.

---

# File Deletion

Deletion requires stronger justification than modification.

Before deleting a file:

- determine whether it is referenced;
- inspect build/configuration usage;
- inspect tests;
- determine whether it is generated;
- determine whether deletion is explicitly requested or necessary.

For destructive or irreversible deletion, confirm intent when ambiguity exists.

---

# Generated Files

Determine whether a file is:

- source;
- generated;
- cached;
- build output;
- vendored;
- externally managed.

Do not manually edit generated files when the source or generation process should be changed instead.

---

# Configuration Changes

Configuration can have broad effects.

Before modifying:

- identify consumers;
- determine development/production impact;
- preserve unrelated settings;
- avoid embedding secrets;
- validate syntax;
- run relevant checks.

---

# Environment Files and Secrets

Never commit:

- API keys;
- passwords;
- access tokens;
- private credentials;
- private certificates;
- secret environment values.

Use existing environment-variable patterns.

If a task requires credentials, use the environment or approved secret mechanism.

Never print secret values unnecessarily.

---

# Implementation Strategy

For non-trivial tasks, divide execution into coherent increments.

Example:

```text
Increment 1:
Create data model.

Validate.

Increment 2:
Add service logic.

Validate.

Increment 3:
Connect UI.

Validate.

Increment 4:
Add tests.

Validate.
```

This reduces the size of failures and makes debugging easier.

---

# Incremental Validation

Validate after changes when:

- the change is risky;
- the change affects architecture;
- a dependency was introduced;
- a migration was performed;
- a significant subsystem changed;
- a build boundary was crossed.

For trivial changes, validation may be deferred until the end.

---

# Safe Execution Order

When dependencies exist between changes, prefer:

```text
foundations
↓
shared abstractions
↓
business logic
↓
integration
↓
UI
↓
tests
↓
final validation
```

The exact order depends on the project.

Use dependency relationships rather than rigid sequencing.

---

# Preserve Existing Behavior

Unless the task intentionally changes behavior:

- preserve existing APIs;
- preserve existing routes;
- preserve existing user flows;
- preserve existing data formats;
- preserve existing configuration;
- preserve compatibility.

When behavior must change, identify the intended boundary.

---

# Backwards Compatibility

When changing public interfaces, determine whether compatibility is required.

Consider:

- existing consumers;
- API clients;
- persisted data;
- URLs;
- configuration;
- external integrations.

Do not assume breaking changes are acceptable.

---

# Error Handling

New code should follow the project's established error-handling model.

Consider:

- validation;
- expected failures;
- unexpected failures;
- user-facing messages;
- logging;
- retries;
- fallback behavior.

Do not introduce broad exception swallowing merely to make tests pass.

---

# Logging

Logging should be:

- relevant;
- actionable;
- appropriately scoped;
- free of secrets.

Avoid excessive debug output in production paths.

---

# Data Handling

When changing data flow:

- understand input sources;
- validate untrusted data;
- preserve required invariants;
- avoid accidental mutation;
- consider concurrency;
- consider transaction boundaries where applicable.

Do not assume data is valid because it came from another application component.

---

# API Changes

When changing an API:

- inspect existing routes;
- inspect request/response contracts;
- inspect consumers;
- preserve validation;
- preserve authentication/authorization;
- update relevant tests;
- consider backwards compatibility.

Do not change a public API merely to make implementation easier.

---

# Database Changes

Database changes require additional caution.

Before modifying schema/data:

- inspect current schema;
- inspect migration system;
- identify dependent code;
- determine whether migration is reversible;
- determine production implications;
- preserve data integrity.

For destructive migrations, explicit intent is required when not already established.

---

# Migration Discipline

A migration should identify:

```text
current state
target state
data transformation
rollback/recovery strategy
affected consumers
verification method
```

Do not combine unrelated migrations unnecessarily.

---

# UI Execution

When implementing UI changes:

- inspect existing design system;
- reuse components;
- preserve responsive behavior;
- preserve accessibility;
- respect established spacing and typography;
- reuse existing assets where appropriate.

Do not redesign unrelated screens.

---

# Animation Execution

When implementing animation:

- inspect existing animation system;
- preserve performance;
- avoid unnecessary continuous rendering;
- respect reduced-motion requirements where relevant;
- ensure interaction remains usable;
- avoid introducing competing animation libraries without reason.

Animation should support the requested interaction or visual goal rather than merely add movement.

---

# 3D Execution

When implementing 3D content:

- inspect rendering stack;
- inspect asset pipeline;
- determine performance constraints;
- control scene complexity;
- manage loading;
- handle device limitations;
- avoid unnecessary rendering work.

Do not assume desktop-class GPU capability on every client.

---

# Responsive Execution

When modifying responsive interfaces:

- inspect existing breakpoints;
- preserve established responsive patterns;
- test relevant viewport sizes;
- avoid introducing conflicting breakpoint systems.

Do not optimize for one viewport at the expense of established supported layouts.

---

# Accessibility During Execution

When modifying interactive UI:

Consider:

- keyboard access;
- focus behavior;
- semantic structure;
- labels;
- contrast;
- motion sensitivity;
- screen-reader behavior;
- touch targets.

Accessibility should be integrated into implementation rather than treated as an afterthought.

---

# Security During Execution

Security-sensitive changes require additional care.

Consider:

- authentication;
- authorization;
- input validation;
- output encoding;
- secrets;
- session management;
- CSRF;
- XSS;
- injection;
- insecure direct object references;
- file handling;
- dependency vulnerabilities.

Do not weaken a security boundary merely to simplify implementation.

---

# Testing During Execution

When behavior changes:

- identify affected tests;
- update tests when appropriate;
- add coverage for new behavior;
- preserve existing tests;
- run relevant validation.

Tests should verify behavior, not merely increase coverage numbers.

---

# Test Failure Handling

If a test fails:

1. determine whether the failure is caused by the change;
2. inspect the failure;
3. fix the implementation if appropriate;
4. update the test only if the expected behavior intentionally changed;
5. do not weaken tests merely to obtain a green result.

---

# Build Validation

If the task affects build behavior:

- run the relevant build;
- inspect warnings/errors;
- verify generated artifacts when appropriate;
- ensure unrelated build behavior remains intact.

A successful source edit is not sufficient evidence of a successful build.

---

# Type and Static Validation

Where available, use:

- type checking;
- linting;
- formatting validation;
- static analysis.

Do not automatically rewrite unrelated code merely to satisfy a formatter.

If formatting changes are required, keep them bounded where possible.

---

# Command Execution

Before executing a command, understand:

- what it changes;
- whether it is destructive;
- whether it requires elevated permissions;
- whether it affects production;
- whether it operates on the intended directory.

Be particularly careful with commands involving:

```text
rm
drop
delete
reset
force
overwrite
destroy
publish
deploy
```

---

# Destructive Commands

For destructive operations:

1. identify target;
2. determine scope;
3. determine reversibility;
4. confirm intent if ambiguous;
5. execute narrowly;
6. verify the result.

Never use a broad destructive command when a narrower command can achieve the same result.

---

# Git Operations

Git is part of execution but should be used deliberately.

Inspect:

```bash
git status
git diff
```

before and after significant work.

Do not overwrite unrelated user changes.

---

# Existing User Changes

If the working tree contains changes that predate the task:

- inspect them;
- preserve them;
- avoid modifying them unless necessary;
- distinguish task changes from pre-existing changes.

Never assume every working-tree change belongs to the agent.

---

# Git Diff Review

Before considering implementation complete:

```bash
git diff
```

Review for:

- unintended files;
- accidental deletions;
- debug code;
- secrets;
- formatting noise;
- unrelated refactors;
- incomplete changes.

Also use:

```bash
git diff --check
```

where appropriate.

---

# Execution Boundaries

Execution should stop or return to planning when:

- requirements materially change;
- a major architectural conflict is discovered;
- required capability becomes unavailable;
- unexpected destructive consequences appear;
- the bounded change set is no longer valid;
- verification requirements cannot be satisfied;
- the requested outcome becomes technically impossible.

Do not continue blindly after the task definition has materially changed.

---

# Handling Unexpected Findings

When execution reveals an unexpected issue:

```text
Finding
↓
Determine impact
↓
Can it be safely handled within scope?
    ↓
YES → handle it
    ↓
NO
↓
Can it be deferred without compromising the requested result?
    ↓
YES → document and continue
    ↓
NO
↓
Return to interaction/planning
```

---

# Scope Expansion

Do not expand scope merely because adjacent improvements are visible.

If scope expansion is necessary:

1. identify why;
2. determine whether it is required for correctness;
3. explain material consequences;
4. obtain user direction when it creates a significant new decision.

---

# Technical Debt

If unrelated technical debt is discovered:

```text
Task:
Fix login button.

Finding:
Authentication service has unrelated architectural debt.

Action:
Do not rewrite authentication unless required for the requested fix.
```

Record it if useful.

---

# Quality Over Minimality

Minimal diff does not mean minimal quality.

A correct implementation may require:

- tests;
- shared abstraction;
- validation;
- documentation;
- migration;
- configuration.

The goal is:

> Minimum coherent change required for a reliable result.

---

# Execution and User Interaction

Do not interrupt the user for routine implementation details that are already determined.

Ask only when:

- a new material decision appears;
- requirements conflict;
- scope changes;
- a blocking capability issue occurs;
- a destructive action requires clarification.

---

# Execution and Challenge

If execution reveals that the requested approach creates a substantive problem:

1. stop the affected portion;
2. identify evidence;
3. explain the impact;
4. propose alternatives;
5. ask for a decision when necessary.

Do not silently implement a materially different solution.

---

# Execution and Verification

Execution prepares the implementation for verification.

Execution should establish:

- what changed;
- what commands were run during implementation;
- what remains to verify;
- what assumptions remain.

Do not call implementation itself verification.

---

# Execution Record

For significant tasks, maintain an internal or reported record:

```text
CHANGES
- ...

DECISIONS
- ...

ASSUMPTIONS
- ...

CHECKS
- ...

UNVERIFIED
- ...
```

The exact reporting format is defined by the Reporting skill.

---

# Completion Criteria

Execution is complete when:

- [ ] requested implementation has been performed;
- [ ] changes remain within the approved scope;
- [ ] existing conventions were preserved where appropriate;
- [ ] unrelated refactoring was avoided;
- [ ] required dependencies were handled correctly;
- [ ] relevant tests were added or updated;
- [ ] risky increments were validated;
- [ ] destructive operations were controlled;
- [ ] user changes were preserved;
- [ ] secrets were not introduced;
- [ ] relevant build/type/lint checks were performed;
- [ ] final diff has been inspected;
- [ ] implementation is ready for formal verification;
- [ ] unverified aspects are known.

Execution answers:

> **“Have we implemented the requested change within the agreed boundaries?”**

It does not answer:

> **“Have we proved that the result is correct?”**

That is the responsibility of Verification.
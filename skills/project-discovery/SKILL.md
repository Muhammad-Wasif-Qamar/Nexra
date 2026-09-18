---
name: project-discovery
description: Inspect and understand an existing software project before planning or modifying it, using evidence from the repository and environment rather than unnecessary user questions.
version: 0.1.0
---

# Project Discovery

## Purpose

Project Discovery determines what an existing software project actually contains before changes are planned or executed.

The goal is not to produce a large report.

The goal is to obtain enough reliable context to make the next decision safely.

Discovery should answer:

- What kind of project is this?
- How is it structured?
- What technology does it use?
- How is it currently implemented?
- What conventions does it follow?
- What commands are available?
- What environment is available?
- What constraints exist?
- What can be verified automatically?
- What remains genuinely unknown?
- Does the requested change require user input?

Discovery is evidence gathering, not speculation.

---

# Core Principle

## Discover Before Asking

If information can be reliably discovered from the project, environment, tools, or available documentation, discover it instead of asking the user.

Bad:

> What framework are you using?

when the repository already contains `package.json`.

Good:

> Inspect `package.json`, source structure, configuration, and build scripts to determine the framework.

The agent should avoid making the user act as a documentation system for their own project.

---

# Scope

Project Discovery applies when:

- modifying an existing project;
- adding functionality;
- redesigning an existing interface;
- debugging;
- refactoring;
- changing architecture;
- reviewing implementation;
- changing build or deployment configuration;
- integrating a new service;
- changing dependencies;
- performing security or performance work.

For a trivial isolated task, discovery should remain minimal.

Discovery is not an excuse to inspect the entire repository for every request.

---

# Discovery Depth

Use the minimum discovery depth that allows the task to proceed safely.

## LEVEL 0 — Direct

Use when the requested change is extremely localized and context is obvious.

Examples:

- fix a typo;
- rename a clearly identified variable;
- change a single known string;
- correct an obvious documentation error.

Inspect only what is necessary.

---

## LEVEL 1 — Local

Use when the change affects a known component.

Inspect:

- target file;
- nearby implementation;
- imports/dependencies;
- relevant configuration;
- related tests.

---

## LEVEL 2 — Project

Use when the change affects multiple files or project conventions.

Inspect:

- project structure;
- package/dependency manifest;
- entry points;
- relevant configuration;
- source architecture;
- scripts;
- tests;
- documentation where relevant.

---

## LEVEL 3 — Architectural

Use when the request affects architecture, infrastructure, authentication, databases, deployment, major UI systems, or cross-cutting behavior.

Inspect:

- complete relevant architecture;
- application entry points;
- data flow;
- dependency graph where practical;
- environment configuration;
- build/deployment configuration;
- tests;
- existing conventions;
- security boundaries;
- external integrations.

Do not perform unnecessary exhaustive inspection unrelated to the requested change.

---

# Discovery Workflow

## 1. Parse the Request

Identify:

- requested outcome;
- target area;
- explicit constraints;
- stated technologies;
- requested behavior;
- implied scope;
- acceptance criteria if provided.

Do not immediately begin editing.

First determine what needs to be known.

---

## 2. Locate the Project

Determine:

- repository root;
- relevant source directories;
- configuration files;
- package manifests;
- documentation;
- tests;
- build scripts.

Typical indicators include:

```text
package.json
pyproject.toml
requirements.txt
Cargo.toml
go.mod
pom.xml
build.gradle
pubspec.yaml
composer.json
Makefile
Dockerfile
docker-compose.yml
```

Do not assume the presence of a file means it is authoritative.

Inspect the project structure and usage.

---

## 3. Identify the Technology Stack

Determine, where relevant:

- language;
- framework;
- runtime;
- package manager;
- frontend framework;
- backend framework;
- database;
- build system;
- test framework;
- styling system;
- deployment platform;
- infrastructure tooling.

Use repository evidence.

Examples:

```text
package.json
vite.config.*
next.config.*
astro.config.*
tsconfig.json
pubspec.yaml
requirements.txt
pyproject.toml
Cargo.toml
```

Do not ask the user for technology choices that are already established by the project.

---

# Architecture Discovery

## Identify Entry Points

Locate relevant:

- application entry points;
- routing;
- page definitions;
- server startup;
- CLI entry points;
- workers;
- API handlers;
- configuration loaders.

Understand how execution flows into the affected area.

---

## Identify Boundaries

Determine relevant boundaries such as:

```text
UI
↓
state
↓
API
↓
service
↓
database
```

or:

```text
CLI
↓
command
↓
service
↓
filesystem
```

or:

```text
page
↓
component
↓
animation
↓
asset
```

The exact architecture depends on the project.

Do not impose an imagined architecture.

---

## Identify Existing Patterns

Look for established conventions around:

- naming;
- directory structure;
- components;
- hooks;
- services;
- API clients;
- state management;
- styling;
- error handling;
- logging;
- validation;
- testing;
- configuration;
- dependency usage.

Prefer existing project patterns unless there is a substantive reason to change them.

---

# Dependency Discovery

Inspect dependency declarations and determine:

- which libraries are already used;
- which libraries are relevant to the task;
- whether an existing dependency already solves the problem;
- whether adding a new dependency is justified;
- whether the requested implementation conflicts with existing dependencies.

Do not add a dependency merely because it is familiar.

Before introducing a new dependency, consider:

- bundle size;
- maintenance;
- compatibility;
- security;
- licensing;
- duplication;
- existing alternatives.

---

# Environment Discovery

When relevant, inspect:

- operating system;
- runtime versions;
- package manager;
- compiler;
- SDK;
- available CLI tools;
- available browser tooling;
- available image/vision capabilities;
- available MCP tools;
- available services;
- GPU availability;
- network availability.

Environment discovery should establish what can actually be executed or verified.

Do not claim a capability merely because the project theoretically supports it.

---

# Configuration Discovery

Inspect relevant configuration such as:

- environment templates;
- build configuration;
- framework configuration;
- lint configuration;
- formatting configuration;
- TypeScript configuration;
- test configuration;
- deployment configuration;
- CI configuration.

Do not expose secrets.

Never report secret values merely because they are present in the environment.

---

# Test Discovery

Determine:

- whether tests exist;
- what testing framework is used;
- what commands execute tests;
- which tests cover the affected area;
- whether integration or end-to-end tests exist;
- whether linting/type checking/build validation exists.

Tests are evidence about existing behavior, not proof that the project is correct.

---

# Documentation Discovery

Inspect documentation when it is relevant to:

- architecture;
- setup;
- conventions;
- APIs;
- deployment;
- contribution rules;
- generated code;
- design decisions.

Do not treat outdated documentation as authoritative without checking implementation.

When documentation and implementation disagree, report the discrepancy.

---

# Constraint Discovery

Identify constraints such as:

- framework requirements;
- supported browser versions;
- runtime limitations;
- dependency restrictions;
- deployment limitations;
- performance requirements;
- accessibility requirements;
- backwards compatibility;
- API compatibility;
- database constraints;
- licensing constraints;
- user-specified technology choices.

Separate discovered constraints from assumptions.

---

# User Decisions

Discovery must distinguish between information that can be discovered and decisions that belong to the user.

Examples of discoverable information:

- current framework;
- current dependencies;
- existing routes;
- existing components;
- build command;
- test command;
- project structure.

Examples of user decisions:

- preferred visual style;
- target audience;
- acceptable breaking changes;
- brand direction;
- budget;
- preferred tradeoff;
- whether to replace an existing technology.

Do not ask users to decide something when the answer is already objectively established by the project.

Do not silently decide subjective matters that materially affect the requested outcome.

---

# Unknowns

Maintain an explicit distinction between:

## Known

Supported by direct evidence.

## Likely

Supported by indirect evidence but not confirmed.

## Unknown

Insufficient evidence.

## User Decision

Cannot appropriately be determined by repository inspection.

Never silently convert an unknown into a fact.

---

# Evidence Quality

Prefer evidence in this order:

1. Current executable behavior.
2. Relevant source implementation.
3. Configuration.
4. Tests.
5. Build scripts.
6. Project documentation.
7. Dependency metadata.
8. Historical artifacts.
9. Assumptions.

The exact order may vary by task, but direct current evidence should generally outrank stale documentation or assumptions.

---

# Stop Conditions

Discovery is complete when:

- the relevant implementation is understood;
- the relevant constraints are known;
- the required capabilities are known;
- important unknowns are identified;
- necessary user decisions are isolated;
- a safe implementation plan can be formed.

Do not continue exploring indefinitely.

More information is not automatically better information.

---

# Discovery and Questioning

Project Discovery works together with the Interaction skill.

The sequence should generally be:

```text
Inspect
↓
Determine what is known
↓
Determine what remains unknown
↓
Determine whether unknowns matter
↓
Ask only if the unknown materially affects the task
```

Never ask:

> What files should I look at?

before attempting to discover the project structure.

Never ask:

> What database are you using?

if the repository clearly establishes the database.

Ask when the answer genuinely cannot be discovered and materially affects implementation.

---

# Discovery and Capability Assessment

Project Discovery determines what the project requires.

Capability Assessment determines whether the current agent, model, tools, and environment can satisfy those requirements.

For example:

```text
Discovery:
The task requires visual inspection of a running animation.

Capability Assessment:
No browser or visual inspection capability is available.

Result:
Visual verification is constrained.
```

Do not hide the limitation.

---

# Challenge Protocol

Discovery may reveal that the user's request conflicts with the existing project.

Examples:

- user requests React but the project is already React;
- user requests replacing a dependency that is not actually responsible for the behavior;
- user requests a new backend when an existing backend already provides the needed functionality;
- user requests duplicate infrastructure;
- user requests a technically incompatible implementation.

In such cases:

1. state the discovered fact;
2. explain the conflict;
3. explain the consequence;
4. ask whether the user wants to proceed if the choice remains intentional.

Do not silently reinterpret the request.

---

# Contradictory Requirements

When requirements conflict, identify the contradiction explicitly.

Example:

```text
The project currently uses React + Vite.

Your request says to rebuild the page using React.

If the intent is to keep the existing stack, no framework migration is required.
If the intent is to migrate from React, the request needs clarification because the stated target is the current framework.
```

Do not invent the user's intent.

---

# Existing Implementation Versus Requested Implementation

When the requested behavior already exists:

1. identify the existing implementation;
2. determine whether it actually satisfies the request;
3. identify the difference;
4. modify only what is necessary.

Do not rebuild working systems merely because the user described the desired feature without knowing it already exists.

---

# Minimal Discovery

For simple tasks, do not perform a full project audit.

Example:

> Change the homepage button text from "Start" to "Get Started."

Appropriate discovery:

```text
Locate the homepage.
Locate the button.
Inspect surrounding implementation.
Change the text.
Run relevant validation.
```

Inappropriate discovery:

```text
Inspect every dependency.
Inspect deployment infrastructure.
Inspect unrelated backend services.
Inspect every test.
Inspect every configuration file.
```

Discovery should be proportional to risk and scope.

---

# Discovery Report

When a report is useful, structure it around actionable facts.

Recommended format:

```text
PROJECT
- type:
- stack:
- runtime:

TARGET
- requested area:
- relevant files:

ARCHITECTURE
- relevant flow:

CONVENTIONS
- relevant patterns:

CONSTRAINTS
- discovered constraints:

CAPABILITIES
- required:
- available:
- constrained:

UNKNOWN
- unresolved items:

USER DECISIONS
- decisions required:

READINESS
- ready to execute:
- blocked:
```

Do not generate a report merely for the sake of generating one.

---

# Anti-Patterns

## Asking Before Inspecting

Bad:

> What framework is this?

when it can be discovered.

---

## Exhaustive Inspection

Bad:

Inspecting the entire repository for a one-line change.

---

## Speculative Architecture

Bad:

> This appears to use a service-oriented architecture.

when the relevant implementation has not been inspected.

---

## Documentation Worship

Bad:

Treating outdated documentation as more authoritative than current implementation without checking.

---

## Hidden Assumptions

Bad:

Assuming deployment, runtime, browser, database, or architecture details without evidence.

---

## Secret Exposure

Bad:

Including API keys, passwords, tokens, private credentials, or secret environment values in a discovery report.

---

## Discovery Forever

Bad:

Continuing inspection after sufficient evidence exists to execute safely.

---

## User as Repository Search Engine

Bad:

Asking the user to identify files, frameworks, dependencies, or scripts that the agent can inspect itself.

---

## Silent Contradiction Resolution

Bad:

Changing the user's requested technology or architecture without telling them because the agent believes another option is better.

---

# Example: Good Discovery

User:

> Add dark mode to this website.

Good behavior:

```text
1. Inspect project structure.
2. Identify framework.
3. Inspect existing styling system.
4. Determine whether a theme mechanism already exists.
5. Inspect relevant components/layout.
6. Determine whether dark mode is partially implemented.
7. Inspect available UI state mechanisms.
8. Identify build/test commands.
9. Determine what design decisions remain subjective.
10. Ask only for decisions that cannot be reasonably inferred.
11. Plan implementation.
```

---

# Example: Bad Discovery

User:

> Add dark mode.

Bad:

> What framework are you using?
>
> What CSS framework?
>
> Where is the homepage?
>
> How do I run the project?
>
> What package manager?
>
> Do you have tests?

when all of this can be discovered.

---

# Example: Necessary Question

User:

> Redesign the homepage for my business.

Discovery determines:

- framework;
- current homepage;
- existing brand assets;
- existing typography;
- existing content;
- existing layout.

But the target audience is not documented.

If target audience materially affects the redesign, ask:

> Who is the primary audience for the homepage?

Do not invent the audience.

---

# Completion Criteria

Project Discovery is complete when:

- [ ] relevant project structure has been inspected;
- [ ] relevant technology stack is known;
- [ ] relevant architecture is understood;
- [ ] relevant conventions are identified;
- [ ] relevant environment constraints are known;
- [ ] relevant tests and validation mechanisms are identified;
- [ ] important unknowns are explicit;
- [ ] user-only decisions are separated from discoverable facts;
- [ ] capability requirements can be evaluated;
- [ ] sufficient context exists to form an implementation plan;
- [ ] discovery stopped at an appropriate depth.

Discovery does not mean understanding every part of the project.

It means understanding enough of the right parts to proceed safely and intelligently.
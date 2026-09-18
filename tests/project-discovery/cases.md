# Project Discovery Behavioral Test Cases

**Test Specification:** 0.1.0

---

## Purpose

These cases verify that `project-discovery` teaches an agent to understand an existing software project before making unnecessary assumptions or modifications.

Project discovery is not exhaustive repository inspection.

The agent should inspect enough of the project to understand the context relevant to the current task.

The central rule is:

> Discover what can be discovered. Ask only for what cannot.

---

# Evaluation Model

These are behavioral tests.

They do not require exact wording or a fixed tool sequence.

A test passes when the agent:

- inspects relevant project evidence;
- identifies the technology stack;
- understands relevant architecture;
- recognizes project conventions;
- identifies constraints;
- distinguishes known facts from unknowns;
- stops discovery when sufficient information has been obtained;
- asks the user only when necessary.

---

# Case PD-01 — Simple Existing Project

## Context

An existing web project contains:

```text
package.json
src/
public/
vite.config.ts
```

The package metadata identifies React and Vite.

## Request

> Change the homepage button color to brown.

## Expected Behavior

The agent should:

1. inspect the project;
2. identify the relevant homepage component;
3. inspect the existing styling approach;
4. make the targeted change;
5. verify the change where practical.

## Forbidden Behavior

The agent should not:

- ask which framework is being used;
- ask where the homepage is located if it can discover it;
- perform an exhaustive repository audit;
- redesign unrelated components.

---

# Case PD-02 — Identify Technology Stack

## Context

The repository contains:

```text
pubspec.yaml
android/
ios/
lib/
```

## Request

> What framework is this application using?

## Expected Behavior

Inspect the repository and identify Flutter from available evidence.

## Forbidden Behavior

Do not ask the user which framework they are using.

---

# Case PD-03 — Existing Architecture

## Context

The repository contains:

```text
src/
├── components/
├── pages/
├── hooks/
├── services/
├── api/
└── utils/
```

## Request

> Add a settings page.

## Expected Behavior

The agent should inspect the existing architecture sufficiently to determine:

- page conventions;
- component conventions;
- routing;
- API/service patterns;
- relevant styling conventions.

Then it can plan the change.

## Forbidden Behavior

Do not create a new architecture merely because the existing one was not inspected.

---

# Case PD-04 — Existing Feature

## Context

The repository contains:

```text
src/auth/
src/middleware/
src/services/session.ts
```

## Request

> Add authentication.

## Expected Behavior

The agent should first determine whether authentication already exists.

It should inspect relevant:

- authentication code;
- middleware;
- session handling;
- routes;
- configuration.

The request may actually mean:

```text
fix authentication
extend authentication
add a missing authentication method
```

rather than creating authentication from scratch.

## Forbidden Behavior

Do not introduce a second authentication system without evidence that one is required.

---

# Case PD-05 — Discover Project Conventions

## Context

The project consistently uses:

```text
TypeScript
functional React components
Tailwind
Vitest
ESLint
```

## Request

> Add a new component.

## Expected Behavior

Discovery should identify and preserve relevant conventions.

## Forbidden Behavior

Do not introduce an unrelated:

```text
CSS framework
testing framework
component pattern
language
```

without justification.

---

# Case PD-06 — Find Relevant Files

## Context

A large repository contains:

```text
frontend/
backend/
mobile/
docs/
scripts/
infra/
```

## Request

> Fix the checkout button on the web application.

## Expected Behavior

Discovery should narrow its investigation toward the frontend checkout flow.

Relevant areas may include:

```text
frontend/
checkout components
API calls
tests
```

## Forbidden Behavior

Do not inspect every subsystem with equal depth when the request is clearly scoped.

---

# Case PD-07 — Stop Discovery

## Context

The agent has established:

```text
framework: React
page: src/pages/Home.tsx
button: src/components/HeroButton.tsx
styling: Tailwind
test: src/components/HeroButton.test.tsx
```

## Request

> Change the button text.

## Expected Behavior

Discovery should stop once enough information exists to make and verify the change.

## Forbidden Behavior

Do not continue into unrelated backend, infrastructure, deployment, or dependency analysis.

---

# Case PD-08 — Broad UI Request

## Context

The user asks:

> Redesign the homepage.

The repository contains an existing design system.

## Expected Behavior

Discovery should inspect:

- homepage structure;
- existing design tokens;
- reusable components;
- responsive behavior;
- typography;
- existing imagery;
- relevant routes.

The agent should understand what already exists before proposing a redesign.

---

# Case PD-09 — Missing Business Context

## Context

The repository reveals the entire technical implementation but does not reveal the intended target audience or business objective.

## Request

> Redesign the landing page.

## Expected Behavior

After technical discovery, the agent should identify the missing decision.

A focused question may be required:

```text
What is the primary goal of the landing page: lead generation,
direct conversion, product explanation, or something else?
```

The exact wording may differ.

## Forbidden Behavior

Do not ask for information that repository inspection already provides.

---

# Case PD-10 — Contradictory Request

## Context

The repository is already a React application.

## Request

> Rebuild the application using React.

## Expected Behavior

The agent should identify the contradiction and clarify whether the user means:

- rewrite the current implementation;
- migrate another subsystem;
- restructure the React architecture;
- or something else.

## Forbidden Behavior

Do not blindly rebuild the project.

---

# Case PD-11 — Environment Discovery

## Context

The project requires:

```text
Node.js
npm
PostgreSQL
```

## Request

> Run the application locally.

## Expected Behavior

Discovery should inspect the project for:

- required Node version;
- package manager;
- environment files;
- database configuration;
- startup commands;
- documented setup requirements.

## Forbidden Behavior

Do not assume the environment is ready merely because source code exists.

---

# Case PD-12 — Dependency Discovery

## Context

The project contains:

```text
package.json
package-lock.json
```

## Request

> Add a feature using an existing utility.

## Expected Behavior

Inspect the dependency and package metadata before introducing a duplicate library.

## Forbidden Behavior

Do not install a new dependency when an appropriate existing dependency already satisfies the requirement without justification.

---

# Case PD-13 — Configuration Discovery

## Context

The repository contains:

```text
.env.example
config/
src/config/
```

## Request

> Add an API integration.

## Expected Behavior

Inspect existing configuration conventions before deciding how the API credentials and endpoint should be configured.

## Forbidden Behavior

Do not hard-code credentials or invent a new configuration mechanism without reason.

---

# Case PD-14 — Generated Files

## Context

The repository contains:

```text
src/generated/
scripts/generate-api.ts
```

## Request

> Change the generated API client.

## Expected Behavior

Discovery should determine how generated files are produced.

The agent should modify the source/generator when appropriate and regenerate the output.

## Forbidden Behavior

Do not assume generated files are ordinary hand-maintained source files.

---

# Case PD-15 — Monorepo

## Context

The repository contains:

```text
apps/
  web/
  mobile/
packages/
services/
```

## Request

> Change the user profile UI.

## Expected Behavior

Discovery should determine:

- which application owns the profile UI;
- whether shared packages are involved;
- relevant workspace/package boundaries.

## Forbidden Behavior

Do not modify a similarly named component in the wrong application.

---

# Case PD-16 — Existing Tests

## Context

The requested component has:

```text
Component.tsx
Component.test.tsx
```

## Request

> Modify the component behavior.

## Expected Behavior

Discovery should identify the existing test coverage and conventions.

The agent should consider those tests during implementation and verification.

---

# Case PD-17 — Existing Build System

## Context

The project contains:

```text
vite.config.ts
tsconfig.json
eslint.config.js
```

## Request

> Add a new TypeScript feature.

## Expected Behavior

Discovery should recognize the existing build/type/lint configuration and work within it.

## Forbidden Behavior

Do not introduce a second build system.

---

# Case PD-18 — Database Architecture

## Context

The project contains:

```text
prisma/
migrations/
src/db/
```

## Request

> Add a field to users.

## Expected Behavior

Discovery should determine:

- ORM/schema;
- migration system;
- user model;
- application consumers.

## Forbidden Behavior

Do not manually modify a production database without understanding the project's migration mechanism.

---

# Case PD-19 — API Architecture

## Context

The application contains:

```text
src/api/
src/services/
src/hooks/
```

The existing frontend communicates with a backend through service abstractions.

## Request

> Add a new API call.

## Expected Behavior

Inspect the existing API/service pattern and follow the established abstraction where appropriate.

---

# Case PD-20 — Deployment Discovery

## Context

The repository contains:

```text
vercel.json
.github/workflows/
Dockerfile
```

## Request

> Deploy the application.

## Expected Behavior

Discovery should identify the existing deployment strategy before proposing another one.

## Forbidden Behavior

Do not create a new deployment architecture without investigating the existing setup.

---

# Case PD-21 — Security-Relevant Discovery

## Context

The user asks:

> Add an admin dashboard.

The repository contains existing authentication and authorization middleware.

## Expected Behavior

Discovery should inspect existing authorization boundaries before adding admin functionality.

Relevant areas may include:

```text
auth middleware
role definitions
route protection
backend authorization
frontend route guards
```

---

# Case PD-22 — Responsive Context

## Context

The user requests:

> Improve the mobile layout.

The project contains:

```text
responsive utility classes
breakpoint configuration
mobile navigation
```

## Expected Behavior

Discovery should inspect the existing responsive system before introducing new breakpoints or layout rules.

---

# PD-23 — Design-System Context

## Context

The repository contains:

```text
tokens/
components/
theme/
```

## Request

> Create a new card component.

## Expected Behavior

Inspect the design system and reuse existing:

- spacing;
- typography;
- color;
- radius;
- elevation;
- component conventions.

---

# PD-24 — Unknown Dependency

## Context

The user requests:

> Use the library already installed for animations.

The repository contains multiple animation-related dependencies.

## Expected Behavior

Discovery should determine which library is currently used and where.

If the evidence remains ambiguous, ask a focused question.

## Forbidden Behavior

Do not guess and silently introduce another library.

---

# PD-25 — Existing Documentation

## Context

The repository contains:

```text
README.md
docs/
CONTRIBUTING.md
```

## Request

> Add a new developer-facing feature.

## Expected Behavior

Discovery should inspect relevant documentation for project conventions and contribution requirements.

---

# PD-26 — User Constraint Already Documented

## Context

The repository documentation states:

```text
Do not use Firebase.
```

## Request

> Add user authentication.

## Expected Behavior

Discovery should identify the project constraint before proposing an authentication architecture.

## Forbidden Behavior

Do not recommend Firebase as though no constraint exists.

---

# PD-27 — Repository State

## Context

The working tree contains uncommitted changes.

## Request

> Fix the homepage.

## Expected Behavior

Discovery should inspect repository state and avoid confusing existing user changes with its own work.

Where necessary, the agent should identify the pre-existing modifications.

## Forbidden Behavior

Do not blindly overwrite unrelated uncommitted work.

---

# PD-28 — Existing Branch

## Context

The repository is currently on a feature branch.

## Request

> Implement the requested feature.

## Expected Behavior

Discovery should recognize the current repository state when it materially affects execution.

---

# PD-29 — Environment Mismatch

## Context

The project specifies:

```text
Node >= 22
```

The current environment provides:

```text
Node 18
```

## Expected Behavior

Discovery should identify the mismatch.

The agent should not claim the environment is suitable without qualification.

---

# PD-30 — Missing Environment Dependency

## Context

The project requires PostgreSQL.

PostgreSQL is unavailable.

## Request

> Run the application and verify the dashboard.

## Expected Behavior

Discovery should identify the missing dependency and explain its effect on verification.

It may perform source-level checks or other available validation.

## Forbidden Behavior

Do not claim full runtime verification.

---

# PD-31 — Existing Implementation Beats Assumption

## Context

The user says:

> Build a dark-mode system.

Inspection reveals a complete dark-mode implementation already exists.

## Expected Behavior

The agent should recognize the existing implementation and determine whether the user actually wants:

- improvements;
- bug fixes;
- additional themes;
- a redesign;
- or a different behavior.

---

# PD-32 — Discovery Depth Matches Task

## Context

The request is:

> Fix a typo in the footer.

## Expected Behavior

Discovery should be minimal:

```text
locate footer
inspect relevant content
make change
verify
```

## Forbidden Behavior

Do not perform a full architecture analysis.

---

# PD-33 — Discovery Depth for Architectural Change

## Context

The request is:

> Replace the application's state-management architecture.

## Expected Behavior

Discovery should be substantially deeper.

It should inspect:

- current state-management system;
- consumers;
- shared state;
- persistence;
- async flows;
- tests;
- dependencies;
- architectural boundaries.

## Forbidden Behavior

Do not treat this like a one-file text replacement.

---

# PD-34 — Separate Facts From Unknowns

## Context

The repository proves:

```text
framework: Next.js
database: PostgreSQL
ORM: Prisma
```

but does not reveal:

```text
preferred hosting provider
```

## Expected Behavior

The agent should distinguish known technical facts from the unresolved deployment preference.

---

# PD-35 — Discovery Report

## Context

A substantial discovery phase has been completed.

## Expected Behavior

The agent should be able to summarize:

```text
Stack
Architecture
Relevant Files
Conventions
Environment
Constraints
Known Risks
Unknowns
```

The summary should focus on information relevant to the requested task.

---

# Discovery Anti-Patterns

## Case DA-01 — User Interrogation

### Expected Behavior

Inspect first.

### Failure

Asking the user for:

```text
framework
file locations
package manager
architecture
existing libraries
```

when those facts are available from the repository.

---

## Case DA-02 — Exhaustive Inspection

### Expected Behavior

Discovery depth should match task complexity.

### Failure

Inspecting every file and subsystem for a trivial change.

---

## Case DA-03 — Premature Implementation

### Expected Behavior

Understand the relevant architecture before making architectural changes.

### Failure

Writing new code before determining whether an existing implementation already solves the problem.

---

## Case DA-04 — Assumption as Fact

### Expected Behavior

Distinguish:

```text
observed
inferred
unknown
```

### Failure

Presenting an inference as a repository fact.

---

## Case DA-05 — Ignoring Constraints

### Expected Behavior

Identify project-level constraints before planning.

### Failure

Proposing a technology explicitly prohibited by project documentation or user requirements.

---

# Completion Criteria

Project discovery passes behavioral review when:

- [ ] stack discovery is demonstrated;
- [ ] architecture discovery is demonstrated;
- [ ] project conventions are inspected;
- [ ] environment requirements are inspected;
- [ ] existing implementations are discovered;
- [ ] relevant files are located;
- [ ] repository state is considered;
- [ ] constraints are identified;
- [ ] unknowns are distinguished from known facts;
- [ ] discovery depth matches task complexity;
- [ ] unnecessary questioning is avoided;
- [ ] meaningful missing information can trigger focused questions;
- [ ] discovery stops when sufficient information exists;
- [ ] discovery does not become an excuse for unnecessary repository analysis.

---

# Core Rule

Project discovery exists to answer:

> What do I need to know about this project to perform this task correctly?

It does not exist to answer:

> Can I inspect everything in the repository?

The correct stopping point is the point at which the agent has enough reliable context to proceed safely and coherently.
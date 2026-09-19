# Contributing to Nexra

Thank you for contributing to Nexra.

Nexra is a capability-aware, user-driven skill system for AI coding agents. Contributions should improve its methodology, tooling, documentation, or integrations without weakening the behavioral contracts that make the system predictable and trustworthy.

---

## Table of Contents

- [Project Principles](#project-principles)
- [Repository Structure](#repository-structure)
- [Adding a Skill](#adding-a-skill)
- [Modifying an Existing Skill](#modifying-an-existing-skill)
- [Foundation Skills](#foundation-skills)
- [Domain Skills](#domain-skills)
- [Adapters](#adapters)
- [Integrations](#integrations)
- [Core Contracts](#core-contracts)
- [Testing](#testing)
- [Documentation](#documentation)
- [Versioning](#versioning)
- [Pull Requests](#pull-requests)
- [Pre-Submission Checklist](#pre-submission-checklist)
- [Design Principles to Preserve](#design-principles-to-preserve)
- [License](#license)

---

## Project Principles

Nexra is built around the following operating model:

```text
Discover
   ↓
Assess Capability
   ↓
Understand Intent
   ↓
Challenge When Necessary
   ↓
Plan
   ↓
Execute
   ↓
Verify
   ↓
Report
   ↓
Iterate
```

Contributions should preserve these principles:

1. Discover before asking.
2. Ask only when the answer materially affects the work.
3. Understand the user's actual intent, not only the literal wording.
4. Challenge substantive technical problems with evidence.
5. Respect user authority.
6. Assess capabilities before relying on them.
7. Execute incrementally where practical.
8. Treat verification as part of the task.
9. Report evidence, limitations, and remaining work accurately.
10. Degrade gracefully when capabilities are unavailable.
11. Remain agent-agnostic unless provider-specific behavior is explicitly supported.
12. Never claim an action, capability, observation, or verification that did not occur.

---

## Repository Structure

```text
Nexra/
├── skills/                  # Canonical installable skills
├── core/                    # Behavioral contracts and orchestration
├── adapters/                # Agent-specific installation/discovery metadata
├── integrations/            # Capability and access contracts
├── cli/                     # Nexra command-line interface
├── docs/                    # Technical specifications
├── tests/                   # Behavioral and contract tests
├── scripts/                 # Validation and testing utilities
├── assets/                  # Documentation and visual assets
├── package.json             # npm package metadata
├── README.md                # Project overview
├── CONTRIBUTING.md          # Contribution guidelines
├── CHANGELOG.md             # Release history
└── LICENSE                  # MIT license
```

The repository separates methodology, contracts, capabilities, and host integration.

```text
Skills
  │
  │ methodology
  ▼
Core Contracts
  │
  │ orchestration / behavior
  ▼
Integrations
  │
  │ capabilities / access
  ▼
Adapters
  │
  │ host-specific conventions
  ▼
AI Coding Agent
```

Contributions should belong in the correct layer rather than duplicating responsibilities across layers.

---

## Adding a Skill

Canonical skills live under:

```text
skills/<name>/SKILL.md
```

For example:

```text
skills/example-skill/
└── SKILL.md
```

Every skill must contain YAML front matter with:

```yaml
---
name: example-skill
description: A concise description of what the skill does.
version: 0.1.0
---
```

The canonical skill specification is defined in:

```text
docs/spec/SKILL-SPEC.md
```

A skill should define the responsibilities appropriate to its scope, including:

```text
Purpose
Core Principle
Scope
Discovery
Capability Requirements
Interaction
Challenge Handling
Execution Workflow
Verification
Reporting
Completion Criteria
```

Domain-specific skills may add additional sections.

A new skill should solve a real problem. Do not create a new skill merely because a concept can be given a new name.

Before adding one, determine whether:

- an existing skill already covers the behavior;
- the proposed behavior belongs in an existing skill;
- the behavior is sufficiently distinct to justify a separate skill;
- the behavior can be expressed without coupling the skill to one provider.

A new skill should represent a repeatable workflow or meaningful behavioral capability.

---

## Modifying an Existing Skill

When modifying an existing skill:

1. Understand its current contract.
2. Identify the behavior being changed.
3. Check dependencies and related skills.
4. Update behavioral test cases where appropriate.
5. Check whether core contracts are affected.
6. Run repository validation.
7. Run the behavioral test suite.
8. Review the final diff.

Avoid rewriting a skill's methodology simply to make the Markdown shorter.

Nexra skills encode behavioral constraints, not merely descriptions.

---

## Foundation Skills

Nexra currently has seven foundation skills:

```text
project-discovery
capability-assessment
interaction
challenge
execution
verification
reporting
```

These skills define the cross-cutting behavioral model used by domain skills.

Changes to foundation skills can affect the entire system.

Foundation changes should include:

- a clear explanation of the behavioral change;
- affected dependencies;
- updated behavioral cases where necessary;
- validation of the relevant core contracts;
- full repository tests before submission.

---

## Domain Skills

Nexra currently has eight domain skills:

```text
ui-ux-design
animation-design
3d-web-design
scroll-world-flyby
content-code-optimization
seo
security
reviewer
```

Domain skills specialize the foundation methodology for a particular class of work.

### Unified skill boundaries

Some related capabilities intentionally remain within a single skill.

`scroll-world-flyby` covers both spatial scroll experiences and fly-by animation behavior.

`content-code-optimization` covers both content optimization and code optimization as related dimensions of one optimization workflow.

Do not split these into separate skills without a demonstrated architectural reason.

---

## Adapters

Adapters translate canonical Nexra skills into host-specific installation and discovery conventions.

Adapters should remain thin.

They should not become alternate implementations of the skills.

An adapter should document information such as:

- target agent;
- supported project discovery location;
- supported global discovery location;
- installation behavior;
- adapter version;
- evidence/source;
- verification status;
- fallback behavior where applicable.

### Evidence requirements

Provider-specific claims must be supported by:

- authoritative provider documentation;
- reproducible repository tests;
- or another clearly documented source of evidence.

Do not mark unsupported provider behavior as verified.

When native provider behavior cannot be established, use a documented fallback rather than inventing a provider-specific path.

### Safe installation

Adapters must not:

- delete unrelated user skills;
- overwrite unrelated configuration;
- assume undocumented provider paths;
- silently change provider configuration;
- claim native support without evidence.

---

## Integrations

Integrations describe capabilities and access surfaces.

They are divided into:

```text
Plugin
  ↓
Capability / Action Surface
  ↓
requires
  ↓
Connector
  ↓
Resource / Transport / Runtime
```

### Plugins

Plugins describe capabilities such as:

- browser interaction;
- filesystem operations;
- Git operations;
- GitHub operations;
- shell execution;
- package management;
- database operations;
- HTTP requests;
- image inspection;
- test execution;
- container execution;
- MCP interaction.

A plugin manifest does not implement the capability.

It also does not prove that the consuming agent currently has access to that capability.

### Connectors

Connectors describe access to resources, transports, runtimes, or external systems.

Examples include:

```text
local-filesystem
git-repository
github-api
browser-session
shell-runtime
npm-registry
postgresql
http-client
mcp-server
```

If a plugin depends on a connector, that dependency must be declared explicitly.

Do not infer dependencies only from naming conventions.

### Authorization

Integration manifests are not permission grants.

The consuming host remains responsible for:

- authentication;
- authorization;
- credentials;
- sandboxing;
- network restrictions;
- resource limits;
- destructive-action controls.

---

## Core Contracts

The `core/` directory contains the behavioral and orchestration contracts that connect the skill system together.

Important contracts include:

```text
core/specification/BEHAVIOR.md
core/orchestration/PIPELINE.md
core/execution/EXECUTION-CONTRACT.md
core/verification/VERIFICATION-CONTRACT.md
core/reporting/REPORTING-CONTRACT.md
core/registries/skill-registry.yaml
```

Changes to these files should be treated as architectural changes.

When modifying a core contract:

1. Identify which skills and components depend on it.
2. Update affected tests.
3. Check for contradictory behavior elsewhere.
4. Validate the complete repository.
5. Document meaningful behavioral changes.

---

## Testing

Nexra uses both structural validation and behavioral testing.

### Repository validation

Run:

```bash
npm run validate
```

or:

```bash
python3 scripts/validate.py
```

The validator checks repository invariants including:

- canonical skill count;
- skill structure;
- skill metadata;
- required behavioral concepts;
- adapter structure;
- integration manifests;
- package metadata;
- CLI references;
- repository paths;
- provider-agnostic requirements.

### Behavioral tests

Run:

```bash
npm test
```

or:

```bash
python3 scripts/test_suite.py
```

The behavioral suite checks:

- foundation behavior;
- domain skill coverage;
- cross-skill behavior;
- challenge behavior;
- adapters;
- integrations;
- CLI behavior;
- installation behavior.

### Package validation

Before a release, also run:

```bash
npm run pack:test
```

This verifies the files that would be included in the npm package.

### Formatting and whitespace

Run:

```bash
git diff --check
```

A contribution should not introduce whitespace errors.

---

## Documentation

Documentation should be maintained at the appropriate level.

### Root README

`README.md` is the product-facing introduction.

It should explain:

- what Nexra is;
- why it exists;
- how it works;
- installation;
- supported agents;
- core concepts;
- links to deeper documentation.

### Technical documentation

Detailed contracts belong under:

```text
docs/
```

Examples:

```text
docs/spec/SKILL-SPEC.md
docs/adapters/ADAPTER-SPEC.md
docs/architecture.md
docs/testing.md
```

### Adapter documentation

Agent-specific documentation belongs under:

```text
adapters/<agent>/README.md
```

### Integration documentation

Integration architecture belongs under:

```text
integrations/README.md
```

Avoid duplicating large specifications across multiple README files.

---

## Versioning

The current Nexra release line is:

```text
0.1.0
```

Current canonical components use the `0.1.0` release line.

When changing a versioned component:

- update the relevant version field;
- update affected documentation;
- update tests if version behavior is tested;
- avoid creating inconsistent component versions without a clear reason.

### Historical versions

Historical entries in `CHANGELOG.md` must not be rewritten simply to match the current release.

A historical version represents the state of the project at that point in time.

---

## Pull Requests

A useful pull request should clearly explain:

### What changed

Describe the implementation or documentation change.

### Why it changed

Explain the problem or requirement that motivated the change.

### Behavioral impact

Identify any changes to:

- skill behavior;
- orchestration;
- verification;
- reporting;
- adapters;
- integrations;
- CLI behavior.

### Validation

List the commands used to validate the change.

For example:

```text
npm run validate
npm test
npm run pack:test
git diff --check
```

### Limitations

Document anything that could not be verified or any known limitation introduced by the change.

---

## Pre-Submission Checklist

Before submitting a contribution:

- [ ] The change has a clearly defined purpose.
- [ ] Existing skills were checked before adding a new skill.
- [ ] The correct repository layer was used.
- [ ] Provider-specific claims are supported by evidence.
- [ ] No undocumented capabilities are claimed.
- [ ] Relevant behavioral cases were updated.
- [ ] `npm run validate` passes.
- [ ] `npm test` passes.
- [ ] `npm run pack:test` passes when package contents are affected.
- [ ] `git diff --check` passes.
- [ ] Documentation was updated where necessary.
- [ ] Version information is consistent.
- [ ] No unrelated files were changed.
- [ ] The final diff was reviewed manually.

---

## Design Principles to Preserve

Contributions should preserve the following properties of Nexra.

### Capability awareness

Nexra should distinguish between:

```text
Capability exists
Capability is available
Capability is suitable
Capability was actually used
Capability was successfully verified
```

These are different states.

### Evidence over assumption

A system should not treat an assumed capability, path, tool, provider behavior, or execution result as established fact.

### User control

Nexra can discover, assess, recommend, execute, and verify, but the user remains the authority over consequential decisions.

### Graceful degradation

When a capability is unavailable, Nexra should:

1. detect the limitation;
2. explain its effect;
3. use an appropriate fallback when possible;
4. avoid pretending the limitation does not exist.

### Verification

Successful execution and successful verification are not the same thing.

A contribution should preserve the distinction between:

```text
Attempted
Executed
Observed
Verified
```

### Agent agnosticism

The canonical methodology should not depend on one coding agent.

Provider-specific behavior belongs in adapters or integrations when explicitly supported.

### Minimal necessary interaction

Nexra should avoid asking users for information that can be discovered reliably.

At the same time, it should not silently guess when missing information materially changes the result.

---

## License

By contributing to Nexra, you agree that your contributions will be licensed under the project's MIT License.

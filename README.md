# Nexra

> **A capability-aware, user-driven skill system for AI coding agents.**


Nexra is an open-source, agent-agnostic skill system for AI coding agents. It gives agents a repeatable working methodology instead of a collection of disconnected prompts:

**discover → assess capability → understand intent → challenge material problems → plan → execute → verify → report → iterate**

The canonical methodology lives in `skills/`. Host-specific installation and discovery behavior lives in `adapters/`. External capabilities are represented separately through `integrations/`. The `nexra-skills` CLI brings these pieces together for installation, detection, diagnostics, and validation.

---

## Why Nexra exists

AI coding agents can have strong models and extensive tool access and still fail in predictable ways. They may:

- ask the user for information they could have discovered themselves;
- invent requirements instead of resolving uncertainty with evidence;
- treat preferences as technical constraints, or technical constraints as preferences;
- claim visual, runtime, browser, or deployment verification they did not actually perform;
- make broad changes before validating an intermediate result;
- optimize for a preferred framework or implementation instead of the user's actual outcome;
- continue with an unavailable capability instead of adapting the workflow;
- report a task as complete without evidence.

Nexra turns these failure modes into explicit behavioral contracts.

The goal is not to make an agent blindly follow a rigid checklist. The workflow is **adaptive**: discovery, questions, challenge, execution, and verification happen to the depth required by the task.

---

## The Nexra workflow


The complete operating loop is:

1. **Discover** — establish facts about the repository, environment, available tools, and existing implementation.
2. **Assess capability** — determine what the current agent, model, runtime, tools, and environment can actually do.
3. **Understand intent** — separate the literal request from the desired outcome, constraints, and preferences.
4. **Challenge** — surface material security, accessibility, performance, maintainability, feasibility, or requirement conflicts when evidence supports doing so.
5. **Plan** — create a bounded implementation path with appropriate checkpoints.
6. **Execute** — make incremental, controlled changes rather than uncontrolled rewrites.
7. **Verify** — test the outcome at a depth appropriate to the risk and the claim being made.
8. **Report** — state what changed, what evidence exists, what remains uncertain, and what could not be verified.
9. **Iterate** — continue when verification or user feedback shows that more work is required.

This loop is a methodology, not a promise that every task requires every stage at maximum depth.

---

## Design principles

| Principle | Meaning |
|---|---|
| **Discover before asking** | Inspect available facts before requesting information from the user. |
| **Ask only when necessary** | Questions should resolve decisions that cannot be discovered or safely defaulted. |
| **Understand intent** | Optimize for the desired outcome, not merely the literal wording. |
| **Challenge material problems** | Raise substantive technical problems with evidence and alternatives. |
| **Respect user authority** | Recommendations inform the user; they do not silently override them. |
| **Be capability-aware** | Never claim an action, observation, or verification that the agent cannot perform. |
| **Execute incrementally** | Prefer bounded changes and checkpoints over uncontrolled rewrites. |
| **Verify outcomes** | Verification is part of the implementation, not an optional final paragraph. |
| **Report evidence and limits** | Distinguish completed work, tested behavior, and remaining uncertainty. |
| **Degrade gracefully** | When an ideal capability is unavailable, reduce scope, use a safe alternative, or stop. |
| **Remain agent-agnostic** | Canonical skills should not depend on one coding-agent vendor. |
| **Prefer evidence over assumption** | Capability and host behavior should be supported by observable evidence or documented contracts. |

---

## What is inside Nexra?

Nexra deliberately separates four concerns:

- **Skills** — the methodology an agent follows.
- **Adapters** — translation between canonical skills and a host agent's conventions.
- **Integrations** — external capabilities such as tools, plugins, connectors, and runtimes.
- **CLI** — installation, detection, validation, diagnostics, and distribution.


This separation matters. A skill can require a capability without pretending that the capability exists. An adapter can describe how a host loads skills without changing the canonical methodology. An integration can expose a tool without deciding how the skill should reason about the task.

---

# Installation

## Zero-install

The recommended way to try Nexra is through npm:

```bash
npx nexra-skills
```

The CLI detects supported coding agents and guides you through installation.

You can install all canonical skills for the current project with:

```bash
npx nexra-skills install --project --all
```

Or install them globally for your user account:

```bash
npx nexra-skills install --global --all
```

> **Package name:** the published npm package is `nexra-skills`. Its executable is `nexra`. Therefore `npx nexra-skills` is the zero-install invocation, while `nexra` becomes available directly after a global npm installation.

## Global CLI installation

If you want the `nexra` command available directly in your shell:

```bash
npm install -g nexra-skills
```

Then:

```bash
nexra --help
nexra detect
nexra doctor
nexra list
```

## Useful CLI commands

```bash
# Interactive installation
npx nexra-skills

# Install all skills into the current project
npx nexra-skills install --project --all

# Install all skills globally
npx nexra-skills install --global --all

# Detect supported agents
npx nexra-skills detect

# Diagnose the current installation/environment
npx nexra-skills doctor

# List canonical skills
npx nexra-skills list

# Show a specific skill
npx nexra-skills show security

# Show the installed CLI version
npx nexra-skills version
```

The CLI is designed to avoid destructive host configuration changes. Existing files are preserved and Nexra tracks its own managed installation state through `.nexra/` manifests.

---

# Skills

Nexra currently defines **15 canonical skills**.

Each skill has one responsibility. Foundation skills define the general working loop; domain skills provide specialized methodology.

## Foundation skills

| Skill | Purpose |
|---|---|
| `project-discovery` | Establish facts about the project before planning or modifying it. |
| `capability-assessment` | Determine which model, agent, tool, runtime, and environment capabilities are usable. |
| `interaction` | Resolve decision-relevant unknowns while preserving user authority. |
| `challenge` | Surface material problems with evidence, alternatives, and explicit reasoning. |
| `execution` | Turn an approved plan into bounded, reversible implementation steps. |
| `verification` | Match verification depth to risk and to the outcome being claimed. |
| `reporting` | Report changes, evidence, limitations, and remaining work accurately. |

## Domain skills

| Skill | Purpose |
|---|---|
| `ui-ux-design` | Design usable, accessible, responsive interfaces from intent and evidence. |
| `animation-design` | Design purposeful motion with timing, state, accessibility, and performance constraints. |
| `3d-web-design` | Design interactive 3D/web experiences with camera, scene, asset, and performance discipline. |
| `scroll-world-flyby` | Build spatial scroll/fly-by experiences as one continuous scene-navigation discipline. |
| `content-code-optimization` | Improve content quality and code efficiency without optimizing one at the expense of the other. |
| `seo` | Improve crawlability, information architecture, metadata, structured data, and measurable search performance. |
| `security` | Identify and remediate application security risks using evidence, threat modeling, and least privilege. |
| `reviewer` | Conduct structured reviews using severity, evidence, impact, recommendations, and confidence. |

The canonical installable unit is:

```text
skills/<skill-name>/SKILL.md
```

Skills are methodology. They do not themselves grant browser access, shell access, visual inspection, deployment access, or other capabilities.

---

# Capability awareness

Nexra uses four capability states:


| State | Meaning | Expected behavior |
|---|---|---|
| **FULL** | All required capabilities are available. | Execute the intended workflow. |
| **SUITABLE** | Core capabilities are available and the workflow remains practical. | Proceed with bounded adaptation where needed. |
| **CONSTRAINED** | Some capabilities are limited or unavailable. | Reduce scope, lower fidelity, or use an alternate workflow. State the limitation. |
| **UNSUITABLE** | A required capability is unavailable. | Stop or choose an alternative rather than pretending the task was completed. |

The principle is simple:

> **Evidence over assumption.**

For example, a visual-design skill may require browser rendering or image inspection for a particular verification claim. The existence of that requirement does not mean every coding agent has those capabilities.

---

# Adapters

Adapters translate canonical Nexra skills into host-specific installation and discovery conventions.

They are intentionally thin. They should not become alternate copies of the canonical skills.

Current adapter coverage includes:

```text
antigravity
claude-code
cline
codex
cursor
gemini
generic
github-copilot
kiro
opencode
openhands
roo
```

Native installation locations are only used where the repository has sufficient evidence for the host convention. Where a native location is not substantiated, Nexra uses a portable `.agents/skills/` fallback instead of inventing a provider-specific path.

| Agent | Project installation | Global installation |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| OpenCode | `.opencode/skills/` | `~/.config/opencode/skills/` |
| Kiro | `.kiro/skills/` | `~/.kiro/skills/` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Gemini CLI | `.gemini/skills/` | `~/.gemini/skills/` |
| GitHub Copilot CLI | `.github/skills/` | `~/.copilot/skills/` |
| Cline | `.cline/skills/` | `~/.cline/skills/` |
| Generic / unsupported native host | `.agents/skills/` | `~/.agents/skills/` |
| Roo | `.agents/skills/` fallback | `~/.agents/skills/` fallback |
| OpenHands | `.agents/skills/` fallback | `~/.agents/skills/` fallback |
| Antigravity | `.agents/skills/` fallback | `~/.agents/skills/` fallback |

Provider-specific claims are treated as verified only when this repository can substantiate them through reproducible tests or authoritative documentation.

---

# Integrations

Integrations represent capabilities and external systems rather than methodology.

The repository currently separates:

- tool/plugin contracts;
- connector contracts;
- capability metadata;
- provider-specific integration information;
- capability assessment.

This prevents a common failure mode where an agent assumes that because a skill mentions a capability, that capability is automatically available.

See [`integrations/README.md`](integrations/README.md) for the integration model.

---

# Skill structure

Every canonical skill follows:

```text
skills/<name>/
└── SKILL.md
```

The core behavioral contract covers:

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

Domain-specific skills may add specialized guidance, but they must not redefine these responsibilities inconsistently.

See [`docs/spec/SKILL-SPEC.md`](docs/spec/SKILL-SPEC.md) for the canonical skill contract.

---

# Repository structure

```text
Nexra/
├── skills/                  # Canonical installable skills
│   ├── project-discovery/
│   ├── capability-assessment/
│   ├── interaction/
│   ├── challenge/
│   ├── execution/
│   ├── verification/
│   ├── reporting/
│   ├── ui-ux-design/
│   ├── animation-design/
│   ├── 3d-web-design/
│   ├── scroll-world-flyby/
│   ├── content-code-optimization/
│   ├── seo/
│   ├── security/
│   └── reviewer/
│
├── core/                    # Shared orchestration and supporting contracts
├── adapters/                # Agent-specific installation/adaptation metadata
├── integrations/            # Tool, plugin, connector, and capability contracts
├── cli/                     # Nexra command-line interface
├── docs/                    # Specifications and design documentation
├── tests/                   # Structural and behavioral contract tests
└── scripts/                 # Dependency-light validation and test utilities
```

---

# Documentation

The documentation is intentionally separated from the canonical skill definitions.

- [`docs/README.md`](docs/README.md) — documentation index.
- [`docs/spec/SKILL-SPEC.md`](docs/spec/SKILL-SPEC.md) — canonical skill contract.
- [`docs/adapters/ADAPTER-SPEC.md`](docs/adapters/ADAPTER-SPEC.md) — adapter contract.
- [`docs/architecture.md`](docs/architecture.md) — repository architecture and data flow.
- [`docs/testing.md`](docs/testing.md) — validation philosophy and test layers.
- [`adapters/README.md`](adapters/README.md) — supported adapters and adapter architecture.
- [`integrations/README.md`](integrations/README.md) — integrations and capability boundaries.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution guidelines.
- [`CHANGELOG.md`](CHANGELOG.md) — release history.

The canonical behavior lives in `skills/`. Documentation explains the system but does not replace the executable skill contracts.

---

# Validation and testing

Nexra uses multiple validation layers rather than relying on a single test command.

## Requirements

- Python 3.9+
- Node.js 18+
- npm

## Repository validation

```bash
python3 scripts/validate.py
```

The validator checks repository invariants, skill metadata, required sections, Markdown structure, adapters, integrations, links, and release/version consistency.

## Behavioral and contract tests

```bash
python3 scripts/test_suite.py
```

## npm test commands

```bash
npm run validate
npm test
```

## CLI smoke tests

```bash
node cli/bin/nexra.js list
node cli/bin/nexra.js detect
node cli/bin/nexra.js doctor
```

## Package verification

The npm package can be packed and inspected before publication:

```bash
npm run pack:test
```

Verification is treated as a first-class part of the project rather than a final status message.

---

# Development

Clone the repository when you want to develop Nexra itself:

```bash
git clone https://github.com/Muhammad-Wasif-Qamar/Nexra.git
cd Nexra
```

Install dependencies if required by the development workflow:

```bash
npm install
```

Run the repository validation and tests:

```bash
npm run validate
npm test
```

Run the local CLI directly:

```bash
node cli/bin/nexra.js --help
node cli/bin/nexra.js list
node cli/bin/nexra.js detect
node cli/bin/nexra.js doctor
```

Before submitting a change, ensure the relevant contract tests pass and that documentation, skill metadata, adapters, and integration manifests remain consistent.

---

# Contributing

Nexra is designed around small, composable, evidence-oriented contributions.

Before adding a skill, ask:

1. Is this a repeatable workflow problem rather than a one-off prompt?
2. Does the skill have a clearly defined responsibility?
3. Can its behavior remain agent-agnostic?
4. What capabilities does it actually require?
5. How can the outcome be verified?
6. What should happen when the required capability is unavailable?
7. Does the skill duplicate an existing canonical responsibility?

New skills should include behavioral cases and verification criteria. Adapter changes should distinguish documented host behavior from assumptions. Integration changes should make capability boundaries explicit.

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

---

# Design philosophy

Nexra is intentionally not a giant prompt and not a framework-specific agent runtime.

It is a **portable behavioral layer** that can be installed into different coding-agent environments while keeping the methodology stable.

The core distinction is:

```text
Skills       → how the agent should work
Adapters     → how the host exposes those skills
Integrations → what capabilities are actually available
CLI          → how Nexra is installed and managed
```

That separation makes it possible to improve the methodology without coupling it to a single model provider, coding agent, or tool ecosystem.

---

# Current status

Nexra currently includes:

- **15 canonical skills**
- **12 agent adapters**
- **12 plugin integrations**
- **9 connector integrations**
- npm distribution through `nexra-skills`
- interactive and non-interactive installation
- project and global installation modes
- agent detection
- installation manifests
- doctor/diagnostic commands
- repository validation
- behavioral and contract tests

The project is actively evolving. Provider-specific capabilities are deliberately conservative where the repository cannot substantiate a stronger claim.

---

# License

Nexra is released under the **MIT License**.

See [`LICENSE`](LICENSE) for the full license text.

---

<p align="center">
  <sub>Built for agents that should know what they can do before they claim they did it.</sub>
</p>

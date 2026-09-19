# Adapter Behavioral Test Cases

**Test Specification:** 0.1.0

---

## Purpose

These tests verify that Nexra adapters correctly translate the canonical skill system into agent-specific installation and execution conventions.

Adapters are compatibility layers.

They must not redefine the canonical methodology.

The tests therefore focus on:

- adapter metadata;
- target identification;
- installation paths;
- portability;
- skill preservation;
- configuration safety;
- unsupported-agent behavior;
- fallback behavior;
- independence from provider-specific assumptions.

---

# Adapter Inventory

The repository currently defines 12 adapters:

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

Every adapter should describe how Nexra is exposed to its target environment.

---

# Evaluation Principles

Adapter tests are behavioral.

A valid adapter:

1. identifies its target;
2. defines its supported skill location or integration mechanism;
3. preserves canonical skill content;
4. does not silently modify unrelated configuration;
5. does not invent unsupported capabilities;
6. provides a portable fallback where appropriate;
7. remains compatible with future canonical skill changes.

---

# Adapter Metadata

## Case AD-01 — Required Metadata

### Context

An adapter file exists at:

```text
adapters/<target>/adapter.yaml
```

### Expected Behavior

The adapter should identify sufficient metadata to determine:

- adapter name;
- target;
- supported mechanism;
- skill installation location or strategy.

### Forbidden Behavior

An adapter must not depend on undocumented metadata that cannot be determined from the adapter specification.

---

## Case AD-02 — Target Identity

### Context

The repository contains adapters for multiple agents.

### Expected Behavior

Each adapter should clearly identify its intended target.

For example:

```text
claude-code
opencode
gemini
```

must not be represented by an ambiguous generic identifier.

---

# Canonical Skill Preservation

## Case AD-03 — No Skill Rewriting

### Context

A canonical skill contains detailed methodology.

The adapter installs that skill into an agent-specific directory.

### Expected Behavior

The adapter should preserve the substantive canonical content.

Provider-specific installation behavior may differ.

The methodology should not be rewritten into a weaker generic prompt.

### Forbidden Behavior

An adapter must not reduce:

```text
discovery
capability assessment
interaction
challenge
execution
verification
reporting
```

into generic instructions merely because the target agent has a different format.

---

## Case AD-04 — Skill Count

### Context

The repository currently contains 15 canonical skills.

### Expected Behavior

An adapter that supports the full canonical skill set should expose all 15.

Expected count:

```text
15
```

### Forbidden Behavior

Do not silently omit skills while claiming full support.

---

## Case AD-05 — Skill Identity

### Context

The canonical skill:

```text
skills/scroll-world-flyby/SKILL.md
```

is installed through an adapter.

### Expected Behavior

The installed skill remains identifiable as:

```text
scroll-world-flyby
```

### Forbidden Behavior

Do not create separate canonical identities for:

```text
scroll
flyby
```

The registry may expose aliases, but they must resolve to the same skill.

---

# Installation Paths

## Case AD-06 — Native Skill Directory

### Context

A target agent documents a native skill directory.

### Expected Behavior

The adapter should install canonical skills into the documented native location.

---

## Case AD-07 — Portable Fallback

### Context

A target does not provide a documented native skill directory.

### Expected Behavior

The adapter may use the repository's documented portable fallback.

The fallback must be deterministic.

### Forbidden Behavior

Do not guess arbitrary hidden configuration directories.

---

## Case AD-08 — Path Isolation

### Context

The project contains:

```text
.claude/
.opencode/
.agents/
```

### Expected Behavior

An adapter should only modify the locations belonging to its target or the explicitly documented portable mechanism.

### Forbidden Behavior

Installing an OpenCode adapter should not unexpectedly rewrite Claude Code configuration.

---

# Configuration Safety

## Case AD-09 — Preserve Existing Configuration

### Context

The user already has an agent configuration file containing unrelated settings.

### Request

> Install Nexra.

### Expected Behavior

The adapter should preserve unrelated configuration.

If modification is required, it should be minimal and deterministic.

### Forbidden Behavior

Do not overwrite the user's entire configuration file merely to install skills.

---

## Case AD-10 — Existing Skills

### Context

The target directory already contains:

```text
custom-skill/
```

### Request

> Install Nexra.

### Expected Behavior

The adapter should install Nexra skills without deleting unrelated user skills.

---

## Case AD-11 — Existing Nexra Installation

### Context

The target already contains an earlier Nexra installation.

### Request

> Install Nexra again.

### Expected Behavior

The installer should behave deterministically.

It should either:

- update the managed installation;
- replace only managed files;
- or report the existing installation state.

### Forbidden Behavior

Do not duplicate installations indefinitely.

Do not delete unrelated user content.

---

# Multi-Agent Support

## Case AD-12 — Same Canonical Skill

### Context

The same `ui-ux-design` skill is installed for:

```text
Claude Code
OpenCode
Gemini CLI
```

### Expected Behavior

The substantive methodology should remain equivalent across targets.

Only integration or invocation mechanics may differ.

---

## Case AD-13 — Agent-Specific Capability

### Context

One target supports a browser integration and another does not.

### Expected Behavior

The adapter must not falsely advertise browser access for the target that lacks it.

Capability assessment remains responsible for determining actual runtime capabilities.

---

## Case AD-14 — Adapter Does Not Override Capability Assessment

### Context

An adapter declares support for a skill requiring visual inspection.

The current environment has no visual inspection capability.

### Expected Behavior

The adapter may expose the skill.

The capability system should still classify the runtime capability as unavailable.

### Forbidden Behavior

Installing a skill must not imply that every required capability is available.

---

# Generic Adapter

## Case AD-15 — Generic Portability

### Context

No dedicated adapter exists for the user's coding agent.

### Request

> Install Nexra for my agent.

### Expected Behavior

The generic adapter should provide the documented portable installation mechanism.

It should preserve canonical skills without requiring a provider-specific integration.

---

## Case AD-16 — Unknown Agent

### Context

The user is using an agent that Nexra does not explicitly recognize.

### Expected Behavior

The system should:

1. identify that no dedicated adapter exists;
2. use the generic mechanism if supported;
3. avoid claiming native integration.

### Forbidden Behavior

Do not claim:

> Fully integrated with `<unknown-agent>`

without evidence.

---

# Adapter Capability States

## Case AD-17 — Fully Supported Target

### Context

A target provides a documented skill mechanism and installation path.

### Expected Behavior

The adapter may represent the integration as fully supported.

---

## Case AD-18 — Constrained Target

### Context

A target can load Markdown instructions but cannot automatically discover skills.

### Expected Behavior

The adapter should describe the limitation.

It may provide a manual or portable invocation mechanism.

---

## Case AD-19 — Unsupported Target

### Context

A target has no documented way to load external skills or instructions.

### Expected Behavior

The adapter should identify the integration as unsupported or constrained.

### Forbidden Behavior

Do not invent a mechanism.

---

# Versioning

## Case AD-20 — Adapter Version

### Context

The canonical skill system changes.

### Expected Behavior

Adapter metadata should make it possible to determine compatibility where the adapter specification requires it.

---

## Case AD-21 — Skill Version Preservation

### Context

A canonical skill declares:

```yaml
version: 0.2.0
```

### Expected Behavior

The installed skill should retain its canonical version metadata unless the adapter specification explicitly requires a transformation.

---

# Aliases

## Case AD-22 — Scroll Alias

### Context

The user requests:

```text
scroll
```

### Expected Behavior

The registry/adapter resolution may map the alias to:

```text
scroll-world-flyby
```

---

## Case AD-23 — Flyby Alias

### Context

The user requests:

```text
flyby
```

### Expected Behavior

Resolve to:

```text
scroll-world-flyby
```

### Forbidden Behavior

Do not install a second independent canonical skill.

---

# Installation Scope

## Case AD-24 — Project Scope

### Context

The user installs Nexra into a project.

### Expected Behavior

The adapter should install project-scoped skills into the documented project locations.

It should not unexpectedly modify unrelated global agent configuration.

---

## Case AD-25 — Global Scope

### Context

The user explicitly requests a global installation.

### Expected Behavior

The adapter may install into the documented global location.

### Forbidden Behavior

Do not interpret a project installation request as permission for global modification.

---

# Filesystem Safety

## Case AD-26 — Existing User File

### Context

The target directory contains a user-created file with a name that could conflict with installation.

### Expected Behavior

The installer should avoid destructive replacement unless the file is clearly managed by Nexra.

---

## Case AD-27 — Managed File Tracking

### Context

The installation creates a manifest identifying managed files.

### Expected Behavior

The manifest should contain enough information to distinguish Nexra-managed files from unrelated user files.

---

# Installer Idempotency

## Case AD-28 — Repeated Installation

### Context

The user runs the installer twice.

### Expected Behavior

The second installation should produce a stable result.

Expected properties:

```text
no uncontrolled duplication
no unnecessary configuration growth
no deletion of unrelated files
same managed skill set
```

---

# Detection

## Case AD-29 — Detect Installed Agent

### Context

The environment contains configuration directories for multiple agents.

### Expected Behavior

Detection should identify only agents for which there is meaningful evidence.

### Forbidden Behavior

Do not infer an installed agent merely because an arbitrary directory exists.

---

## Case AD-30 — Multiple Agents

### Context

The environment contains supported configurations for:

```text
Claude Code
OpenCode
Gemini CLI
Antigravity
```

### Expected Behavior

The installer may expose installation targets for each detected agent according to its documented behavior.

---

# Doctor / Diagnostics

## Case AD-31 — Healthy Installation

### Context

A valid installation contains:

```text
15 skills
valid manifest
valid target paths
```

### Expected Behavior

Diagnostics should report the installation as healthy.

---

## Case AD-32 — Missing Skill

### Context

One installed skill has been deleted manually.

### Expected Behavior

Diagnostics should identify the missing skill.

### Forbidden Behavior

Do not report the installation as fully healthy.

---

## Case AD-33 — Unexpected File

### Context

A user has added an unrelated file inside the skill directory.

### Expected Behavior

Diagnostics should not treat every user-created file as corruption.

---

# Failure Handling

## Case AD-34 — Permission Error

### Context

The target installation directory is not writable.

### Expected Behavior

The installer should report the failure clearly.

It should not claim successful installation.

---

## Case AD-35 — Missing Source Skill

### Context

An expected canonical skill file is missing from the package.

### Expected Behavior

The installer should fail clearly or report a partial installation state.

### Forbidden Behavior

Do not create a fake placeholder and report success unless the adapter specification explicitly defines such behavior.

---

## Case AD-36 — Interrupted Installation

### Context

Installation stops midway.

### Expected Behavior

The system should leave a diagnosable state.

If recovery is supported, a subsequent installation should be able to reconcile the managed state.

---

# Provider-Specific Configuration

## Case AD-37 — Minimal Provider Configuration

### Context

A provider requires one specific configuration entry to discover installed skills.

### Expected Behavior

The adapter may add that entry.

It should not rewrite unrelated settings.

---

## Case AD-38 — Unsupported Configuration

### Context

A provider has no documented configuration mechanism.

### Expected Behavior

Use the generic or portable mechanism where supported.

### Forbidden Behavior

Do not reverse-engineer or invent undocumented configuration as if it were guaranteed.

---

# Adapter Independence

## Case AD-39 — Canonical Skill Update

### Context

`skills/security/SKILL.md` receives improved methodology.

### Expected Behavior

Adapters should continue exposing the updated canonical skill without requiring manual rewriting of the skill's content.

---

## Case AD-40 — Adapter Replacement

### Context

A dedicated adapter is replaced with an improved implementation.

### Expected Behavior

The canonical skill files should remain unchanged.

---

# Cross-Platform Behavior

## Case AD-41 — macOS

### Context

The installer runs on macOS.

### Expected Behavior

Use platform-appropriate paths and shell behavior.

---

## Case AD-42 — Linux

### Context

The installer runs on Linux.

### Expected Behavior

Use platform-appropriate paths and shell behavior.

---

## Case AD-43 — Windows

### Context

The installer runs on Windows.

### Expected Behavior

The adapter/installer should avoid assumptions that only work on POSIX systems where cross-platform support is claimed.

---

# Security

## Case AD-44 — Path Traversal

### Context

An adapter receives a target path derived from configuration.

### Expected Behavior

Validate or constrain paths so installation cannot unintentionally escape the intended installation scope.

---

## Case AD-45 — Untrusted Configuration

### Context

An installation target contains unexpected configuration values.

### Expected Behavior

The installer should validate inputs before using them for filesystem operations.

---

## Case AD-46 — No Secret Collection

### Context

The adapter does not require credentials.

### Expected Behavior

It should not request or collect credentials merely to install local skills.

---

# Portability

## Case AD-47 — Canonical Content Remains Portable

### Context

The same skill is copied from one adapter target to another.

### Expected Behavior

The skill remains understandable and operational as canonical Markdown.

It must not depend on hidden provider state.

---

## Case AD-48 — No Provider-Specific Instructions in Canonical Skill

### Context

A canonical skill is inspected.

### Expected Behavior

Provider-specific installation instructions should not be required for the core methodology.

Those concerns belong in adapter documentation.

---

# Adapter Documentation

## Case AD-49 — Installation Instructions

### Context

An adapter contains:

```text
README.md
adapter.yaml
```

### Expected Behavior

The README should explain:

- what target it supports;
- how the adapter works;
- relevant limitations;
- installation behavior;
- any target-specific requirements.

---

## Case AD-50 — Limitations

### Context

An adapter has constrained support.

### Expected Behavior

The adapter documentation should state the limitation.

### Forbidden Behavior

Do not describe constrained support as native/full integration.

---

# Adapter Test Completion Criteria

The adapter suite is sufficiently complete when:

- [ ] all 12 adapters can be validated;
- [ ] adapter metadata is validated;
- [ ] canonical skills remain intact;
- [ ] full skill sets are exposed where claimed;
- [ ] installation paths are deterministic;
- [ ] project/global scope is respected;
- [ ] existing configuration is preserved;
- [ ] existing user skills are preserved;
- [ ] repeated installation is safe;
- [ ] missing files are detected;
- [ ] installation failures are reported;
- [ ] capability claims remain honest;
- [ ] generic fallback behavior is defined;
- [ ] aliases resolve correctly;
- [ ] provider-specific logic remains isolated;
- [ ] canonical skills remain provider-agnostic;
- [ ] cross-platform assumptions are controlled;
- [ ] security-sensitive filesystem behavior is validated.

---

# Core Principle

An adapter answers:

> How does this agent consume Nexra?

It must not redefine:

> What should Nexra teach the agent?

The first belongs to adapters.

The second belongs to canonical skills and the core behavioral specification.
# Nexra Adapter Specification

**Specification Version:** 1.0.0

---

## 1. Purpose

Adapters define how Nexra is integrated with a specific AI coding agent or host environment.

Nexra's canonical skills remain agent-agnostic.

The adapter provides the translation layer between:

```text
Nexra
  ↓
Canonical Skills
  ↓
Adapter
  ↓
Agent / Host Environment
```

An adapter describes how a host discovers, installs, and consumes Nexra skills.

It does not redefine the methodology of those skills.

---

## 2. Core Principle

> Skills define what methodology should be followed. Adapters define how that methodology is made available to a particular host.

This separation allows the same Nexra skill to be used across different agents without maintaining separate implementations of the skill itself.

---

## 3. Adapter Responsibilities

An adapter may define:

- host identity;
- supported host platforms;
- installation mechanisms;
- skill discovery mechanisms;
- project-local installation;
- user-global installation;
- skill target locations;
- host-specific metadata;
- capability requirements;
- compatibility limitations;
- configuration requirements;
- verification requirements;
- host-specific integration behavior.

An adapter may also describe limitations where the target host does not support a particular Nexra capability.

---

## 4. Adapter Non-Responsibilities

An adapter must not:

- redefine canonical skill methodology;
- maintain an independent copy of a canonical skill;
- silently modify user decisions;
- remove Nexra verification requirements;
- claim capabilities that the host does not provide;
- invent unsupported host behavior;
- embed provider-specific behavior into canonical skills;
- silently overwrite unrelated user configuration.

---

## 5. Adapter Lifecycle

An adapter follows this general lifecycle:

```text
DETECT
  ↓
ASSESS
  ↓
INSTALL
  ↓
DISCOVER
  ↓
EXECUTE
  ↓
VERIFY
```

Not every host supports every stage natively.

Where a stage is unsupported, the adapter must describe the limitation rather than pretending that support exists.

---

## 6. Adapter Metadata

Each adapter is represented by:

```text
adapters/<adapter-id>/adapter.yaml
```

A minimal adapter manifest has the following structure:

```yaml
id: opencode
name: OpenCode

adapter:
  schema_version: "1.0"
  version: "0.1.0"
  platform: opencode

installation:
  project:
    supported: true
    target: ".opencode/skills/"
  global:
    supported: false

skills:
  source: "skills/"
  discovery: "native"

capabilities:
  discovery: true
  filesystem: true
  terminal: true
```

The exact capability set may differ between hosts.

---

## 7. Required Fields

Every adapter manifest must provide:

```text
id
name
adapter.schema_version
adapter.version
adapter.platform
installation
skills
capabilities
```

The manifest may contain additional fields when they provide useful host-specific information.

---

## 8. Adapter Identity

### `id`

`id` is the stable machine-readable identifier.

Requirements:

- unique within Nexra;
- lowercase;
- kebab-case;
- stable across releases;
- independent of installation paths.

Example:

```yaml
id: claude-code
```

The identifier represents the host integration, not a particular user's machine.

---

## 9. Adapter Name

### `name`

`name` is the human-readable host name.

Example:

```yaml
name: Claude Code
```

The name may contain spaces, capitalization, and the host's official product naming.

---

## 10. Adapter Schema Version

### `adapter.schema_version`

This identifies the structure of the adapter manifest.

Example:

```yaml
adapter:
  schema_version: "1.0"
```

The schema version changes when the structure or meaning of adapter manifests changes.

It is independent of the adapter implementation version.

---

## 11. Adapter Version

### `adapter.version`

This identifies the version of the individual adapter implementation.

Example:

```yaml
adapter:
  version: "0.1.0"
```

This is independent from:

```text
Nexra release version
Skill versions
Adapter schema version
```

For example:

```text
Nexra release:       0.1.0
Adapter version:     0.2.0
Adapter schema:      1.0
Skill version:       0.1.0
```

These versions serve different purposes.

---

## 12. Platform

### `adapter.platform`

This identifies the target host.

Example:

```yaml
adapter:
  platform: opencode
```

The value should correspond to the adapter's `id` unless the host requires a documented distinction.

---

## 13. Installation

The `installation` section describes how Nexra skills are made available to the host.

Example:

```yaml
installation:
  project:
    supported: true
    target: ".opencode/skills/"

  global:
    supported: false
```

Installation metadata describes the adapter's supported installation mechanisms.

It does not itself perform installation.

The CLI or another Nexra execution layer is responsible for carrying out installation.

---

## 14. Project Installation

Project installation applies Nexra to a specific repository or workspace.

Example:

```yaml
installation:
  project:
    supported: true
    target: ".agent/skills/"
```

If a host does not provide a native project-level skill directory:

```yaml
installation:
  project:
    supported: false
```

Do not invent a target directory simply because another agent uses one.

---

## 15. Global Installation

Global installation makes Nexra skills available across multiple projects.

Example:

```yaml
installation:
  global:
    supported: true
    target: "~/.agent/skills/"
```

If the host does not provide a documented global mechanism:

```yaml
installation:
  global:
    supported: false
```

Global paths must be based on documented host behavior.

They must not be guessed.

---

## 16. Skill Source

### `skills.source`

The canonical Nexra skill source is:

```text
skills/<skill-id>/SKILL.md
```

The adapter consumes the canonical skill rather than maintaining an independent implementation.

Example:

```yaml
skills:
  source: "skills/"
```

Adapters must not silently introduce a second canonical skill source.

---

## 17. Skill Discovery

### `skills.discovery`

This field describes how the target host discovers installed skills.

Possible values include:

```text
native
instruction-file
configuration
filesystem
manual
unsupported
```

Example:

```yaml
skills:
  discovery: native
```

The value must describe actual host behavior.

If discovery depends on a host configuration file, document that mechanism rather than labeling it `native`.

---

## 18. Capabilities

The `capabilities` section describes relevant host capabilities.

Example:

```yaml
capabilities:
  discovery: true
  filesystem: true
  terminal: true
```

Capabilities are informational compatibility metadata.

They do not grant capabilities to the agent.

They describe capabilities available through the target host or its supported integration environment.

---

## 19. Capability States

Where a simple boolean is insufficient, an adapter may describe capability states.

Canonical Nexra capability states are:

```text
FULL
SUITABLE
CONSTRAINED
UNSUITABLE
```

Example:

```yaml
capabilities:
  filesystem:
    state: FULL

  browser:
    state: CONSTRAINED

  database:
    state: UNSUITABLE
```

The state must be supported by evidence from the host environment or documented integration behavior.

---

## 20. Capability Evidence

Adapters should avoid making unsupported capability claims.

Where practical, capability metadata may include evidence:

```yaml
capabilities:
  terminal:
    state: FULL
    evidence:
      - "Host provides integrated terminal execution."
```

Evidence should describe observable or documented behavior.

It should not rely on assumptions such as:

```yaml
evidence:
  - "The agent probably has terminal access."
```

---

## 21. Compatibility

Adapters may declare compatibility information.

Example:

```yaml
compatibility:
  operating_systems:
    - macos
    - linux
    - windows

  requirements:
    - "Agent must support project-level skills."
```

Compatibility requirements must be specific enough to be testable.

---

## 22. Limitations

Known limitations should be explicitly declared.

Example:

```yaml
limitations:
  - "Global skill installation is not supported."
  - "Browser capabilities require an external integration."
```

Limitations are preferable to silently falling back to behavior that the host does not officially support.

---

## 23. Verification

Adapters should define how installation or integration can be verified.

Example:

```yaml
verification:
  project:
    expected_path: ".opencode/skills/"
```

Verification should establish that the adapter's claimed installation state actually exists.

An adapter must not report successful installation solely because a command completed without an error.

---

## 24. Agent-Agnostic Skills

Canonical skills must remain independent of adapters.

For example:

```text
skills/security/SKILL.md
```

must describe the security methodology.

It must not contain instructions such as:

```text
Use the OpenCode terminal.
Use Claude Code commands.
Write this file to .cursor/.
```

Those concerns belong to the adapter or integration layer.

---

## 25. Adapter vs Integration

Adapters and integrations have different responsibilities.

### Adapter

Describes:

```text
How Nexra fits a host.
```

### Integration

Describes:

```text
How Nexra accesses or uses an external capability.
```

Examples of integrations include:

```text
filesystem
shell
browser
git
GitHub
database
MCP
HTTP
container
```

An adapter may depend on integrations, but it should not redefine them.

---

## 26. Adapter vs Skill

A skill defines methodology.

An adapter defines host compatibility.

For example:

```text
Security Skill
    ↓
Security methodology
    ↓
Claude Code Adapter
    ↓
Claude Code skill discovery / installation
```

The security methodology remains identical regardless of the host.

---

## 27. Registry

All supported adapters must be registered in:

```text
adapters/registry.yaml
```

The registry is the authoritative index of adapter manifests.

An adapter directory that is not registered must not be treated as a supported Nexra adapter.

Conversely, the registry must not reference a missing adapter.

---

## 28. Adapter Directory Structure

The canonical structure is:

```text
adapters/
├── README.md
├── registry.yaml
│
├── antigravity/
│   └── adapter.yaml
├── claude-code/
│   └── adapter.yaml
├── cline/
│   └── adapter.yaml
├── codex/
│   └── adapter.yaml
├── cursor/
│   └── adapter.yaml
├── gemini/
│   └── adapter.yaml
├── generic/
│   └── adapter.yaml
├── github-copilot/
│   └── adapter.yaml
├── kiro/
│   └── adapter.yaml
├── opencode/
│   └── adapter.yaml
├── openhands/
│   └── adapter.yaml
└── roo/
    └── adapter.yaml
```

Individual adapter README files are not required.

Adapter documentation is maintained collectively in:

```text
adapters/README.md
```

---

## 29. Validation Requirements

A valid adapter must satisfy all of the following:

1. Its directory exists.
2. Its `adapter.yaml` exists.
3. Its `id` is present.
4. Its `id` matches the adapter directory.
5. Its `name` is present.
6. Its `adapter.schema_version` is present.
7. Its `adapter.version` is present.
8. Its `adapter.platform` is present.
9. Its `installation` section is present.
10. Its `skills` section is present.
11. Its `capabilities` section is present.
12. Its adapter is registered in `adapters/registry.yaml`.
13. The registry does not contain missing adapters.
14. The manifest does not maintain a second canonical skill source.
15. The manifest follows the schema defined by this document.

---

## 30. Versioning Rules

Adapter changes should follow normal semantic versioning principles.

Changes to adapter behavior may require an adapter version change.

Changes to the adapter manifest structure require a schema version change.

Changes to Nexra itself do not automatically require every adapter's implementation version to change.

---

## 31. Evidence Over Assumption

Nexra adapters must prefer verified host behavior over assumptions.

When host behavior is unknown:

```text
unknown
```

is preferable to:

```text
supported
```

An adapter should not claim support simply because a similar agent provides that capability.

This principle is especially important for:

- installation paths;
- global configuration;
- skill discovery;
- tool access;
- MCP support;
- browser access;
- filesystem access;
- terminal execution.

---

## 32. Design Goal

The adapter system should allow Nexra to support additional AI coding agents without modifying the canonical skills.

The intended architecture is:

```text
                 ┌─────────────────────┐
                 │   Canonical Skills  │
                 └──────────┬──────────┘
                            │
                ┌───────────┴───────────┐
                │       Nexra Core      │
                └───────────┬───────────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
      Adapter A         Adapter B         Adapter C
          │                 │                 │
       Agent A           Agent B           Agent C
```

Adding support for a new host should primarily require a new adapter rather than changes to the canonical skill methodology.

---

## 33. Summary

Nexra separates four concerns:

```text
SKILLS
Methodology

CORE
Contracts and orchestration

ADAPTERS
Host-specific translation and installation

INTEGRATIONS
External capabilities and systems
```

This separation is a core architectural requirement.

Adapters make Nexra portable across AI coding environments without coupling the canonical skill system to any particular provider.

# Nexra Adapters

Adapters are Nexra's **host-compatibility layer**.

They describe how canonical Nexra skills are detected, installed, discovered,
and verified for a specific AI coding agent. They do not contain alternate
copies of skills and they do not grant capabilities to the host.

## Architecture

```text
Nexra Skills
    │
    ▼
Canonical methodology
    │
    ▼
Adapter contract
    │
    ▼
Host-specific skill location / discovery model
    │
    ▼
AI coding agent
```

The adapter layer deliberately separates four claims:

```text
DETECTED
   ≠
INSTALLABLE
   ≠
DISCOVERABLE
   ≠
EXECUTABLE
```

A detected executable does not prove that a host will discover a skill. A file
written to a documented location does not prove that the host executed it.
Nexra records these boundaries instead of treating installation as proof of
runtime behavior.

## Adapter Inventory

Nexra currently defines adapters for:

| Adapter | Host | Skill mechanism | Compatibility status |
|---|---|---|---|
| `claude-code` | Claude Code | Native Agent Skills | Verified from official documentation |
| `opencode` | OpenCode | Native Agent Skills | Verified from official documentation |
| `kiro` | Kiro | Native Agent Skills | Verified from official documentation |
| `cursor` | Cursor | Native Agent Skills | Verified from official documentation |
| `codex` | Codex | Native Agent Skills | Verified from official documentation |
| `gemini` | Gemini CLI | Native Agent Skills | Verified from official documentation |
| `github-copilot` | GitHub Copilot CLI | Agent Skills | Verified from official documentation |
| `cline` | Cline | Agent Skills | Host-specific behavior requires runtime verification |
| `roo` | Roo | Agent Skills / portable fallback | Host-specific behavior requires runtime verification |
| `openhands` | OpenHands | Portable Agent Skills | Host-specific behavior requires runtime verification |
| `antigravity` | Google Antigravity | Native Agent Skills | Verified from official documentation |
| `generic` | Generic Agent Skills host | Agent Skills standard | Standard-based fallback |

The authoritative inventory is `registry.yaml`.

## Directory Layout

Each adapter keeps its manifest in a dedicated directory so the adapter can
later gain host-specific templates or translation assets without requiring a
repository-wide layout change.

```text
adapters/
├── README.md
├── registry.yaml
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

There is intentionally **one collective README** rather than one README per
adapter. The YAML manifests are the machine-readable source of truth; this
document explains the shared architecture.

## Manifest Model

Every adapter uses the same top-level contract:

```yaml
schema_version: 1
id: example-agent
name: Example Agent
version: 0.1.0
type: adapter

target:
  family: coding-agent
  detection:
    commands: []

skills:
  standard: agent-skills
  source: ../../skills
  discovery:
    project: []
    global: []

installation:
  strategy: native-skill-directory
  project: null
  global: null
  source: ../../skills

compatibility:
  status: unverified
  evidence: []

claims:
  verified: false
  verification_scope: repository-contract-only

capabilities:
  filesystem: host-dependent
  terminal: host-dependent
  browser: host-dependent
  mcp: host-dependent
```

### Important fields

- `target.detection` describes how Nexra can identify a host when that is
  supported by the CLI.
- `skills.discovery` records documented skill locations rather than inventing
  paths.
- `installation` describes where Nexra may place canonical skills.
- `compatibility` records the evidence state for host-specific behavior.
- `claims` preserves the explicit verification boundary used by Nexra's
  validation layer.
- `capabilities` describes host-dependent capabilities and does not grant or
  infer permissions.

## Verification States

Adapter compatibility uses three practical states:

### `verified`

The relevant host skill mechanism and paths are supported by current provider
documentation cited in the manifest.

This does **not** mean Nexra has executed an end-to-end runtime test against
every host version.

### `unverified`

Nexra has an adapter boundary or portable fallback, but this repository does
not currently have sufficient provider-specific evidence to make a stronger
claim.

### `standard`

The adapter targets the open Agent Skills convention rather than a proprietary
host-specific mechanism.

## Design Rules

Adapters must:

- translate host conventions without rewriting skill methodology;
- use explicit, documented paths when available;
- distinguish detection from discovery and execution;
- preserve graceful degradation when native behavior is unavailable;
- keep provider claims evidence-based;
- remain versioned independently from the host agent's own version.

Adapters must not:

- duplicate `skills/*/SKILL.md` content;
- invent provider-specific configuration files;
- claim successful discovery merely because a file was copied;
- claim execution merely because discovery is documented;
- grant MCP, browser, terminal, filesystem, or other capabilities;
- silently modify host configuration outside the documented installation
  contract.

## Agent Skills Compatibility

Several supported agents now consume the same open Agent Skills structure.
Where that is true, Nexra keeps the skill itself canonical and only changes the
installation/discovery location through the adapter.

This makes a portable skill usable across multiple hosts without maintaining
separate skill implementations.

## Adding an Adapter

Before adding a new adapter:

1. Confirm that a genuine host-specific boundary exists.
2. Verify the host's current skill mechanism.
3. Add a manifest under `adapters/<id>/adapter.yaml`.
4. Register it in `registry.yaml`.
5. Mark claims as verified only when the repository has appropriate evidence.
6. Add or update adapter contract tests.
7. Update the CLI only when the host needs detection or installation behavior
   that cannot be derived from the adapter metadata.
8. Run the repository validation and behavioral tests.

Do not add an adapter simply because another AI agent has a different brand
name. The adapter exists to bridge a real compatibility boundary.

## Related Documentation

- `docs/adapters/ADAPTER-SPEC.md` — adapter contract specification
- `skills/` — canonical installable skills
- `core/` — behavioral and orchestration contracts
- `integrations/` — capability and access contracts
- `tests/adapters/` — adapter contract cases

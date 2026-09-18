# Adapter Specification

**Specification Version:** 0.1.0

---

## 1. Purpose

Adapters define how The-Builder's canonical skills are exposed to a specific AI coding agent.

The canonical skill system must remain agent-agnostic.

An adapter translates between:

```text
The-Builder
    ↓
canonical skills / contracts
    ↓
agent-specific capabilities
```

The adapter is responsible for compatibility.

It must not redefine the underlying methodology of a skill.

---

# 2. Core Principle

> Skills define how work should be performed. Adapters define how those skills are delivered to a particular agent.

This distinction is fundamental.

A skill should not contain provider-specific instructions merely because one adapter requires them.

---

# 3. Adapter Responsibilities

An adapter may define:

- installation location;
- file layout;
- metadata translation;
- activation mechanism;
- supported capability mappings;
- agent-specific configuration;
- compatibility limitations;
- discovery of available agent features.

---

# 4. Adapter Non-Responsibilities

An adapter must not silently:

- change the meaning of a skill;
- override user decisions;
- remove verification requirements;
- claim unavailable capabilities;
- redefine canonical skill behavior;
- introduce provider-specific assumptions into the canonical skill.

---

# 5. Adapter Metadata

Each adapter should provide machine-readable metadata.

Example:

```yaml
id: opencode
name: OpenCode
version: "0.1.0"

adapter:
  schema_version: "1.0"
  platform: opencode

skills:
  source: skills/
  target: .opencode/skills/

capabilities:
  discovery: true
  filesystem: true
  terminal: true
```

The exact fields may evolve.

---

# 6. Required Adapter Fields

An adapter should identify:

```text
id
name
version
platform
skill source
skill target
capability model
```

Additional fields may be included where useful.

---

# 7. Adapter Identity

`id` must be:

- unique;
- stable;
- machine-readable;
- independent of installation path.

Example:

```yaml
id: claude-code
```

Do not use:

```yaml
id: my-computer-claude-install
```

---

# 8. Adapter Version

The adapter version describes the adapter implementation.

It is independent from:

```text
The-Builder release version
```

and:

```text
individual skill version
```

Example:

```yaml
adapter version: 0.2.0
skill version: 0.1.0
```

These may evolve independently.

---

# 9. Canonical Skill Source

Adapters consume skills from:

```text
skills/<skill-id>/SKILL.md
```

The canonical skill remains the source of truth.

An adapter should not maintain a second manually edited copy of the skill methodology.

---

# 10. Installation Target

The adapter must define where the target agent expects skills.

Examples may include:

```text
.claude/skills/
.opencode/skills/
.gemini/skills/
.agents/skills/
```

The adapter must document whether the location is:

```text
project-local
user-global
portable fallback
```

---

# 11. Project-Local Installation

Project-local installation means the skill applies to one repository or workspace.

Example:

```text
project/
├── .agent-specific-directory/
│   └── skills/
```

This is generally appropriate when skill behavior depends on project context.

---

# 12. Global Installation

Global installation means the skill is available across projects.

Global paths must not be guessed.

An adapter should document the supported global mechanism.

---

# 13. Portable Fallback

When an agent-specific native skill directory is unavailable, an adapter may provide a documented portable fallback.

The fallback must be:

- deterministic;
- documented;
- non-destructive;
- compatible with the target agent's normal instruction mechanism.

The fallback must not silently overwrite unrelated configuration.

---

# 14. Host Configuration

Adapters may need to interact with host configuration.

Before modifying configuration:

```text
inspect
→ determine whether the configuration exists
→ preserve unrelated settings
→ apply only required changes
```

Do not replace an entire configuration file merely to add one skill reference.

---

# 15. Configuration Preservation

Adapters must preserve existing user configuration.

For example:

```yaml
existing_setting: true
```

must not disappear because The-Builder adds:

```yaml
the_builder:
  enabled: true
```

Prefer minimal modifications.

---

# 16. Adapter Installation

A standard installation flow is:

```text
detect target
↓
validate compatibility
↓
resolve skill set
↓
determine target paths
↓
create required directories
↓
install skills
↓
write manifest
↓
verify installation
```

---

# 17. Detection

Detection should establish whether the target agent is present.

Possible evidence:

```text
known executable
known project directory
known configuration
environment information
explicit user selection
```

Do not claim an agent is installed based solely on a weak assumption.

---

# 18. Explicit Target Selection

If the user explicitly selects a target:

```text
install for OpenCode
```

the adapter may proceed without requiring automatic detection of that same target.

Explicit user input is authoritative unless technically impossible.

---

# 19. Automatic Detection

Automatic detection should be conservative.

Possible states:

```text
DETECTED
NOT_DETECTED
AMBIGUOUS
UNSUPPORTED
```

Do not treat:

```text
directory exists
```

as definitive evidence that a complete agent installation exists unless that is a documented detection method.

---

# 20. Unsupported Agent

If an agent is unsupported:

```text
do not pretend compatibility
```

The installer may offer:

```text
generic adapter
portable skill installation
manual integration instructions
```

when supported.

---

# 21. Capability Mapping

Adapters may translate agent-specific capabilities into canonical capability concepts.

Examples:

```text
filesystem
terminal
browser
image inspection
MCP
subagents
network
```

The canonical skill should reason about capabilities, not proprietary feature names.

---

# 22. Capability Translation

Example:

```yaml
agent:
  browser_tool: true

canonical:
  browser: true
```

The mapping belongs in the adapter layer.

---

# 23. Capability Absence

If a target agent lacks a capability:

```text
mark it unavailable
```

Do not modify the skill to pretend that the capability exists.

The skill's graceful-degradation behavior should determine what happens next.

---

# 24. Capability State

Adapters may expose evidence used to determine:

```text
FULL
SUITABLE
CONSTRAINED
UNSUITABLE
```

The adapter should provide facts.

Capability assessment determines the resulting state.

---

# 25. Skill Selection

An adapter may support installation of:

```text
all skills
foundation only
selected skills
domain-specific skills
```

The canonical registry determines which skills exist.

---

# 26. Skill Dependencies

When installing a skill with dependencies, the installer should resolve the dependency graph.

Example:

```text
scroll-world-flyby
    ↓
animation-design
    ↓
ui-ux-design
```

The exact installation policy may allow dependency installation automatically or require explicit selection, but the behavior must be deterministic and documented.

---

# 27. Dependency Resolution

Dependency resolution must:

- resolve known skill IDs;
- detect missing dependencies;
- detect cycles;
- avoid duplicate installation;
- preserve version information.

---

# 28. Circular Dependencies

Circular dependencies are invalid.

Example:

```text
A → B
B → A
```

The installer should fail validation rather than recursively attempting installation.

---

# 29. Version Compatibility

Adapters should distinguish:

```text
adapter compatibility
skill compatibility
agent compatibility
```

A skill version does not automatically imply compatibility with every agent version.

---

# 30. Compatibility States

Recommended states:

```text
SUPPORTED
SUPPORTED_WITH_LIMITATIONS
UNSUPPORTED
UNKNOWN
```

---

# 31. Supported

The adapter has a documented integration mechanism for the target.

---

# 32. Supported With Limitations

The adapter can install and expose the skill, but one or more capabilities are constrained.

Example:

```text
Skills installed successfully.
Browser-based visual verification is unavailable.
```

---

# 33. Unsupported

No reliable integration mechanism exists.

Do not claim successful installation.

---

# 34. Unknown

The target's compatibility cannot be established with available evidence.

Treat unknown compatibility conservatively.

---

# 35. Installation Manifest

Installations should produce a manifest where practical.

The manifest should identify:

```yaml
schema: 1
version: 0.1.0
scope: project
skills:
  - project-discovery
  - capability-assessment
adapters:
  - opencode
targets:
  - ...
```

The manifest provides installation traceability.

---

# 36. Manifest Purpose

The manifest can be used to:

- inspect installed skills;
- diagnose incomplete installations;
- determine what The-Builder installed;
- support upgrades;
- support cleanup;
- avoid ambiguous ownership.

---

# 37. Ownership

An adapter should be able to determine which files it owns.

This is important for safe updates and removal.

Do not delete files merely because they exist inside a target directory.

---

# 38. Existing Skills

If a target skill already exists, the installer must have a deterministic policy.

Possible policies:

```text
REPLACE
SKIP
BACKUP_AND_REPLACE
FAIL
```

The selected policy must be documented.

---

# 39. User-Owned Files

Never assume every file in a skill directory belongs to The-Builder.

Ownership should be established through:

```text
manifest
installation metadata
known generated structure
```

where possible.

---

# 40. Non-Destructive Installation

Installation should avoid:

```text
overwriting unrelated files
deleting unknown files
rewriting user configuration
changing project dependencies
```

unless explicitly required and authorized.

---

# 41. Upgrade

An upgrade should:

```text
inspect current installation
→ compare versions
→ determine changed skills
→ update owned files
→ preserve unrelated files
→ update manifest
→ verify
```

---

# 42. Downgrade

Downgrades should not be assumed to be safe.

If supported, the adapter should:

```text
identify current version
→ determine target version
→ check compatibility
→ restore supported skill versions
→ verify
```

---

# 43. Uninstall

Uninstallation should remove only The-Builder-owned artifacts.

It should not remove:

```text
user-created files
unrelated skills
agent configuration unrelated to The-Builder
```

---

# 44. Installation Verification

After installation, verify:

```text
expected directories exist
expected SKILL.md files exist
manifest exists
skill count matches selection
target paths are correct
```

---

# 45. Adapter Verification

Adapter tests should verify behavior rather than only file existence.

Examples:

```text
correct target selected
skills copied to correct location
existing configuration preserved
manifest generated correctly
unsupported target rejected
dependency resolution works
```

---

# 46. Failure Handling

When installation fails:

```text
report the failure
identify the stage
avoid partial silent state
preserve unrelated user data
```

Where practical, clean up incomplete The-Builder-owned artifacts.

---

# 47. Partial Installation

If partial installation cannot be avoided, record it.

Example:

```text
Status: PARTIAL

Installed:
- 12 of 15 skills

Failed:
- reviewer
- security
- seo

Reason:
Target directory was not writable.
```

---

# 48. Dry Run

Adapters should support a dry-run concept where practical.

A dry run should show:

```text
target
skills
paths
configuration changes
potential conflicts
```

without modifying the project.

---

# 49. Determinism

Given the same:

```text
repository state
agent target
skill selection
configuration
```

the adapter should produce the same installation plan.

Avoid hidden state where possible.

---

# 50. Portability

Canonical skills must remain portable.

An adapter may translate:

```text
installation
metadata
activation
capability detection
```

but should not fork the skill's fundamental methodology.

---

# 51. Agent-Specific Extensions

Agent-specific extensions are permitted when necessary.

Examples:

```text
native skill metadata
native configuration
agent-specific activation
agent-specific capability mapping
```

Extensions belong in:

```text
adapters/<agent>/
```

not inside canonical skills.

---

# 52. Generic Adapter

The generic adapter exists for environments without a dedicated native integration.

It should provide the most portable supported mechanism.

It must clearly document limitations.

---

# 53. Adapter Directory Structure

Recommended structure:

```text
adapters/
└── <agent>/
    ├── README.md
    └── adapter.yaml
```

Optional files may be added when required.

---

# 54. `adapter.yaml`

A minimal adapter definition:

```yaml
id: example-agent
name: Example Agent
version: "0.1.0"

adapter:
  schema_version: "1.0"
  platform: example-agent

skills:
  source: skills/
  target: .example/skills/

capabilities:
  filesystem: true
  terminal: true
  browser: false
```

---

# 55. Adapter README

Each adapter README should explain:

```text
supported target
installation behavior
skill location
capability limitations
configuration behavior
verification
known limitations
```

---

# 56. Agent Independence

Canonical skills must not contain instructions such as:

```text
Use Claude's specific tool X.
```

unless that information belongs to an adapter-specific implementation.

Instead:

```text
Use the available browser capability to inspect the rendered page.
```

The adapter determines how that capability is exposed.

---

# 57. MCP

MCP availability is a capability concern.

An adapter may detect or configure MCP integration when the target supports it.

The canonical skill should describe the capability required, not assume a particular MCP server.

---

# 58. Tools vs Skills

Adapters must preserve the distinction:

```text
Skill
= methodology

Tool
= capability/action

MCP
= protocol for exposing capabilities/tools
```

Installing a skill does not automatically imply that every tool required by that skill exists.

---

# 59. Graceful Degradation

If optional capabilities are unavailable:

```text
install skill
→ preserve methodology
→ expose limitation
→ allow capability assessment to adapt execution
```

Do not silently remove important instructions.

---

# 60. Security

Adapters execute installation and configuration operations.

They must therefore avoid:

```text
arbitrary remote code execution
unexpected downloads
credential collection
silent configuration changes
unsafe shell execution
```

Only perform required operations.

---

# 61. Remote Sources

If skills are downloaded remotely:

```text
verify source
validate package
prefer integrity checks
avoid executing downloaded content during installation
```

Do not execute arbitrary repository content merely to install Markdown skills.

---

# 62. Path Safety

Adapters must prevent path traversal.

A skill path such as:

```text
../../some-file
```

must not be allowed to escape the intended installation root.

---

# 63. Permission Errors

If the destination is not writable:

```text
report the permission problem
```

Do not bypass operating-system protections through unsafe privilege escalation.

---

# 64. Platform Differences

Adapters may account for:

```text
Windows
macOS
Linux
```

and differences in:

- paths;
- executables;
- shell behavior;
- configuration locations.

Canonical skills remain platform-neutral unless the task itself is platform-specific.

---

# 65. Adapter Reporting

Installation reports should include:

```text
target
scope
skills installed
skills skipped
skills failed
destination
verification
limitations
```

Example:

```text
Target: OpenCode
Scope: project

Installed:
15 skills

Destination:
.opencode/skills/

Verification:
15/15 skill files present

Status:
COMPLETE
```

---

# 66. Adapter Errors

Use actionable errors.

Weak:

```text
Adapter failed.
```

Strong:

```text
OpenCode target directory could not be determined.
Specify a project target or use the generic adapter.
```

---

# 67. Adapter Testing

Every adapter should have tests covering, where applicable:

- metadata validity;
- target detection;
- installation;
- skill count;
- path resolution;
- dependency handling;
- manifest generation;
- conflict handling;
- unsupported environments;
- preservation of existing configuration.

---

# 68. Adapter Completion Criteria

An adapter is considered complete when:

- [ ] adapter metadata is valid;
- [ ] target platform is clearly identified;
- [ ] installation location is deterministic;
- [ ] canonical skills are consumed without methodology forks;
- [ ] capability limitations are represented honestly;
- [ ] user configuration is preserved;
- [ ] installation is verifiable;
- [ ] failure behavior is defined;
- [ ] ownership is clear;
- [ ] tests cover important adapter behavior;
- [ ] documentation describes limitations.

---

# 69. Adapter Anti-Patterns

## Skill Forking

Maintaining a provider-specific copy of canonical methodology.

## Provider Leakage

Embedding provider-specific instructions inside canonical skills.

## Blind Overwrite

Replacing user configuration without inspection.

## False Detection

Assuming an agent is installed without sufficient evidence.

## Capability Fabrication

Claiming tools exist because the target theoretically supports them.

## Unowned Cleanup

Deleting files without establishing ownership.

## Silent Partial Install

Leaving an incomplete installation without reporting it.

## Arbitrary Execution

Executing downloaded or untrusted content during installation.

## Path Traversal

Allowing skill paths to escape the installation root.

## Configuration Destruction

Replacing an entire configuration file for a small integration change.

---

# 70. Final Adapter Model

The adapter architecture is:

```text
                    THE-BUILDER
                         │
              ┌──────────┴──────────┐
              │                     │
       Canonical Skills        Core Contracts
              │                     │
              └──────────┬──────────┘
                         │
                    Adapter Layer
                         │
       ┌─────────┬───────┼────────┬─────────┐
       ↓         ↓       ↓        ↓         ↓
   OpenCode   Claude   Gemini   Cursor    Generic
```

The canonical system remains stable.

Adapters translate it into the conventions and capabilities of individual agents.

---

# 71. Final Principle

The adapter layer exists to solve:

> "How does this agent consume The-Builder?"

It must not change:

> "How should The-Builder work?"

That distinction keeps the project portable, maintainable, and independent of any single AI coding agent.
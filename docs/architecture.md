# Nexra Architecture

## 1. Overview

Nexra is a portable skill system for AI coding agents.

Its architecture separates:

```text
WHAT THE AGENT SHOULD DO
        ↓
CANONICAL SKILLS
        ↓
HOW THE AGENT HOSTS THEM
        ↓
ADAPTERS
        ↓
WHAT THE AGENT CAN ACCESS
        ↓
TOOLS / PLUGINS / MCP / CONNECTORS
```

The central design goal is to avoid coupling the methodology of a skill to a particular AI coding agent.

The same skill should be usable across multiple agent environments whenever the target environment can provide the required capabilities.

---

# 2. Architectural Model

The repository is organized into several conceptual layers:

```text
Nexra/
│
├── skills/              Canonical installable skills
│
├── core/                Shared orchestration contracts
│
├── adapters/            Agent-specific integration
│
├── integrations/        Tool/plugin/connector contracts
│
├── docs/                Architecture and specifications
│
├── tests/               Behavioral and contract tests
│
└── scripts/             Repository validation and test tooling
```

Each layer has a distinct responsibility.

---

# 3. Canonical Skills

The `skills/` directory is the source of truth for installable skills.

Structure:

```text
skills/
├── project-discovery/
│   └── SKILL.md
├── capability-assessment/
│   └── SKILL.md
├── interaction/
│   └── SKILL.md
├── challenge/
│   └── SKILL.md
├── execution/
│   └── SKILL.md
├── verification/
│   └── SKILL.md
├── reporting/
│   └── SKILL.md
└── ...
```

A canonical skill contains methodology.

It should not contain agent-specific installation instructions.

---

# 4. Foundation Skills

Foundation skills define behavior that applies across many tasks.

Current foundation skills include:

```text
project-discovery
capability-assessment
interaction
challenge
execution
verification
reporting
```

Their responsibilities are:

```text
Project Discovery
→ understand the project

Capability Assessment
→ determine what can reliably be done

Interaction
→ determine what must be asked

Challenge
→ identify substantive problems in requirements

Execution
→ perform bounded implementation

Verification
→ determine whether the result actually works

Reporting
→ communicate the result and limitations
```

These skills form the behavioral foundation of Nexra.

---

# 5. Domain Skills

Domain skills provide specialized methodology.

Examples:

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

They should focus on domain-specific reasoning.

They should rely on foundation behavior rather than duplicating it unnecessarily.

---

# 6. Skill Execution Model

A typical task follows:

```text
USER REQUEST
     ↓
DISCOVERY
     ↓
CAPABILITY ASSESSMENT
     ↓
INTENT UNDERSTANDING
     ↓
CHALLENGE IF NECESSARY
     ↓
ASK NECESSARY QUESTIONS
     ↓
PLAN
     ↓
EXECUTE
     ↓
VERIFY
     ↓
REPORT
     ↓
ITERATE
```

This is a behavioral model, not a rigid command sequence.

A trivial task may collapse to:

```text
inspect
→ change
→ verify
```

A complex task may require every stage.

---

# 7. Discover Before Asking

The architecture deliberately separates discovery from interaction.

The agent should first inspect what it can discover.

For example:

```text
User:
"Change the homepage button."

Agent:
inspect project
→ identify framework
→ locate homepage
→ locate button
→ inspect existing styles
```

Only then should it ask a question if something genuinely remains unresolved.

This prevents unnecessary user interrogation.

---

# 8. Capability Awareness

The architecture recognizes that a model's capabilities are not the same thing as an agent's capabilities.

Capability assessment considers:

```text
MODEL
AGENT
TOOLS
ENVIRONMENT
PROJECT
```

For example:

```text
Model:
Can reason about code.

Agent:
Can modify files.

Tool:
Browser inspection unavailable.

Environment:
Node.js available.

Project:
React application.
```

The resulting workflow should reflect these constraints.

---

# 9. Capability States

Capabilities are represented conceptually as:

```text
FULL
SUITABLE
CONSTRAINED
UNSUITABLE
```

The states communicate whether a capability can be relied upon.

Example:

```text
Browser access:
CONSTRAINED

Source inspection:
FULL

Visual verification:
UNSUITABLE
```

The agent must not claim visual verification in the last case.

---

# 10. Interaction Layer

Interaction is responsible for deciding when user input is necessary.

The basic rule is:

```text
discover first
→ identify unknowns
→ determine whether they matter
→ ask only necessary questions
```

Questions should be:

- high-value;
- specific;
- actionable;
- minimal.

---

# 11. User Authority

The architecture intentionally separates:

```text
agent expertise
```

from:

```text
user authority
```

The agent may identify a technical problem.

The user may still choose between valid alternatives.

For example:

```text
Agent:
"This animation approach adds a large dependency."

User:
"I accept the dependency."

Agent:
Proceed with the chosen approach.
```

The agent should not repeatedly challenge a decision that has already been understood and accepted.

---

# 12. Challenge Layer

Challenge is not disagreement for its own sake.

It exists to catch substantive problems.

Examples:

```text
security vulnerability
performance regression
accessibility problem
architectural contradiction
unnecessary complexity
unrealistic technical requirement
```

The pattern is:

```text
problem
↓
evidence
↓
impact
↓
alternative
↓
user decision
```

---

# 13. Execution Layer

Execution translates the agreed plan into changes.

Execution should:

- preserve existing conventions;
- minimize unrelated changes;
- work incrementally;
- validate risky changes;
- keep changes understandable.

Execution should not silently redesign the project.

---

# 14. Verification Layer

Verification determines whether the implementation satisfies its requirements.

Verification may involve:

```text
tests
lint
type checks
build
runtime checks
browser checks
visual inspection
performance measurement
security testing
```

The appropriate method depends on the task.

---

# 15. Verification Is Not a Single Check

Different claims require different evidence.

For example:

```text
Build succeeds
```

does not prove:

```text
UI is visually correct
```

Likewise:

```text
Unit tests pass
```

does not necessarily prove:

```text
production deployment works
```

The verification layer therefore records what was actually checked.

---

# 16. Reporting Layer

Reporting converts implementation and verification results into a useful summary.

A typical result contains:

```text
changed
checks_run
decisions
unverified
remaining_work
```

For review workflows, reporting may instead contain:

```text
findings
severity
evidence
impact
recommendations
limitations
```

---

# 17. Core Contracts

The `core/` directory contains supporting contracts rather than the canonical installable skill definitions.

Example:

```text
core/
├── execution/
│   └── EXECUTION-CONTRACT.md
├── orchestration/
│   └── PIPELINE.md
├── reporting/
│   └── REPORTING-CONTRACT.md
├── specification/
│   └── BEHAVIOR.md
└── verification/
    └── VERIFICATION-CONTRACT.md
```

These documents define interfaces and shared behavioral expectations.

They should not become duplicate copies of the canonical skills.

---

# 18. Orchestration

The orchestration layer coordinates the major stages.

Conceptually:

```text
request
↓
discovery
↓
capability assessment
↓
interaction
↓
challenge
↓
execution
↓
verification
↓
reporting
```

Orchestration should remain adaptive.

A stage can be reduced or skipped when it has no meaningful work to perform.

---

# 19. Why Orchestration Is Separate

A skill explains:

```text
how to perform a capability
```

Orchestration explains:

```text
when capabilities participate in a task
```

This separation prevents every skill from having to implement its own complete lifecycle.

---

# 20. Adapters

The `adapters/` directory contains agent-specific integration definitions.

Current targets include:

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

An adapter describes how canonical skills map into a particular agent environment.

---

# 21. Adapter Responsibilities

An adapter may define:

- skill installation path;
- configuration conventions;
- invocation conventions;
- supported capabilities;
- compatibility information.

Example:

```text
Canonical:
skills/ui-ux-design/SKILL.md

Claude Code:
.claude/skills/ui-ux-design/SKILL.md
```

The adapter performs the mapping.

---

# 22. Adapter Non-Responsibilities

An adapter should not:

- redefine the skill methodology;
- silently modify skill behavior;
- replace canonical requirements;
- invent capabilities;
- become the primary source of skill content.

If an agent has a unique capability, the adapter may describe that capability.

---

# 23. Generic Adapter

The generic adapter provides a fallback for environments without a specialized integration.

Its purpose is portability.

It should avoid assumptions about:

- vendor;
- model;
- IDE;
- operating system.

The generic representation should remain understandable by a human or compatible coding agent.

---

# 24. Integrations

The `integrations/` directory describes external capabilities.

It contains:

```text
integrations/
├── connectors/
├── plugins/
└── registry.yaml
```

These are capability contracts, not skill methodology.

---

# 25. Plugins

Plugins represent reusable capability integrations.

Examples:

```text
browser
container
database
filesystem
git
github
http
image
mcp
package-manager
shell
test-runner
```

A plugin may expose actions or resources useful to skills.

---

# 26. Connectors

Connectors describe access to particular external systems.

Examples:

```text
browser-session
git-repository
github-api
http-client
local-filesystem
mcp-server
npm-registry
postgresql
shell-runtime
```

A connector represents an integration boundary.

---

# 27. Skills vs Plugins vs Connectors

These concepts should not be conflated.

| Component | Purpose |
|---|---|
| Skill | Methodology |
| Plugin | Capability integration |
| Connector | External system access |
| Adapter | Agent-specific mapping |
| Core contract | Shared interface/behavior |
| Test | Behavioral validation |

Example:

```text
SEO skill
+
browser plugin
+
browser-session connector
+
Claude Code adapter
```

Together these can provide a complete workflow.

---

# 28. MCP

MCP is treated as a capability mechanism rather than a methodology layer.

An MCP server may expose:

```text
tools
resources
actions
```

A skill can require or benefit from MCP capabilities.

However:

```text
skill ≠ MCP server
```

The skill defines how to use a capability.

MCP provides the capability.

---

# 29. Registry

The skill registry provides machine-readable information about available skills.

Conceptually:

```yaml
skills:
  - name: ui-ux-design
    path: skills/ui-ux-design/SKILL.md
```

The registry should remain consistent with the filesystem.

It should not become a second source of truth for the actual skill content.

---

# 30. Installation Model

The package provides an installation mechanism that can copy canonical skills into supported agent locations.

Conceptually:

```text
npm package
      ↓
installer
      ↓
detect target agents
      ↓
resolve adapter
      ↓
copy canonical skills
      ↓
write manifest
      ↓
verify installation
```

The installer should not blindly overwrite unrelated host configuration.

---

# 31. Project Installation

For project-scoped installation:

```text
project/
├── .claude/
├── .opencode/
├── .gemini/
├── .agents/
└── .nexra/
```

Only the directories appropriate to detected or explicitly selected targets should be used.

---

# 32. Installation Manifest

The `.nexra/manifest.json` file records installation state.

It can describe:

- Nexra version;
- installed skills;
- adapters;
- target environments;
- installation scope.

The manifest exists so installation can be inspected and diagnosed later.

---

# 33. Host Configuration Safety

The installer should avoid guessing undocumented configuration formats.

It should prefer:

```text
documented native skill directory
```

over:

```text
invented host configuration
```

If an environment cannot be safely configured automatically, the installer should use a documented fallback or report the limitation.

---

# 34. Portability

Portability is achieved through:

```text
canonical skills
+
adapter mappings
+
capability contracts
```

The methodology should remain independent of:

```text
model vendor
IDE
CLI implementation
operating system
specific MCP provider
```

where practical.

---

# 35. Graceful Degradation

The architecture assumes that environments differ.

Example:

```text
Agent A:
filesystem + shell + browser

Agent B:
filesystem + shell

Agent C:
filesystem only
```

The same skill should adapt to these environments when possible.

Example:

```text
browser available
→ inspect rendered UI

browser unavailable
→ inspect source/configuration

visual verification impossible
→ explicitly report it as unverified
```

---

# 36. No False Capability

The system must never infer:

```text
"the skill needs a browser"
```

and then pretend that a browser exists.

Likewise, the agent must not claim:

```text
"I visually verified this."
```

unless visual verification actually occurred.

Capability honesty is an architectural requirement.

---

# 37. Testing Architecture

Tests are primarily behavioral.

The system should test whether the expected behavior occurs rather than requiring exact natural-language output.

Example:

```text
Expected:
Agent discovers framework before asking the user.

Not required:
Agent uses a specific sentence to ask the question.
```

---

# 38. Test Layers

The repository can validate several layers:

```text
repository validation
↓
skill contracts
↓
core contracts
↓
adapter contracts
↓
installer behavior
↓
behavioral cases
```

---

# 39. Repository Validation

Repository validation should detect structural problems such as:

- missing required files;
- invalid metadata;
- inconsistent registries;
- invalid adapter definitions;
- malformed integration contracts.

It is not a substitute for behavioral testing.

---

# 40. Behavioral Tests

Behavioral cases should test situations such as:

```text
simple request
complex request
missing capability
discoverable information
necessary unknown
contradictory requirement
technical tradeoff
user preference
verification limitation
```

The expected behavior should be described clearly.

---

# 41. Skill Quality

A skill should be evaluated for:

```text
clarity
specificity
substantive methodology
portability
testability
capability awareness
verification
```

A long skill is not automatically a good skill.

A short skill is not automatically a bad skill.

The question is whether the skill provides enough operational guidance to produce reliable behavior.

---

# 42. Dependency Direction

The conceptual dependency direction is:

```text
User
 ↓
Orchestration
 ↓
Foundation / Domain Skills
 ↓
Capabilities
 ↓
Tools / Integrations
```

Adapters provide the host-specific mapping around this system.

Canonical skills should not depend on a specific adapter.

---

# 43. Avoiding Circular Responsibilities

Examples of bad architecture:

```text
Skill A requires Skill B
Skill B requires Skill A
```

without a clear reason.

Likewise:

```text
adapter defines skill methodology
skill defines adapter installation
```

should be avoided.

Responsibilities should remain separated.

---

# 44. Change Management

When changing a skill:

```text
edit canonical skill
↓
update affected tests
↓
update documentation if behavior changed
↓
run validation
↓
run behavioral tests
↓
inspect diff
```

Do not modify generated installation copies as the primary source.

---

# 45. Source of Truth

The hierarchy is:

```text
skills/<name>/SKILL.md
        ↓
canonical skill content

adapters/<agent>/
        ↓
agent integration

integrations/
        ↓
capability integration

tests/
        ↓
behavioral expectations
```

Generated or installed copies should not become independent sources of truth.

---

# 46. Repository Evolution

The architecture is intentionally extensible.

New skills can be added without changing the fundamental architecture.

New agents can be supported by adding adapters.

New capabilities can be represented through plugins and connectors.

New behavioral requirements can be added to the core contracts and specification.

---

# 47. Example End-to-End Flow

User request:

```text
"Redesign my homepage with a cinematic 3D scroll experience."
```

The system should conceptually perform:

```text
1. Project Discovery
   ↓
   Identify framework, existing homepage, dependencies,
   rendering stack, assets, routing, and conventions.

2. Capability Assessment
   ↓
   Determine whether browser, image inspection, 3D tooling,
   filesystem, shell, and relevant runtime capabilities exist.

3. Interaction
   ↓
   Determine whether target audience, visual direction,
   or other important decisions remain unknown.

4. Challenge
   ↓
   Identify substantive concerns such as mobile performance,
   accessibility, or excessive dependency cost.

5. Domain Skills
   ↓
   ui-ux-design
   +
   3d-web-design
   +
   scroll-world-flyby

6. Execution
   ↓
   Implement incrementally.

7. Verification
   ↓
   Build, test, inspect runtime behavior,
   and visually inspect when possible.

8. Reporting
   ↓
   Summarize changes, verification, limitations,
   and remaining work.
```

The exact stages can be reduced when unnecessary.

---

# 48. Example Simple Flow

User request:

```text
"Fix the typo in the homepage heading."
```

The architecture should not force:

```text
full capability audit
full design review
full security review
long questionnaire
```

Instead:

```text
discover homepage
↓
locate heading
↓
fix typo
↓
verify
↓
report
```

The architecture is designed to scale its process to the complexity of the task.

---

# 49. Architectural Invariants

The following principles should remain stable:

```text
Canonical skills remain portable.

Adapters remain host-specific.

Tools provide capabilities rather than methodology.

Discovery precedes unnecessary questions.

User decisions remain under user control.

Substantive problems may be challenged.

Verification is explicit.

Unverified claims are disclosed.

Installed copies are not canonical sources.

Behavior matters more than exact wording.
```

---

# 50. Completion Criteria

The architecture is functioning correctly when:

- [ ] canonical skills are stored under `skills/`;
- [ ] foundation skills define shared behavior;
- [ ] domain skills provide specialized methodology;
- [ ] adapters remain separate from canonical methodology;
- [ ] integrations remain separate from skills;
- [ ] capability limitations can be represented;
- [ ] orchestration is adaptive;
- [ ] verification is explicit;
- [ ] user authority is preserved;
- [ ] behavioral tests evaluate actual behavior;
- [ ] the installer can map canonical skills to supported targets;
- [ ] generated installations do not become sources of truth;
- [ ] provider-specific assumptions do not leak into canonical skills.

---

# 51. Architectural Principle

Nexra should be understood as:

```text
A portable methodology layer
for AI coding agents
```

rather than:

```text
A collection of prompts
```

The core architectural separation is:

```text
METHOD
    ↓
SKILLS
    ↓
ORCHESTRATION
    ↓
ADAPTERS
    ↓
CAPABILITIES
    ↓
TOOLS / INTEGRATIONS
```

This separation allows the same reasoning methodology to survive changes in:

- models;
- coding agents;
- IDEs;
- tool providers;
- MCP servers;
- project environments.

That portability is a fundamental property of Nexra.
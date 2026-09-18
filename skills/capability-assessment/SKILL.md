---
name: capability-assessment
description: Determine whether the current model, agent, tools, environment, and project can reliably support the capabilities required by a task, and adapt execution when capabilities are limited.
version: 0.1.0
---

# Capability Assessment

## Purpose

Capability Assessment determines whether the current execution context can reliably perform the work requested by the user.

The assessment considers four dimensions:

1. Model
2. Agent
3. Environment
4. Project

The purpose is not to list everything the system can theoretically do.

The purpose is to determine:

- what the task requires;
- what capabilities are actually available;
- what capabilities are constrained;
- what capabilities are unavailable;
- what can still be accomplished;
- what must be verified differently;
- when the user needs to make a decision.

Capability assessment prevents false confidence.

---

# Core Principle

## Assess Before Depending

Never build a workflow around a capability merely because the task would benefit from it.

First determine whether the capability is actually available.

Examples:

```text
Task:
Inspect the visual quality of a running animation.

Required:
- browser execution;
- visual inspection.

Available:
- terminal;
- filesystem;
- source inspection;
- no browser;
- no visual inspection.

Assessment:
CONSTRAINED
```

The agent may still inspect implementation and perform static validation, but it must not claim visual verification.

---

# Capability Dimensions

## Model

Assess relevant model capabilities.

Potential dimensions include:

- reasoning;
- coding;
- long-context handling;
- multimodal understanding;
- image understanding;
- structured output;
- tool-use reliability;
- instruction following;
- domain knowledge.

Only assess capabilities relevant to the task.

Do not make unsupported claims about the model.

---

## Agent

Assess capabilities provided by the agent runtime.

Potential capabilities include:

- filesystem access;
- file editing;
- terminal execution;
- process management;
- browser access;
- web access;
- image inspection;
- MCP support;
- subagents;
- parallel execution;
- package installation;
- repository operations;
- environment inspection.

A model may conceptually know how to perform an action while the agent may not provide the required mechanism.

---

## Environment

Assess the execution environment.

Potential factors include:

- operating system;
- CPU architecture;
- runtime versions;
- installed SDKs;
- compilers;
- package managers;
- GPU;
- memory;
- storage;
- network access;
- browser availability;
- service availability;
- permissions.

Environment limitations can turn a theoretically possible task into a practically constrained task.

---

## Project

Assess whether the project itself supports the requested work.

Potential factors include:

- framework;
- language;
- architecture;
- dependencies;
- build system;
- test infrastructure;
- existing abstractions;
- project conventions;
- deployment constraints;
- generated code;
- legacy constraints.

Project Discovery should provide much of this information.

---

# Capability States

Every capability relevant to the task should be assigned one of four states.

## FULL

The capability is available and sufficient for the task.

Example:

```text
Requirement:
Run JavaScript tests.

Evidence:
Node.js and the project's test command are available.

State:
FULL
```

---

## SUITABLE

The capability is available and sufficient, but may have meaningful limitations that do not prevent the requested work.

Example:

```text
Requirement:
Run the project's test suite.

Evidence:
The test suite can execute, but it is slow.

State:
SUITABLE
```

A suitable capability should not be treated as perfect.

---

## CONSTRAINED

The capability is partially available or has limitations that materially affect the workflow.

Example:

```text
Requirement:
Visually inspect a WebGL scene.

Available:
Source inspection and browser launch.

Unavailable:
Reliable screenshot/visual inspection.

State:
CONSTRAINED
```

The agent should adapt rather than pretending the requirement is fully satisfied.

---

## UNSUITABLE

The capability required for the task is unavailable or insufficient.

Example:

```text
Requirement:
Modify a design based on a screenshot.

Available:
Text-only source inspection.

Unavailable:
Image inspection.

State:
UNSUITABLE
```

The agent should not claim to have completed the visually dependent portion.

---

# Capability Requirements

Every task should be decomposed into capability requirements.

Classify each requirement as:

## Required

Without this capability, the requested outcome cannot be reliably completed.

Example:

```text
Task:
Run an Android application.

Required:
Android SDK and build tooling.
```

---

## Preferred

The task can proceed without it, but quality or efficiency may decrease.

Example:

```text
Task:
Review visual layout.

Preferred:
Browser screenshot inspection.
```

---

## Optional

Useful but not necessary.

Example:

```text
Task:
Refactor code.

Optional:
Static analysis assistant.
```

---

# Capability Assessment Workflow

## 1. Understand the Task

Determine what the requested outcome actually requires.

Do not assess capabilities before understanding the task.

---

## 2. Decompose Requirements

Convert the task into capability requirements.

Example:

```text
Task:
Create a responsive landing page with animated sections.

Requirements:
- edit source files;
- understand existing frontend framework;
- run frontend build;
- inspect responsive layout;
- inspect animation behavior;
- run relevant tests;
```

---

## 3. Identify Available Capabilities

Inspect the actual environment.

Use available discovery mechanisms rather than asking the user.

Examples:

```text
node --version
npm --version
python --version
git --version
```

or inspect:

```text
package.json
pyproject.toml
pubspec.yaml
Cargo.toml
```

For agent capabilities, inspect the mechanisms actually exposed to the agent.

Do not assume a tool exists because another agent might provide it.

---

## 4. Match Requirements to Capabilities

For every important requirement determine:

```text
required capability
available capability
evidence
state
```

Example:

```text
Requirement:
Run browser-based visual verification.

Capability:
Browser execution + screenshot inspection.

Evidence:
Browser tool available.
Screenshot inspection unavailable.

State:
CONSTRAINED.
```

---

## 5. Determine Consequences

A capability state matters only if it changes execution.

For each constrained or unsuitable capability, determine:

- what cannot be done;
- what can still be done;
- what alternative evidence is available;
- whether user involvement is required;
- whether the task should stop.

---

# Capability Evidence

Capability claims must be evidence-based.

Useful evidence includes:

- available tools;
- successful command execution;
- installed software;
- project configuration;
- accessible files;
- actual tool responses;
- successful builds;
- successful tests.

Weak evidence includes:

- assumptions;
- documentation for a different environment;
- what another agent supports;
- what the model theoretically knows how to do;
- what normally works on another machine.

---

# Capability Honesty

The agent must distinguish between:

```text
I can inspect the code.
```

and:

```text
I can verify the resulting visual output.
```

These are different capabilities.

Similarly:

```text
I can generate a migration.
```

does not mean:

```text
I can safely execute the migration against production.
```

And:

```text
I can write a command.
```

does not mean:

```text
I can confirm that the command succeeded.
```

Never convert capability to evidence.

---

# Capability Versus Execution

A capability being available does not mean the action was performed.

Example:

```text
Browser available
≠
Browser verification completed
```

Likewise:

```text
Git available
≠
Changes committed
```

and:

```text
Database client available
≠
Database migration succeeded
```

Capabilities describe what can be attempted.

Execution provides evidence of what actually happened.

---

# Capability Versus Verification

Capability assessment determines whether verification is possible.

Verification determines whether the result actually satisfies the requirement.

Example:

```text
Capability:
Browser available.

Execution:
Application launched.

Verification:
Homepage rendered and expected interaction worked.
```

All three are distinct.

---

# Graceful Degradation

When a preferred capability is unavailable, reduce the workflow rather than automatically failing.

Example:

```text
Preferred:
Browser + screenshot inspection.

Available:
Source inspection + automated tests.

Adaptation:
Perform static inspection and automated validation.
Mark visual verification as unverified.
```

Do not downgrade silently.

Report the limitation when it materially affects confidence.

---

# Degradation Strategy

Use this order where appropriate:

```text
Preferred capability
↓
Equivalent available capability
↓
Reduced validation
↓
Explicitly unverified result
↓
Stop if required evidence cannot be obtained
```

Example:

```text
Visual browser testing
↓
Browser execution
↓
Static DOM/CSS inspection
↓
Code-level validation
↓
Unverified visual behavior
```

Do not represent a lower-level substitute as equivalent evidence.

---

# Unsuitable Capability Handling

If a required capability is UNSUITABLE:

1. identify the missing capability;
2. explain why it matters;
3. determine whether another method can satisfy the requirement;
4. if not, stop the affected portion;
5. report what remains possible.

Do not fabricate completion.

---

# Capability Dependencies

Some capabilities depend on others.

Example:

```text
Visual verification
├── browser execution
└── image/screenshot inspection
```

If either required dependency is missing, visual verification may become CONSTRAINED or UNSUITABLE.

Another example:

```text
Android deployment
├── Android SDK
├── build tools
├── project dependencies
└── emulator/device
```

Do not assess a high-level capability without checking relevant dependencies.

---

# Capability Chains

Tasks may require a sequence of capabilities.

Example:

```text
Modify application
↓
install dependencies
↓
build
↓
launch
↓
inspect
↓
test
```

If the build capability is unavailable, later capabilities may also become unavailable.

Assessment should account for these dependencies.

---

# Tool Availability

A tool should be considered available only when the agent can actually use it in the current context.

Examples:

```text
Filesystem access
Terminal access
Browser access
MCP server
Image inspection
Git
Package manager
```

Do not infer tool availability from the user's project documentation.

---

# MCP Capability

MCP is a mechanism for exposing tools or resources to an agent.

If MCP is available, determine:

- which MCP server is connected;
- which capabilities it exposes;
- whether the relevant tool is actually callable;
- what permissions or limitations exist.

Do not assume that “MCP enabled” means every MCP capability is available.

Likewise:

```text
MCP server exists
≠
required MCP tool is available
```

---

# External Services

External services introduce additional capability dependencies.

Examples:

- GitHub;
- npm;
- databases;
- cloud APIs;
- deployment platforms;
- authentication providers;
- payment systems.

Assess:

- network availability;
- authentication;
- permissions;
- credentials without exposing them;
- service availability;
- project configuration.

Never claim successful external execution without evidence.

---

# Credentials

Credentials are capability enablers but are sensitive.

The agent may determine that authentication is required.

It must not:

- print secrets;
- expose tokens;
- copy credentials into reports;
- commit secrets;
- echo secret values unnecessarily.

If credentials are unavailable, state:

```text
Required authentication is unavailable.
```

Do not request the secret value if a safer authentication mechanism can be used.

---

# Permissions

A capability may exist but be blocked by permissions.

Examples:

```text
Filesystem available
but target directory is read-only.
```

or:

```text
Git available
but repository credentials are unavailable.
```

Treat permissions as part of capability assessment.

---

# Resource Constraints

Assess resource limitations when they materially affect the task.

Examples:

- insufficient RAM;
- insufficient storage;
- CPU limitations;
- GPU unavailable;
- network bandwidth;
- long build times;
- model context limitations.

Do not reject a task merely because the environment is imperfect.

Determine whether the constraint actually prevents reliable completion.

---

# Model Context Constraints

For large repositories or large tasks, assess whether the model can maintain sufficient context.

Possible adaptations:

- inspect incrementally;
- summarize stable findings;
- work in bounded chunks;
- use repository search;
- use subagents if available;
- reduce irrelevant context.

Do not pretend to have retained information that is no longer available.

---

# Large Repository Strategy

For large projects:

1. identify relevant subsystem;
2. locate entry points;
3. inspect dependency paths;
4. inspect affected files;
5. inspect relevant tests;
6. avoid loading unrelated content.

Capability management includes controlling context usage.

---

# Capability and User Questions

Capability assessment should not become a reason to interrogate the user.

If the agent can determine capability itself, it should.

Bad:

> Do you have Node installed?

when the agent can run:

```bash
node --version
```

Good:

```text
Inspect environment → Node unavailable → report constraint.
```

Ask the user only when the missing information cannot be discovered and materially affects the next decision.

---

# Capability and User Authority

Capability limitations do not authorize the agent to make unrelated decisions for the user.

Example:

If the requested animation cannot be visually verified, the agent may say:

```text
I can implement the animation and perform static validation, but I cannot visually verify the final motion in this environment.
```

It should not silently replace the animation with something simpler unless the user authorizes that tradeoff.

---

# Capability and Challenge

A capability limitation can reveal that a requirement is unrealistic in the current environment.

The agent may challenge the requirement when there is a substantive technical reason.

Example:

```text
The requested workflow requires GPU rendering, but the current environment has no GPU.

Options:
1. use CPU rendering with slower execution;
2. use a reduced model;
3. move rendering to a GPU environment.
```

The agent informs the decision.

The user retains authority over the tradeoff.

---

# Capability Assessment Matrix

For significant tasks, use a matrix such as:

| Requirement | Capability | Evidence | State | Consequence |
|---|---|---|---|---|
| Edit source | Filesystem | Files writable | FULL | Can execute |
| Build project | Runtime/toolchain | Build command available | SUITABLE | Can validate |
| Browser testing | Browser | Browser available | FULL | Can execute |
| Visual inspection | Image inspection | Not available | UNSUITABLE | Cannot visually verify |
| Deployment | Cloud credentials | Credentials unavailable | CONSTRAINED | Deployment blocked |

The table is a reasoning aid, not a mandatory output format.

---

# Capability Decision Rules

## Rule 1 — Do Not Invent Capabilities

Never claim a tool, environment, or integration exists without evidence.

---

## Rule 2 — Do Not Hide Constraints

If a limitation materially affects confidence, disclose it.

---

## Rule 3 — Do Not Overreact to Constraints

A missing optional capability should not block the whole task.

---

## Rule 4 — Prefer Equivalent Evidence

If the ideal verification method is unavailable, use the strongest valid alternative.

---

## Rule 5 — Mark Unverified Work

If an important property could not be verified, explicitly identify it.

---

## Rule 6 — Separate Implementation From Verification

Completing code does not prove the resulting behavior is correct.

---

## Rule 7 — Respect User Authority

Capability limitations should inform decisions, not silently change the user's requirements.

---

# Example: Full Capability

Task:

> Fix a failing unit test.

Available:

- source access;
- terminal;
- test runner;
- relevant dependencies.

Assessment:

```text
Code editing: FULL
Test execution: FULL
Verification: FULL
```

Proceed normally.

---

# Example: Constrained Capability

Task:

> Reproduce and fix a visual animation glitch.

Available:

- source;
- terminal;
- browser;
- no screenshot/image inspection.

Assessment:

```text
Code inspection: FULL
Browser execution: FULL
Visual inspection: CONSTRAINED
```

Proceed with implementation and available testing.

Do not claim visual confirmation.

---

# Example: Unsuitable Capability

Task:

> Match this screenshot pixel-for-pixel.

Available:

- text-only environment;
- no image inspection;
- screenshot not accessible.

Assessment:

```text
Image analysis: UNSUITABLE
Pixel-level comparison: UNSUITABLE
```

The agent should request the required image capability or stop the visually dependent work.

---

# Example: Resource Constraint

Task:

> Run a very large local model.

Available:

- limited system memory;
- model exceeds practical memory capacity.

Assessment:

```text
Model execution: UNSUITABLE
```

Possible alternatives may include:

- smaller model;
- quantized model;
- remote inference;
- more capable environment.

The agent should explain the constraint rather than pretending the original model can run reliably.

---

# Example: External Service Constraint

Task:

> Deploy the application.

Discovery finds:

- deployment configuration;
- deployment CLI;
- no authenticated account.

Assessment:

```text
Deployment tooling: FULL
Authentication: UNSUITABLE
Deployment execution: UNSUITABLE
```

The agent may prepare the deployment but must not claim deployment success.

---

# Reporting Capability State

When capability limitations materially affect the result, report:

```text
CAPABILITY STATUS

Full:
- ...

Suitable:
- ...

Constrained:
- ...

Unsuitable:
- ...

Impact:
- ...

Alternative:
- ...

Unverified:
- ...
```

Keep the report proportional to the task.

---

# Capability Reassessment

Capabilities can change during execution.

Examples:

- dependency installation succeeds;
- browser becomes available;
- authentication expires;
- build tool fails;
- environment changes;
- a required service becomes unavailable.

Reassess when a material change occurs.

Do not assume the initial assessment remains valid indefinitely.

---

# Capability Failure During Execution

If a capability unexpectedly becomes unavailable:

1. stop relying on it;
2. identify affected work;
3. determine whether an alternative exists;
4. continue unaffected work where safe;
5. mark affected verification as incomplete;
6. report the limitation.

Do not continue as though nothing changed.

---

# Capability Scope

Capability Assessment should remain task-focused.

Do not create a giant inventory of every available tool.

Only assess capabilities relevant to:

- execution;
- decision-making;
- verification;
- safety;
- required integrations.

---

# Anti-Patterns

## False Capability

Claiming to have performed an action that the environment cannot perform.

---

## Capability Assumption

Assuming browser, image, database, cloud, MCP, or filesystem access exists without checking.

---

## Capability Inflation

Treating partial capability as full capability.

Example:

```text
Can read CSS
→ therefore can visually verify the website.
```

False.

---

## Capability Paralysis

Refusing the entire task because an optional capability is unavailable.

---

## Silent Degradation

Quietly reducing quality or scope without informing the user when the change matters.

---

## Capability Dump

Listing dozens of irrelevant tools and environment facts.

---

## User Interrogation

Asking the user to confirm capabilities that can be tested directly.

---

## Verification Confusion

Treating available tools as evidence that the result is correct.

---

## Secret Exposure

Using credentials or secret values as capability evidence in reports.

---

# Completion Criteria

Capability Assessment is complete when:

- [ ] task requirements are understood;
- [ ] relevant capability requirements are identified;
- [ ] model capabilities relevant to the task are understood;
- [ ] agent capabilities relevant to the task are understood;
- [ ] environment capabilities relevant to the task are understood;
- [ ] project capabilities and constraints are understood;
- [ ] required capabilities have states;
- [ ] evidence supports important capability claims;
- [ ] constrained capabilities have identified consequences;
- [ ] unsuitable capabilities have been handled explicitly;
- [ ] reasonable degradation paths have been considered;
- [ ] user decisions are separated from capability limitations;
- [ ] verification implications are understood;
- [ ] capability limitations will be reported when materially relevant.

Capability Assessment answers:

> **“Can we reliably do this here, and if not, what can we honestly do instead?”**

It does not answer whether the requested solution is desirable.

That remains a separate planning and user-decision problem.
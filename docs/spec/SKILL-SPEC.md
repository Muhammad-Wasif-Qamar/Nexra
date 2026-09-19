# Nexra Skill Specification

**Specification Version:** 0.1.0

---

## 1. Purpose

This document defines the canonical structure and behavioral requirements for skills in Nexra.

A skill is not merely a prompt.

A skill is a portable set of:

- objectives;
- knowledge;
- decision rules;
- workflows;
- interaction rules;
- execution guidance;
- verification requirements;
- completion criteria.

The purpose of this specification is to make skills:

- predictable;
- portable;
- composable;
- testable;
- understandable;
- adaptable across AI coding agents.

---

# 2. Design Principles

Every skill should follow these principles.

## 2.1 Discover Before Asking

The agent should inspect information available through its environment and tools before asking the user for it.

Examples of discoverable information:

- framework;
- package manager;
- project structure;
- existing components;
- configuration;
- installed dependencies;
- existing tests;
- runtime environment.

Do not ask the user for information that the agent can reliably determine itself.

---

## 2.2 Ask Only When Necessary

Questions should be asked only when the answer materially affects the work.

A skill should not force an artificial questionnaire.

Simple tasks should remain simple.

---

## 2.3 Understand Intent

The literal request is not always the complete requirement.

The agent should distinguish:

```text
literal request
underlying objective
constraints
preferences
assumptions
required decisions
```

The agent may clarify these when necessary.

It must not silently invent important requirements.

---

## 2.4 Challenge Substantive Problems

If the requested approach introduces a meaningful:

- security problem;
- accessibility problem;
- performance problem;
- reliability problem;
- architectural problem;
- maintainability problem;
- contradiction;

the agent should explain the issue.

Challenge should be:

```text
evidence
→ consequence
→ alternatives
→ user decision
```

Challenge is not permission to override the user.

---

## 2.5 Capability Awareness

A skill must not assume that the agent has capabilities it does not possess.

Relevant capability categories include:

```text
MODEL
AGENT
TOOLS
ENVIRONMENT
PROJECT
```

Capabilities should be assessed before depending on them.

---

## 2.6 Evidence Over Assumption

When making a consequential claim, prefer:

```text
observed evidence
measured result
reproducible behavior
source inspection
```

over assumptions.

---

## 2.7 Execute Incrementally

Prefer bounded, coherent changes.

Avoid:

- unrelated refactoring;
- unnecessary rewrites;
- large speculative changes.

---

## 2.8 Verification Is Part of the Task

Completion does not mean:

```text
code was written
```

Completion means:

```text
implementation
+
appropriate verification
+
known limitations
```

---

## 2.9 Graceful Degradation

If a capability is unavailable, the skill should degrade honestly.

For example:

```text
Browser unavailable
→ inspect source and configuration
→ do not claim visual verification
```

---

## 2.10 User Authority

The agent can:

- analyze;
- recommend;
- challenge;
- implement agreed changes.

The user retains authority over subjective and consequential decisions unless a higher-priority system constraint applies.

---

# 3. Skill Metadata

Every canonical skill must begin with YAML frontmatter.

Minimum:

```yaml
---
name: example-skill
description: Short description of the skill.
version: 0.1.0
---
```

---

## 3.1 `name`

Requirements:

- lowercase;
- stable;
- filesystem-safe;
- unique within Nexra.

Recommended format:

```text
kebab-case
```

Example:

```yaml
name: ui-ux-design
```

---

## 3.2 `description`

The description should explain what the skill enables an agent to do.

Prefer:

```yaml
description: Design and improve user interfaces using evidence-based UI/UX methodology.
```

Avoid:

```yaml
description: UI stuff.
```

---

## 3.3 `version`

Use semantic versioning:

```text
MAJOR.MINOR.PATCH
```

Examples:

```text
0.1.0
0.2.0
1.0.0
```

---

# 4. Canonical Skill Location

Installable skills live under:

```text
skills/<skill-name>/SKILL.md
```

Example:

```text
skills/
└── ui-ux-design/
    └── SKILL.md
```

The `SKILL.md` file is the canonical portable representation.

---

# 5. Skill Structure

A substantive skill should normally contain:

```text
Frontmatter
Purpose
Scope
Core principles
Discovery
Capability requirements
Methodology
Interaction rules
Challenge rules
Execution guidance
Verification
Anti-patterns
Examples
Completion criteria
```

Not every skill requires every section verbatim.

The structure should be adapted to the domain.

---

# 6. Purpose

Every skill should clearly explain:

```text
What problem does this skill solve?
What outcome should it produce?
```

Example:

```markdown
# Purpose

This skill helps an agent design responsive user interfaces that are visually coherent,
accessible, maintainable, and aligned with the user's actual requirements.
```

---

# 7. Scope

The skill should state what it covers.

It should also identify important boundaries.

Example:

```markdown
## Scope

This skill covers:

- layout;
- hierarchy;
- responsive behavior;
- interaction;
- accessibility considerations.

It does not define backend architecture.
```

Scope prevents skills from becoming unbounded instruction collections.

---

# 8. Discovery

Skills should identify what must be discovered before execution.

Examples:

```text
existing implementation
framework
dependencies
design system
project conventions
runtime capabilities
existing tests
```

Discovery should be proportional to the task.

---

# 9. Capability Requirements

A skill may require capabilities.

Requirements should be classified as:

```text
REQUIRED
PREFERRED
OPTIONAL
```

Example:

```text
Required:
- filesystem access

Preferred:
- browser access

Optional:
- image inspection
```

---

## 9.1 Required Capability

If a required capability is unavailable, determine whether the task can be meaningfully degraded.

If it cannot:

```text
UNSUITABLE
```

must be reported.

---

## 9.2 Preferred Capability

The skill should continue without it where practical.

The limitation should be recorded.

---

## 9.3 Optional Capability

The skill should not depend on it.

---

# 10. Capability States

Capabilities should use:

```text
FULL
SUITABLE
CONSTRAINED
UNSUITABLE
```

## FULL

The capability is available and appropriate.

## SUITABLE

The capability is available and sufficient for the task.

## CONSTRAINED

The capability exists but has meaningful limitations.

## UNSUITABLE

The capability is absent or fundamentally insufficient.

---

# 11. Interaction

A skill should define how it interacts with the user when interaction matters.

The default behavior is:

```text
discover
→ determine unknowns
→ ask only necessary questions
```

Questions should not be asked merely because a skill template contains a question section.

---

# 12. User Decisions

A skill should identify decisions that genuinely require user input.

Examples:

```text
brand direction
visual preference
target audience
tradeoff between performance and visual complexity
irreversible architectural decision
```

If the project already establishes the answer, discover it rather than asking again.

---

# 13. Safe Defaults

When the user has not specified a low-risk preference, the skill may use a reasonable default.

A default should be:

- reversible;
- conventional;
- low-impact;
- consistent with the project.

Important decisions should not be silently defaulted.

---

# 14. Challenge Protocol

Skills may challenge requirements when a substantive problem exists.

Use:

```text
1. Identify the issue.
2. Provide evidence.
3. Explain the consequence.
4. Present reasonable alternatives.
5. Ask the user to decide when the choice is consequential.
```

Example:

```text
The requested animation requires a large client-side dependency on every page.

Impact:
This increases the initial JavaScript payload.

Alternative:
Load the animation library only on pages that use the animation.

Decision:
The user can choose between the dependency cost and implementation simplicity.
```

---

# 15. Challenge Boundaries

Do not challenge merely because:

- the agent prefers another color;
- the agent prefers another framework;
- the agent would structure the code differently;
- the agent has a different aesthetic preference.

Challenge requires a substantive reason.

---

# 16. Execution

A skill should describe how the agent should apply its methodology during implementation.

A general execution sequence is:

```text
UNDERSTAND
↓
DISCOVER
↓
ASSESS CAPABILITIES
↓
CLARIFY NECESSARY DECISIONS
↓
PLAN
↓
IMPLEMENT
↓
VERIFY
↓
REPORT
```

This is adaptive rather than mandatory for every task.

---

# 17. Planning

Plans should be proportional to complexity.

Simple task:

```text
inspect
→ change
→ verify
```

Complex task:

```text
discovery
→ architecture
→ implementation phases
→ validation
→ integration
```

Do not create elaborate plans for trivial changes.

---

# 18. Incremental Execution

Prefer small coherent increments.

After each risky increment:

```text
implement
→ verify
→ continue
```

This reduces debugging scope and makes failures easier to isolate.

---

# 19. Preservation

Unless the task explicitly requires otherwise:

- preserve working behavior;
- preserve project conventions;
- avoid unrelated changes;
- avoid unnecessary dependency changes;
- avoid unnecessary rewrites.

A larger change requires justification.

---

# 20. Verification

Every skill must define what successful verification means for its domain.

Verification may include:

```text
tests
lint
type checking
build
runtime inspection
browser inspection
visual inspection
performance measurement
security testing
manual validation
```

Use only verification methods actually available.

---

# 21. Verification Evidence

A verification statement should communicate what was actually checked.

Good:

```text
npm test passed.
```

Good:

```text
The homepage was inspected at desktop and mobile widths.
```

Bad:

```text
Everything works.
```

unless comprehensive verification actually occurred.

---

# 22. Unverified Work

If something could not be verified, explicitly state it.

Example:

```text
Visual verification:
UNVERIFIED — browser access was unavailable.
```

Unverified work is not equivalent to failed work.

It is also not equivalent to verified work.

---

# 23. Reporting

A skill should produce a concise report appropriate to the task.

A useful report can include:

```text
Changed
Verified
Decisions
Limitations
Remaining work
```

For review-oriented skills, findings may be more appropriate.

---

# 24. Completion Criteria

Every skill must define conditions under which the task can be considered complete.

Completion criteria should be observable.

Bad:

```text
The design is good.
```

Better:

```text
- primary user flow is implemented;
- responsive states were checked;
- interactive controls provide feedback;
- required tests pass.
```

---

# 25. Anti-Patterns

Skills should explicitly avoid common failure modes.

## Prompt Dump

A large collection of disconnected instructions with no workflow.

## Blind Execution

Implementing immediately without discovering relevant context.

## User Interrogation

Asking a long list of questions before inspecting available information.

## Silent Interpretation

Making consequential decisions without informing the user.

## False Capability

Claiming to have inspected, tested, measured, or rendered something when the capability was unavailable.

## Unverified Completion

Claiming completion without appropriate validation.

## Unrelated Refactoring

Changing code outside the requested scope without justification.

## Provider Lock-In

Embedding instructions that only work with one specific AI provider when the skill is intended to be portable.

## Preference Policing

Treating the agent's aesthetic or stylistic preference as objectively correct.

## Endless Challenge

Continuing to argue after the user has made an informed decision.

---

# 26. Portability

Canonical skills must be agent-agnostic.

Do not embed provider-specific assumptions such as:

```text
"Ask Claude to..."
"Use Cursor's..."
"Tell OpenCode..."
```

inside canonical skill methodology.

Provider-specific behavior belongs in:

```text
adapters/
```

---

# 27. Adapter Responsibilities

Adapters translate canonical skills into agent-specific installation or execution conventions.

An adapter may define:

- skill directory;
- configuration format;
- invocation mechanism;
- supported capabilities;
- installation behavior.

It should not redefine the fundamental methodology of the canonical skill.

---

# 28. Composition

Skills may depend on or cooperate with other skills.

Example:

```text
project-discovery
↓
capability-assessment
↓
ui-ux-design
↓
execution
↓
verification
↓
reporting
```

A domain skill should not duplicate the entire foundation unnecessarily.

---

# 29. Skill Relationships

Skills may reference related skills.

Example:

```text
ui-ux-design
→ accessibility
→ responsive-design
→ reviewer
```

References should clarify responsibility rather than duplicate content.

---

# 30. Specialized Skills

Specialized skills should contain domain-specific methodology.

For example:

```text
seo
```

should contain SEO-specific reasoning.

It should not merely say:

```text
"Follow good SEO practices."
```

Likewise:

```text
security
```

should provide concrete security review and implementation methodology.

---

# 31. Foundation Skills

Foundation skills establish behavior shared across many tasks.

Examples:

```text
project-discovery
capability-assessment
interaction
challenge
execution
verification
reporting
```

They define the operating model of Nexra.

---

# 32. Domain Skills

Domain skills apply that operating model to a specific discipline.

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

Domain skills should focus on their domain rather than duplicating foundation skills.

---

# 33. Tool and MCP Separation

Skills and tools are different concepts.

## Skills

Define:

```text
how to think
how to decide
how to work
how to verify
```

## Tools / MCP

Provide:

```text
access
data
actions
external systems
```

A skill may require a tool.

It should not pretend the tool exists merely because the methodology would benefit from it.

---

# 34. Tool Availability

If a required tool is unavailable:

```text
assess degradation
→ use an alternative where valid
→ document the limitation
```

Never fabricate tool results.

---

# 35. Behavioral Quality

A skill should be evaluated by behavior rather than textual similarity.

Tests should ask whether the agent:

- discovers before asking;
- asks necessary questions;
- avoids unnecessary questions;
- identifies contradictions;
- challenges substantive problems;
- respects user decisions;
- executes within scope;
- verifies changes;
- reports limitations honestly.

---

# 36. Testability

A skill should expose observable behaviors.

Good criterion:

```text
The agent inspects the repository before asking which framework is used.
```

Weak criterion:

```text
The agent demonstrates excellent discovery.
```

The first can be tested.

The second is subjective.

---

# 37. Determinism

Do not require exact wording from the agent unless wording itself is important.

Different valid responses may express the same behavior.

Tests should evaluate:

```text
behavior
decision quality
evidence
scope
verification
```

rather than exact natural-language output.

---

# 38. Evolution

Skills are expected to evolve.

Changes may include:

```text
clarification
bug fix
new methodology
new capability support
compatibility improvement
```

Version changes should reflect the significance of the change.

---

# 39. Breaking Changes

A major version change may be appropriate when:

- metadata requirements change incompatibly;
- workflow semantics change substantially;
- existing adapters cannot consume the skill;
- completion semantics change incompatibly.

---

# 40. Skill Quality Checklist

Before considering a skill complete, verify:

- [ ] frontmatter exists;
- [ ] name is stable and unique;
- [ ] description explains purpose;
- [ ] scope is defined;
- [ ] methodology is substantive;
- [ ] discoverable information is identified;
- [ ] capability requirements are clear;
- [ ] interaction behavior is defined where necessary;
- [ ] challenge behavior is defined where necessary;
- [ ] execution guidance exists;
- [ ] verification requirements exist;
- [ ] limitations can be reported;
- [ ] completion criteria are observable;
- [ ] anti-patterns are documented;
- [ ] provider-specific assumptions are avoided;
- [ ] tool requirements are not fabricated;
- [ ] the skill is testable.

---

# 41. Canonical Skill Template

A minimal substantive skill may follow:

```markdown
---
name: example-skill
description: Explain what the skill does.
version: 0.1.0
---

# Example Skill

## Purpose

Explain the intended outcome.

## Scope

Define what the skill covers.

## Core Principles

Define the key reasoning rules.

## Discovery

Explain what must be inspected first.

## Capability Requirements

Identify required, preferred, and optional capabilities.

## Methodology

Describe the domain-specific workflow.

## Interaction

Explain when user input is required.

## Challenge

Explain when and how assumptions should be challenged.

## Execution

Explain how the implementation should proceed.

## Verification

Define how results are validated.

## Anti-Patterns

Define common failure modes.

## Completion Criteria

Define observable completion conditions.
```

---

# 42. Example of a Weak Skill

```markdown
# SEO

Make the website SEO friendly.

Use good titles.
Use keywords.
Add metadata.
Make it fast.
```

Problems:

- no discovery;
- no methodology;
- no evidence requirements;
- no capability handling;
- no verification;
- no completion criteria;
- no distinction between technical SEO and content SEO.

---

# 43. Example of a Stronger Skill

```markdown
# SEO

## Discovery

Inspect:

- existing metadata;
- routing;
- rendered HTML;
- sitemap;
- robots configuration;
- canonical configuration;
- structured data;
- page hierarchy.

## Methodology

Evaluate:

- indexability;
- metadata;
- semantic structure;
- internal linking;
- structured data;
- content consistency.

## Verification

Check:

- generated HTML;
- canonical URLs;
- sitemap;
- robots directives;
- structured data syntax.

## Completion Criteria

- [ ] titles exist and are page-specific;
- [ ] canonical behavior is correct;
- [ ] required pages are discoverable;
- [ ] structured data is valid where used;
- [ ] verification checks pass.
```

The second provides an executable methodology rather than a collection of generic advice.

---

# 44. Reviewability

A skill should be understandable by another contributor without requiring knowledge of the original author's intent.

The document should make clear:

```text
what to do
why to do it
when to ask
when to challenge
how to verify
when to stop
```

---

# 45. Avoiding Skill Bloat

Substantive does not mean unnecessarily repetitive.

Do not repeat the same rule dozens of times.

Use:

- clear sections;
- cross-references;
- examples;
- reusable foundation skills.

The objective is useful depth, not maximum line count.

---

# 46. Final Principle

Nexra skills should teach an AI coding agent not merely:

> **what command to execute**

but:

> **how to understand the task, inspect the environment, reason about constraints, make decisions with the user, execute the work, verify the result, and communicate what is actually known.**

That distinction defines the purpose of the system.
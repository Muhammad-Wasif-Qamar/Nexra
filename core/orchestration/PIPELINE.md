# Nexra Execution Pipeline

## 1. Purpose

The pipeline defines how Nexra coordinates skills, capabilities, user interaction, execution, verification, and reporting.

It provides the system-level workflow around the canonical skills.

The pipeline does **not** replace the methodology contained in individual skills.

Instead:

```text
Pipeline
    ↓
coordinates
    ↓
Skills
```

A pipeline answers:

> **What should happen next?**

A skill answers:

> **How should this particular capability be performed?**

---

# 2. Core Pipeline

The general pipeline is:

```text
USER REQUEST
     ↓
DISCOVER
     ↓
ASSESS CAPABILITIES
     ↓
UNDERSTAND INTENT
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

This sequence is adaptive.

Not every task requires every stage.

---

# 3. Pipeline Principle

The pipeline must optimize for:

```text
minimum necessary process
+
maximum useful confidence
```

A trivial change should remain trivial.

A complex change should receive sufficient discovery, planning, execution, and verification.

---

# 4. Stage 1 — User Request

Input:

```text
user request
```

The system should extract:

- requested outcome;
- explicit constraints;
- known preferences;
- apparent scope;
- referenced files or systems;
- urgency where relevant.

Do not treat the initial request as a complete technical specification automatically.

---

# 5. Stage 2 — Discovery

Invoke the appropriate discovery behavior.

Determine:

```text
What already exists?
What is relevant?
What can be inspected?
What conventions are present?
What constraints are observable?
```

Typical discovery targets:

```text
filesystem
repository
framework
dependencies
configuration
tests
runtime
architecture
existing UI
deployment configuration
```

---

# 6. Discovery Before Questions

The pipeline must not ask the user:

```text
"What framework are you using?"
```

if the framework can be discovered from the project.

Instead:

```text
inspect
→ determine framework
→ continue
```

Questions are a fallback for genuine unknowns, not a substitute for inspection.

---

# 7. Discovery Depth

Discovery depth should depend on task complexity.

## Minimal Task

Example:

```text
Fix a typo.
```

Required discovery may be:

```text
locate relevant file
→ inspect surrounding context
```

## Moderate Task

Example:

```text
Add a new component.
```

Discovery may include:

```text
framework
component structure
styling conventions
routing
tests
```

## Complex Task

Example:

```text
Add authentication.
```

Discovery may include:

```text
frontend
backend
database
existing auth
session model
API architecture
deployment
security conventions
tests
```

---

# 8. Stage 3 — Capability Assessment

Determine whether the environment can support the requested work.

Assess:

```text
MODEL
AGENT
TOOLS
ENVIRONMENT
PROJECT
```

Potential capabilities:

```text
filesystem
shell
browser
visual inspection
image inspection
database access
network access
MCP
package manager
test runner
GPU
runtime
```

---

# 9. Capability States

Use:

```text
FULL
SUITABLE
CONSTRAINED
UNSUITABLE
```

The state should describe the capability **for the current task**.

A capability can be available but unsuitable.

Example:

```text
GPU:
available

Task:
small CSS change

GPU capability:
irrelevant
```

The pipeline should not introduce unnecessary dependencies merely because capabilities exist.

---

# 10. Capability Failure

If a required capability is unavailable:

```text
determine whether degradation is possible
```

If yes:

```text
continue with reduced confidence
+
record limitation
```

If no:

```text
UNSUITABLE
+
stop or request an alternative workflow
```

Never simulate unavailable evidence.

---

# 11. Stage 4 — Intent Understanding

Separate:

```text
LITERAL REQUEST
UNDERLYING GOAL
CONSTRAINTS
PREFERENCES
ASSUMPTIONS
```

Example:

```text
User:
"Make this page load faster."

Literal:
Improve page loading performance.

Potential underlying goal:
Improve user-perceived responsiveness.

Relevant constraints:
Preserve current design.

Possible assumptions:
That JavaScript is the primary bottleneck.
```

The assumption should be tested rather than accepted automatically.

---

# 12. Stage 5 — Challenge

Challenge only when there is a substantive reason.

Potential reasons:

```text
security risk
performance cost
accessibility issue
contradictory requirements
architectural problem
unnecessary complexity
data integrity risk
unrealistic implementation constraint
```

Challenge format:

```text
Issue
↓
Evidence
↓
Impact
↓
Alternative
↓
Decision
```

---

# 13. Challenge Does Not Mean Override

The pipeline does not authorize silent requirement changes.

Example:

```text
User requests:
Use library X everywhere.

Agent discovers:
Library X substantially increases the client bundle.

Agent:
Explain the tradeoff.

User:
Proceed anyway.

Pipeline:
Proceed with the user's decision unless a higher-priority constraint prevents it.
```

---

# 14. Stage 6 — Questions

After discovery and capability assessment, determine whether questions remain.

Questions are appropriate when:

```text
the answer is not discoverable
AND
the answer materially affects the implementation
```

Do not ask questions simply because multiple technically valid implementations exist.

---

# 15. Question Priority

Questions should be prioritized.

## Blocking

Work cannot proceed safely or meaningfully without the answer.

Ask immediately.

## High Value

The answer materially affects architecture, behavior, or outcome.

Ask before implementation.

## Medium Value

The answer affects quality but a reasonable reversible default exists.

Use a default when appropriate or ask if efficient.

## Low Value

Minor preference.

Do not interrupt execution unnecessarily.

---

# 16. Question Batching

If several questions are necessary, batch related questions.

Bad:

```text
Question
wait
Question
wait
Question
wait
```

Better:

```text
I need three decisions before implementation:
1. ...
2. ...
3. ...
```

Do not batch questions that depend on answers to previous questions.

---

# 17. Stage 7 — Plan

The plan should reflect task complexity.

Simple:

```text
locate
→ modify
→ verify
```

Complex:

```text
discovery
→ architecture
→ implementation phases
→ verification
→ integration
```

The plan should identify:

- scope;
- important decisions;
- implementation steps;
- verification strategy.

---

# 18. Plan Stability

Do not treat the initial plan as immutable.

Unexpected discoveries may require:

```text
replanning
```

When the implementation diverges materially from the plan:

```text
stop
→ explain finding
→ reassess
→ update plan
```

Do not continue blindly.

---

# 19. Stage 8 — Execution

Execution applies the selected plan.

Execution should:

- stay within scope;
- preserve existing behavior;
- follow project conventions;
- minimize unrelated changes;
- make incremental changes;
- validate risky changes.

---

# 20. Execution Boundaries

The pipeline should prevent scope creep.

Example:

```text
Requested:
Fix login redirect.

Discovered:
The project also has inconsistent naming.

Action:
Fix login redirect.

Not automatically:
Refactor the entire naming system.
```

Additional improvements can be reported separately.

---

# 21. Incremental Execution

For complex tasks:

```text
implement phase
↓
verify phase
↓
continue
```

This reduces the cost of failure.

Especially validate after changes involving:

- authentication;
- database migrations;
- dependency upgrades;
- routing;
- build configuration;
- infrastructure;
- complex animations;
- 3D rendering.

---

# 22. Unexpected Findings

If execution reveals a new issue:

```text
classify finding
↓
determine whether it blocks current work
```

Possible outcomes:

```text
non-blocking
→ continue

important but independent
→ continue + report

requires plan change
→ pause + replan

unsafe to continue
→ stop + explain
```

---

# 23. Stage 9 — Verification

Verification should correspond to the claims being made.

Examples:

```text
Code change
→ source inspection + relevant tests

Build change
→ build

API change
→ API/integration tests

UI change
→ runtime/browser inspection where available

Performance change
→ measurement

Security change
→ targeted security testing
```

---

# 24. Verification Levels

A useful conceptual model is:

```text
SOURCE
RUNTIME
INTEGRATION
VISUAL
MEASURED
```

Different tasks require different levels.

Do not imply that one level proves another.

---

# 25. Verification Matrix

The pipeline can track:

| Claim | Verification | Result |
|---|---|---|
| Code compiles | Build | PASS |
| Tests pass | Test runner | PASS |
| UI renders | Browser | PASS |
| Mobile layout works | Responsive browser inspection | PASS |
| Performance improved | Benchmark | UNVERIFIED |
| Production deployment works | Production environment | NOT TESTED |

This prevents broad claims based on narrow checks.

---

# 26. Failed Verification

If verification fails:

```text
do not report completion
```

Instead:

```text
identify failure
→ diagnose
→ fix if within scope
→ verify again
```

If the issue cannot be resolved:

```text
report incomplete state
+
failure evidence
+
remaining work
```

---

# 27. Unavailable Verification

If verification cannot be performed:

```text
UNVERIFIED
```

must be reported.

Examples:

```text
Browser unavailable.
Production environment unavailable.
GPU unavailable.
External API unavailable.
```

Do not substitute confidence for evidence.

---

# 28. Stage 10 — Reporting

The final report should summarize:

```text
WHAT CHANGED
WHAT WAS VERIFIED
WHAT WAS NOT VERIFIED
WHAT DECISIONS WERE MADE
WHAT REMAINS
```

For simple tasks:

```text
Changed:
...

Verified:
...

Remaining:
...
```

For complex tasks:

```text
Summary
Changes
Decisions
Verification
Limitations
Known issues
Remaining work
```

---

# 29. Stage 11 — Iteration

The pipeline is not necessarily complete after one execution cycle.

After reporting:

```text
user feedback
↓
new request
↓
discovery
↓
updated plan
↓
execution
```

The new cycle should reuse known project context where valid.

---

# 30. Skill Selection

The pipeline should select skills based on the task.

Example:

```text
"Build a cinematic scrolling 3D homepage."

Likely:
project-discovery
capability-assessment
interaction
challenge
ui-ux-design
3d-web-design
scroll-world-flyby
execution
verification
reporting
```

Not every listed skill must execute fully.

---

# 31. Skill Composition

Skills may be composed.

Example:

```text
project-discovery
        ↓
capability-assessment
        ↓
ui-ux-design
        ↓
animation-design
        ↓
execution
        ↓
verification
        ↓
reporting
```

A domain skill can invoke or rely on another skill's methodology where appropriate.

---

# 32. Avoiding Duplicate Work

The pipeline should prevent repeated discovery.

For example:

```text
project-discovery
→ identifies React + Vite

ui-ux-design
→ should reuse that fact
```

It should not independently ask:

```text
"Are you using React?"
```

unless the project state has changed or the previous evidence is no longer reliable.

---

# 33. State

The pipeline should conceptually maintain task state.

Example:

```yaml
task:
  request: ...
  scope: ...

discovery:
  facts: ...
  unknowns: ...

capabilities:
  model: ...
  agent: ...
  tools: ...
  environment: ...
  project: ...

decisions:
  user: ...

plan:
  steps: ...

execution:
  changes: ...

verification:
  checks: ...

report:
  limitations: ...
  remaining_work: ...
```

This state does not require a particular implementation format.

---

# 34. Evidence

Important decisions should be associated with evidence when possible.

Example:

```text
Decision:
Use existing animation library.

Evidence:
The project already uses the library for three existing components.
```

This is preferable to:

```text
Use library because it seems good.
```

---

# 35. Confidence

The pipeline should distinguish confidence from verification.

Example:

```text
High confidence:
Source implementation clearly handles the case.

Verified:
Automated test confirms the behavior.
```

These are different claims.

High confidence is not proof.

---

# 36. Stop Conditions

The pipeline should stop when:

```text
task is complete
+
required verification passed
```

or when:

```text
safe/meaningful execution is impossible
```

or:

```text
required user decision is unavailable
```

or:

```text
new information invalidates the current plan
```

---

# 37. Replanning Conditions

Replanning is appropriate when:

- requirements change;
- architecture differs from assumptions;
- a dependency is unavailable;
- a required capability is missing;
- implementation reveals a major constraint;
- verification exposes a significant defect.

Do not restart discovery unnecessarily for minor findings.

---

# 38. Failure Handling

A pipeline failure should identify:

```text
stage
cause
evidence
impact
possible next step
```

Example:

```text
Stage:
Verification

Cause:
Browser runtime unavailable.

Impact:
Visual behavior cannot be verified.

Next step:
Run the application in a browser-enabled environment.
```

---

# 39. Safety Boundaries

The pipeline must not:

- fabricate evidence;
- fabricate tool output;
- claim unavailable capabilities;
- silently change requirements;
- expose secrets;
- make irreversible changes without appropriate confirmation;
- continue through known unsafe states.

---

# 40. Irreversible Operations

Operations with meaningful irreversible consequences should receive additional caution.

Examples:

```text
destructive database migration
data deletion
production deployment
credential rotation
mass file deletion
public API breaking change
```

Where practical:

```text
explain
→ confirm
→ execute
→ verify
```

Routine reversible changes do not require unnecessary confirmation.

---

# 41. Minimal Intervention

The pipeline should prefer:

```text
smallest change that reliably satisfies the requirement
```

unless the user explicitly requests a broader redesign.

This reduces:

- regression risk;
- review complexity;
- debugging cost;
- unintended behavior changes.

---

# 42. Quality Gate

Before declaring completion:

```text
Requirement satisfied?
        ↓
Yes
        ↓
Implementation complete?
        ↓
Yes
        ↓
Relevant verification performed?
        ↓
Yes / limitations documented
        ↓
Report
```

If a critical condition fails:

```text
do not declare complete
```

---

# 43. Example: Simple Task

Request:

```text
Change the homepage button from blue to brown.
```

Pipeline:

```text
Discovery
→ locate homepage and button styles.

Capability
→ filesystem available.

Interaction
→ no question required if the intended brown is already specified by existing design context.
   Otherwise ask only if color choice is genuinely unresolved.

Execution
→ modify relevant style.

Verification
→ inspect source/build or rendered result where available.

Reporting
→ state the change and verification.
```

---

# 44. Example: Contradictory Task

Request:

```text
"Rebuild the React app using React."
```

Pipeline:

```text
Discovery
→ existing application is already React.

Intent
→ identify whether the user actually means a rewrite,
   refactor, migration, or visual rebuild.

Interaction
→ clarify the ambiguity.

Execution
→ proceed only after the intended scope is clear.
```

---

# 45. Example: Missing Capability

Request:

```text
"Reproduce this animation exactly."
```

Environment:

```text
No browser
No visual inspection
```

Pipeline:

```text
Capability assessment
→ visual verification unavailable.

Execution
→ source-level implementation may still be possible.

Verification
→ visual result remains UNVERIFIED.

Reporting
→ explicitly state the limitation.
```

The pipeline must not claim exact visual reproduction.

---

# 46. Example: Technical Tradeoff

Request:

```text
"Use a separate animation library for every section."
```

Discovery reveals:

```text
five different animation dependencies
```

Pipeline:

```text
Challenge
→ explain dependency and maintenance cost.

Alternative
→ evaluate whether existing animation infrastructure can support the requirements.

User decision
→ preserve user authority.

Execution
→ implement the selected approach.

Verification
→ measure bundle impact where relevant.
```

---

# 47. Example: Complex Feature

Request:

```text
"Add authentication."
```

Pipeline:

```text
Discovery
→ inspect frontend, backend, database, current session model.

Capability
→ determine database, runtime, shell, package manager, test environment.

Intent
→ determine authentication requirements.

Questions
→ ask only for decisions not discoverable from the project.

Challenge
→ identify security or architecture risks.

Plan
→ authentication flow, storage, authorization, tests.

Execution
→ implement incrementally.

Verification
→ test success, failure, authorization, expiry, and relevant security boundaries.

Reporting
→ changes, checks, limitations, remaining work.
```

---

# 48. Pipeline Anti-Patterns

## Rigid Pipeline

Forcing every task through every stage.

Bad:

```text
Fix typo
→ 30-minute architecture analysis
```

---

## Skip Discovery

Asking the user for information that can be inspected.

---

## Skip Capability Assessment

Assuming tools or runtime capabilities exist.

---

## Skip Verification

Declaring success because code was written.

---

## Over-Questioning

Turning every task into an interview.

---

## Silent Replanning

Changing architecture without informing the user when the change is consequential.

---

## Endless Replanning

Restarting the entire process because of minor findings.

---

## Scope Creep

Using a small request as justification for unrelated improvements.

---

## False Completion

Reporting successful completion despite failed or unavailable verification.

---

# 49. Pipeline Invariants

The following must remain true:

```text
Discovery precedes unnecessary questions.

Capabilities are assessed before being relied upon.

User decisions are respected.

Substantive technical problems may be challenged.

Execution remains within agreed scope.

Verification corresponds to claims.

Unavailable verification is disclosed.

Failures are not reported as success.

The pipeline adapts to task complexity.

Skills remain responsible for domain methodology.
```

---

# 50. Completion Criteria

The pipeline implementation is conceptually complete when:

- [ ] user requests can enter the pipeline;
- [ ] discovery can occur before unnecessary questioning;
- [ ] capabilities can be assessed;
- [ ] intent can be clarified;
- [ ] substantive problems can be challenged;
- [ ] necessary user decisions can be collected;
- [ ] plans can be created proportionally;
- [ ] execution can occur incrementally;
- [ ] verification can be performed;
- [ ] limitations can be recorded;
- [ ] results can be reported;
- [ ] tasks can iterate after feedback;
- [ ] unavailable capabilities do not produce fabricated evidence;
- [ ] simple tasks are not forced through unnecessary complexity.

---

# 51. Final Principle

The pipeline exists to coordinate intelligent work, not to create bureaucracy.

The desired behavior is:

```text
Understand what is being asked.
        ↓
Discover what can be known.
        ↓
Determine what can actually be done.
        ↓
Resolve only important unknowns.
        ↓
Challenge substantive problems.
        ↓
Execute the agreed solution.
        ↓
Verify what can be verified.
        ↓
Report what actually happened.
```

The pipeline should be as lightweight as the task allows and as rigorous as the task requires.
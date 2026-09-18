# Testing The-Builder

**Testing Specification:** 0.1.0

---

## 1. Purpose

The-Builder is not only a collection of Markdown files.

It is a behavioral system.

Testing must therefore verify both:

1. **structural correctness** — the repository is valid and internally consistent;
2. **behavioral correctness** — an agent following the system behaves according to its principles.

A repository can pass structural validation while still teaching poor behavior.

---

# 2. Testing Philosophy

The primary question is:

> Does The-Builder cause an agent to behave correctly under different task conditions?

Tests should therefore focus on observable behavior.

The tests should not require exact wording.

---

# 3. Testing Layers

The repository uses several testing layers:

```text
STRUCTURE
    ↓
SCHEMA
    ↓
REGISTRY
    ↓
CONTRACT
    ↓
BEHAVIOR
    ↓
INSTALLATION
    ↓
ADAPTER
```

Each layer catches a different class of failure.

---

# 4. Structural Tests

Structural tests verify that expected files and directories exist.

Examples:

```text
skills/<skill-id>/SKILL.md
adapters/<adapter>/adapter.yaml
core/<contract>
```

Structural tests should not be treated as proof that the content is good.

---

# 5. Schema Tests

Schema tests validate machine-readable files.

Examples:

```text
skill metadata
adapter metadata
registry YAML
plugin contracts
connector contracts
manifest
package metadata
```

Malformed configuration should fail validation.

---

# 6. Registry Tests

The registry should be checked for:

- unique skill IDs;
- valid paths;
- existing skill files;
- valid dependency references;
- valid versions;
- valid categories.

---

# 7. Contract Tests

Core contracts should be checked for required concepts.

Examples:

```text
execution
→ scope control
→ incremental execution
→ error handling
→ evidence
→ completion criteria

verification
→ evidence
→ limitations
→ failure states
→ completion criteria

reporting
→ status
→ changes
→ verification
→ limitations
→ remaining work
```

Contract tests should avoid requiring exact prose.

---

# 8. Behavioral Tests

Behavioral tests evaluate whether a skill or contract produces the intended behavior.

Examples:

```text
Do not ask for discoverable information.

Ask when a genuinely required decision is unavailable.

Challenge substantive technical problems.

Do not challenge subjective preferences unnecessarily.

Do not claim unavailable capabilities.

Verify implementation.

Report unverified work.
```

---

# 9. Why Behavioral Tests Matter

Consider two implementations:

```text
Implementation A:
Contains all required headings.

Implementation B:
Contains fewer headings but reliably causes correct behavior.
```

A structural test may prefer A.

A behavioral test should determine which actually satisfies the system's intended behavior.

---

# 10. Test Case Structure

A behavioral test should describe:

```yaml
id: example-case

context:
  ...

request:
  ...

available_capabilities:
  ...

expected_behavior:
  - ...

forbidden_behavior:
  - ...
```

Exact output wording should normally not be required.

---

# 11. Behavioral Evaluation

A test should evaluate observable behavior such as:

```text
asked unnecessary question
did not ask necessary question
identified contradiction
challenged substantive issue
respected user preference
claimed unavailable capability
performed verification
reported limitation
```

---

# 12. Positive Assertions

Positive assertions describe behavior that should occur.

Example:

```text
The agent inspects the project before asking which framework is used.
```

---

# 13. Negative Assertions

Negative assertions describe behavior that must not occur.

Example:

```text
The agent must not ask the user which framework is used when the repository can be inspected.
```

Negative assertions are important because many failures are failures of omission or restraint.

---

# 14. Anti-Pattern Testing

Important anti-patterns should have tests.

Examples:

```text
interrogation
blind execution
false capability
silent override
unverified completion
scope creep
provider lock-in
```

---

# 15. Project Discovery Tests

Project discovery should test whether the agent:

- inspects the repository;
- identifies technology;
- understands architecture;
- recognizes conventions;
- identifies constraints;
- distinguishes known from unknown information;
- stops discovery when enough information exists.

---

# 16. Capability Tests

Capability assessment should test whether the agent:

- distinguishes model capabilities from agent capabilities;
- checks available tools;
- considers environment constraints;
- considers project requirements;
- assigns appropriate capability states;
- degrades gracefully;
- avoids fabricated capabilities.

---

# 17. Interaction Tests

Interaction should test whether the agent:

- discovers information before asking;
- asks only high-value questions;
- batches related questions;
- respects explicit preferences;
- identifies genuine ambiguity;
- avoids repetitive questioning;
- stops asking once sufficient information exists.

---

# 18. Challenge Tests

Challenge behavior should test:

```text
substantive technical weakness
contradictory requirements
unnecessary complexity
security risk
performance risk
maintainability risk
```

It should also test that the agent does **not** challenge merely because:

```text
it prefers another style
it personally prefers another library
the user chose a subjective visual preference
```

---

# 19. Execution Tests

Execution should test:

- scope control;
- incremental implementation;
- preservation of existing conventions;
- dependency discipline;
- safe handling of risky changes;
- error handling;
- final diff inspection.

---

# 20. Verification Tests

Verification should test whether the agent:

- selects appropriate checks;
- distinguishes implementation from verification;
- reports actual evidence;
- recognizes failed checks;
- recognizes unavailable checks;
- reports unverified areas;
- avoids false completion claims.

---

# 21. Reporting Tests

Reporting should test whether the agent:

- gives an accurate status;
- summarizes meaningful changes;
- reports verification;
- identifies limitations;
- identifies remaining work;
- distinguishes recommendations from completed work;
- avoids unsupported certainty.

---

# 22. Domain Skill Tests

Domain skills should be tested against their intended methodology.

Examples:

```text
UI/UX
→ hierarchy, responsiveness, accessibility, consistency

Animation
→ timing, purpose, performance, reduced motion

3D
→ rendering cost, asset handling, loading, fallback

Scroll World / Fly-by
→ camera movement, scene transitions, depth, scroll interaction

Content + Code Optimization
→ content quality, performance, maintainability

SEO
→ crawlability, metadata, semantics, content structure

Security
→ threat identification, evidence, remediation, verification

Reviewer
→ structured findings, severity, evidence, impact, recommendation
```

---

# 23. Test Scope

Tests should remain focused.

A test for SEO should not require the agent to redesign the entire application.

A test for animation should not require database modifications.

---

# 24. Fixture Projects

Behavioral tests may use fixture projects representing common situations.

Examples:

```text
simple React project
Flutter project
Node API
full-stack application
unknown/empty project
legacy project
broken project
security-sensitive application
```

Fixtures should be minimal enough to understand.

---

# 25. Unknown Project Fixture

An unknown project should test whether the agent discovers:

```text
framework
language
package manager
architecture
entry points
```

before making assumptions.

---

# 26. Existing Project Fixture

An existing project should test whether the agent respects existing conventions.

Example:

```text
Existing:
React + Tailwind + existing component library

Request:
Change homepage button color.
```

Expected:

```text
inspect relevant implementation
→ make targeted change
→ verify
```

Not:

```text
rewrite styling system
```

---

# 27. Ambiguous Request Fixture

Example:

```text
Make the homepage better.
```

The test should establish whether the agent:

```text
discovers existing context
→ identifies meaningful ambiguity
→ asks high-value questions
```

It should not ask an exhaustive questionnaire.

---

# 28. Discoverable Information Fixture

Example:

```text
User:
What framework is this project using?
```

If the repository is available, expected behavior is:

```text
inspect repository
→ identify framework
→ answer
```

Not:

```text
ask user which framework they use
```

---

# 29. Preference Fixture

Example:

```text
User:
Make the animation slower.
```

Expected:

```text
implement slower animation
```

No challenge is necessary merely because the agent prefers faster animation.

---

# 30. Technical Tradeoff Fixture

Example:

```text
User:
Use a separate animation library for every section.
```

If this creates meaningful dependency, bundle, or maintenance costs, expected behavior is:

```text
identify tradeoff
→ explain evidence
→ propose alternatives
→ preserve user authority
```

The agent should not silently substitute its preferred architecture.

---

# 31. Capability-Limited Fixture

Example:

```text
User:
Match this website's animation exactly.
```

Environment:

```text
no browser
no visual inspection
```

Expected:

```text
implementation may proceed if source-level evidence is sufficient
visual verification must be marked unavailable
```

Forbidden:

```text
"The animation matches exactly."
```

---

# 32. Security Fixture

Example:

```text
User:
Add authentication.
```

Expected behavior includes discovering:

```text
existing backend
existing auth
database
session model
authorization requirements
deployment constraints
```

before choosing a specific implementation unnecessarily.

---

# 33. Reviewer Fixture

A reviewer test should contain a known issue.

Expected output should identify:

```text
severity
evidence
problem
impact
recommendation
classification
```

The exact wording is not important.

---

# 34. Regression Tests

Every important bug discovered in The-Builder should become a regression test when practical.

Example:

```text
Bug:
Installer claimed all targets were installed even when one target was missing.

Regression:
Test each target independently.
```

---

# 35. Test Naming

Use descriptive IDs.

Good:

```text
discover-framework-before-asking
respect-user-animation-preference
report-unavailable-visual-verification
detect-contradictory-stack-request
```

Avoid:

```text
test1
test2
caseA
```

---

# 36. Deterministic Tests

Tests should be deterministic whenever possible.

Avoid relying on:

```text
random model output
network timing
external service availability
current date
unstable third-party websites
```

when a controlled fixture can provide equivalent evidence.

---

# 37. External Services

When testing integrations with external services:

```text
mock when practical
```

Use live integration tests only when they provide meaningful additional coverage.

---

# 38. Network Independence

Core repository validation should not require network access unless explicitly testing network functionality.

A user should be able to clone the repository and run core validation offline where practical.

---

# 39. Test Isolation

Tests should not depend on:

```text
another test's filesystem state
global user configuration
personal credentials
previous installation
```

Each test should establish its required state.

---

# 40. Temporary Directories

Installer tests should use temporary directories.

After testing:

```text
clean up temporary state
```

Do not pollute the user's repository.

---

# 41. Installer Tests

Installer tests should verify:

```text
project installation
global installation
skill count
target paths
manifest
AGENTS instructions
repeat installation
```

where supported.

---

# 42. Installation Idempotency

Running installation twice should not create uncontrolled duplication.

Example:

```text
install
→ install again
```

Expected:

```text
same intended final state
```

---

# 43. Installer Conflict Tests

Test existing files and directories.

Examples:

```text
existing skill
existing configuration
existing manifest
existing unrelated file
```

The installer must follow its documented conflict policy.

---

# 44. Adapter Tests

Each adapter should be tested for:

```text
metadata
detection
path resolution
installation
skill availability
configuration behavior
limitations
```

---

# 45. CLI Tests

CLI tests should verify:

```text
help
version
install
doctor
test
invalid command
invalid option
```

where those commands exist.

---

# 46. CLI Error Behavior

Invalid usage should produce:

```text
clear error
non-zero exit status
```

when appropriate.

The CLI should not silently succeed on invalid input.

---

# 47. Validation Script

The repository validator should check structural invariants.

Example categories:

```text
required files
skill count
metadata
registry
adapter metadata
plugin metadata
connector metadata
```

---

# 48. Test Suite

The behavioral test suite should verify cross-cutting contracts.

It should test:

```text
core behavior
skill behavior
adapter behavior
installer behavior
challenge behavior
project discovery behavior
```

---

# 49. Multiple Test Runners

If The-Builder exposes multiple test entry points, they should agree on the same repository state.

For example:

```bash
python3 scripts/test_suite.py
```

and:

```bash
node cli/bin/the-builder.js test
```

should not silently validate different definitions of correctness.

---

# 50. Test Output

Test output should be concise and actionable.

Example:

```text
PASS: repository validation
skills=15 adapters=12 plugins=12 connectors=9

PASS: behavioral and contract tests
```

On failure:

```text
FAIL: 2 tests

- installer-project-skills
- adapter-metadata
```

---

# 51. Failure Diagnostics

A failing test should provide enough information to identify:

```text
which test failed
expected condition
observed condition
relevant fixture or file
```

Avoid dumping unrelated repository content.

---

# 52. Test Exit Codes

Recommended behavior:

```text
0 = all required tests passed

non-zero = one or more required tests failed
```

This allows CI systems to consume the result.

---

# 53. Continuous Integration

CI should run at minimum:

```bash
python3 scripts/validate.py
python3 scripts/test_suite.py
node cli/bin/the-builder.js test
```

when those commands are supported by the project.

---

# 54. CI Environment

CI should test in a clean environment.

Do not rely on:

```text
developer-specific files
local credentials
uncommitted changes
global agent installations
```

---

# 55. Documentation Tests

Documentation should be checked for:

- stale commands;
- incorrect paths;
- references to removed skills;
- invalid skill IDs;
- obsolete installation instructions.

---

# 56. Command Consistency

Search for stale command references after CLI changes.

Example:

```bash
grep -RIn --exclude-dir=.git 'npx the-builder' .
```

If the package is scoped, documentation should use the current scoped package command.

---

# 57. Registry Consistency

The registry should agree with:

```text
skills/
installer
tests
documentation
```

A skill present in the filesystem but absent from the registry is a consistency problem unless intentionally excluded.

---

# 58. Skill Count

When the project defines a canonical skill count, tests should verify it.

Current expected count:

```text
15
```

The count should be changed deliberately when skills are added or removed.

---

# 59. Adapter Count

Adapter count should likewise remain consistent with the repository's declared supported adapters.

Current repository expectation:

```text
12 adapters
```

If this changes, update:

```text
registry/documentation/tests
```

as appropriate.

---

# 60. Plugin and Connector Counts

If the repository declares plugin and connector registries, validation should ensure:

```text
registered item
↔
corresponding contract
```

and detect broken references.

---

# 61. Quality Gates

A release should not be considered ready merely because:

```text
files exist
```

A useful release gate is:

```text
structural validation
+
contract validation
+
behavioral tests
+
installer tests
+
CLI tests
+
documentation consistency
```

as applicable.

---

# 62. Test Limitations

Tests themselves have limitations.

Passing repository tests does not establish:

```text
every skill is universally effective
every agent behaves identically
every generated implementation is correct
every environment is supported
```

Tests provide evidence about tested behavior.

---

# 63. Model-Dependent Testing

If a test depends on an LLM's behavior, define observable criteria rather than requiring exact output.

Bad:

```text
Expected exact paragraph.
```

Better:

```text
Expected:
- does not ask for discoverable framework information;
- identifies the framework from repository evidence.
```

---

# 64. Human Evaluation

Some skill behaviors may require human evaluation.

Examples:

```text
visual quality
writing quality
UX quality
reasonableness of challenge
quality of recommendations
```

Human evaluation should be explicitly identified as such.

---

# 65. Human Evaluation Rubric

When human evaluation is required, evaluate observable criteria.

Example:

```text
Did the agent identify the important ambiguity?
Did it avoid unnecessary questions?
Did it preserve user authority?
Did it provide evidence for the challenge?
Did it accurately report limitations?
```

Do not evaluate based solely on whether the evaluator personally prefers the output.

---

# 66. Skill Regression

When changing a foundational skill such as:

```text
interaction
capability-assessment
challenge
verification
```

rerun domain and cross-cutting behavioral tests.

Foundation changes can affect many skills.

---

# 67. Domain Regression

When changing a domain skill:

```text
run its targeted tests
run relevant core tests
```

Example:

```text
Change SEO skill
→ SEO tests
→ core behavior tests
```

---

# 68. Release Testing

Before a release:

```text
clean checkout
↓
install dependencies
↓
validate repository
↓
run behavioral tests
↓
run CLI tests
↓
test installation
↓
inspect package contents
```

---

# 69. Package Testing

Before publishing an npm package, inspect the generated package contents.

Useful command:

```bash
npm pack --dry-run
```

Verify that required files are included and unwanted development artifacts are excluded.

---

# 70. Published Package Testing

When a package is published, test the actual published package in a clean temporary directory.

Example:

```bash
npx --yes @scope/package@version
```

Then verify:

```text
installation
skill count
targets
manifest
doctor
```

The published artifact is what users consume.

---

# 71. Clean-Environment Test

A release should be tested without relying on the source repository's local state.

Example:

```text
empty directory
↓
install package
↓
run installer
↓
inspect generated files
```

---

# 72. Test Matrix

For significant releases, consider a matrix:

| Area | Local | CI | Clean Install | Published Package |
|---|---:|---:|---:|---:|
| Validation | ✓ | ✓ | ✓ | ✓ |
| Behavioral tests | ✓ | ✓ | — | — |
| CLI | ✓ | ✓ | ✓ | ✓ |
| Installer | ✓ | ✓ | ✓ | ✓ |
| Adapters | ✓ | ✓ | ✓ | ✓ |

The exact matrix depends on project capabilities.

---

# 73. Test Maintenance

Tests should evolve with the project.

When behavior intentionally changes:

```text
update implementation
→ update affected tests
→ document intentional behavior change
```

Do not weaken a test merely because it became inconvenient.

---

# 74. Removing Tests

A test may be removed when:

- the behavior no longer exists;
- the test is invalid;
- a stronger test replaces it.

Do not remove a test solely because it fails after a change.

---

# 75. Testing Anti-Patterns

## Exact-Output Testing

Requiring one exact response from a probabilistic model.

## Structural-Only Testing

Checking headings while ignoring behavior.

## Happy-Path Only

Testing only successful scenarios.

## Test Theater

Adding superficial tests that provide little evidence.

## Environment Dependence

Requiring the developer's personal setup.

## Network Dependence

Making core tests fail without internet access.

## State Leakage

Allowing tests to depend on previous runs.

## Silent Test Skipping

Skipping important tests without reporting why.

## False Green

Allowing a command to exit successfully despite failed assertions.

## Release Without Clean Install

Assuming the source repository and published package are identical.

---

# 76. Completion Criteria

Testing is sufficiently complete for a change when:

- [ ] relevant structural checks pass;
- [ ] relevant contract checks pass;
- [ ] relevant behavioral tests pass;
- [ ] affected installer/adapter tests pass;
- [ ] relevant regression tests pass;
- [ ] failures are understood or explicitly reported;
- [ ] unavailable tests are documented;
- [ ] release artifacts are tested when applicable.

---

# 77. Final Testing Model

The-Builder testing model is:

```text
                TEST THE SYSTEM
                      │
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
    STRUCTURE      CONTRACT      BEHAVIOR
        │             │             │
        └─────────────┼─────────────┘
                      ↓
                 INTEGRATION
                      ↓
                  INSTALLER
                      ↓
                   ADAPTER
                      ↓
                    CLI
                      ↓
                 RELEASE
```

The purpose of this model is to prevent a common failure:

> A repository can be technically valid while teaching the wrong behavior.

The-Builder must therefore be tested both as **software** and as a **behavioral methodology**.
---
name: verification
description: Determine whether an implemented change actually satisfies its requirements using appropriate evidence, tests, inspection, and validation without overstating what has been verified.
version: 0.1.0
---

# Verification

## Purpose

Verification determines whether the implemented result satisfies the requested outcome and its acceptance criteria.

Implementation and verification are separate activities.

An agent may successfully modify files while still producing:

- broken behavior;
- incomplete behavior;
- regressions;
- incorrect assumptions;
- untested edge cases;
- visual defects;
- security weaknesses;
- deployment failures.

Verification exists to distinguish:

```text
"I changed it"
```

from:

```text
"I have evidence that it works as required."
```

---

# Core Principle

## Evidence Over Assumption

Never treat an implementation action as proof of correctness.

Examples:

```text
File was modified
≠
Feature works
```

```text
Tests passed
≠
Every aspect of the feature is correct
```

```text
Build succeeded
≠
Runtime behavior is correct
```

```text
No error appeared
≠
The system is secure
```

Verification should use evidence appropriate to the claim being made.

---

# Verification Scope

Verification should evaluate:

- functional correctness;
- acceptance criteria;
- regression risk;
- relevant edge cases;
- integration behavior;
- build correctness;
- test results;
- performance where relevant;
- accessibility where relevant;
- security where relevant;
- visual behavior where relevant;
- deployment behavior where relevant.

Not every task requires every category.

Verification depth should match task risk and complexity.

---

# Verification Levels

Use an adaptive verification depth.

## Level 0 — Basic

For trivial changes.

Examples:

- typo correction;
- documentation wording;
- simple configuration comment.

Typical verification:

- inspect diff;
- inspect changed location;
- run lightweight syntax/check if appropriate.

---

## Level 1 — Functional

For ordinary code changes.

Typical verification:

- relevant tests;
- type checking;
- linting;
- build;
- direct behavior check.

---

## Level 2 — Integration

For changes crossing components or systems.

Typical verification:

- unit tests;
- integration tests;
- build;
- API/data-flow validation;
- affected user flow;
- regression checks.

---

## Level 3 — High Risk

For changes involving:

- authentication;
- authorization;
- payments;
- destructive data operations;
- security boundaries;
- production infrastructure;
- migrations;
- sensitive data;
- major architectural changes.

Verification should include stronger evidence and explicit limitations.

---

# Verification Planning

Verification should be considered before implementation.

For each significant acceptance criterion, identify:

```text
criterion
↓
verification method
↓
expected evidence
```

Example:

```text
Criterion:
User can reset their password.

Method:
Integration test + manual flow.

Evidence:
Reset request succeeds and new password authenticates.
```

---

# Acceptance Criteria

Verify against the actual acceptance criteria.

Do not replace the user's requested outcome with an easier internal interpretation.

Example:

User asks:

> Make the animation feel smooth at 60 FPS.

A build passing is insufficient evidence.

Relevant verification may require:

- runtime inspection;
- frame/performance measurements;
- representative hardware;
- browser profiling.

---

# Verification Matrix

For larger tasks, use a matrix:

| Requirement | Method | Result | Evidence |
|---|---|---|---|
| Feature exists | Functional test | PASS | Test output |
| API returns expected data | Integration test | PASS | Response/assertion |
| Mobile layout works | Visual inspection | PASS | Supported viewport |
| No type errors | Type check | PASS | Command output |
| Production build works | Build | PASS | Build result |

Do not claim PASS without corresponding evidence.

---

# Evidence Quality

Evidence can be classified as:

## Direct

The behavior was directly observed or tested.

Example:

```text
Automated test passed.
```

## Strong Indirect

The implementation was validated through a reliable proxy.

Example:

```text
Type checker passed for the affected module.
```

## Weak Indirect

The result is plausible but not directly established.

Example:

```text
The code path appears correct by inspection.
```

## Unknown

No reliable evidence exists.

Example:

```text
Visual behavior could not be inspected because no browser/visual capability was available.
```

---

# Verification Claims

Use precise language.

Prefer:

```text
Verified:
The authentication integration tests pass.
```

Not:

```text
Authentication is definitely working everywhere.
```

Prefer:

```text
The production build completes successfully.
```

Not:

```text
The application is production-ready.
```

---

# Verification Boundaries

Every verification result has a scope.

Example:

```text
Verified:
Desktop Chromium at 1440×900.

Not verified:
Safari, mobile browsers, low-end devices.
```

Do not generalize beyond the evidence.

---

# Automated Tests

Run the most relevant automated tests available.

Consider:

- unit tests;
- integration tests;
- end-to-end tests;
- regression tests;
- snapshot tests;
- contract tests.

Choose tests based on the affected behavior.

Do not run every test blindly when a smaller relevant set provides sufficient evidence.

For high-risk changes, broader testing may be justified.

---

# Test Interpretation

A passing test means the tested assertion passed under the tested conditions.

It does not prove:

- untested behavior;
- production configuration;
- unsupported platforms;
- visual quality;
- security;
- performance.

Always understand what the test actually covers.

---

# Failed Tests

When tests fail:

1. identify the failure;
2. determine whether it is caused by the current change;
3. inspect the relevant code;
4. fix the implementation when appropriate;
5. update tests only when expected behavior intentionally changed;
6. rerun affected tests.

Never suppress or remove a test merely because it is inconvenient.

---

# Flaky Tests

If a test appears flaky:

- rerun when appropriate;
- inspect historical/contextual evidence if available;
- distinguish infrastructure failure from implementation failure;
- record uncertainty.

Do not claim a flaky test is fixed without evidence.

---

# Build Verification

If the task affects build behavior, verify the relevant build.

Check:

- compilation;
- bundling;
- asset processing;
- dependency resolution;
- configuration;
- generated output.

A successful build is evidence about build correctness, not complete application correctness.

---

# Type Checking

When a typed language is used, run relevant type checking where available.

Type checking can detect:

- invalid interfaces;
- missing properties;
- incompatible values;
- incorrect function usage;
- unresolved types.

Passing type checks does not establish runtime correctness.

---

# Linting

Use linting where it is part of the project workflow.

Linting may detect:

- syntax problems;
- suspicious patterns;
- style violations;
- unused variables;
- unsafe constructs.

Do not treat linting as functional verification.

---

# Formatting

Formatting validation is useful for:

- consistency;
- CI compatibility;
- reducing accidental formatting differences.

It is not evidence that functionality works.

---

# Runtime Verification

When possible, exercise the actual behavior.

Examples:

```text
create account
→ login
→ access protected page
→ logout
```

or:

```text
open page
→ trigger animation
→ resize viewport
→ interact
→ confirm expected result
```

Runtime verification provides stronger evidence than source inspection alone.

---

# Browser Verification

For web applications, verify relevant browser behavior when browser access is available.

Consider:

- console errors;
- network failures;
- layout;
- interaction;
- navigation;
- responsive behavior;
- loading behavior.

If browser access is unavailable, do not claim browser behavior was verified.

---

# Visual Verification

Visual requirements require visual evidence.

Examples:

- UI redesign;
- animation;
- 3D scene;
- responsive layout;
- typography;
- spacing;
- color;
- visual hierarchy.

Source inspection alone cannot establish visual correctness.

If visual inspection is unavailable:

```text
Visual verification: UNVERIFIED
Reason: no visual/browser capability available.
```

Do not fabricate screenshots, observations, or visual results.

---

# Responsive Verification

For responsive interfaces, test representative viewport classes.

Consider:

```text
mobile
tablet
desktop
large desktop
```

Use the project's actual supported breakpoints where known.

Do not claim universal responsiveness from one viewport.

---

# Accessibility Verification

Where UI behavior changes, verify relevant accessibility characteristics.

Consider:

- keyboard navigation;
- focus behavior;
- semantic structure;
- accessible names;
- labels;
- contrast;
- reduced motion;
- screen-reader semantics;
- touch target usability.

Automated accessibility checks are useful but incomplete.

Manual inspection may still be required.

---

# Performance Verification

Performance requirements require measurement where possible.

Possible evidence:

- Lighthouse;
- browser performance profiling;
- bundle analysis;
- request counts;
- response timings;
- memory usage;
- frame timing;
- load metrics.

Avoid claims such as:

```text
This is much faster.
```

unless supported by comparative evidence.

Prefer:

```text
Bundle size decreased from X to Y.
```

or:

```text
The affected test completed in X ms versus Y ms previously.
```

---

# Animation Verification

For animation changes, verify:

- intended trigger;
- timing;
- sequencing;
- interaction;
- interruption behavior;
- responsive behavior;
- reduced-motion handling where relevant;
- runtime performance.

A syntactically valid animation implementation is not enough.

---

# 3D Verification

For 3D experiences, verify:

- scene loads;
- assets load;
- camera behavior;
- interaction;
- lighting/material behavior;
- responsive behavior;
- performance;
- fallback behavior where required.

If GPU/device testing was not possible, state that limitation.

---

# Scroll World / Fly-by Verification

Verify:

- camera progression;
- scene transitions;
- scroll mapping;
- spatial continuity;
- depth/parallax;
- loading transitions;
- interaction behavior;
- performance.

If the experience depends on precise visual timing, visual inspection is required for strong verification.

---

# API Verification

For API changes, verify:

- request validation;
- expected responses;
- error responses;
- authentication;
- authorization;
- relevant status codes;
- serialization;
- integration with consumers.

Where appropriate, test malformed and unauthorized requests.

---

# Database Verification

For database changes, verify:

- schema state;
- migration success;
- data integrity;
- application compatibility;
- indexes/constraints where relevant;
- rollback/recovery behavior where required.

Never assume a migration is safe merely because it executes successfully.

---

# Security Verification

Security-sensitive changes require security-focused verification.

Check relevant areas such as:

- authorization boundaries;
- authentication behavior;
- input validation;
- output encoding;
- injection risks;
- secret handling;
- session behavior;
- access control;
- file upload/download behavior;
- dependency vulnerabilities.

Distinguish between:

```text
security test passed
```

and:

```text
system is secure
```

The latter is generally too broad to claim.

---

# Regression Verification

Determine what existing behavior could have been affected.

Regression testing should focus on:

- changed interfaces;
- shared components;
- reused utilities;
- common services;
- data contracts;
- routing;
- authentication;
- build configuration.

A focused change can have a wide impact if it modifies shared infrastructure.

---

# Negative Testing

Where appropriate, verify failure behavior.

Examples:

```text
invalid input
missing required field
unauthorized request
expired session
missing resource
network failure
duplicate request
```

Negative testing is particularly important for validation and security-sensitive behavior.

---

# Edge Cases

Consider relevant boundaries:

- empty values;
- null/undefined;
- maximum/minimum values;
- duplicate data;
- malformed input;
- slow network;
- missing assets;
- unsupported viewport;
- concurrent operations.

Do not invent excessive edge cases for trivial tasks.

---

# Integration Verification

When multiple systems interact, verify the integration boundary.

Example:

```text
Frontend
↓
API
↓
Database
```

Testing only the frontend component does not prove the entire flow works.

---

# External Services

External integrations may depend on:

- credentials;
- network access;
- service availability;
- rate limits;
- configuration;
- third-party behavior.

If real external verification is unavailable, identify the boundary explicitly.

Example:

```text
Local integration verified.
Production third-party delivery unverified.
```

---

# Environment Verification

Verification should consider the environment in which it was performed.

Record relevant facts such as:

- operating system;
- runtime version;
- browser;
- package version;
- device;
- GPU;
- deployment environment.

Do not imply that local verification represents every supported environment.

---

# Capability Limitations

If a required verification capability is unavailable:

1. identify the missing capability;
2. determine what can still be verified;
3. perform available verification;
4. mark the remainder unverified;
5. do not fabricate evidence.

Example:

```text
Code and type checks verified.

Visual appearance unverified because browser/visual inspection was unavailable.
```

---

# Partial Verification

A task may be partially verified.

Represent it explicitly:

```text
Functional behavior: VERIFIED
Type checking: VERIFIED
Build: VERIFIED
Visual behavior: UNVERIFIED
Mobile behavior: UNVERIFIED
```

Partial verification is more useful than an unsupported PASS/FAIL conclusion.

---

# Verification Status

Use precise statuses.

## VERIFIED

Reliable evidence directly supports the claim.

## PARTIALLY VERIFIED

Some relevant behavior has evidence, but important portions remain untested.

## UNVERIFIED

The claim could not be reliably tested.

## FAILED

Available verification produced evidence that the requirement is not satisfied.

## BLOCKED

Verification could not proceed because a required capability, environment, credential, dependency, or decision is unavailable.

---

# Verification Evidence

For each important claim, preserve useful evidence.

Examples:

```text
Command:
npm test

Result:
42 passed, 0 failed.
```

```text
Build:
npm run build

Result:
completed successfully.
```

```text
Manual:
Password reset flow completed successfully in local environment.
```

Avoid storing sensitive output merely for documentation.

---

# Reproducibility

Verification should be reproducible where practical.

Record:

- command;
- relevant arguments;
- environment;
- expected result;
- observed result.

A future contributor should be able to understand how the result was established.

---

# Final Diff Inspection

Before reporting completion:

```bash
git diff
git diff --check
git status
```

where applicable.

Inspect for:

- unintended modifications;
- debug statements;
- temporary files;
- accidental deletions;
- secrets;
- unrelated refactors.

---

# Verification vs Review

Verification asks:

> Does the implementation satisfy the requirements?

Review asks:

> Is the implementation acceptable in quality, architecture, security, maintainability, and other relevant dimensions?

These overlap but are not identical.

---

# Verification vs Testing

Testing is one verification mechanism.

Verification is broader.

It may include:

```text
tests
+
builds
+
static analysis
+
runtime inspection
+
visual inspection
+
measurements
+
diff inspection
+
manual workflows
```

---

# Verification vs Execution

Execution changes the project.

Verification evaluates the resulting state.

Do not report:

```text
Implemented successfully.
```

as equivalent to:

```text
Verified successfully.
```

---

# Verification and User Decisions

If verification reveals a genuine product decision rather than a technical defect:

- report the finding;
- explain the available behavior;
- ask the user when a meaningful choice is required.

Do not silently change product behavior to satisfy the verifier's preference.

---

# Verification and Challenge

Verification may reveal that an accepted approach produces a substantive problem.

In that case:

1. provide evidence;
2. identify the affected requirement;
3. explain the consequence;
4. propose alternatives;
5. return to interaction/challenge when user direction is required.

Do not hide failed requirements behind implementation details.

---

# Verification Failure Handling

When verification fails:

```text
Failure
↓
Identify cause
↓
Determine whether implementation can be corrected
↓
Correct
↓
Re-verify
```

If the failure is caused by an external limitation:

```text
Identify limitation
↓
Document it
↓
Determine remaining verification
↓
Report blocked/unverified scope
```

---

# Do Not Game Verification

Never:

- weaken assertions merely to pass;
- delete failing tests without justification;
- mock away the behavior being tested;
- disable security checks;
- suppress errors;
- change acceptance criteria silently;
- avoid difficult test cases solely to obtain a green result.

Verification exists to produce trustworthy evidence, not favorable output.

---

# Verification Depth by Risk

| Task | Typical Verification |
|---|---|
| Typo | Diff inspection |
| Documentation | Diff + syntax if relevant |
| Simple function | Unit test/type check |
| UI component | Tests + visual inspection |
| API change | Unit + integration tests |
| Database migration | Migration + integrity checks |
| Authentication | Integration + negative/security tests |
| Payment | Strong integration/sandbox verification |
| 3D experience | Runtime + visual + performance |
| Production infrastructure | Automated + environment-specific validation |

This is guidance, not a rigid rule.

---

# Examples

## Example 1 — Simple Text Change

Request:

> Fix the typo on the homepage.

Verification:

```text
Inspect diff.
Confirm intended text changed.
Confirm no unrelated files changed.
```

No need for an end-to-end test.

---

## Example 2 — API Endpoint

Request:

> Add a POST /users endpoint.

Verification:

```text
Valid request → expected response.
Invalid request → validation error.
Unauthorized request → rejected.
Database record → created correctly.
Relevant tests → pass.
```

---

## Example 3 — UI Redesign

Request:

> Redesign the dashboard.

Verification should include:

```text
component tests where applicable
build/type checks
responsive inspection
visual inspection
interaction checks
accessibility checks
```

A successful build alone is insufficient.

---

## Example 4 — Animation

Request:

> Add a scroll-driven hero animation.

Verification:

```text
scroll trigger works
camera/element movement follows scroll
animation reaches intended states
resize does not break behavior
reduced-motion behavior considered
runtime performance inspected
visual appearance inspected
```

---

## Example 5 — Missing Browser Capability

Request:

> Reproduce this exact visual animation.

Agent can modify code but cannot visually inspect a browser.

Correct result:

```text
Implementation: completed.
Static checks: passed.
Build: passed.
Visual verification: unverified.
```

Incorrect result:

```text
The animation looks correct.
```

---

# Verification Report

A useful final verification report contains:

```text
STATUS
VERIFIED / PARTIALLY VERIFIED / UNVERIFIED / FAILED / BLOCKED

REQUIREMENTS
- requirement → status

CHECKS
- command/test → result

EVIDENCE
- relevant observations

UNVERIFIED
- remaining areas

LIMITATIONS
- environment/capability limitations

REGRESSIONS
- detected or not detected within tested scope
```

The Reporting skill defines the broader reporting structure.

---

# Completion Criteria

Verification is complete when:

- [ ] acceptance criteria have been evaluated;
- [ ] appropriate verification depth was selected;
- [ ] relevant automated tests were run;
- [ ] relevant build/type/static checks were run;
- [ ] runtime behavior was tested where appropriate;
- [ ] visual behavior was inspected where required and possible;
- [ ] security/accessibility/performance checks were performed where relevant;
- [ ] regressions were considered;
- [ ] failed checks were investigated;
- [ ] verification limitations are explicit;
- [ ] evidence supports reported claims;
- [ ] final diff was inspected;
- [ ] no unsupported claims of success remain.

Verification answers:

> **“What evidence do we have that the requested result works?”**

It does not answer:

> **“What should we build?”**

That belongs to discovery, interaction, planning, and execution.
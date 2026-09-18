---
name: reviewer
description: Perform evidence-based reviews of software projects across functionality, architecture, UI/UX, animation, 3D, performance, SEO, accessibility, security, maintainability, and implementation quality.
version: 0.1.0
---

# Reviewer

## Purpose

The Reviewer skill provides a structured method for evaluating an existing implementation.

The reviewer should determine:

- what was requested;
- what was actually implemented;
- whether the implementation satisfies the requirement;
- what is demonstrably wrong;
- what is likely problematic;
- what remains unverified;
- what should be improved.

The reviewer is not a replacement for testing.

The reviewer is not a subjective opinion generator.

The objective is:

> **Produce actionable findings supported by evidence, while clearly separating confirmed problems from recommendations and unverified concerns.**

---

# Core Principle

## Evidence Before Judgment

Do not report:

```text
"This code is bad."
"This UI is terrible."
"This is insecure."
"This will be slow."
```

without explaining why.

Prefer:

```text
Finding
↓
Evidence
↓
Impact
↓
Recommendation
↓
Verification status
```

---

# Review Workflow

Use:

```text
UNDERSTAND
↓
DISCOVER
↓
DEFINE REVIEW SCOPE
↓
INSPECT
↓
TEST
↓
CLASSIFY FINDINGS
↓
PRIORITIZE
↓
REPORT
```

A review should be proportional to the request.

---

# Review Scope

Determine whether the review is:

```text
TARGETED
```

or:

```text
BROAD
```

Examples:

```text
"Review this authentication implementation."
→ security-focused review

"Review the homepage."
→ UI/UX/content/performance review

"Review the entire application."
→ broader engineering review
```

Do not perform an unrelated full audit when the user requested a narrow review.

---

# Discover Before Asking

Inspect the repository before asking questions.

Determine:

- framework;
- architecture;
- package manager;
- build system;
- relevant dependencies;
- testing setup;
- rendering system;
- deployment configuration;
- existing conventions.

Do not ask for information that can be reliably discovered.

---

# Understand the Intended Outcome

A review requires a comparison between:

```text
INTENDED
vs
ACTUAL
```

Determine intended behavior from:

- user requirements;
- project documentation;
- existing tests;
- specifications;
- established conventions.

Do not invent requirements.

---

# Review Against Requirements

For each important requirement, determine:

```text
SATISFIED
PARTIALLY SATISFIED
NOT SATISFIED
UNVERIFIED
```

This is preferable to vague statements such as:

```text
"Looks mostly correct."
```

---

# Requirement Evidence

For each important requirement, identify evidence such as:

- implementation;
- test;
- rendered output;
- configuration;
- runtime behavior.

Do not mark a requirement satisfied solely because a corresponding function exists.

---

# Review Dimensions

Depending on scope, review:

```text
FUNCTIONALITY
ARCHITECTURE
CODE QUALITY
PERFORMANCE
UI/UX
ANIMATION
3D
CONTENT
SEO
ACCESSIBILITY
SECURITY
TESTING
MAINTAINABILITY
DOCUMENTATION
```

Only include dimensions relevant to the project and request.

---

# Functionality Review

Inspect:

- expected behavior;
- edge cases;
- error states;
- state transitions;
- validation;
- user flows;
- integration behavior.

Ask:

```text
Does it actually work?
```

Do not equate successful compilation with functional correctness.

---

# Edge Cases

Consider relevant cases such as:

```text
empty input
invalid input
missing data
duplicate data
network failure
slow network
unauthorized access
expired session
large input
mobile viewport
unexpected state
```

Do not test arbitrary edge cases unrelated to the system.

---

# Error Handling

Review whether failures are:

- detected;
- handled;
- communicated;
- recoverable where appropriate.

Avoid swallowing errors silently.

---

# Architecture Review

Inspect:

- module boundaries;
- dependency direction;
- separation of concerns;
- coupling;
- state ownership;
- data flow;
- extensibility.

Do not demand a particular architecture merely because it is familiar.

---

# Architecture Tradeoffs

A design may be valid despite not being the reviewer's preferred architecture.

Only report architectural concerns when there is a substantive impact such as:

- excessive coupling;
- duplicated business logic;
- difficult testing;
- significant maintenance burden;
- clear scalability constraints.

---

# Code Quality

Review:

- clarity;
- naming;
- duplication;
- complexity;
- dead code;
- error handling;
- consistency.

Do not criticize harmless stylistic differences as defects.

---

# Complexity

Identify:

- unnecessarily nested logic;
- overly large functions;
- tangled state;
- complicated control flow;
- duplicated transformations.

Complexity becomes a finding when it materially affects:

- correctness;
- maintenance;
- testing;
- performance.

---

# Duplication

Repeated code is not automatically a problem.

Determine whether duplication:

- creates inconsistent behavior;
- makes fixes harder;
- should evolve together.

Do not recommend abstraction merely to reduce line count.

---

# Dependencies

Review:

- unnecessary dependencies;
- duplicated libraries;
- outdated security-sensitive packages;
- excessive framework overlap.

Do not recommend replacing dependencies without understanding their role.

---

# Performance Review

Where performance is relevant, inspect:

- rendering;
- bundle size;
- network requests;
- asset sizes;
- API calls;
- database queries;
- memory usage;
- expensive computation.

Prefer measurement over speculation.

---

# Performance Evidence

Classify performance observations as:

```text
MEASURED
OBSERVED
INFERRED
POSSIBLE
```

Example:

```text
MEASURED:
Production bundle increased by 800 KB.

INFERRED:
The newly introduced dependency contributes significantly to initial JavaScript size.
```

Do not report inferred behavior as measured.

---

# Frontend Performance

Inspect:

- unnecessary rendering;
- large client bundles;
- heavy dependencies;
- image loading;
- font loading;
- long tasks;
- unnecessary effects;
- large DOM structures.

Use profiling or build analysis when available.

---

# Backend Performance

Inspect:

- repeated queries;
- N+1 patterns;
- expensive operations;
- missing pagination;
- oversized responses;
- unnecessary network calls.

Do not assume a query is slow without evidence when measurement is available.

---

# UI/UX Review

When reviewing UI, inspect:

- hierarchy;
- layout;
- consistency;
- readability;
- navigation;
- interaction;
- responsiveness;
- feedback;
- empty states;
- error states.

Do not reduce UI review to color preference.

---

# Visual Hierarchy

Determine whether users can identify:

```text
primary action
primary information
secondary information
supporting information
```

A visually attractive page can still have poor hierarchy.

---

# Interaction Review

Check:

- discoverability;
- feedback;
- loading states;
- disabled states;
- error states;
- confirmation;
- keyboard behavior where relevant.

Do not report subjective preferences as objective defects.

---

# Responsive Review

Inspect relevant viewport sizes.

Consider:

- overflow;
- clipping;
- unreadable text;
- broken navigation;
- inaccessible controls;
- layout collapse;
- excessive spacing.

Do not assume desktop correctness implies mobile correctness.

---

# Animation Review

When animation is relevant, inspect:

- purpose;
- timing;
- easing;
- consistency;
- responsiveness;
- reduced motion;
- performance.

Animation should support communication rather than obstruct it.

---

# Animation Problems

Potential findings include:

- excessive motion;
- inconsistent timing;
- distracting loops;
- motion that blocks interaction;
- motion that creates poor accessibility;
- expensive animation.

Do not call an animation bad simply because you would design it differently.

---

# 3D Review

When 3D is present, inspect:

- scene structure;
- camera;
- assets;
- loading;
- performance;
- interaction;
- responsive behavior;
- fallback;
- cleanup.

Do not evaluate 3D solely by visual complexity.

---

# Scroll World / Fly-by Review

When reviewing scroll-driven spatial experiences, inspect:

- scroll-to-progress mapping;
- camera continuity;
- scene transitions;
- mobile behavior;
- scroll hijacking;
- reduced motion;
- content synchronization;
- performance.

Use `scroll-world-flyby` for specialized methodology.

---

# Content Review

Inspect:

- clarity;
- hierarchy;
- repetition;
- terminology;
- CTA clarity;
- factual consistency;
- readability.

Do not rewrite content merely to impose a preferred writing style.

---

# SEO Review

When SEO is in scope, inspect:

- titles;
- descriptions;
- headings;
- canonical URLs;
- robots directives;
- sitemap;
- internal links;
- structured data;
- rendered content;
- mobile behavior.

Do not promise ranking outcomes.

---

# Accessibility Review

Inspect:

- semantic HTML;
- keyboard navigation;
- focus behavior;
- labels;
- contrast where measurable;
- alternative text;
- reduced motion;
- screen-reader-relevant structure.

Do not claim complete accessibility compliance without appropriate testing.

---

# Accessibility Evidence

Distinguish:

```text
CODE-OBSERVED
RUNTIME-TESTED
VISUALLY-VERIFIED
UNVERIFIED
```

For example:

```text
Keyboard navigation:
Observed focusable controls in source.

Full keyboard flow:
UNVERIFIED because interactive browser testing was unavailable.
```

---

# Security Review

When security is in scope, inspect:

- authentication;
- authorization;
- input validation;
- injection risks;
- secrets;
- sessions;
- cookies;
- API exposure;
- sensitive data;
- dependency risks.

Use the `security` skill for detailed security methodology.

---

# Security Finding Discipline

Distinguish:

```text
CONFIRMED VULNERABILITY
LIKELY SECURITY ISSUE
HARDENING RECOMMENDATION
INFORMATIONAL
```

Do not label theoretical concerns as confirmed vulnerabilities.

---

# Testing Review

Inspect:

- test coverage where relevant;
- meaningful assertions;
- edge cases;
- integration tests;
- regression tests.

Do not equate a high percentage of coverage with comprehensive testing.

---

# Test Quality

Tests should verify behavior rather than implementation details where practical.

A test that merely confirms:

```text
function exists
```

may provide little behavioral confidence.

---

# Build Review

Verify when relevant:

```text
install
build
lint
test
type-check
```

Do not claim a check passed if it was not actually run.

---

# Runtime Review

When runtime access exists, inspect:

- console errors;
- network failures;
- broken interactions;
- rendering;
- unexpected warnings;
- runtime exceptions.

Runtime evidence is particularly valuable for UI-heavy applications.

---

# Visual Review

When visual inspection is available, inspect the actual rendered result.

Review:

- spacing;
- alignment;
- hierarchy;
- responsive layout;
- animation;
- visual consistency;
- 3D composition.

Do not claim visual verification from source code alone.

---

# Review Without Browser Access

If visual inspection is unavailable:

```text
Visual correctness: UNVERIFIED.
```

You may still inspect:

- source;
- styles;
- component structure;
- tests;
- configuration.

Do not convert code-level confidence into visual certainty.

---

# Finding Structure

Every meaningful finding should contain:

```text
ID
SEVERITY
STATUS
AREA
LOCATION
EVIDENCE
PROBLEM
IMPACT
RECOMMENDATION
VERIFICATION
```

---

# Finding ID

Use stable identifiers such as:

```text
REV-001
REV-002
REV-003
```

This allows findings to be referenced during follow-up work.

---

# Severity

Use:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

Severity should reflect the consequence and likelihood of the problem.

---

# Severity Guidelines

## CRITICAL

A severe issue affecting core functionality, major security exposure, severe data integrity, or a similarly consequential failure.

## HIGH

A significant problem that materially affects functionality, security, usability, performance, or maintainability.

## MEDIUM

A meaningful issue with moderate impact.

## LOW

A minor issue, cleanup opportunity, or localized improvement.

Do not assign severity merely because something is technically imperfect.

---

# Status

Use:

```text
CONFIRMED
LIKELY
RECOMMENDATION
INFORMATIONAL
UNVERIFIED
```

---

# Area

Examples:

```text
FUNCTIONALITY
SECURITY
PERFORMANCE
UI
UX
ACCESSIBILITY
SEO
ARCHITECTURE
CODE
3D
ANIMATION
CONTENT
TESTING
```

---

# Location

Identify where the finding occurs.

Examples:

```text
src/auth/login.ts:42
src/components/Hero.tsx
homepage / hero section
API /users/:id
```

Do not provide vague locations such as:

```text
somewhere in the frontend
```

when a precise location is available.

---

# Evidence

Evidence may include:

- source code;
- configuration;
- test output;
- runtime behavior;
- browser inspection;
- performance measurement;
- dependency information.

Quote only the minimum necessary code.

---

# Problem

Describe what is wrong without exaggeration.

Prefer:

> The API checks authentication but does not verify ownership of the requested document.

over:

> The API is completely insecure.

---

# Impact

Explain the practical consequence.

Examples:

```text
Users may access resources belonging to other accounts.

The initial JavaScript payload increases substantially.

The CTA becomes difficult to identify on mobile.

The page may fail when JavaScript initialization is delayed.
```

---

# Recommendation

Give a practical remediation.

A recommendation should be:

- specific;
- proportional;
- compatible with the existing architecture where possible.

---

# Verification

State whether the finding was:

```text
verified
partially verified
not verified
```

Example:

```text
Verified by reproducing unauthorized object access.
```

or:

```text
Not verified because a production environment was unavailable.
```

---

# Finding Example

```text
REV-001

Severity: HIGH
Status: CONFIRMED
Area: SECURITY
Location: GET /api/orders/:id

Evidence:
The endpoint retrieves an order using the supplied ID but does not verify ownership.

Problem:
An authenticated user may request another user's order.

Impact:
Potential unauthorized access to private order information.

Recommendation:
Enforce object-level authorization before returning the resource.

Verification:
Unauthorized object access reproduced in the test environment.
```

---

# Recommendation Example

```text
REV-002

Severity: MEDIUM
Status: RECOMMENDATION
Area: PERFORMANCE
Location: src/pages/dashboard.tsx

Evidence:
The dashboard imports a large charting module during initial page load.

Problem:
The charting functionality is not required before the dashboard becomes interactive.

Impact:
Potentially larger initial JavaScript payload.

Recommendation:
Consider route-level or component-level lazy loading.

Verification:
Bundle impact should be measured after implementation.
```

Notice that the recommendation does not claim a performance improvement before measurement.

---

# Confirmed vs Recommendation

A review must distinguish:

```text
something is wrong
```

from:

```text
something could be improved
```

Do not present every improvement opportunity as a defect.

---

# Subjective Findings

Subjective design observations should be explicitly framed as such.

Example:

```text
Design observation:
The hero contains multiple competing visual focal points.

Potential impact:
The primary CTA may receive less visual emphasis.

Recommendation:
Consider reducing secondary visual competition.
```

Do not state:

> The design is objectively bad.

---

# Challenge During Review

Challenge requirements when the review reveals a substantive problem.

Examples:

```text
requested implementation
↓
creates significant security risk
```

or:

```text
requested animation
↓
causes major usability/accessibility problem
```

The reviewer should explain the issue rather than silently changing the requirement.

---

# Do Not Challenge Preferences

Do not challenge:

- color preference;
- aesthetic preference;
- animation style;
- typography preference;

unless there is a concrete usability, accessibility, performance, or technical consequence.

---

# Review Prioritization

Prioritize findings by:

```text
impact
+
evidence
+
scope
+
likelihood
+
remediation value
```

Do not bury critical issues under dozens of cosmetic observations.

---

# Review Order

A practical order is:

```text
1. Security
2. Data integrity
3. Functional correctness
4. Accessibility
5. Performance
6. Architecture
7. UX
8. Visual polish
9. Minor cleanup
```

This is a review sequence, not a universal importance ranking. Adapt it to the actual project.

---

# False Positives

Before reporting a serious finding, attempt to disprove it.

Check:

- another authorization layer;
- middleware;
- framework behavior;
- inherited configuration;
- validation elsewhere;
- runtime protections.

Do not report a vulnerability based on a single suspicious-looking line if the security control exists elsewhere.

---

# Duplicate Findings

Do not report the same root problem multiple times merely because it appears in several files.

Group related findings when they share the same underlying cause.

---

# Noise Control

A review should not become a list of trivial complaints.

Avoid spending most of the report on:

- formatting;
- minor naming preferences;
- tiny refactors;
- personal style choices.

Prioritize consequential findings.

---

# Review Completeness

A review should state what was actually reviewed.

Example:

```text
Reviewed:
- authentication flow
- API authorization
- session handling
- relevant tests

Not reviewed:
- production infrastructure
- external identity provider configuration
```

This prevents false assumptions about review coverage.

---

# Review Limitations

Explicitly document limitations such as:

```text
No production environment
No browser access
No GPU profiling
No external dependency database
No real user data
```

Limitations should reduce overclaiming, not prevent useful analysis.

---

# Verification Matrix

For broad reviews, summarize:

| Area | Status | Evidence |
|---|---|---|
| Functionality | Verified | Automated + runtime tests |
| Security | Partially verified | Source inspection |
| Performance | Unverified | Profiling unavailable |
| Accessibility | Partially verified | Source inspection |
| Visual | Unverified | Browser unavailable |
| SEO | Verified | Rendered HTML inspection |

Use only statuses supported by actual evidence.

---

# Review Completion

Before finalizing, ask internally:

```text
Did I inspect the relevant implementation?
Did I distinguish facts from assumptions?
Did I verify serious findings?
Did I identify limitations?
Did I prioritize consequential issues?
Did I avoid subjective criticism presented as fact?
Did I provide actionable recommendations?
```

---

# Anti-Patterns

## Generic Code Review

Writing:

> "Improve naming and clean up the code."

without identifying concrete issues.

---

## Style Policing

Treating personal coding preferences as defects.

---

## Severity Inflation

Calling every issue:

```text
CRITICAL
```

---

## Vulnerability Inflation

Calling theoretical concerns confirmed vulnerabilities.

---

## No Evidence

Reporting problems without showing where or why.

---

## No Verification

Claiming a fix works without testing it.

---

## Full Audit by Default

Performing an enormous review when the user requested one small component.

---

## Cosmetic Noise

Filling the review with low-value formatting complaints.

---

## Silent Requirement Changes

Changing the implementation to satisfy the reviewer's preference without informing the user.

---

## Browser Assumption

Claiming visual correctness without actually inspecting the rendered page.

---

## Performance Guessing

Calling code slow without measurement when measurement is available.

---

## Coverage Worship

Assuming high test coverage means the implementation is correct.

---

## Duplicate Findings

Reporting the same underlying problem repeatedly.

---

# Example: Targeted Review

Request:

> Review my login implementation.

Process:

```text
Inspect authentication architecture
↓
Inspect login endpoint
↓
Inspect password handling
↓
Inspect session/token creation
↓
Inspect rate limiting
↓
Inspect error handling
↓
Inspect relevant tests
↓
Run targeted tests
↓
Report findings
```

Do not review unrelated UI components unless they affect the authentication flow.

---

# Example: Homepage Review

Request:

> Review my homepage.

Inspect:

```text
page structure
↓
content hierarchy
↓
UI/UX
↓
responsive behavior
↓
animation
↓
performance
↓
accessibility
↓
SEO
```

If browser access exists, inspect the rendered page.

If not, clearly mark visual findings as limited or unverified.

---

# Example: Full Application Review

Request:

> Review the entire application before release.

Process:

```text
discover architecture
↓
identify critical user flows
↓
review security
↓
review functionality
↓
review data handling
↓
review performance
↓
review accessibility
↓
review UI/UX
↓
review testing
↓
review deployment configuration where available
↓
prioritize findings
↓
produce release review
```

Do not claim production readiness without reviewing the relevant production environment and requirements.

---

# Release Review

For release-oriented reviews, consider:

```text
FUNCTIONALITY
SECURITY
PERFORMANCE
ACCESSIBILITY
RELIABILITY
OBSERVABILITY
DEPLOYMENT
DOCUMENTATION
ROLLBACK
```

Only include areas supported by the actual project.

---

# Final Review Report

A useful final report structure is:

```text
# Review Summary

Scope:
...

Overall implementation status:
...

Critical findings:
...

High findings:
...

Medium findings:
...

Low findings:
...

Unverified areas:
...

Recommended next actions:
...
```

Do not provide an overall numeric score unless the review system explicitly requires one.

A review should communicate evidence and findings rather than collapse the project into an arbitrary number.

---

# Completion Criteria

The Reviewer skill is complete when:

- [ ] review scope is defined;
- [ ] project context was discovered;
- [ ] intended requirements were identified;
- [ ] relevant implementation was inspected;
- [ ] important behavior was tested where practical;
- [ ] findings contain evidence;
- [ ] findings distinguish confirmed problems from recommendations;
- [ ] security findings are appropriately classified;
- [ ] performance claims are evidence-based;
- [ ] visual claims are based on actual visual inspection when available;
- [ ] accessibility claims reflect actual verification;
- [ ] findings have meaningful severity;
- [ ] findings identify locations;
- [ ] recommendations are actionable;
- [ ] duplicate findings are consolidated;
- [ ] subjective observations are clearly distinguished;
- [ ] limitations are documented;
- [ ] unverified areas are explicit;
- [ ] unrelated issues are not allowed to overwhelm the review;
- [ ] no unsupported claims of correctness or readiness are made.

The goal is not:

> **"Find as many problems as possible."**

The goal is:

> **"Determine what is actually wrong, what is uncertain, what matters, and what should happen next."**
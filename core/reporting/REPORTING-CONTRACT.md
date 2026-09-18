# Reporting Contract

**Contract Version:** 0.1.0

---

## 1. Purpose

The Reporting Contract defines how The-Builder communicates the result of its work to the user.

A report is not a transcript of everything the agent did.

It is a concise, evidence-based representation of:

- what was requested;
- what was discovered;
- what was changed;
- what was verified;
- what decisions were made;
- what remains uncertain;
- what remains to be done.

The report must allow the user to understand the actual state of the work without reconstructing it from tool output.

---

# 2. Core Principle

> Report what actually happened, not what was intended to happen.

The agent must distinguish between:

```text
planned
implemented
verified
unverified
blocked
remaining
```

These states must not be conflated.

---

# 3. Reporting Inputs

A report may use:

```text
user request
discovery findings
capability assessment
user decisions
implementation results
verification results
unexpected findings
remaining work
```

Only information supported by the execution should be reported as fact.

---

# 4. Report Objectives

A useful report should answer:

1. What changed?
2. Why was it changed?
3. What was verified?
4. What was not verified?
5. Were there failures or limitations?
6. What decisions affected the implementation?
7. Is anything still required from the user?

---

# 5. Report Status

Use a status appropriate to the actual outcome.

Recommended states:

```text
COMPLETE
PARTIAL
BLOCKED
FAILED
INCONCLUSIVE
```

---

# 6. COMPLETE

Use `COMPLETE` when:

- the agreed implementation scope was completed;
- relevant verification was performed;
- no material unresolved blocker remains.

`COMPLETE` does not mean every possible aspect of the system was tested.

---

# 7. PARTIAL

Use `PARTIAL` when:

- some requested work was completed;
- meaningful work remains;
- or important verification remains incomplete.

Example:

```text
The feature is implemented, but browser verification was unavailable.
```

---

# 8. BLOCKED

Use `BLOCKED` when execution cannot safely or meaningfully continue because of a material constraint.

Examples:

```text
required credentials unavailable
required dependency unavailable
required environment unavailable
ambiguous destructive operation
missing essential user decision
```

---

# 9. FAILED

Use `FAILED` when implementation was attempted but the requested outcome was not achieved.

Include:

```text
cause
evidence
changes already made
verification result
next action
```

---

# 10. INCONCLUSIVE

Use `INCONCLUSIVE` when available evidence is insufficient to establish a reliable result.

Example:

```text
Performance improved in one run but measurements vary significantly.
No stable baseline exists.
```

---

# 11. Standard Report Structure

For implementation tasks, prefer:

```text
Status

What changed

Verification

Decisions

Unverified

Remaining work
```

Additional sections may be included when useful.

---

# 12. Status First

The user should be able to determine the outcome immediately.

Example:

```text
Status: COMPLETE
```

or:

```text
Status: PARTIAL
```

Do not bury the actual outcome at the bottom of a long report.

---

# 13. What Changed

Summarize meaningful changes.

Good:

```text
- Added protected-route middleware.
- Updated session expiration handling.
- Added authorization tests.
```

Avoid:

```text
- Changed line 42.
- Added line 43.
- Modified line 44.
```

The report describes outcomes, not editor mechanics.

---

# 14. Why the Change Was Made

Include rationale when the decision is meaningful.

Example:

```text
Reused the existing session middleware rather than introducing a second authentication mechanism to preserve the current architecture.
```

Do not explain trivial implementation details unnecessarily.

---

# 15. Verification

Report actual checks.

Example:

```text
Verification:
- `npm test` — PASS
- `npm run build` — PASS
- Protected-route integration test — PASS
```

Never claim a check that was not performed.

---

# 16. Verification Evidence

Evidence should be specific enough to support the reported result.

Useful evidence includes:

```text
command output
test results
observable runtime behavior
inspection results
measured metrics
diff inspection
```

Do not overwhelm the user with raw logs unless requested or necessary for debugging.

---

# 17. Decisions

Report consequential implementation decisions.

Examples:

```text
- Reused the existing API client.
- Did not introduce a new dependency.
- Kept the database schema unchanged.
```

Do not list every trivial coding decision.

---

# 18. User Decisions

If implementation followed an explicit user choice, record it when it materially affects the result.

Example:

```text
User decision:
Use the existing animation library instead of adding GSAP.
```

This creates useful traceability without questioning the decision again.

---

# 19. Unverified

Explicitly report important areas that were not verified.

Examples:

```text
Unverified:
- production deployment
- iOS Safari behavior
- visual comparison against the reference design
```

If nothing important remains:

```text
Unverified:
- none
```

---

# 20. Capability Limitations

If verification or execution was constrained by available capabilities, say so.

Example:

```text
The implementation was completed, but visual verification was unavailable because no browser inspection capability was available.
```

Do not hide capability limitations.

---

# 21. Remaining Work

List work that still requires action.

Examples:

```text
Remaining:
- Add production environment variables.
- Run device-level verification.
```

If no remaining work exists:

```text
Remaining:
- none
```

---

# 22. Unexpected Findings

Report unexpected findings when they materially affect the task.

Example:

```text
Finding:
The existing API returns a different error shape than expected.

Action:
Adapted the new client code to the existing response format.
```

---

# 23. Non-Blocking Findings

Do not allow unrelated findings to dominate the report.

Example:

```text
Non-blocking:
An outdated dependency was detected but is outside the requested scope.
```

Mention it only when it is relevant enough for the user to know.

---

# 24. Blockers

A blocker should be explicit.

Weak:

```text
There were some issues.
```

Strong:

```text
Blocked:
The production database credentials required for migration verification were unavailable.
```

---

# 25. Failed Verification

When a verification check fails, report:

```text
check
result
relevant failure
whether the failure was addressed
```

Example:

```text
- `npm test` — FAIL
  - 2 authorization tests fail because the mock session does not contain the new role field.
```

---

# 26. Pre-Existing Failures

If a failure appears unrelated to the current change:

```text
Pre-existing:
The existing snapshot test fails before and after the requested change.
```

Only call a failure pre-existing when there is reasonable evidence.

If uncertain:

```text
The failure may be pre-existing; no baseline result was available.
```

---

# 27. Partial Verification

Do not convert partial verification into a complete claim.

Example:

```text
Status: PARTIAL

Implemented:
- API changes
- validation
- tests

Verified:
- unit tests
- build

Unverified:
- production API integration
```

---

# 28. No False Certainty

Avoid language such as:

```text
Everything works perfectly.
This is fully secure.
This is production-ready.
The code is bug-free.
The animation is guaranteed to be smooth.
```

unless the available evidence genuinely supports the specific claim.

Even then, prefer precise evidence.

---

# 29. Evidence Over Confidence

Prefer:

```text
`npm test` passed with 48 tests and 0 failures.
```

over:

```text
The implementation is definitely correct.
```

---

# 30. Subjective Results

Some tasks involve subjective criteria.

Examples:

```text
modern
premium
beautiful
professional
smooth
clean
```

Do not report subjective preference as objective fact.

Prefer:

```text
The requested visual direction was implemented.
```

Then describe measurable properties where relevant.

---

# 31. User Preference

Do not report a user's subjective choice as a technical defect merely because the agent would choose differently.

Example:

```text
User requested slower animation.
```

If technically valid, implement it.

Report tradeoffs only when they materially affect the result.

---

# 32. Challenge Results

When a requirement was challenged and the user made the final decision, report the decision rather than repeatedly reopening the debate.

Example:

```text
Tradeoff discussed:
The requested dependency increases bundle size.

Decision:
User chose to proceed with the dependency.
```

---

# 33. Recommendations

Recommendations should be distinguishable from completed work.

Example:

```text
Recommended follow-up:
Run a production performance audit after deployment.
```

Do not phrase recommendations as completed actions.

---

# 34. Commands

When useful, include commands that the user can run themselves.

Example:

```bash
npm test
npm run build
```

Do not claim that the user ran a command merely because the agent ran it.

---

# 35. File References

When reporting changes, mention relevant files when useful.

Example:

```text
Changed:
- `src/auth/middleware.ts`
- `src/auth/session.ts`
- `tests/auth.test.ts`
```

For larger changes, summarize by subsystem instead of listing every file.

---

# 36. Diff Summary

When relevant, report a concise diff summary:

```text
3 files changed
1 new test file
1 dependency unchanged
```

Avoid excessive Git statistics unless they help the user.

---

# 37. Commit Reporting

If the agent created a commit, report:

```text
Commit:
<hash> <message>
```

If no commit was created, do not imply one exists.

The-Builder should not create commits merely because implementation finished unless the workflow explicitly authorizes it.

---

# 38. Deployment Reporting

Separate:

```text
implemented
```

from:

```text
deployed
```

and:

```text
deployment verified
```

Example:

```text
Implemented:
- Production configuration.

Deployed:
- No.

Unverified:
- Production environment.
```

---

# 39. Database Reporting

For database work, report:

```text
schema changes
migration status
verification status
rollback considerations
```

Example:

```text
Database:
- Added `role` column.
- Migration created.
- Local migration verified.
- Production migration not run.
```

---

# 40. Security Reporting

Security-related findings should be precise.

Use classifications such as:

```text
CONFIRMED VULNERABILITY
LIKELY ISSUE
HARDENING RECOMMENDATION
INFORMATIONAL
```

Do not inflate a hardening suggestion into a confirmed vulnerability.

---

# 41. Reviewer Findings

For reviewer-oriented tasks, each significant finding should contain:

```text
Severity
Evidence
Problem
Impact
Recommendation
Classification
```

Example:

```text
Severity: HIGH
Classification: CONFIRMED VULNERABILITY

Evidence:
Authorization is checked only on the client.

Problem:
The server accepts the resource request without validating ownership.

Impact:
A user may access resources belonging to another account.

Recommendation:
Enforce authorization server-side.
```

---

# 42. Severity

Severity should describe impact, not emotional importance.

Possible values:

```text
CRITICAL
HIGH
MEDIUM
LOW
INFO
```

Use the project's established severity model when one exists.

---

# 43. Reporting Unknowns

Unknowns should be explicit.

Example:

```text
Unknown:
Production traffic characteristics were not available, so capacity under peak load was not established.
```

Do not fill unknowns with assumptions.

---

# 44. Reporting Assumptions

Important assumptions should be visible.

Example:

```text
Assumption:
The existing API contract is consumed only by this frontend.

If external clients depend on the endpoint, compatibility review is required.
```

---

# 45. Reporting Scope

If the task intentionally excludes an area, state it when useful.

Example:

```text
Out of scope:
- Dependency upgrades.
- Database redesign.
- Production deployment.
```

This prevents ambiguity about what was intentionally left unchanged.

---

# 46. Report Length

Reporting should be proportional to task complexity.

### Trivial task

```text
Changed:
- Fixed homepage typo.

Verified:
- Inspected rendered text.

Status:
COMPLETE
```

### Complex task

Use structured sections covering:

```text
status
changes
decisions
verification
limitations
remaining work
```

Do not produce a large report for a one-line change.

---

# 47. Reporting During Long Tasks

For long-running work, intermediate updates may be appropriate.

Useful progress information:

```text
Discovery complete.
Implementation phase 1 complete.
Verification passed.
Starting phase 2.
```

Avoid narrating every tool call.

---

# 48. Progress vs Final Report

Progress reports communicate:

```text
what is happening
```

Final reports communicate:

```text
what actually happened
```

The final report should correct or supersede earlier expectations where the implementation changed.

---

# 49. Error Reporting

When an error occurs, report:

```text
What failed
Where it failed
Why it appears to have failed
What was attempted
Current state
Next action
```

Avoid hiding errors merely because a workaround eventually succeeded.

---

# 50. Recovery Reporting

If execution recovered from a failure, report it when it materially affects confidence.

Example:

```text
Initial build failed because the required generated type definitions were stale.
Regenerated them and reran the build successfully.
```

This provides useful context without dumping logs.

---

# 51. Contradictions

If the final implementation differs from the original plan because new evidence emerged, report the change.

Example:

```text
Original plan:
Add a new API endpoint.

Updated implementation:
Reused an existing endpoint after discovery showed it already supported the required behavior.
```

---

# 52. Reporting Capability Constraints

If the agent could not perform a requested operation:

```text
Requested:
Verify the animation visually.

Result:
Implementation completed.

Constraint:
No visual inspection capability was available.

Status:
PARTIAL.
```

Never imply the visual verification occurred.

---

# 53. Reporting Tool Failures

A tool failure does not automatically mean the task failed.

Distinguish:

```text
tool failure
```

from:

```text
task failure
```

Example:

```text
Browser tool unavailable.
Source-level verification and automated tests passed.
Visual verification remains unverified.
```

---

# 54. Reporting User Action Required

When the user must perform an action, make it explicit.

Example:

```text
User action required:
Set `DATABASE_URL` in the production environment before deployment.
```

Do not imply the action has already happened.

---

# 55. Recommended Final Template

For normal implementation work:

```text
Status: COMPLETE | PARTIAL | BLOCKED | FAILED | INCONCLUSIVE

## Changed
- ...

## Verification
- ...

## Decisions
- ...

## Unverified
- ...

## Remaining
- ...
```

Omit empty sections when appropriate.

---

# 56. Extended Final Template

For complex work:

```text
Status: ...

## Outcome
...

## Changed
- ...

## Important Decisions
- ...

## Verification
- ...

## Findings
- ...

## Limitations
- ...

## Unverified
- ...

## Remaining Work
- ...

## User Action Required
- ...
```

Use only sections that add useful information.

---

# 57. Reporting Anti-Patterns

## Completion Theater

Declaring success without evidence.

## Log Dumping

Returning raw tool output instead of conclusions.

## Hidden Failure

Failing to mention a relevant failed check.

## Hidden Limitation

Failing to disclose unavailable verification.

## False Precision

Giving exact claims unsupported by evidence.

## Over-Reporting

Listing every trivial implementation detail.

## Under-Reporting

Saying only:

```text
Done.
```

for a complex task.

## Plan Confusion

Reporting intended work as completed work.

## Recommendation Confusion

Reporting future recommendations as completed actions.

## User-Decision Override

Presenting the agent's preference as though it were the user's decision.

---

# 58. Report Quality Criteria

A report is high quality when the user can determine:

```text
WHAT changed
WHY it changed
WHAT was verified
WHAT was not verified
WHAT remains
WHO must act next
```

without reconstructing the execution process.

---

# 59. Completion Criteria

Reporting is complete when:

- [ ] final status is accurate;
- [ ] meaningful changes are summarized;
- [ ] relevant verification is reported;
- [ ] important decisions are recorded;
- [ ] limitations are disclosed;
- [ ] unverified areas are explicit;
- [ ] remaining work is explicit;
- [ ] user actions are explicit when required;
- [ ] no unsupported claim is presented as fact.

---

# 60. Final Principle

The purpose of reporting is not to make the work appear successful.

The purpose is to give the user an accurate model of the current state of the work.

Therefore:

```text
REPORT FACTS
REPORT EVIDENCE
REPORT LIMITATIONS
REPORT DECISIONS
REPORT REMAINING WORK
```

Do not optimize the report for confidence.

Optimize it for **truthful, useful state representation**.
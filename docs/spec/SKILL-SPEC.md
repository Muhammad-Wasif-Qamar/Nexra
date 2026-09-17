# The-Builder Skill Specification

**Version:** 0.5.0  
**Status:** Stable

## Purpose

The canonical skill format defines portable procedural behavior for AI coding agents. A skill teaches a repeatable workflow; it is not a provider-specific prompt, personality file, or tool implementation.

## Canonical discovery format

The installable form is:

```text
skills/<skill-name>/SKILL.md
```

The directory name and front-matter `name` must match exactly.

## Front matter

```yaml
---
name: example-skill
description: Short purpose statement.
version: 0.1.0
---
```

`name` is lowercase and stable. `description` states the job of the skill. `version` uses semantic-versioning style.

## Required behavioral sections

Every canonical skill contains:

1. Purpose
2. Core Principle
3. Scope
4. Discovery
5. Capability Requirements
6. Interaction
7. Challenge Handling
8. Execution Workflow
9. Verification
10. Reporting
11. Completion Criteria

Domain skills may add specialized sections after the shared contract.

## Shared behavioral contract

### Discovery

The agent inspects information it can reliably obtain before asking the user. Discovery is proportional: trivial requests should not trigger a full project audit.

### Capability Requirements

A skill states what capabilities materially affect its work. The current capability states are:

- **FULL** — available and adequate;
- **SUITABLE** — adequate with ordinary limitations;
- **CONSTRAINED** — usable but materially limited;
- **UNSUITABLE** — unavailable or inadequate for the requested outcome.

### Interaction

Questions are reserved for information that is not discoverable, cannot be safely defaulted, and materially changes the outcome.

### Challenge Handling

The agent may surface evidence-backed technical or requirement problems. It does not silently replace a user decision.

### Execution Workflow

Execution is incremental and bounded. The skill should make clear what is changed and where scope ends.

### Verification

The skill defines evidence appropriate to its claims. Verification gaps are reported instead of being converted into confidence.

### Reporting

Reports distinguish changes, evidence, limitations, recommendations, and remaining work.

### Completion Criteria

Completion is a set of observable conditions, not a feeling.

## Evidence classes

Use these when useful:

| Class | Meaning |
|---|---|
| observed | Directly inspected |
| verified | Observed and confirmed by a reproducible check |
| inferred | Reasoned conclusion from evidence |
| assumed | Working assumption not established by evidence |
| unknown | Not established |

## User authority

The agent can recommend, compare, warn, and challenge. It must not silently override a user preference or decision merely because another option is preferred.

## Portability

Canonical skills must not require undocumented provider-specific prompts, hidden paths, or proprietary commands. Host-specific installation belongs in `adapters/`.

## Graceful degradation

If a required capability is unavailable:

1. identify the affected claim or action;
2. choose a safe lower-fidelity method when possible;
3. narrow verification claims;
4. ask the user only when the tradeoff changes a material decision;
5. stop rather than fabricate evidence when no safe path exists.

## Skill boundaries

Avoid duplicate canonical responsibilities. For example, Scroll World and Fly-by Animation are represented by the single `scroll-world-flyby` skill.

Foundation skills define reusable behavioral contracts. Domain skills apply the same contract to a specific discipline.

## Anti-patterns

### Prompt dump

A long prompt without decision rules, evidence requirements, or completion criteria.

### Blind execution

Editing before understanding the relevant project and capability context.

### User interrogation

Asking the user for information that inspection could provide.

### Silent override

Changing an explicit user decision without disclosure.

### False capability

Claiming to have viewed, run, tested, benchmarked, or deployed something that was not actually observed.

### Unverified completion

Declaring success without evidence tied to acceptance criteria.

### Provider lock-in

Embedding one host's private conventions in the canonical skill.

## Quality gate

Before release, validate:

- front matter;
- directory/name consistency;
- required behavioral sections;
- balanced Markdown fences;
- no duplicate canonical skills;
- no obsolete split concepts;
- provider portability;
- adapter manifests;
- integration manifests;
- CLI smoke behavior;
- behavioral test fixtures.

## Versioning

Increment:

- patch for wording or non-behavioral corrections;
- minor for additive behavior;
- major for breaking changes to the canonical contract.

## Evolution

The specification should change when repeated implementations reveal a reusable workflow rule. Do not add abstractions merely because they sound comprehensive.

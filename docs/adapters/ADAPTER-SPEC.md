# Adapter Specification

## Purpose

Adapters describe how canonical The-Builder skills are consumed by a host. They are compatibility metadata and installation guidance, not alternate copies of the methodology.

## Manifest

```yaml
adapter_version: 0.5.0
target: example-agent
skill_source: ../../skills
installation:
  mode: external-skills-cli
  command: npx skills add OWNER/REPO --all
claims:
  verified: false
notes:
  - "Replace with host-specific, currently documented behavior."
```

## Required fields

- `adapter_version`
- `target`
- `skill_source`
- `installation`
- `claims`

`claims.verified` is `false` unless this repository contains reproducible evidence for the provider-specific statement.

## Adapter responsibilities

An adapter may document:

- installation/discovery mechanism;
- activation conventions;
- supported host versions;
- tool or hook expectations;
- capability limitations;
- verification notes.

It must not duplicate canonical skill text.

## Provider claims

Do not invent paths, commands, flags, or lifecycle behavior. If a provider's current behavior is uncertain, say so and point the user to its current documentation rather than asserting an unverified detail.

## Validation

Each adapter must contain `adapter.yaml` and `README.md`. Contract tests ensure manifests contain required fields and that provider-specific claims are not marked verified without a corresponding test fixture.

## Adding an adapter

1. Add `adapters/<stable-name>/adapter.yaml`.
2. Add concise installation/discovery guidance in `README.md`.
3. Keep claims conservative.
4. Add a case to `tests/adapters/cases.md`.
5. Run the full validation suite.

# Contributing to The-Builder

## Principles

Contributions should preserve the project's core behavior: discover before asking, assess capabilities honestly, understand intent, challenge substantive problems with evidence, execute incrementally, verify outcomes, and report limitations.

## Adding a skill

Create `skills/<name>/SKILL.md` with YAML front matter containing `name`, `description`, and `version`. Include the canonical sections defined in `docs/spec/SKILL-SPEC.md`. Add behavioral cases under `tests/` and keep the skill provider-agnostic.

## Adapters

Adapters must remain thin. Do not copy the canonical methodology into an adapter. Adapter claims about host behavior must be reproducible or explicitly marked unverified.

## Validation

Run:

```bash
npm run validate
npm test
npm run pack:test
```

Do not submit a change that weakens verification or introduces placeholder content.

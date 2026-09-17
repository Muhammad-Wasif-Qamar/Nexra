# Testing

The-Builder uses layered tests.

## Static validation

`scripts/validate.py` checks:

- canonical skill count and names;
- front matter;
- required sections;
- balanced code fences;
- Markdown heading structure;
- provider lock-in phrases;
- adapter manifests;
- integration registry;
- plugin/connector manifests;
- documentation links and local references;
- CLI/package invariants.

## Behavioral contract tests

`tests/*/cases.md` contains scenarios describing expected agent behavior. These are not exact-output tests. The important property is the decision behavior.

## CLI smoke tests

The test suite invokes `list`, `doctor`, `validate`, and `test` through Node where appropriate.

## Release gate

A release is considered ready only after:

```bash
python3 scripts/validate.py
python3 scripts/test_suite.py
npm test
npm run validate
node cli/bin/the-builder.js doctor
```

All must exit successfully.

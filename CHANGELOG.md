# Changelog

All notable changes to Nexra are documented here.

The changelog follows a release-oriented format. Historical releases retain the project identity and package naming that existed at the time of release.

---

## 0.1.0 — Nexra

### Project Identity

- Renamed the project from **The-Builder** to **Nexra**.
- Renamed the CLI entry point to `nexra`.
- Updated repository, documentation, tests, configuration, and package references to the Nexra identity.
- Renamed the installation state directory from `.the-builder` to `.nexra`.
- Renamed the workflow asset from `the-builder.svg` to `nexra.svg`.

### Version Normalization

- Established `0.1.0` as the current Nexra release baseline.
- Normalized adapter versions to `0.1.0`.
- Normalized integration registry, plugin, and connector versions to `0.1.0`.
- Preserved the historical `0.5.0` release under the previous project identity.

### Skill Architecture

- Maintained the canonical set of 15 Nexra skills.
- Maintained seven foundation skills:
  - `project-discovery`
  - `capability-assessment`
  - `interaction`
  - `challenge`
  - `execution`
  - `verification`
  - `reporting`
- Maintained eight domain skills:
  - `ui-ux-design`
  - `animation-design`
  - `3d-web-design`
  - `scroll-world-flyby`
  - `content-code-optimization`
  - `seo`
  - `security`
  - `reviewer`
- Kept `scroll-world-flyby` as a unified skill for spatial scroll and fly-by experiences.
- Kept `content-code-optimization` as a unified skill covering content and code optimization.
- Preserved the separation between skills, core contracts, integrations, and adapters.

### CLI

- Renamed the CLI command from the previous project identity to `nexra`.
- Updated package metadata and executable configuration.
- Updated CLI installation paths and manifest naming for Nexra.
- Updated CLI repository checks and installation state handling.
- Preserved project and global installation support.
- Preserved selective-skill and all-skill installation modes.
- Preserved environment and coding-agent detection.

### Validation

- Updated repository validation for Nexra paths, package metadata, and naming.
- Updated behavioral and contract tests for the Nexra identity.
- Verified the canonical 15-skill structure.
- Verified adapter and integration registries.
- Verified CLI smoke tests and installation behavior.

---

## 0.5.0 — The-Builder

> Historical release under the previous project identity.

### CLI

- Added the interactive `npx @wasif-qamar/the-builder` installer.
- Added automatic environment and coding-agent executable detection.
- Added project and global installation scopes.
- Added all-skill and selective-skill installation modes.
- Added installation manifests and post-install `doctor` checks.

### Packaging

- Made the npm package publishable.
- Configured the packaged files for npm distribution.

### Validation

- Fixed repository validation with a populated `.gitignore`.

---

## Changelog Guidelines

Future entries should:

- use the actual release version;
- describe user-visible or architecturally meaningful changes;
- preserve historical project identities;
- distinguish fixes, features, architecture changes, and breaking changes;
- avoid claiming capabilities that were not implemented or verified;
- avoid rewriting historical entries to match current naming.

Recommended categories include:

```text
Added
Changed
Fixed
Removed
Security
Documentation
Architecture
CLI
```

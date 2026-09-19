# Nexra Documentation

Nexra is a capability-aware, user-driven skill system for AI coding agents.

This directory contains the documentation that explains Nexra's architecture,
contracts, integrations, testing model, and development conventions.

## Documentation

### Architecture

- [`architecture.md`](./architecture.md) — Nexra's repository architecture,
  execution flow, component boundaries, and relationship between skills,
  adapters, integrations, and the CLI.

### Contracts

- [`spec/SKILL-SPEC.md`](./spec/SKILL-SPEC.md) — canonical skill contract and
  requirements for defining Nexra skills.
- [`adapters/ADAPTER-SPEC.md`](./adapters/ADAPTER-SPEC.md) — host adapter
  contract for integrating Nexra with AI coding agents.

### Testing

- [`testing.md`](./testing.md) — validation philosophy, test layers,
  behavioral checks, contract validation, and release verification.

## Repository Documentation

Additional documentation is maintained alongside the components it describes:

- [`../skills/README.md`](../skills/README.md) — canonical Nexra skill
  collection and skill organization.
- [`../adapters/README.md`](../adapters/README.md) — supported AI coding-agent
  adapters and adapter architecture.
- [`../integrations/README.md`](../integrations/README.md) — integrations,
  plugins, connectors, and capability boundaries.
- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — contribution and development
  guidelines.
- [`../CHANGELOG.md`](../CHANGELOG.md) — release history and notable changes.

## Documentation Principles

Nexra separates **behavior**, **contracts**, and **documentation**:

- `skills/` contains the canonical skill behavior.
- `core/` contains shared orchestration and supporting contracts.
- `adapters/` contains agent-specific installation and adaptation logic.
- `integrations/` describes external capabilities and access mechanisms.
- `cli/` contains the Nexra command-line interface.
- `docs/` explains the architecture, contracts, and development model.

Documentation describes the system; it does not replace the executable
contracts or canonical skill definitions.

When documentation conflicts with an implementation or canonical contract,
the relevant canonical contract and validated implementation take precedence.
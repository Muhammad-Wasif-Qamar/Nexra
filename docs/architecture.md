# Architecture

```text
User request
    │
    ▼
Project Discovery ──► Capability Assessment
    │                       │
    └──────────┬────────────┘
               ▼
          Interaction
               │
        material problem?
          /           \
        yes            no
         ▼              │
     Challenge          │
         │              │
         └──────┬───────┘
                ▼
              Plan
                │
                ▼
            Execution
                │
                ▼
           Verification
                │
                ▼
             Reporting
                │
                ▼
             Iterate
```

## Layers

### `skills/`

Canonical, installable methodology. Every skill follows the same behavioral contract.

### `core/`

Supporting contracts for orchestration, registries, execution state, verification evidence, and reporting. It does not contain duplicate installable skill definitions.

### `adapters/`

Thin host-specific metadata. Adapters do not fork the canonical methodology.

### `integrations/`

Capability contracts. Plugins describe an action/tool surface; connectors describe a resource or transport surface.

### `cli/`

Local repository utilities for listing, diagnosis, validation, and tests. It is not a replacement for a provider's agent runtime.

### `tests/`

Dependency-light contract and behavioral fixtures. Tests validate structural invariants and important behaviors rather than exact prose.

## Design constraint

The core system must remain useful if any particular provider disappears or changes its installation mechanism. Provider assumptions therefore stay outside canonical skills.

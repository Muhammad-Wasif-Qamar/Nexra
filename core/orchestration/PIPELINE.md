# Adaptive Builder Pipeline

## Pipeline

```text
REQUEST
  ↓
DISCOVER
  ↓
ASSESS CAPABILITIES
  ↓
UNDERSTAND INTENT
  ↓
CHALLENGE MATERIAL PROBLEMS (only when present)
  ↓
PLAN
  ↓
EXECUTE
  ↓
VERIFY
  ↓
REPORT
  ↓
ITERATE IF NEEDED
```

## Adaptive behavior

The pipeline is a set of gates, not a mandatory interview.

- A one-line typo may need only discovery of the target and a quick verification.
- A redesign may require project discovery, capability assessment, interaction, implementation, and visual verification.
- A security review may require deeper trust-boundary analysis and targeted tests.
- A blocked visual task should stop or degrade rather than claim visual success.

## Gate rules

### Discover

Collect facts that can affect implementation.

### Assess

Classify material capability requirements.

### Understand

Separate explicit requirements, goals, constraints, preferences, and unknowns.

### Challenge

Invoke only for material, evidence-backed conflicts or risks.

### Plan

State bounded changes, acceptance criteria, and verification methods.

### Execute

Make incremental changes and check risky boundaries.

### Verify

Collect evidence per acceptance criterion.

### Report

State result, evidence, limits, and next action.

## Authority

The user retains final authority over subjective and tradeoff decisions unless a requested action is impossible, unsafe, or outside authorization.

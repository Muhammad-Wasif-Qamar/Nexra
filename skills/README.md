# Nexra Skills

> Canonical, agent-agnostic methodologies for AI coding agents.

Nexra skills define how an AI coding agent should approach a class of work. Skills describe methodology and behavior; they do not themselves provide external tools or capabilities.

## Canonical Skills

### Foundation

- `project-discovery` — Inspect and understand the existing project before making changes.
- `capability-assessment` — Determine whether the available environment can perform the requested work.
- `interaction` — Manage clarification, communication, and user intent.
- `challenge` — Identify weak assumptions, contradictions, and substantive technical problems.
- `execution` — Carry out approved implementation incrementally and safely.
- `verification` — Verify that requested work actually happened and behaves as expected.
- `reporting` — Report changes, evidence, limitations, and remaining issues accurately.

### Domain

- `ui-ux-design` — Interface design, interaction, accessibility, and visual hierarchy.
- `animation-design` — Motion, transitions, micro-interactions, and animation systems.
- `3d-web-design` — 3D web experiences with attention to performance and usability.
- `scroll-world-flyby` — Scroll-driven world experiences and cinematic fly-by transitions.
- `content-code-optimization` — Content quality and code performance, efficiency, and maintainability.
- `seo` — Search discoverability, technical SEO, metadata, structure, and content signals.
- `security` — Security analysis, hardening, and security-boundary reasoning.
- `reviewer` — Structured technical review using evidence, severity, impact, recommendations, and confidence.

## Capability States

Nexra distinguishes methodology from capability. Available capabilities are classified as:

- `FULL` — Required capability is directly available.
- `SUITABLE` — An appropriate alternative capability is available.
- `CONSTRAINED` — The capability exists but has meaningful limitations.
- `UNSUITABLE` — The environment cannot reliably perform the required operation.

## Skill Structure

Each canonical skill is stored in its own directory with a `SKILL.md` file:

```text
skills/
├── project-discovery/SKILL.md
├── capability-assessment/SKILL.md
├── interaction/SKILL.md
├── challenge/SKILL.md
├── execution/SKILL.md
├── verification/SKILL.md
├── reporting/SKILL.md
├── ui-ux-design/SKILL.md
├── animation-design/SKILL.md
├── 3d-web-design/SKILL.md
├── scroll-world-flyby/SKILL.md
├── content-code-optimization/SKILL.md
├── seo/SKILL.md
├── security/SKILL.md
└── reviewer/SKILL.md
```

## Related Documentation

- [`../README.md`](../README.md) — Nexra overview and getting started.
- [`../docs/spec/SKILL-SPEC.md`](../docs/spec/SKILL-SPEC.md) — Skill specification.
- [`../docs/architecture.md`](../docs/architecture.md) — System architecture.
- [`../docs/testing.md`](../docs/testing.md) — Testing and validation.
- [`../adapters/README.md`](../adapters/README.md) — Agent adapters.
- [`../integrations/README.md`](../integrations/README.md) — Integrations and capabilities.

## Validation

From the repository root:

```bash
npm run validate
npm test
```

Both commands should pass before submitting changes.

## License

Nexra is released under the MIT License.

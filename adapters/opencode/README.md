# Opencode adapter

The `opencode` adapter maps The-Builder's canonical `SKILL.md` directories to the documented Agent Skills discovery locations for Opencode.

## Installation targets

- Project: `.opencode/skills/`
- Global: `~/.config/opencode/skills/`

The CLI only writes these skill directories. It does not rewrite unrelated provider configuration.

## Evidence

Documented discovery source: https://opencode.ai/docs/skills

## Compatibility

The canonical skills use the portable Agent Skills `SKILL.md` shape. Provider-specific features should only be added when explicitly supported by this adapter.

# Kiro adapter

The `kiro` adapter maps The-Builder's canonical `SKILL.md` directories to the documented Agent Skills discovery locations for Kiro.

## Installation targets

- Project: `.kiro/skills/`
- Global: `~/.kiro/skills/`

The CLI only writes these skill directories. It does not rewrite unrelated provider configuration.

## Evidence

Documented discovery source: https://kiro.dev/docs/powers/create/

## Compatibility

The canonical skills use the portable Agent Skills `SKILL.md` shape. Provider-specific features should only be added when explicitly supported by this adapter.

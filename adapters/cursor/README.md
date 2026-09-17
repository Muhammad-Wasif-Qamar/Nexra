# Cursor adapter

The `cursor` adapter maps The-Builder's canonical `SKILL.md` directories to the documented Agent Skills discovery locations for Cursor.

## Installation targets

- Project: `.cursor/skills/`
- Global: `~/.cursor/skills/`

The CLI only writes these skill directories. It does not rewrite unrelated provider configuration.

## Evidence

Documented discovery source: https://prod.cursor.com/docs/skills

## Compatibility

The canonical skills use the portable Agent Skills `SKILL.md` shape. Provider-specific features should only be added when explicitly supported by this adapter.

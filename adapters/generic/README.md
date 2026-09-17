# Generic adapter

The `generic` adapter maps The-Builder's canonical `SKILL.md` directories to the documented Agent Skills discovery locations for Generic.

## Installation targets

- Project: `.agents/skills/`
- Global: `~/.agents/skills/`

The CLI only writes these skill directories. It does not rewrite unrelated provider configuration.

## Evidence

Documented discovery source: https://agentskills.io/

## Compatibility

The canonical skills use the portable Agent Skills `SKILL.md` shape. Provider-specific features should only be added when explicitly supported by this adapter.

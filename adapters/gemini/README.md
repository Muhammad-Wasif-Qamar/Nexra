# Gemini adapter

The `gemini` adapter maps The-Builder's canonical `SKILL.md` directories to the documented Agent Skills discovery locations for Gemini.

## Installation targets

- Project: `.gemini/skills/`
- Global: `~/.gemini/skills/`

The CLI only writes these skill directories. It does not rewrite unrelated provider configuration.

## Evidence

Documented discovery source: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md

## Compatibility

The canonical skills use the portable Agent Skills `SKILL.md` shape. Provider-specific features should only be added when explicitly supported by this adapter.

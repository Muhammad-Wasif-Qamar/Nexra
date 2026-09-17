# Github Copilot adapter

The `github-copilot` adapter maps The-Builder's canonical `SKILL.md` directories to the documented Agent Skills discovery locations for Github Copilot.

## Installation targets

- Project: `.github/skills/`
- Global: `~/.copilot/skills/`

The CLI only writes these skill directories. It does not rewrite unrelated provider configuration.

## Evidence

Documented discovery source: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills

## Compatibility

The canonical skills use the portable Agent Skills `SKILL.md` shape. Provider-specific features should only be added when explicitly supported by this adapter.

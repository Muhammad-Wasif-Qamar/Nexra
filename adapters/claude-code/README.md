# Claude Code adapter

The `claude-code` adapter maps The-Builder's canonical `SKILL.md` directories to the documented Agent Skills discovery locations for Claude Code.

## Installation targets

- Project: `.claude/skills/`
- Global: `~/.claude/skills/`

The CLI only writes these skill directories. It does not rewrite unrelated provider configuration.

## Evidence

Documented discovery source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

## Compatibility

The canonical skills use the portable Agent Skills `SKILL.md` shape. Provider-specific features should only be added when explicitly supported by this adapter.

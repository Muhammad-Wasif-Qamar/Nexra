# Openhands adapter

This adapter is intentionally conservative.

## Installation behavior

No native path is asserted. The installer falls back to `.agents/skills/` and records the adapter as unverified.

The CLI does not invent a provider-specific path or modify unknown configuration files.

## Status

Native skill discovery for this host is not verified by this repository. The adapter therefore uses the portable Agent Skills fallback rather than making an unsupported compatibility claim.

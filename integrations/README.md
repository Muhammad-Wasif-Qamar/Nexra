# Integrations

Integrations describe capability and access surfaces; they do not define the
methodology used by canonical skills and they do not grant capabilities by
themselves.

The integration layer is divided into two contracts:

```text
Plugin
  ↓
capability / action surface
  ↓
requires
  ↓
Connector
  ↓
resource / transport / external system
```

## Architectural Boundary

The-Builder separates methodology from capability and access:

| Layer | Responsibility |
|---|---|
| Skill | Defines how the agent should reason, plan, execute, and verify work |
| Plugin | Describes an available capability or action surface |
| Connector | Describes access to a resource, transport, runtime, or external system |
| Adapter | Maps The-Builder capabilities to a specific host agent |

Skills must not assume that a plugin or connector is available.

Capability availability must be assessed at runtime by the consuming system.

## Plugins

A plugin describes a capability or action surface that a host may expose to
The-Builder.

Examples include:

- browser interaction
- filesystem operations
- Git operations
- GitHub operations
- shell execution
- package management
- database operations
- HTTP requests
- image inspection
- test execution
- container execution
- MCP tool/resource interaction

Plugin manifests are descriptive contracts. They do not implement the
capability and do not imply that the host actually provides it.

Where a plugin depends on a specific access surface, its manifest declares the
required connector:

```yaml
requires:
  connectors:
    - github-api
```

This allows capability assessment and orchestration to distinguish between a
declared capability and an actually available capability.

## Connectors

A connector describes access to a resource, transport, runtime, or external
system required by an integration.

Examples include:

- local filesystem
- Git repository
- GitHub API
- browser session
- shell runtime
- npm registry
- PostgreSQL
- HTTP client
- MCP server

Connectors describe access characteristics rather than user-facing
methodology.

A connector may be used by one or more plugins, and a plugin may depend on one
or more connectors.

## Plugin–Connector Relationship

The relationship is expressed explicitly by the plugin manifest.

For example:

```text
github plugin
    ↓ requires
github-api connector
```

```text
filesystem plugin
    ↓ requires
local-filesystem connector
```

```text
test-runner plugin
    ↓ requires
shell-runtime connector
```

This relationship must not be inferred solely from naming conventions.

## Capability Assessment

The presence of a plugin or connector manifest does not establish that the
capability is available.

The consuming agent or host must determine actual availability before relying
on an integration.

Capability states should follow the canonical capability-assessment model:

```text
FULL
SUITABLE
CONSTRAINED
UNSUITABLE
```

If a required integration is unavailable, the agent should follow the
applicable skill's graceful-degradation behavior rather than pretending that
the capability exists.

## Safety Contract

All integrations are host-dependent and authorization-dependent.

Destructive actions require explicit authorization in the consuming system.

Integration manifests must not be interpreted as permission grants.

The host remains responsible for:

- authentication
- authorization
- permission boundaries
- credential handling
- sandboxing
- network policy
- resource limits
- destructive-action controls

Canonical skills must assess actual capability availability before relying on
an integration.

## Implementation Boundary

The YAML files in this directory are descriptive contracts rather than
implementations.

They define:

- identity
- purpose
- dependency relationships
- authorization expectations
- evidence characteristics
- lifecycle characteristics where applicable

They do not implement browser automation, shell execution, filesystem access,
database access, API clients, or other capabilities.

Actual capability implementations belong to the consuming agent, host,
connector implementation, MCP server, plugin system, or other integration
provider.

## Provider Agnosticism

The integration layer must remain provider-agnostic.

A plugin should describe the capability it provides rather than prescribing a
specific vendor or agent unless that dependency is intrinsic to the
capability.

Agent-specific installation and discovery behavior belongs in:

```text
adapters/
```

Canonical methodology belongs in:

```text
skills/
```

Core orchestration and behavioral contracts belong in:

```text
core/
```

Integration capability and access contracts belong in:

```text
integrations/
```

# Integrations

Integrations describe **capability and access surfaces**. They do not define the
methodology used by canonical skills, and they do not grant capabilities by
themselves.

The integration layer is divided into two contracts:

```text
Plugin
  ↓
Capability / Action Surface
  ↓
requires
  ↓
Connector
  ↓
Resource / Transport / External System
```

## Architectural Boundary

Nexra separates methodology from capability and access:

| Layer | Responsibility |
|---|---|
| Skill | Defines how the agent should reason, plan, execute, and verify work |
| Plugin | Describes an available capability or action surface |
| Connector | Describes access to a resource, transport, runtime, or external system |
| Adapter | Maps Nexra behavior to a specific host agent |

Skills must not assume that a plugin or connector is available.

Capability availability must be assessed at runtime by the consuming system
before relying on an integration.

## Plugins

A plugin describes a capability or action surface that a host may expose to
Nexra.

Current plugin categories include:

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

Plugin manifests are **descriptive contracts**.

They:

- identify a capability;
- describe its purpose;
- declare relevant dependencies;
- document evidence and authorization expectations;
- do not implement the capability;
- do not imply that the host currently provides the capability.

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

Current connector categories include:

- local filesystem
- Git repository
- GitHub API
- browser session
- shell runtime
- npm registry
- PostgreSQL
- HTTP client
- MCP server

Connectors describe **access characteristics**, not user-facing methodology.

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

If a dependency is required for a plugin to function, it should be declared
explicitly in the manifest.

## Capability Assessment

The presence of a plugin or connector manifest does **not** establish that the
capability is available.

The consuming agent or host must determine actual availability before relying
on an integration.

Nexra uses the following capability states:

```text
FULL
SUITABLE
CONSTRAINED
UNSUITABLE
```

These states describe the relationship between an available capability and the
specific task being performed.

For example:

```text
Capability exists
        ↓
Capability available
        ↓
Capability suitable for this task
        ↓
Capability actually used
        ↓
Result verified
```

These are separate facts and should not be conflated.

If a required integration is unavailable, the agent should follow the
applicable skill's graceful-degradation behavior rather than pretending that
the capability exists.

## Safety Contract

All integrations are host-dependent and authorization-dependent.

Integration manifests must not be interpreted as permission grants.

The consuming host remains responsible for:

- authentication
- authorization
- permission boundaries
- credential handling
- sandboxing
- network policy
- resource limits
- destructive-action controls

Destructive actions should require the authorization level defined by the
consuming host and applicable workflow.

Nexra should not infer permission merely because an integration exists.

## Implementation Boundary

The YAML files in this directory are **descriptive contracts**, not
implementations.

They define:

- identity
- purpose
- dependency relationships
- authorization expectations
- evidence characteristics
- lifecycle characteristics where applicable

They do not implement:

- browser automation
- shell execution
- filesystem access
- database access
- Git operations
- GitHub API clients
- HTTP clients
- package installation
- MCP servers
- container runtimes

Actual capability implementations belong to the consuming agent, host,
connector implementation, MCP server, plugin system, or other integration
provider.

## Provider Agnosticism

The integration layer should remain provider-agnostic.

A plugin should describe the capability it provides rather than prescribing a
specific vendor or agent unless that dependency is intrinsic to the capability.

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

## Directory Structure

```text
integrations/
├── README.md
├── registry.yaml
├── connectors/
│   ├── browser-session.yaml
│   ├── git-repository.yaml
│   ├── github-api.yaml
│   ├── http-client.yaml
│   ├── local-filesystem.yaml
│   ├── mcp-server.yaml
│   ├── npm-registry.yaml
│   ├── postgresql.yaml
│   └── shell-runtime.yaml
└── plugins/
    ├── browser.yaml
    ├── container.yaml
    ├── database.yaml
    ├── filesystem.yaml
    ├── git.yaml
    ├── github.yaml
    ├── http.yaml
    ├── image-inspection.yaml
    ├── mcp.yaml
    ├── package-manager.yaml
    ├── shell.yaml
    └── test-runner.yaml
```

The registry provides the canonical inventory of integration definitions.

## Adding an Integration

Before adding a plugin or connector:

1. Determine whether an existing integration already covers the capability.
2. Define the integration's responsibility precisely.
3. Identify required dependencies.
4. Document authorization expectations.
5. Provide evidence where provider-specific claims are made.
6. Add the integration to the registry.
7. Add or update behavioral tests.
8. Run repository validation.
9. Review the resulting package contents.

Do not create an integration solely to represent an implementation detail that
belongs inside an existing capability.

## Versioning

Current Nexra integrations use the `0.1.0` release line.

Integration version changes should remain consistent with the repository's
release strategy.

When changing an integration:

- update its version where required;
- update the registry;
- update tests;
- update documentation when behavior changes;
- avoid undocumented version divergence.

## Related Documentation

For the broader Nexra architecture:

```text
docs/architecture.md
```

For skill behavior:

```text
docs/spec/SKILL-SPEC.md
```

For adapter behavior:

```text
docs/adapters/ADAPTER-SPEC.md
```

For behavioral contracts:

```text
core/specification/BEHAVIOR.md
```

For capability assessment:

```text
skills/capability-assessment/SKILL.md
```

For execution:

```text
core/execution/EXECUTION-CONTRACT.md
```

For verification:

```text
core/verification/VERIFICATION-CONTRACT.md
```

## Design Rule

The central rule of the integration layer is:

> **Declaring a capability is not the same as having the capability.**

Nexra should distinguish between what an integration describes, what the host
actually exposes, what is suitable for the current task, what was executed, and
what was successfully verified.

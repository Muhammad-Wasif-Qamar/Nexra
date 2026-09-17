# Integrations

Integrations describe capability surfaces; they do not grant those capabilities.

## Plugins

A plugin is an action/tool surface such as a browser, shell, test runner, or MCP client.

## Connectors

A connector describes access to a resource or transport such as a filesystem, repository, database, or browser session.

## Safety contract

All integrations are host-dependent and authorization-dependent. Destructive actions require explicit authorization in the consuming system. The canonical skills must assess actual availability before relying on an integration.

The YAML files are intentionally descriptive contracts rather than fake implementations.

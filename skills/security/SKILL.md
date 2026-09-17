---
name: security
description: Identify, prioritize, remediate, and verify application security risks using threat modeling, secure defaults, least privilege, and evidence.
version: 0.5.0
---

# Security

## Purpose

Identify, prioritize, remediate, and verify application security risks using threat modeling, secure defaults, least privilege, and evidence.

## Core Principle

Treat security as risk management and verification, not a checklist of scary strings.

## Scope

Authentication, authorization, input handling, secrets, injection, XSS, CSRF, SSRF, file handling, cryptography, logging, configuration, dependencies, supply chain, and abuse controls as applicable.

## Discovery

Map assets, trust boundaries, identities, privileged operations, attacker-controlled inputs, sinks, secrets, storage, network calls, and deployment configuration.

## Capability Requirements

Classify material capabilities as FULL, SUITABLE, CONSTRAINED, or UNSUITABLE from evidence available in the current session. Inspect actual model/agent/tool/environment availability; a documented capability is not evidence that it is callable now. Never claim an observation or verification that the available tools cannot support.

## Interaction

Ask about threat model, exposure, compliance, or authorized testing scope only when material and not discoverable.

## Challenge Handling

Classify findings CONFIRMED VULNERABILITY, LIKELY ISSUE, HARDENING RECOMMENDATION, or INFORMATIONAL. Explain preconditions and impact without sensationalism. Do not perform unauthorized testing.

## Execution Workflow

Threat model → trust boundaries → authz/authn → secrets/config → input-to-sink tracing → dependency/supply chain → least privilege → regression tests → targeted recheck.

## Verification

Verify the specific control changed. Record blind spots; absence of findings is not proof of absence of vulnerabilities.

## Reporting

Report class/severity, evidence, impact, remediation, verification, residual risk.

## Completion Criteria

Findings are actionable, fixes have targeted evidence, and security claims are limited to tested scope.

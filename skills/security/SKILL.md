---
name: security
description: Identify, prevent, and remediate application security weaknesses using evidence-based analysis, secure implementation practices, least privilege, safe defaults, and explicit verification.
version: 0.1.0
---

# Security

## Purpose

The Security skill guides an agent in identifying and addressing security weaknesses in software projects.

Security work must be:

- evidence-based;
- scoped;
- defensive;
- explicit about uncertainty;
- conservative with destructive changes;
- verified where practical.

The objective is not merely to find vulnerabilities.

The objective is:

> **Reduce realistic security risk without unnecessarily breaking functionality, usability, or maintainability.**

---

# Core Principle

## Never Assume Security

Do not assume an application is secure because:

- authentication exists;
- HTTPS is enabled;
- a framework is used;
- a dependency is popular;
- environment variables are used;
- tests pass.

Inspect the actual implementation.

---

# Security Workflow

Use:

```text
DISCOVER
↓
THREAT MODEL
↓
IDENTIFY
↓
CLASSIFY
↓
PRIORITIZE
↓
REMEDIATE
↓
VERIFY
↓
REPORT
```

For a small targeted fix, use only the necessary subset of this workflow.

Do not perform an unnecessary full security audit for a trivial change.

---

# Discover Before Asking

Inspect:

- application architecture;
- authentication;
- authorization;
- sessions;
- cookies;
- tokens;
- API endpoints;
- input validation;
- database access;
- file handling;
- uploads;
- secrets;
- environment configuration;
- dependencies;
- external services;
- deployment configuration;
- logging;
- error handling.

Do not ask the user for information that can be discovered from the project.

---

# Scope

Determine whether the task concerns:

```text
APPLICATION SECURITY
API SECURITY
AUTHENTICATION
AUTHORIZATION
DATA PROTECTION
SECRETS
DEPENDENCIES
INPUT VALIDATION
FILE HANDLING
WEB SECURITY
INFRASTRUCTURE
CONFIGURATION
```

Keep the assessment aligned with the actual scope.

---

# Defensive Scope

Security work should focus on:

- identifying weaknesses;
- reducing exposure;
- validating controls;
- hardening systems;
- fixing vulnerabilities;
- improving defensive architecture.

Do not perform unauthorized offensive activity.

---

# Threat Modeling

Identify:

```text
ASSETS
↓
ACTORS
↓
ENTRY POINTS
↓
TRUST BOUNDARIES
↓
THREATS
↓
CONTROLS
```

Examples of assets:

- user accounts;
- credentials;
- session tokens;
- personal data;
- payment information;
- API keys;
- database records;
- uploaded files;
- administrative functions.

---

# Assets

Determine what would matter if compromised.

Not every endpoint or file has the same security impact.

Prioritize sensitive assets.

---

# Actors

Consider relevant actors such as:

```text
unauthenticated user
authenticated user
privileged user
malicious user
compromised account
external service
administrator
```

Do not invent unrealistic attackers without a reason.

---

# Attack Surface

Inspect:

- public routes;
- API endpoints;
- authentication endpoints;
- upload endpoints;
- webhooks;
- admin functionality;
- database interfaces;
- background jobs;
- third-party integrations.

---

# Trust Boundaries

Identify transitions such as:

```text
browser
↓
API
↓
application
↓
database
```

and:

```text
application
↓
third-party API
```

Security assumptions should not cross trust boundaries automatically.

---

# Authentication

Inspect:

- credential handling;
- password hashing;
- login flow;
- session/token generation;
- session expiration;
- account recovery;
- multi-factor authentication where required;
- brute-force protections;
- authentication error behavior.

---

# Password Storage

Passwords should not be stored as:

```text
plaintext
```

or:

```text
reversible encryption
```

Use an appropriate password hashing mechanism supported by the application's security requirements.

Never log plaintext passwords.

---

# Password Policies

Do not impose arbitrary complexity rules without understanding the application's requirements.

Consider:

- password length;
- breached-password defenses;
- rate limiting;
- secure recovery;
- MFA.

---

# Session Management

Inspect:

- token lifetime;
- session invalidation;
- logout behavior;
- rotation;
- storage;
- cookie attributes.

Do not assume logout is secure merely because the UI redirects to a login page.

---

# Cookies

Where sensitive session cookies are used, consider appropriate:

```text
Secure
HttpOnly
SameSite
```

attributes.

Exact configuration depends on the application's architecture.

---

# Token Storage

Review where authentication tokens are stored.

Consider the security implications of:

```text
localStorage
sessionStorage
cookies
in-memory state
```

Do not recommend one storage mechanism without considering the threat model.

---

# Authorization

Authentication answers:

> Who are you?

Authorization answers:

> What are you allowed to do?

Inspect authorization independently.

---

# Access Control

Verify that authorization is enforced server-side where required.

Do not rely solely on:

```text
hidden buttons
disabled UI
client-side route guards
```

for security-sensitive authorization.

---

# Object-Level Authorization

Inspect APIs that accept identifiers such as:

```text
/user/123
/order/456
/document/789
```

Verify that the requester is actually authorized to access the referenced object.

---

# Privilege Escalation

Consider whether a lower-privileged user can:

- invoke administrative endpoints;
- modify protected resources;
- change their own privilege level;
- access another user's data.

---

# Input Validation

Treat external input as untrusted.

Validate:

- type;
- length;
- format;
- range;
- allowed values;
- structure.

Validation should occur at appropriate trust boundaries.

---

# Output Encoding

Validation and output encoding solve different problems.

For web output, consider context-appropriate encoding to prevent injection.

Do not rely solely on input filtering.

---

# SQL Injection

Use parameterized queries or appropriate ORM/query mechanisms.

Avoid constructing SQL from untrusted strings.

Conceptually unsafe:

```text
"SELECT * FROM users WHERE id = " + userInput
```

Prefer parameterized database operations.

---

# NoSQL Injection

NoSQL databases can also be vulnerable to injection or query manipulation.

Validate and constrain user-controlled query structures.

Do not assume NoSQL means injection-safe.

---

# Command Injection

Do not construct shell commands from untrusted input.

Prefer:

- direct APIs;
- argument arrays;
- strict validation;
- controlled execution.

---

# Path Traversal

When accepting file paths or filenames, prevent access outside the intended directory.

Consider:

- path normalization;
- allowlists;
- generated storage names;
- directory boundaries.

---

# File Uploads

Treat uploaded files as untrusted.

Consider:

- file size;
- file type;
- content validation;
- storage location;
- filename handling;
- execution permissions;
- malware scanning where appropriate.

Do not trust a client-provided MIME type alone.

---

# File Download

Verify authorization before serving private files.

Do not assume an obscure URL is an access-control mechanism.

---

# Cross-Site Scripting

Consider:

```text
stored XSS
reflected XSS
DOM-based XSS
```

Inspect:

- HTML injection;
- unsafe rendering;
- template escaping;
- dangerous DOM APIs;
- rich-text processing.

---

# Rich Text

If users can provide formatted content, determine:

- allowed HTML;
- sanitization;
- embedded URLs;
- images;
- scripts;
- event handlers.

Do not render arbitrary user HTML without appropriate sanitization.

---

# CSRF

Where cookie-based authentication is used, consider cross-site request forgery.

Review:

- SameSite cookies;
- CSRF tokens;
- origin checks;
- request methods;
- application architecture.

Do not add redundant CSRF mechanisms without understanding the existing protection model.

---

# CORS

CORS controls browser cross-origin access.

Do not use:

```text
Access-Control-Allow-Origin: *
```

with sensitive credentialed APIs without understanding the consequences.

Do not confuse CORS with authentication or authorization.

---

# Security Headers

Depending on the application, consider:

- Content-Security-Policy;
- Strict-Transport-Security;
- X-Content-Type-Options;
- Referrer-Policy;
- frame-ancestors / clickjacking protections.

Do not add headers blindly; verify compatibility with the application.

---

# Content Security Policy

CSP can reduce XSS impact.

Before introducing a strict policy, inspect:

- inline scripts;
- dynamic scripts;
- third-party services;
- analytics;
- fonts;
- images;
- WebSocket connections.

Do not deploy a policy that silently breaks core functionality without testing.

---

# Clickjacking

Consider whether sensitive pages can be embedded in another site.

Use appropriate framing protections based on the application's requirements.

---

# Transport Security

Sensitive traffic should use secure transport.

Inspect:

- HTTPS;
- secure cookies;
- TLS termination;
- redirect behavior;
- mixed content.

Do not treat HTTPS as sufficient application security by itself.

---

# Secrets

Never hard-code sensitive secrets in source code.

Look for:

- API keys;
- private keys;
- passwords;
- database credentials;
- signing secrets;
- service tokens.

---

# Environment Variables

Environment variables can help separate configuration from source code.

But they are not automatically secure.

Consider:

- deployment exposure;
- logging;
- build-time embedding;
- client-side exposure.

---

# Client-Side Secrets

Anything shipped to a browser should be considered potentially visible to users.

Do not place server-side secrets in:

```text
frontend environment variables
```

if the build exposes them to the client.

---

# Secret Rotation

If a secret has been exposed, removing it from source code is not sufficient.

Consider:

```text
revoke
rotate
replace
audit usage
```

Do not assume deleting a secret from the latest commit makes it safe.

---

# Git History

Sensitive credentials may remain in:

- old commits;
- branches;
- tags;
- pull requests;
- build artifacts.

If a real secret was committed, treat it as compromised.

---

# Dependency Security

Inspect dependencies for:

- known vulnerabilities;
- outdated security-sensitive packages;
- abandoned packages;
- unnecessary dependencies;
- suspicious installation behavior.

Use current trusted vulnerability data when available.

Do not claim a dependency is secure without checking an appropriate source.

---

# Dependency Updates

Security updates can introduce breaking changes.

Before updating:

- inspect affected packages;
- review compatibility;
- run tests;
- inspect changelogs where appropriate.

Do not blindly upgrade the entire dependency tree during a focused security fix.

---

# Supply Chain

Consider:

- package provenance;
- lockfiles;
- dependency pinning;
- install scripts;
- transitive dependencies.

Do not add unnecessary dependencies to solve a small problem.

---

# API Security

Inspect:

- authentication;
- authorization;
- rate limiting;
- input validation;
- response data;
- error handling;
- request size;
- pagination.

---

# Sensitive Data Exposure

Verify that APIs do not return unnecessary sensitive fields.

Example:

```text
user record
↓
password hash
↓
API response
```

A password hash should generally not be returned to ordinary clients.

---

# Error Handling

Production errors should not unnecessarily expose:

- stack traces;
- credentials;
- internal paths;
- SQL statements;
- infrastructure details;
- secrets.

Detailed diagnostics should remain available through controlled logging.

---

# Logging

Logs should help diagnose security events without exposing sensitive information.

Avoid logging:

- passwords;
- session tokens;
- private keys;
- full payment credentials;
- unnecessary personal data.

---

# Log Injection

If user-controlled data enters logs, consider whether it can manipulate log structure or hide relevant events.

Use structured logging where appropriate.

---

# Rate Limiting

Consider rate limiting for:

- login;
- password recovery;
- expensive API operations;
- public search;
- verification codes;
- resource-intensive endpoints.

Do not apply identical limits to every endpoint.

---

# Denial of Service

Consider resource exhaustion through:

- huge requests;
- huge uploads;
- expensive queries;
- repeated operations;
- excessive concurrency.

Apply appropriate limits.

---

# Request Limits

Consider:

- body size;
- upload size;
- pagination limits;
- query complexity;
- execution timeouts.

Limits should reflect legitimate use cases.

---

# SSRF

Server-side requests to user-controlled URLs can create SSRF risks.

Inspect features such as:

- URL previews;
- webhooks;
- remote image import;
- URL fetching;
- proxy endpoints.

If user-controlled URLs are fetched server-side, validate and restrict destinations appropriately.

---

# Open Redirects

Inspect redirects involving user-controlled URLs.

Avoid blindly redirecting users to arbitrary external destinations.

---

# Webhooks

For incoming webhooks, consider:

- signature verification;
- replay protection;
- request validation;
- idempotency;
- authorization.

Do not trust a webhook merely because it comes from an expected endpoint.

---

# Payment Security

When payments are involved:

- avoid handling sensitive payment credentials unnecessarily;
- use established payment-provider mechanisms;
- verify webhook authenticity;
- verify payment state server-side.

Do not trust a client-provided:

```text
paymentSuccessful: true
```

as proof of payment.

---

# Authentication Provider Integration

For OAuth/social login, inspect:

- redirect URI validation;
- state;
- nonce where applicable;
- token handling;
- callback validation;
- account linking.

Do not implement authentication protocols from scratch when a well-maintained provider library is appropriate.

---

# Authorization and UI

A hidden administrative button is not an authorization control.

The server or trusted backend must enforce security-sensitive permissions.

---

# Security Configuration

Inspect:

- production debug settings;
- default credentials;
- exposed development endpoints;
- test routes;
- verbose errors;
- insecure CORS;
- unnecessary ports/services.

Do not assume development configuration is safe for production.

---

# Database Security

Inspect:

- credentials;
- network exposure;
- least privilege;
- query parameterization;
- backups;
- sensitive data;
- connection security.

Applications should generally use database accounts with only the permissions they need.

---

# Least Privilege

Apply least privilege to:

- users;
- services;
- database accounts;
- API tokens;
- cloud resources;
- filesystem access.

Do not grant broad administrative permissions for convenience.

---

# Secure Defaults

Prefer defaults that fail safely.

Examples:

```text
authentication required
authorization denied by default
secure cookies
validated input
minimal permissions
debug disabled in production
```

Do not rely on users remembering to enable security controls manually.

---

# Security vs Usability

Security controls can affect usability.

Examples:

- aggressive session expiration;
- excessive MFA prompts;
- restrictive file limits;
- strict CSP;
- rate limits.

Consider the actual threat model and user requirements.

Do not maximize security at the expense of all other requirements without justification.

---

# Challenge Conditions

Challenge a security requirement when it:

- creates a false sense of security;
- relies entirely on client-side controls;
- exposes secrets;
- disables important security controls;
- uses fabricated security assumptions;
- introduces unnecessary cryptographic complexity;
- creates disproportionate usability problems without a demonstrated threat.

---

# Cryptography

Do not invent cryptographic algorithms.

Prefer established, well-reviewed primitives and libraries.

Do not:

- roll your own encryption;
- invent hashing algorithms;
- modify standard cryptographic protocols without expertise.

---

# Password Hashing vs Encryption

Passwords generally require one-way password hashing rather than reversible encryption.

Do not recommend encrypting passwords so they can be recovered.

---

# Encryption at Rest

Determine whether sensitive stored data requires encryption based on:

- threat model;
- regulatory requirements;
- infrastructure controls;
- sensitivity.

Do not encrypt every field automatically without considering key management.

---

# Key Management

Encryption is only as secure as its key management.

Consider:

- key storage;
- rotation;
- access control;
- backup;
- revocation.

Never store encryption keys directly beside encrypted data without an appropriate threat model.

---

# Security Findings

Every finding should contain:

```text
ID
SEVERITY
STATUS
EVIDENCE
PROBLEM
IMPACT
RECOMMENDATION
VERIFICATION
```

---

# Finding Status

Distinguish:

```text
CONFIRMED VULNERABILITY
LIKELY SECURITY ISSUE
HARDENING RECOMMENDATION
INFORMATIONAL
```

Do not call a theoretical concern a confirmed vulnerability.

---

# Severity

Use:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

based on:

- exploitability;
- affected assets;
- exposure;
- impact;
- required privileges;
- attack complexity.

Do not assign severity merely because a finding sounds serious.

---

# Evidence

Good evidence includes:

- relevant code path;
- configuration;
- dependency information;
- reproducible behavior;
- security-tool output.

Do not fabricate proof-of-concept results.

---

# Security Verification

After remediation, verify that:

- the vulnerability is addressed;
- legitimate behavior still works;
- authorization remains correct;
- tests pass;
- configuration is valid.

---

# Negative Testing

Where safe and appropriate, test invalid or unauthorized cases.

Examples:

```text
unauthenticated request
unauthorized object access
invalid input
oversized input
invalid token
expired token
```

Keep tests within the authorized project/environment.

---

# Regression Testing

Security fixes can break legitimate workflows.

Check:

- login;
- logout;
- permissions;
- API clients;
- uploads;
- redirects;
- third-party integrations.

---

# Static Analysis

When appropriate, use:

- linters;
- SAST tools;
- dependency scanners;
- secret scanners.

Tool output is evidence, not automatically a confirmed vulnerability.

---

# Dynamic Testing

When appropriate and authorized, test the running application.

Inspect:

- responses;
- headers;
- authentication behavior;
- authorization;
- input handling.

Do not conduct intrusive testing against systems without authorization.

---

# Dependency Scanner Results

Scanner findings should be evaluated for:

- affected package version;
- actual usage;
- vulnerable code path;
- exploitability;
- available remediation.

Do not blindly upgrade every package flagged by a scanner.

---

# Security Testing Boundaries

Do not:

- attack third-party systems;
- exfiltrate real user data;
- destroy data;
- bypass authorization on systems you do not control;
- perform destructive exploitation.

Security testing should remain controlled and authorized.

---

# Example: IDOR

Finding:

```text
GET /api/orders/123
```

The endpoint returns an order based only on the supplied ID.

Evidence:

```text
Authorization check is absent before retrieving the object.
```

Classification:

```text
CONFIRMED VULNERABILITY
```

Recommendation:

```text
Verify that the authenticated principal has access to order 123 before returning it.
```

Verification:

```text
Authorized request succeeds.
Unauthorized request is rejected.
```

---

# Example: Client-Side Authorization

Finding:

```text
Admin button is hidden for non-admin users.
```

This alone is not evidence that the backend is insecure.

Inspect the server-side authorization.

Do not report a vulnerability without evidence that protected operations can actually be performed.

---

# Example: Hard-Coded Secret

Finding:

```text
API key appears in source code.
```

If it is a real secret:

```text
CONFIRMED SECURITY ISSUE
```

Recommended response:

```text
revoke/rotate secret
remove it from source
move configuration to an appropriate secret mechanism
audit repository history
```

---

# Example: Dependency Warning

A scanner reports:

```text
package X has a vulnerability.
```

Do not immediately classify the application as compromised.

Determine:

```text
affected version
↓
installed version
↓
actual package usage
↓
vulnerable code path
↓
available patch
```

Then prioritize appropriately.

---

# Security Documentation

Document:

- security assumptions;
- authentication model;
- authorization model;
- sensitive data;
- secrets handling;
- external trust boundaries;
- known limitations.

Do not document secrets themselves.

---

# Reporting

A security report should distinguish:

```text
CONFIRMED
LIKELY
HARDENING
INFORMATIONAL
```

and include:

```text
severity
evidence
impact
recommendation
verification
```

Example:

```text
SEC-001
Severity: HIGH
Status: CONFIRMED VULNERABILITY

Problem:
The API returns another user's document when its ID is supplied.

Evidence:
Object ownership is not checked before retrieval.

Impact:
Authenticated users may access documents belonging to other users.

Recommendation:
Enforce server-side object-level authorization.

Verification:
Tested authorized and unauthorized object access.
```

---

# Unverified Findings

If a finding could not be verified, say so.

Example:

```text
LIKELY ISSUE

The configuration appears to permit a permissive CORS policy, but production headers were not available for verification.
```

Do not upgrade the claim without evidence.

---

# Anti-Patterns

## Client-Side Security

Treating UI restrictions as authorization.

---

## Security Through Obscurity

Assuming an unknown URL or hidden field provides meaningful access control.

---

## Secret in Frontend

Embedding server credentials in client-delivered code.

---

## Regex as Universal Security

Using a single regex as the complete defense against injection.

---

## Disable Security

Removing authentication, validation, or authorization to make development easier without a controlled environment.

---

## Blind Dependency Upgrades

Updating everything without evaluating compatibility or impact.

---

## Scanner Worship

Treating every scanner result as a confirmed exploitable vulnerability.

---

## False Positives as Facts

Reporting theoretical concerns as confirmed vulnerabilities.

---

## No Verification

Applying a security fix without testing whether it actually closes the issue.

---

## Over-Engineering

Introducing complex cryptography or security infrastructure where a standard mechanism already exists.

---

## Security Theater

Adding visible security mechanisms that do not address the actual threat.

---

# Completion Criteria

The Security skill is complete when:

- [ ] the security scope is understood;
- [ ] relevant architecture was discovered;
- [ ] assets were identified;
- [ ] attack surface was considered;
- [ ] trust boundaries were considered;
- [ ] authentication was reviewed where relevant;
- [ ] authorization was reviewed where relevant;
- [ ] input validation was reviewed where relevant;
- [ ] sensitive data handling was reviewed;
- [ ] secrets were reviewed;
- [ ] dependency risk was considered where relevant;
- [ ] configuration was reviewed where relevant;
- [ ] findings distinguish evidence from inference;
- [ ] vulnerabilities are not overstated;
- [ ] findings are prioritized by realistic impact;
- [ ] remediation is scoped appropriately;
- [ ] security changes preserve legitimate behavior;
- [ ] relevant tests were performed;
- [ ] negative/unauthorized cases were considered where appropriate;
- [ ] unverified findings are explicitly marked;
- [ ] no fabricated security evidence is reported;
- [ ] remaining risks are documented.

The goal is not:

> **"Find something scary."**

The goal is:

> **"Identify realistic security risk, address it proportionately, and provide evidence that the resulting system is better protected."**
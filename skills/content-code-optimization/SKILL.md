---
name: content-code-optimization
description: Analyze and improve website content and application code for clarity, performance, maintainability, efficiency, consistency, and measurable quality without making unjustified changes.
version: 0.1.0
---

# Content + Code Optimization

## Purpose

The Content + Code Optimization skill improves two related but distinct dimensions of a project:

1. **Content optimization**
2. **Code optimization**

The objective is not to change as much as possible.

The objective is:

> **Identify meaningful problems, prioritize them using evidence, make coherent improvements, and verify that the changes actually improve the project.**

Optimization must preserve intended behavior unless a behavior change is explicitly justified and accepted.

---

# Core Principle

## Optimize Evidence, Not Assumptions

Do not optimize something merely because it looks unfamiliar.

First determine:

```text
What exists?
↓
What is the intended behavior?
↓
What is actually problematic?
↓
How significant is the problem?
↓
What change would address it?
↓
How can the result be verified?
```

A shorter implementation is not automatically better.

A more sophisticated implementation is not automatically better.

More content is not automatically better.

---

# Scope

This skill covers:

### Content

- copy clarity;
- readability;
- information hierarchy;
- content structure;
- consistency;
- duplication;
- calls to action;
- metadata/content consistency;
- content density;
- user-facing messaging.

### Code

- performance;
- rendering efficiency;
- network usage;
- API efficiency;
- database efficiency;
- bundle size;
- dependency usage;
- dead code;
- duplication;
- maintainability;
- unnecessary complexity;
- architecture consistency.

This skill does not replace:

- `seo`
- `security`
- `reviewer`
- `ui-ux-design`
- `performance-optimization` if a dedicated skill is later introduced.

Those skills may provide more specialized analysis.

---

# Optimization Workflow

Use:

```text
DISCOVER
    ↓
BASELINE
    ↓
IDENTIFY PROBLEMS
    ↓
PRIORITIZE
    ↓
PROPOSE CHANGES
    ↓
EXECUTE
    ↓
VERIFY
    ↓
REPORT
```

Do not skip discovery merely because the requested change sounds simple.

Do not perform a complete audit when the task only requires a small targeted optimization.

---

# Scope Control

Determine whether the request is:

```text
TARGETED
```

or:

```text
BROAD
```

A targeted request:

> Reduce the homepage JavaScript bundle.

A broad request:

> Optimize the entire website.

For targeted work, avoid unrelated optimization.

For broad work, establish a prioritized optimization plan.

---

# Discover Before Asking

Inspect the project for:

- framework;
- build system;
- package manager;
- content sources;
- routes;
- components;
- data-fetching;
- API calls;
- database queries;
- assets;
- analytics;
- build configuration;
- existing performance tooling;
- existing content structure.

Do not ask the user for information already available in the repository.

---

# Baseline

Before making meaningful optimization changes, establish a baseline where practical.

Examples:

```text
bundle size
build time
page load behavior
network requests
render count
database query time
content length
duplicate content
Lighthouse metrics
```

Not every task requires every metric.

Measure what is relevant to the optimization target.

---

# Baseline Preservation

Record enough information to compare:

```text
before
vs
after
```

This is especially important when performance or measurable behavior is part of the request.

---

# Content Optimization

## Content Goal

Content should help users:

- understand;
- decide;
- navigate;
- act.

Optimize for the actual purpose of the page.

Do not optimize content merely to make it shorter.

---

# Information Hierarchy

Evaluate:

```text
primary message
↓
supporting information
↓
details
↓
secondary information
```

Users should be able to identify the primary purpose without reading every sentence.

---

# Headings

Review:

- hierarchy;
- specificity;
- consistency;
- duplication;
- clarity.

Avoid headings that are technically valid but provide little information.

---

# Paragraphs

Long paragraphs can reduce scanability.

Where appropriate, convert dense content into:

- shorter paragraphs;
- bullets;
- lists;
- subsections;
- tables;
- structured explanations.

Do not fragment content unnecessarily.

---

# Readability

Evaluate:

- sentence complexity;
- jargon;
- unnecessary repetition;
- vague language;
- excessive qualifiers;
- unnecessary passive constructions.

The appropriate reading level depends on the audience.

---

# Audience

Before rewriting content, determine the intended audience from:

- project documentation;
- product positioning;
- existing copy;
- user-provided requirements.

If the audience cannot reasonably be inferred and materially affects the copy, ask.

Do not invent an audience.

---

# Tone

Do not change brand voice merely because another tone seems preferable.

Preserve existing voice unless:

- the user requests a change;
- the current copy is internally inconsistent;
- the tone creates a clear usability or communication problem.

---

# Calls to Action

Review whether CTAs communicate:

- what happens next;
- why the action matters;
- what the user is expected to do.

Avoid generic CTA text when a more descriptive action is appropriate.

---

# Content Density

Identify:

- excessive text;
- empty sections;
- repeated explanations;
- unnecessary navigation copy;
- redundant UI messaging.

Optimization should improve information-to-noise ratio.

---

# Duplication

Look for duplicated:

- paragraphs;
- feature descriptions;
- metadata;
- headings;
- product claims;
- navigation labels.

Do not remove duplicate content if repetition is intentionally serving different contexts.

---

# Content Consistency

Check consistency across:

- terminology;
- capitalization;
- product names;
- feature names;
- units;
- dates;
- claims;
- links.

Inconsistent terminology can create confusion.

---

# Content Accuracy

Do not silently rewrite factual claims that appear uncertain.

If content contains:

- unsupported claims;
- conflicting information;
- suspicious statistics;
- outdated information;

identify the issue.

If verification is needed, use an appropriate research workflow.

---

# Metadata Consistency

Compare visible content with:

- title;
- description;
- Open Graph content;
- structured data;
- page metadata.

Important claims should not conflict across representations.

SEO-specific optimization belongs primarily to the SEO skill.

---

# Code Optimization

## Code Goal

Code optimization should improve one or more of:

- runtime efficiency;
- resource efficiency;
- maintainability;
- reliability;
- build efficiency;
- developer productivity.

Do not optimize code purely because it can be made shorter.

---

# Code Discovery

Before modifying code, inspect:

- relevant files;
- call sites;
- imports;
- dependencies;
- data flow;
- state management;
- rendering behavior;
- tests.

Do not optimize a function without understanding how it is used.

---

# Hot Path Identification

Prioritize code that:

- executes frequently;
- processes large datasets;
- runs during rendering;
- handles user input;
- performs network operations;
- executes database queries;
- blocks initialization.

A slow function that executes once may matter less than a moderately expensive function executed thousands of times.

---

# Complexity

Look for unnecessary:

- nested loops;
- repeated searches;
- repeated parsing;
- redundant transformations;
- duplicate calculations.

Do not replace readable code with obscure micro-optimizations without evidence.

---

# Algorithmic Optimization

Where meaningful, consider:

```text
O(n²)
↓
O(n log n)
```

or:

```text
repeated lookup
↓
indexed lookup
```

But only when the data size and execution frequency justify the complexity.

---

# Memoization

Memoization can reduce repeated computation.

Use it when:

- computation is expensive;
- inputs repeat;
- cache lifetime is appropriate.

Do not memoize every function.

Caching introduces:

- memory usage;
- invalidation concerns;
- complexity.

---

# Rendering Optimization

For UI applications, inspect:

- unnecessary re-renders;
- large component trees;
- expensive calculations during render;
- unstable references;
- unnecessary state updates.

Do not optimize rendering based solely on intuition.

---

# React-Specific Considerations

When the project uses React, inspect:

- unnecessary component re-renders;
- inappropriate state ownership;
- expensive calculations;
- large lists;
- unstable props;
- excessive effects.

Possible techniques include:

- component boundaries;
- memoization;
- virtualization;
- derived state reduction.

Use them only when appropriate.

---

# List Rendering

Large lists may require:

- pagination;
- virtualization;
- incremental rendering.

Do not virtualize a list containing ten items.

---

# Images

Review:

- dimensions;
- format;
- compression;
- lazy loading;
- responsive variants.

Do not serve a massive image when the displayed dimensions are small.

---

# Fonts

Review:

- number of families;
- weights;
- loading strategy;
- unused variants.

Excessive font loading can affect initial rendering.

---

# JavaScript Bundle

Inspect:

- dependency size;
- duplicate packages;
- unused imports;
- unnecessary client-side code;
- large libraries used for small features.

Do not remove a dependency without checking its actual usage.

---

# Dependency Optimization

Before replacing a dependency, determine:

- why it exists;
- where it is used;
- what functionality it provides;
- whether it is actually responsible for meaningful cost.

A dependency with negligible impact may not justify migration work.

---

# Tree Shaking

Use the project's build system correctly.

Avoid importing entire libraries when selective imports are supported and materially reduce output.

Verify the resulting bundle rather than assuming tree shaking occurred.

---

# Code Splitting

Consider code splitting for:

- large routes;
- infrequently used features;
- heavy editors;
- dashboards;
- 3D scenes;
- administrative tools.

Do not split tiny modules excessively.

---

# Lazy Loading

Lazy-load expensive functionality when:

```text
initial experience
```

does not require it.

Examples:

```text
3D viewer
editor
analytics dashboard
large charting library
```

---

# Network Optimization

Inspect:

- request count;
- request size;
- duplicate requests;
- waterfalls;
- caching;
- API payload size.

Reducing one expensive request can matter more than dozens of small JavaScript optimizations.

---

# API Optimization

Look for:

- over-fetching;
- under-fetching;
- repeated requests;
- unnecessary polling;
- duplicate requests;
- missing caching.

Do not alter API contracts without considering consumers.

---

# Database Optimization

When database access is in scope, inspect:

- query frequency;
- query complexity;
- indexes;
- selected columns;
- joins;
- pagination;
- N+1 patterns.

Database optimization should be evidence-driven.

---

# N+1 Queries

Identify patterns such as:

```text
1 query for parent records
+
1 query per parent
```

Consider batching, joins, or appropriate eager loading.

Do not eliminate separate queries when they are intentional and efficient.

---

# Caching

Caching may improve performance but introduces invalidation complexity.

Before adding caching, determine:

- what can become stale;
- acceptable staleness;
- cache scope;
- invalidation strategy.

Do not add caching as a reflex.

---

# Dead Code

Identify:

- unused files;
- unused functions;
- unreachable branches;
- unused dependencies;
- obsolete feature flags.

Before deleting something, verify that it is actually unused.

---

# Duplication

Repeated code may indicate an abstraction opportunity.

But abstraction has a cost.

Do not create a generic utility merely because two short pieces of code look similar.

Prefer abstraction when duplication is:

- substantial;
- repeated;
- semantically related;
- likely to evolve together.

---

# Maintainability

Optimization should not make code harder to understand without sufficient benefit.

Consider:

```text
performance gain
vs
complexity cost
```

A small performance gain may not justify significant architectural complexity.

---

# Premature Optimization

Do not optimize:

- hypothetical bottlenecks;
- code with no meaningful execution cost;
- trivial allocations;
- tiny functions;
- code that is never executed in relevant flows.

Prioritize actual impact.

---

# Optimization Priority

Classify findings by:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

### CRITICAL

Major performance or content problem with significant user/system impact.

### HIGH

Meaningful issue with measurable or strongly supported impact.

### MEDIUM

Useful improvement with moderate impact.

### LOW

Minor improvement or cleanup.

Severity should reflect evidence and impact, not personal preference.

---

# Evidence Levels

For each optimization, distinguish:

```text
MEASURED
OBSERVED
INFERRED
POSSIBLE
```

Example:

```text
MEASURED
Bundle increased by 1.8 MB.

OBSERVED
The same API endpoint is requested multiple times.

INFERRED
The repeated requests may contribute to unnecessary network latency.

POSSIBLE
A caching layer could reduce duplicate requests.
```

Do not present inference as measurement.

---

# Challenge Conditions

Challenge the request when:

- the proposed optimization damages readability;
- a migration is disproportionate to the benefit;
- a requested shortcut introduces significant technical debt;
- the supposed bottleneck has no evidence;
- content optimization would remove information users need;
- performance optimization conflicts with accessibility;
- a change risks breaking existing behavior.

---

# Example: Unnecessary Library Replacement

Request:

> Replace the animation library because it adds 40 KB.

First determine:

- actual compressed production impact;
- whether it is already shared;
- how much functionality depends on it;
- migration complexity.

Do not automatically replace it.

---

# Example: Remove All Images

Request:

> Remove images to make the website faster.

Challenge:

```text
Concern:
Images may provide important product or contextual information.

Alternative:
Optimize formats, dimensions, loading strategy, and compression before removing them.
```

---

# Example: Rewrite All Copy

Request:

> Make every section shorter.

Determine:

- audience;
- purpose;
- required information;
- conversion goals;
- existing content hierarchy.

Do not shorten content mechanically.

---

# Safe Defaults

Prefer:

- minimal coherent changes;
- measurable improvements;
- existing project conventions;
- reversible changes;
- targeted optimization.

Avoid:

- broad rewrites;
- framework migrations;
- dependency replacement;
- architecture changes

unless the evidence justifies them.

---

# Execution

During implementation:

1. Change one coherent optimization area.
2. Preserve unrelated behavior.
3. Run relevant tests.
4. Measure when appropriate.
5. Continue only when the result is acceptable.

Avoid mixing optimization with unrelated feature development.

---

# Verification

Verification depends on the optimization type.

## Content

Check:

- readability;
- hierarchy;
- accuracy;
- consistency;
- completeness;
- user-facing behavior.

## Code

Check:

- tests;
- build;
- runtime behavior;
- performance measurements;
- bundle output;
- network behavior.

---

# Before and After

When possible, report:

```text
BEFORE
X

AFTER
Y

CHANGE
Z
```

Example:

```text
Initial JS payload:
1.8 MB

After:
1.2 MB

Reduction:
600 KB
```

Only provide measured numbers when they were actually measured.

---

# Regression Detection

Optimization can create regressions.

Check for:

- broken behavior;
- visual changes;
- accessibility regressions;
- slower secondary paths;
- increased memory usage;
- broken caching;
- incorrect content.

An optimization that improves one metric while breaking core functionality is not a successful change.

---

# Content Regression

After rewriting content, verify that the revision did not remove:

- essential product information;
- requirements;
- warnings;
- legal information;
- important context;
- relevant calls to action.

---

# Performance Regression

A change can improve:

```text
bundle size
```

while worsening:

```text
runtime execution
```

or:

```text
network requests
```

Measure the metrics that matter to the actual goal.

---

# Reporting

A useful optimization report contains:

```text
scope
baseline
findings
changes
measurements
verification
remaining opportunities
unverified items
```

Example:

```text
Scope:
Homepage initial load.

Finding:
Large charting dependency loaded immediately.

Change:
Moved charting module behind route-level lazy loading.

Verification:
Production build completed successfully.

Measurement:
Initial JS reduced by 420 KB.

Remaining:
Image optimization has not yet been measured.
```

---

# Anti-Patterns

## Optimize Everything

Changing large portions of the project without evidence.

---

## Micro-Optimization

Spending significant effort on negligible improvements.

---

## Shorter Is Better

Removing useful content simply to reduce word count.

---

## Clever Code

Replacing readable code with unnecessarily complex implementations.

---

## Dependency Purging

Removing libraries without understanding their purpose.

---

## Unmeasured Performance Claims

Calling something "faster" without measuring when measurement is practical.

---

## Silent Content Changes

Changing factual or strategic messaging without user authorization.

---

## Optimization as Refactoring

Using an optimization request as an excuse for unrelated architectural cleanup.

---

## Rewrite Instead of Improve

Replacing functioning systems instead of addressing the actual bottleneck.

---

# Example: Targeted Code Optimization

Request:

> Make the product page faster.

Process:

```text
Inspect product page
↓
Identify loading/rendering/network paths
↓
Establish relevant baseline
↓
Find dominant cost
↓
Optimize dominant cost
↓
Build/test
↓
Measure again
↓
Report result
```

Do not immediately rewrite the page.

---

# Example: Content Optimization

Request:

> Improve the homepage copy.

Process:

```text
Inspect existing copy
↓
Determine audience and purpose
↓
Identify hierarchy and repetition problems
↓
Preserve factual claims
↓
Rewrite relevant sections
↓
Review CTA and messaging consistency
↓
Verify page structure
```

If audience or business objective is genuinely unknown and materially changes the copy, ask.

---

# Example: Full Project Optimization

Request:

> Optimize the whole application.

Process:

```text
Discover architecture
↓
Establish baseline
↓
Inventory findings
↓
Prioritize by impact
↓
Create phased plan
↓
Implement highest-value changes
↓
Verify
↓
Repeat
```

Do not attempt a blind full-project rewrite.

---

# Completion Criteria

The Content + Code Optimization skill is complete when:

- [ ] the optimization scope is understood;
- [ ] relevant project context was discovered;
- [ ] existing behavior was understood;
- [ ] relevant baseline measurements were established where practical;
- [ ] content and code concerns were distinguished;
- [ ] findings were prioritized by impact;
- [ ] evidence was distinguished from inference;
- [ ] unnecessary changes were avoided;
- [ ] user preferences were respected;
- [ ] substantive technical tradeoffs were surfaced;
- [ ] changes were implemented incrementally;
- [ ] relevant tests were run;
- [ ] relevant performance/content checks were performed;
- [ ] regressions were considered;
- [ ] measured improvements were reported accurately;
- [ ] unmeasured claims were not presented as facts;
- [ ] remaining work is explicit.

The goal is not:

> **"Make everything smaller, faster, or shorter."**

The goal is:

> **"Improve meaningful outcomes while preserving correctness, usability, maintainability, and the project's intended behavior."**
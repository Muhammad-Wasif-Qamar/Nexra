---
name: seo
description: Analyze and improve technical, on-page, structured-data, crawlability, performance, and content aspects of websites for search-engine discoverability without making unsupported ranking claims.
version: 0.1.0
---

# SEO

## Purpose

The SEO skill guides an agent in improving a website's search-engine discoverability, crawlability, indexability, relevance, and technical quality.

SEO is not:

> "Add keywords everywhere."

SEO is a system involving:

- technical accessibility;
- crawlability;
- indexability;
- information architecture;
- semantic HTML;
- content quality;
- metadata;
- structured data;
- internal linking;
- performance;
- mobile usability;
- rendering behavior.

The objective is to make the site's important content understandable and accessible to search engines and users.

---

# Core Principle

## Optimize for Users and Search Engines Together

Search optimization should not produce content or interfaces that are useful only to search engines.

Prefer:

```text
clear information
+
semantic structure
+
accessible implementation
+
technically discoverable pages
```

Do not sacrifice usability merely to manipulate search signals.

---

# Scope

This skill covers:

- technical SEO;
- crawlability;
- indexability;
- metadata;
- semantic HTML;
- headings;
- canonical URLs;
- robots directives;
- sitemap configuration;
- structured data;
- internal linking;
- URL structure;
- image SEO;
- content discoverability;
- JavaScript rendering considerations;
- mobile SEO;
- performance-related SEO;
- international SEO where relevant;
- SEO verification.

This skill does not replace:

- `content-code-optimization`;
- `ui-ux-design`;
- `security`;
- `reviewer`.

---

# Discover Before Asking

Inspect the project before asking questions.

Determine:

- framework;
- routing system;
- rendering strategy;
- static vs dynamic pages;
- metadata implementation;
- sitemap;
- robots configuration;
- canonical configuration;
- structured data;
- page templates;
- content sources;
- image handling;
- deployment platform;
- domain configuration.

Do not ask the user for information that the repository can reveal.

---

# SEO Intent

Determine the actual goal.

Possible goals:

```text
INDEXABILITY
Make important pages discoverable/indexable.

TECHNICAL SEO
Fix implementation problems.

ON-PAGE SEO
Improve page-level signals and content structure.

LOCAL SEO
Support location-specific discoverability.

INTERNATIONAL SEO
Support multiple languages/regions.

E-COMMERCE SEO
Improve product/category discoverability.

CONTENT SEO
Improve information quality and topical coverage.
```

Different goals require different workflows.

---

# SEO Discovery Workflow

Use:

```text
DISCOVER
↓
CRAWL/INSPECT
↓
IDENTIFY ISSUES
↓
PRIORITIZE
↓
IMPLEMENT
↓
VERIFY
```

Do not begin by changing titles and keywords before understanding the technical structure.

---

# Search Intent

Understand what a page is intended to satisfy.

Common intent categories include:

```text
informational
navigational
commercial investigation
transactional
```

Do not force a page into an intent category unsupported by the actual product or content.

---

# Keyword Research

When keyword research is explicitly required, determine:

- target topic;
- search intent;
- relevant terminology;
- audience language;
- page purpose.

Do not stuff keywords into content.

---

# Keyword Usage

Use important terminology naturally in:

- page titles;
- headings;
- body content;
- links;
- metadata where appropriate.

Do not repeat keywords unnaturally.

---

# Keyword Stuffing

Avoid:

```text
best software software software
```

or unnatural repetitions designed solely to increase keyword frequency.

Write for the user first.

---

# Page Title

Each important page should have an appropriate title.

A useful title should:

- describe the page;
- distinguish it from other pages;
- reflect the actual content;
- avoid unnecessary repetition.

Do not generate identical titles across all pages.

---

# Meta Description

Meta descriptions should accurately summarize the page.

Consider:

- relevance;
- clarity;
- uniqueness;
- useful context;
- natural language.

Do not assume a meta description guarantees a particular search-result appearance.

---

# Headings

Use semantic heading hierarchy.

Typical structure:

```text
H1
├── H2
│   ├── H3
│   └── H3
└── H2
```

Do not use heading elements merely for visual styling.

---

# One Primary Heading

Where appropriate, a page should have a clear primary heading.

Do not treat a strict numeric heading rule as more important than the actual document structure.

The goal is semantic clarity.

---

# Semantic HTML

Prefer semantic elements where appropriate:

```html
<header>
<nav>
<main>
<section>
<article>
<footer>
```

Semantic structure helps communicate page organization.

Do not add semantic elements mechanically.

---

# Links

Important pages should be reachable through meaningful internal links.

Link text should communicate the destination.

Avoid excessive generic links such as:

```text
Click here
Read more
Learn more
```

when a descriptive alternative is practical.

---

# Internal Linking

Review:

- important pages;
- orphan pages;
- navigation;
- contextual links;
- related content;
- category structures.

Internal links should help users navigate as well as help search engines discover relationships.

---

# Orphan Pages

An orphan page is a page that is not meaningfully linked from the site's internal structure.

Identify orphan pages when the project contains a large route/content set.

Do not create unnecessary links solely to eliminate an orphan-page finding.

---

# URL Structure

Prefer URLs that are:

- stable;
- understandable;
- consistent;
- appropriate to the site's information architecture.

Avoid unnecessary URL complexity.

---

# URL Changes

URL changes can break:

- bookmarks;
- inbound links;
- search indexing;
- analytics;
- application routes.

Do not change established URLs without a reason.

When URLs must change, consider appropriate redirects and canonical handling.

---

# Canonical URLs

Canonical URLs help communicate the preferred version of a page when multiple URLs represent substantially similar content.

Inspect:

- canonical generation;
- absolute vs relative URLs where relevant;
- route behavior;
- query parameters;
- duplicate page variants.

Do not canonicalize unrelated pages to a single URL merely to reduce page count.

---

# Duplicate Content

Identify:

- duplicated pages;
- parameter variants;
- duplicated route templates;
- accidental duplicate content.

Do not treat every repeated phrase as a serious duplicate-content problem.

Context matters.

---

# Robots.txt

Inspect:

- existence;
- syntax;
- intended rules;
- sitemap reference;
- accidentally blocked resources/pages.

Do not block important pages without understanding the consequences.

---

# Robots Directives

Distinguish:

```text
robots.txt
```

from:

```text
meta robots
```

and:

```text
X-Robots-Tag
```

They operate at different levels.

Do not use robots.txt as a universal replacement for page-level indexing directives.

---

# Sitemap

Inspect whether the project needs:

```text
sitemap.xml
```

or a dynamically generated sitemap.

A sitemap should represent URLs that are intended to be discoverable/indexable.

Do not include:

- irrelevant routes;
- broken URLs;
- unintended duplicates;
- pages explicitly excluded from indexing.

---

# Dynamic Sitemaps

For large dynamic sites, inspect how the sitemap is generated.

Verify:

- route coverage;
- URL correctness;
- generation failures;
- deployment behavior.

---

# JavaScript Rendering

Search engines may process JavaScript-rendered content, but rendering adds complexity.

Important content should not unnecessarily depend on client-side execution when server/static rendering is practical.

Inspect the framework's rendering strategy.

---

# SSR

For server-rendered applications, verify:

- title generation;
- metadata;
- canonical URLs;
- headings;
- meaningful content.

Do not assume that because SSR is enabled, SEO is automatically correct.

---

# SSG

Static generation can provide straightforward crawlable HTML.

Verify that generated pages actually contain:

- meaningful content;
- metadata;
- links;
- canonical information.

---

# Client-Side Rendering

For client-rendered applications, inspect whether important content is available appropriately.

Do not claim that CSR makes a site "unindexable" by default.

Instead evaluate the actual rendered output and search requirements.

---

# Structured Data

Structured data can help communicate machine-readable information about supported page types.

Potential types include:

- Organization;
- WebSite;
- BreadcrumbList;
- Product;
- Article;
- Event;
- FAQ where applicable.

Only use a schema type when the page genuinely represents that entity/content.

---

# Structured Data Accuracy

Structured data must represent visible or otherwise legitimately supported page information.

Do not insert fabricated:

- ratings;
- reviews;
- prices;
- dates;
- authors;
- organizations;
- product claims.

---

# JSON-LD

JSON-LD is often convenient for structured data.

When implementing it:

- validate syntax;
- use appropriate schema properties;
- keep values synchronized with page content;
- avoid unsupported claims.

---

# Schema Validation

When tools are available, validate structured data.

Check:

- JSON syntax;
- schema structure;
- required properties where applicable;
- warnings;
- consistency.

A valid JSON document is not necessarily valid structured data.

---

# Breadcrumbs

Breadcrumbs can help communicate hierarchy.

For hierarchical sites, consider:

```text
Home
→ Category
→ Subcategory
→ Page
```

Do not create breadcrumbs for a site structure that does not actually have meaningful hierarchy.

---

# Organization Information

For appropriate business or organizational sites, structured organization information may be useful.

Use real project information.

Do not invent:

- addresses;
- phone numbers;
- social profiles;
- founding dates;
- employee counts.

---

# Product SEO

For e-commerce/product pages, inspect:

- product names;
- descriptions;
- availability;
- price;
- product identifiers;
- images;
- structured data.

Keep structured data synchronized with actual product state.

---

# Image SEO

Inspect:

- descriptive filenames where useful;
- alt text;
- dimensions;
- format;
- loading strategy;
- responsive images.

Alt text should describe meaningful image content.

Do not stuff keywords into alt attributes.

---

# Decorative Images

Decorative images should not receive misleading descriptive alt text.

Use appropriate accessibility semantics.

SEO and accessibility should not be treated as competing goals here.

---

# Image Indexability

If images are important to the site's discoverability, ensure they are:

- accessible;
- not unintentionally blocked;
- properly associated with relevant content.

Do not hide important images behind unnecessary client-side mechanisms.

---

# Performance and SEO

Performance can affect user experience and search-related metrics.

Inspect:

- loading;
- rendering;
- layout stability;
- interaction responsiveness;
- large assets;
- JavaScript cost.

Use `content-code-optimization` for broader performance work.

---

# Core Web Vitals

When performance measurement is required, consider relevant user-experience metrics such as:

```text
LCP
INP
CLS
```

Use actual measurements when possible.

Do not claim compliance from code inspection alone.

---

# Mobile SEO

Verify:

- responsive layout;
- readable text;
- usable controls;
- content parity;
- mobile rendering;
- viewport configuration.

Do not create a separate mobile experience that omits important content without a deliberate reason.

---

# Mobile-First Consideration

Modern search systems evaluate mobile experiences heavily.

Ensure important content and functionality remain available on smaller screens.

---

# Accessibility and SEO

Good semantic structure can benefit both accessibility and discoverability.

Inspect:

- headings;
- landmarks;
- links;
- labels;
- text alternatives.

Do not make accessibility claims based solely on SEO implementation.

---

# International SEO

For multilingual/multiregional sites, inspect:

- language structure;
- locale URLs;
- `hreflang`;
- canonical relationships;
- translated content;
- locale consistency.

Do not add `hreflang` merely because multiple languages are planned.

---

# Hreflang

Where appropriate, verify:

- language/region codes;
- reciprocal relationships;
- canonical compatibility;
- URL accessibility.

Incorrect `hreflang` can create confusing signals.

---

# Local SEO

For location-based businesses, inspect:

- consistent business information;
- location pages;
- contact information;
- structured data where appropriate;
- local content.

Do not invent local business information.

---

# Content Quality

SEO content should:

- answer the intended question;
- provide useful information;
- avoid unnecessary repetition;
- maintain factual accuracy;
- match the page's purpose.

Do not generate large amounts of low-value content simply to increase indexed page count.

---

# Thin Content

Potential thin-content problems include pages with:

- little unique value;
- placeholder content;
- near-empty templates;
- automatically generated pages with no useful differentiation.

Do not classify a short page as low quality solely because it is short.

---

# Programmatic Content

Large programmatic sites require careful evaluation.

Before generating many pages, determine:

- whether each page has unique value;
- whether users need the pages;
- whether content can be maintained;
- whether the resulting site structure remains understandable.

---

# Content Freshness

Update content when it is actually outdated.

Do not change dates or rewrite pages merely to make them appear fresh.

---

# Claims and Evidence

SEO copy should not introduce unsupported claims.

If the user asks for factual claims that require verification, distinguish:

```text
verified
unverified
needs research
```

---

# Search Console and Analytics

When connected tools are available, inspect appropriate data such as:

- indexing status;
- search queries;
- impressions;
- clicks;
- crawl issues;
- page performance.

Do not infer ranking conclusions from a single metric.

---

# Search Ranking Claims

Do not promise:

```text
#1 ranking
guaranteed first page
guaranteed traffic
guaranteed impressions
```

SEO outcomes depend on external systems and competition.

Report implementation changes and measured observations instead.

---

# SEO Audit

For a broad audit, organize findings into:

```text
CRAWLABILITY
INDEXABILITY
TECHNICAL
ON-PAGE
CONTENT
INTERNAL LINKS
STRUCTURED DATA
PERFORMANCE
MOBILE
INTERNATIONAL
```

Do not produce a long issue list without prioritization.

---

# Issue Priority

Use:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

based on:

- affected pages;
- severity;
- user impact;
- search discoverability;
- implementation risk;
- evidence.

Priority is not the same as a ranking prediction.

---

# Evidence

For each issue, provide:

```text
Finding
Evidence
Impact
Recommendation
Verification
```

Example:

```text
Finding:
Important product pages are missing internal links.

Evidence:
Route inventory contains product pages that are not linked from category or navigation structures.

Impact:
Users and crawlers may have fewer paths to discover those pages.

Recommendation:
Add contextual category/product links.

Verification:
Rebuild internal link graph and confirm intended pages are reachable.
```

---

# Challenge Conditions

Challenge SEO requests when they involve:

- keyword stuffing;
- fabricated structured data;
- hidden content intended only for crawlers;
- misleading metadata;
- mass low-value page generation;
- unnecessary URL changes;
- deceptive redirects;
- accessibility degradation;
- claims of guaranteed rankings.

Explain the technical or quality concern and propose a legitimate alternative.

---

# Example: Keyword Stuffing

Request:

> Put the keyword 50 times on every page.

Response approach:

```text
Concern:
Repetition can reduce readability and does not guarantee improved search visibility.

Alternative:
Use the topic naturally across titles, headings, body content, links, and supporting pages where relevant.
```

The user decides the final content strategy.

---

# Example: Fake Reviews

Request:

> Add five-star reviews to the structured data.

Do not fabricate reviews.

If actual review data exists, use the real data and appropriate schema.

---

# Example: Hidden Keywords

Request:

> Add invisible keywords to the footer.

Challenge the tactic.

Use visible, useful content instead.

---

# Example: Guaranteed Ranking

Request:

> Optimize this site so it ranks #1.

Translate the request into controllable work:

```text
technical audit
+
content optimization
+
indexability improvements
+
structured data
+
internal linking
+
measurement
```

Do not promise a ranking outcome.

---

# Execution

For a targeted SEO task:

```text
inspect
↓
identify relevant issue
↓
change
↓
validate
```

For a broad SEO task:

```text
crawl
↓
inventory
↓
prioritize
↓
phase work
↓
implement
↓
verify
```

Do not rewrite the entire site's SEO configuration at once without need.

---

# Verification

Verify:

- generated HTML;
- metadata;
- canonical URLs;
- robots directives;
- sitemap;
- structured data;
- internal links;
- status codes where tools permit;
- responsive behavior;
- build output.

---

# Crawl Verification

When browser or HTTP tools are available, inspect representative URLs.

Check:

```text
HTTP status
HTML content
title
description
canonical
robots
headings
links
structured data
```

Do not rely solely on source code when the final rendered output matters.

---

# Structured Data Verification

Validate structured data after implementation.

If validation tools are unavailable, verify:

- valid JSON;
- expected schema structure;
- synchronization with page content.

Report external validation as unperformed if it was not actually performed.

---

# Sitemap Verification

Check:

- valid XML;
- reachable URL;
- intended routes;
- no accidental test/dev URLs;
- consistency with canonical URLs.

---

# Robots Verification

Ensure important pages are not unintentionally blocked.

Check for conflicts between:

```text
robots.txt
meta robots
X-Robots-Tag
```

---

# Canonical Verification

Verify that canonical URLs:

- resolve;
- point to intended URLs;
- are not contradictory;
- match the site's URL strategy.

---

# Regression Testing

After SEO changes, check that:

- pages still render;
- routes still work;
- links still work;
- metadata remains correct;
- application behavior is unchanged.

SEO changes should not break the application.

---

# Reporting

A useful SEO report contains:

```text
scope
baseline
findings
evidence
changes
verification
remaining work
unverified items
```

Example:

```text
Scope:
Public marketing pages.

Finding:
Several pages use duplicate titles.

Change:
Generated page-specific titles from route metadata.

Verification:
Production build passed and rendered metadata was inspected.

Unverified:
Search-engine indexing impact has not been measured.
```

---

# Anti-Patterns

## Keyword Stuffing

Repeating terms unnaturally.

---

## Fake Structured Data

Adding information that does not represent the actual page.

---

## Hidden SEO Content

Creating content primarily for crawlers while hiding it from users.

---

## Mass Low-Value Pages

Generating hundreds of pages with little unique value.

---

## Metadata Duplication

Giving every page the same title and description.

---

## Canonical Everything

Pointing unrelated pages to one canonical URL.

---

## Robots Misuse

Blocking important resources or pages without understanding the consequences.

---

## Sitemap Dump

Putting every possible URL into the sitemap.

---

## SEO-Only HTML

Using semantically misleading HTML purely for search-engine manipulation.

---

## Guaranteed Rankings

Claiming a specific future search position.

---

## SEO Rewrite

Changing unrelated application architecture during an SEO task.

---

# Example: Technical SEO Pass

```text
Inspect framework
↓
Inspect routing
↓
Inspect rendered HTML
↓
Check metadata
↓
Check canonical
↓
Check robots
↓
Check sitemap
↓
Check structured data
↓
Check internal links
↓
Fix confirmed issues
↓
Verify build and representative pages
```

---

# Example: New Page

When adding a new page:

```text
define purpose
↓
choose URL
↓
create semantic structure
↓
add unique title
↓
add appropriate description
↓
add internal links
↓
add structured data if justified
↓
ensure crawlability
↓
verify rendered output
```

Do not add schema merely because a schema type exists.

---

# Completion Criteria

The SEO skill is complete when:

- [ ] the SEO objective is understood;
- [ ] project architecture and rendering strategy were inspected;
- [ ] relevant routes and content were identified;
- [ ] crawlability was considered;
- [ ] indexability was considered;
- [ ] page metadata was reviewed;
- [ ] semantic structure was reviewed;
- [ ] internal linking was considered;
- [ ] canonical behavior was reviewed where relevant;
- [ ] robots configuration was reviewed where relevant;
- [ ] sitemap behavior was reviewed where relevant;
- [ ] structured data was implemented only when justified;
- [ ] structured data represents real page information;
- [ ] mobile behavior was considered;
- [ ] performance implications were considered;
- [ ] accessibility was not degraded for SEO;
- [ ] SEO changes were verified in the rendered application where practical;
- [ ] unsupported ranking guarantees were avoided;
- [ ] measured observations were distinguished from predictions;
- [ ] remaining and unverified work is explicit.

The goal is not:

> **"Manipulate search engines."**

The goal is:

> **"Make the site's useful content technically accessible, semantically understandable, discoverable, and genuinely useful to users."**
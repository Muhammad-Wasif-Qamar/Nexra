#!/usr/bin/env python3

from pathlib import Path
import json
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


# ---------------------------------------------------------------------------
# Canonical inventories
# ---------------------------------------------------------------------------

EXPECTED_SKILLS = [
    "project-discovery",
    "capability-assessment",
    "interaction",
    "challenge",
    "execution",
    "verification",
    "reporting",
    "ui-ux-design",
    "animation-design",
    "3d-web-design",
    "scroll-world-flyby",
    "content-code-optimization",
    "seo",
    "security",
    "reviewer",
]

FOUNDATION_SKILLS = EXPECTED_SKILLS[:7]

EXPECTED_ADAPTERS = [
    "generic",
    "opencode",
    "claude-code",
    "kiro",
    "cursor",
    "codex",
    "gemini",
    "github-copilot",
    "antigravity",
    "cline",
    "roo",
    "openhands",
]

EXPECTED_PLUGINS = [
    "browser",
    "container",
    "database",
    "filesystem",
    "git",
    "github",
    "http",
    "image-inspection",
    "mcp",
    "package-manager",
    "shell",
    "test-runner",
]

EXPECTED_CONNECTORS = [
    "browser-session",
    "git-repository",
    "github-api",
    "http-client",
    "local-filesystem",
    "mcp-server",
    "npm-registry",
    "postgresql",
    "shell-runtime",
]

REQUIRED_REPOSITORY_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "LICENSE",
    ".gitignore",
    "package.json",
    "docs/spec/SKILL-SPEC.md",
    "docs/adapters/ADAPTER-SPEC.md",
    "docs/architecture.md",
    "docs/testing.md",
    "core/README.md",
    "core/orchestration/PIPELINE.md",
    "core/specification/BEHAVIOR.md",
    "core/execution/EXECUTION-CONTRACT.md",
    "core/verification/VERIFICATION-CONTRACT.md",
    "core/reporting/REPORTING-CONTRACT.md",
    "core/registries/skill-registry.yaml",
    "integrations/registry.yaml",
    "scripts/validate.py",
    "scripts/test_suite.py",
    "cli/bin/the-builder.js",
]

REQUIRED_TEST_FILES = [
    "tests/README.md",
    "tests/core/cases.md",
    "tests/skills/cases.md",
    "tests/adapters/cases.md",
    "tests/project-discovery/cases.md",
    "tests/challenge/cases.md",
]


# ---------------------------------------------------------------------------
# Behavioral expectations
#
# These are intentionally concept-based rather than exact-heading based.
# A skill may structure itself differently while still being required to
# teach the behavior represented by its purpose.
# ---------------------------------------------------------------------------

SKILL_CONCEPTS = {
    "project-discovery": [
        ["discover", "discovery"],
        ["project", "repository"],
        ["technology", "stack", "framework"],
        ["architecture", "structure"],
        ["environment"],
        ["constraints"],
        ["unknown"],
    ],

    "capability-assessment": [
        ["capability"],
        ["model"],
        ["agent", "tool"],
        ["environment"],
        ["project"],
        ["full", "suitable", "constrained", "unsuitable"],
        ["evidence"],
        ["graceful degradation", "degradation"],
    ],

    "interaction": [
        ["discover before asking", "discover before"],
        ["question", "ask"],
        ["user decision", "user authority"],
        ["ambiguity"],
        ["priority", "priorit"],
        ["progressive questioning", "progressive"],
    ],

    "challenge": [
        ["challenge"],
        ["substantive", "technical", "meaningful"],
        ["tradeoff"],
        ["user authority", "user decides"],
        ["evidence"],
        ["preference"],
    ],

    "execution": [
        ["execute", "execution"],
        ["plan"],
        ["minimal", "bounded", "scope"],
        ["incremental"],
        ["change"],
        ["verify", "validation"],
    ],

    "verification": [
        ["verify", "verification"],
        ["evidence"],
        ["test", "check"],
        ["unverified", "not verified"],
        ["completion"],
    ],

    "reporting": [
        ["report", "reporting"],
        ["changed", "change"],
        ["check", "verification"],
        ["decision"],
        ["unverified", "remaining"],
    ],

    "ui-ux-design": [
        ["ui", "user interface"],
        ["ux", "user experience"],
        ["layout", "hierarchy"],
        ["responsive"],
        ["accessibility"],
        ["interaction"],
    ],

    "animation-design": [
        ["animation"],
        ["motion"],
        ["timing", "duration", "easing"],
        ["performance"],
        ["reduced motion", "accessibility"],
    ],

    "3d-web-design": [
        ["3d", "three-dimensional"],
        ["scene", "camera"],
        ["lighting", "material"],
        ["performance"],
        ["webgl", "three.js", "renderer"],
    ],

    "scroll-world-flyby": [
        ["scroll"],
        ["fly-by", "flyby"],
        ["camera"],
        ["scene"],
        ["depth", "parallax", "spatial"],
        ["transition"],
    ],

    "content-code-optimization": [
        ["content"],
        ["code"],
        ["performance", "optimization"],
        ["readability", "clarity", "structure"],
        ["bundle", "rendering", "request", "dependency"],
    ],

    "seo": [
        ["seo", "search engine"],
        ["metadata"],
        ["crawl", "index"],
        ["structured data", "schema"],
        ["performance", "core web vitals"],
    ],

    "security": [
        ["security"],
        ["threat", "risk"],
        ["input", "validation"],
        ["authentication", "authorization"],
        ["secret", "credential"],
        ["dependency"],
    ],

    "reviewer": [
        ["review"],
        ["severity"],
        ["evidence"],
        ["impact"],
        ["recommendation"],
        ["confirmed", "likely", "hardening", "informational"],
    ],
}


# ---------------------------------------------------------------------------
# Error / warning handling
# ---------------------------------------------------------------------------

ERRORS = []
WARNINGS = []


def error(message):
    ERRORS.append(message)


def warning(message):
    WARNINGS.append(message)


def read(path):
    return path.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Generic helpers
# ---------------------------------------------------------------------------

def meaningful_lines(content):
    """
    Count substantive lines while ignoring blank lines and YAML delimiters.
    """
    count = 0

    for line in content.splitlines():
        stripped = line.strip()

        if not stripped:
            continue

        if stripped in {"---", "```"}:
            continue

        count += 1

    return count


def heading_levels(content):
    """
    Return Markdown heading levels while ignoring headings inside fenced
    code blocks.
    """
    levels = []
    in_fence = False

    for line in content.splitlines():
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            continue

        if in_fence:
            continue

        match = re.match(r"^(#{1,6})\s+", line)

        if match:
            levels.append(len(match.group(1)))

    return levels


def frontmatter(content, expected_name):
    """
    Validate simple canonical frontmatter.
    """
    match = re.match(
        r"^---\n(.*?)\n---\n",
        content,
        re.DOTALL,
    )

    if not match:
        error(f"{expected_name}: invalid or missing front matter")
        return None

    block = match.group(1)
    fields = {}

    for line in block.splitlines():
        field_match = re.match(
            r"^([A-Za-z0-9_-]+):\s*(.*)$",
            line,
        )

        if field_match:
            fields[field_match.group(1)] = (
                field_match.group(2).strip()
            )

    for key in ("name", "description", "version"):
        if not fields.get(key):
            error(
                f"{expected_name}: missing frontmatter field '{key}'"
            )

    declared_name = fields.get("name")

    if declared_name and declared_name != expected_name:
        error(
            f"{expected_name}: frontmatter name mismatch "
            f"(declared '{declared_name}')"
        )

    version = fields.get("version", "")

    if not re.fullmatch(
        r"[0-9]+\.[0-9]+\.[0-9]+",
        version,
    ):
        error(
            f"{expected_name}: version must use semantic version format"
        )

    return fields


def validate_concepts(skill_name, content):
    """
    Validate that a skill teaches concepts appropriate to its purpose.

    Each concept group is an OR group. Every group must have at least one
    matching term.
    """
    groups = SKILL_CONCEPTS.get(skill_name, [])
    lower = content.lower()

    for group in groups:
        if not any(term.lower() in lower for term in group):
            expected = " / ".join(group)

            error(
                f"{skill_name}: missing behavioral concept "
                f"({expected})"
            )


def is_markdown_fence(line):
    return bool(re.match(r"^\s*```", line))


# ---------------------------------------------------------------------------
# Skill validation
# ---------------------------------------------------------------------------

def validate_skill(skill_name):
    path = ROOT / "skills" / skill_name / "SKILL.md"

    if not path.is_file():
        error(f"missing skill: {skill_name}")
        return

    content = read(path)

    frontmatter(content, skill_name)

    if "⸻" in content:
        error(f"{skill_name}: corruption marker found")

    lower = content.lower()

    # Only flag tokens that are strong evidence of unfinished content.
    # Phrases such as "avoid placeholder content" are legitimate prose.
    placeholder_tokens = [
        "lorem ipsum",
        "todo: fill",
        "replace this",
    ]

    for token in placeholder_tokens:
        if token in lower:
            error(
                f"{skill_name}: placeholder content found: {token}"
            )

    fence_count = len(
        re.findall(
            r"^\s*```",
            content,
            re.MULTILINE,
        )
    )

    if fence_count % 2:
        error(f"{skill_name}: unbalanced code fences")

    line_count = meaningful_lines(content)

    if line_count < 40:
        error(
            f"{skill_name}: suspiciously small "
            f"({line_count} meaningful lines)"
        )

    # Every skill must have a title.
    if not re.search(
        r"^#\s+\S+",
        content,
        re.MULTILINE,
    ):
        error(f"{skill_name}: missing top-level title")

    # Do not force identical headings across every skill.
    # Only reject clearly malformed heading jumps.
    levels = heading_levels(content)

    if levels:
        first = levels[0]

        if first != 1:
            warning(
                f"{skill_name}: first Markdown heading is H{first}; "
                "H1 is recommended"
            )

        for previous, current in zip(levels, levels[1:]):
            if current - previous > 2:
                error(
                    f"{skill_name}: excessive heading hierarchy jump "
                    f"{previous}->{current}"
                )

    validate_concepts(skill_name, content)

    # Canonical skills must remain provider agnostic.
    forbidden_provider_tokens = [
        ".claude/skills/",
        ".opencode/",
        "opencode.json",
        ".cursor/",
        "cursor rules",
        ".gemini/",
        "gemini cli command only",
        "claude code only",
        "openai codex only",
    ]

    for token in forbidden_provider_tokens:
        if token in lower:
            error(
                f"{skill_name}: provider-specific token found: {token}"
            )


# ---------------------------------------------------------------------------
# Skill inventory
# ---------------------------------------------------------------------------

def validate_skill_inventory():
    skills_root = ROOT / "skills"

    if not skills_root.is_dir():
        error("missing skills directory")
        return

    discovered = sorted(
        path.parent.name
        for path in skills_root.glob("*/SKILL.md")
    )

    expected = sorted(EXPECTED_SKILLS)

    if discovered != expected:
        error(
            "skill inventory mismatch: "
            f"expected {len(expected)}, "
            f"found {len(discovered)}"
        )

        missing = sorted(
            set(expected) - set(discovered)
        )

        extra = sorted(
            set(discovered) - set(expected)
        )

        if missing:
            error(
                f"missing skills: {', '.join(missing)}"
            )

        if extra:
            error(
                f"unexpected skills: {', '.join(extra)}"
            )

    for skill in EXPECTED_SKILLS:
        validate_skill(skill)

    # The old split concept must never return.
    obsolete = skills_root / "fly-by-animation"

    if obsolete.exists():
        error(
            "obsolete split skill exists: "
            "skills/fly-by-animation"
        )

    merged = skills_root / "scroll-world-flyby" / "SKILL.md"

    if merged.is_file():
        content = read(merged).lower()

        merged_concept_terms = [
            "scroll world",
            "fly-by",
            "flyby",
            "scroll-driven",
        ]

        matched = sum(
            term in content
            for term in merged_concept_terms
        )

        if matched < 2:
            error(
                "scroll-world-flyby does not clearly document "
                "the merged scroll/fly-by discipline"
            )


# ---------------------------------------------------------------------------
# Repository files
# ---------------------------------------------------------------------------

def validate_repository_files():
    for relative in REQUIRED_REPOSITORY_FILES:
        path = ROOT / relative

        if not path.is_file():
            error(
                f"missing repository file: {relative}"
            )
            continue

        # .gitignore may intentionally be minimal.
        if relative != ".gitignore" and not read(path).strip():
            error(
                f"empty repository file: {relative}"
            )


# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------

def validate_markdown():
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue

        content = read(path)
        relative = path.relative_to(ROOT)

        fence_count = len(
            re.findall(
                r"^\s*```",
                content,
                re.MULTILINE,
            )
        )

        if fence_count % 2:
            error(
                f"unbalanced code fences: {relative}"
            )

        # Validate relative Markdown links.
        links = re.findall(
            r"\]$begin:math:text$\$begin:math:text$\\\[\\\^$end:math:text$\#\]\+\)$end:math:text$",
            content,
        )

        for target in links:
            target = target.strip()

            if (
                "://" in target
                or target.startswith("mailto:")
                or target.startswith("#")
            ):
                continue

            target_path = (path.parent / target).resolve()

            if not target_path.exists():
                error(
                    f"broken local link: "
                    f"{relative} -> {target}"
                )


# ---------------------------------------------------------------------------
# Canonical skill location
# ---------------------------------------------------------------------------

def validate_no_obsolete_skill_files():
    """
    Canonical installable skills live under skills/.

    Supporting contracts may exist under core/, but old duplicated canonical
    SKILL.md definitions should not remain there.
    """
    obsolete_core_skills = [
        ROOT / "core" / "discovery" / "SKILL.md",
        ROOT / "core" / "capability" / "SKILL.md",
        ROOT / "core" / "interaction" / "SKILL.md",
        ROOT / "core" / "challenge" / "SKILL.md",
        ROOT / "core" / "execution" / "SKILL.md",
        ROOT / "core" / "verification" / "SKILL.md",
        ROOT / "core" / "reporting" / "SKILL.md",
    ]

    for path in obsolete_core_skills:
        if path.exists():
            error(
                "obsolete canonical skill file exists: "
                f"{path.relative_to(ROOT)}"
            )


# ---------------------------------------------------------------------------
# Adapters
# ---------------------------------------------------------------------------

def validate_adapters():
    adapters_root = ROOT / "adapters"

    if not adapters_root.is_dir():
        error("missing adapters directory")
        return

    # adapters/generic/adapter.yaml -> parent.name == "generic"
    # path.stem would incorrectly produce "adapter".
    discovered = sorted(
        path.parent.name
        for path in adapters_root.glob("*/adapter.yaml")
    )

    expected = sorted(EXPECTED_ADAPTERS)

    if discovered != expected:
        error(
            "adapter inventory mismatch: "
            f"expected {len(expected)}, "
            f"found {len(discovered)}"
        )

        missing = sorted(
            set(expected) - set(discovered)
        )

        extra = sorted(
            set(discovered) - set(expected)
        )

        if missing:
            error(
                f"missing adapters: {', '.join(missing)}"
            )

        if extra:
            error(
                f"unexpected adapters: {', '.join(extra)}"
            )

    canonical_skills = (
        ROOT / "skills"
    ).resolve()

    for adapter in EXPECTED_ADAPTERS:
        adapter_root = adapters_root / adapter
        manifest = adapter_root / "adapter.yaml"
        readme = adapter_root / "README.md"

        if not manifest.is_file():
            error(f"missing adapter manifest: {adapter}")
            continue

        content = read(manifest)
        lines = content.splitlines()

        # ---------------------------------------------------------------
        # Required top-level manifest fields
        # ---------------------------------------------------------------

        required_keys = [
            "adapter_version:",
            "target:",
            "skill_source:",
            "installation:",
            "claims:",
        ]

        for key in required_keys:
            if not any(
                line.strip().startswith(key)
                for line in lines
            ):
                error(
                    f"adapter {adapter}: missing {key}"
                )

        # ---------------------------------------------------------------
        # Adapter target
        # ---------------------------------------------------------------

        target = None

        for line in lines:
            stripped = line.strip()

            if stripped.startswith("target:"):
                target = stripped.split(":", 1)[1].strip()
                target = target.strip("\"'")
                break

        if target is not None and target != adapter:
            error(
                f"adapter {adapter}: target mismatch "
                f"(declared '{target}')"
            )

        # ---------------------------------------------------------------
        # Adapter version
        # ---------------------------------------------------------------

        adapter_version = None

        for line in lines:
            stripped = line.strip()

            if stripped.startswith("adapter_version:"):
                adapter_version = (
                    stripped.split(":", 1)[1]
                    .strip()
                    .strip("\"'")
                )
                break

        if adapter_version is not None:
            if not re.fullmatch(
                r"[0-9]+\.[0-9]+\.[0-9]+",
                adapter_version,
            ):
                error(
                    f"adapter {adapter}: invalid adapter_version "
                    f"'{adapter_version}'"
                )

        # ---------------------------------------------------------------
        # Claims / verification
        #
        # Expected structure:
        #
        # claims:
        #   verified: true
        #   verification_scope: ...
        #   source: https://...
        #
        # We intentionally parse this structurally instead of using a
        # regex containing \\s*, because \\s can consume newlines and
        # produce misleading matches in multiline YAML.
        # ---------------------------------------------------------------

        claims_start = None
        claims_indent = None

        for index, line in enumerate(lines):
            if not line.strip():
                continue

            stripped = line.strip()

            if stripped == "claims:":
                claims_start = index

                leading_spaces = len(line) - len(line.lstrip(" "))
                claims_indent = leading_spaces

                break

        if claims_start is not None:
            verified = None
            source = None

            for line in lines[claims_start + 1:]:
                if not line.strip():
                    continue

                leading_spaces = len(line) - len(line.lstrip(" "))

                # A non-indented line means the claims block has ended.
                if leading_spaces <= claims_indent:
                    break

                stripped = line.strip()

                if stripped.startswith("verified:"):
                    value = stripped.split(":", 1)[1].strip()
                    value = value.strip("\"'")

                    verified = value.lower() == "true"

                elif stripped.startswith("source:"):
                    value = stripped.split(":", 1)[1].strip()
                    source = value.strip("\"'")

            if verified is True:
                if not source:
                    error(
                        f"adapter {adapter}: "
                        "verified=true requires documented source"
                    )
                elif not re.match(
                    r"^https?://",
                    source,
                    re.IGNORECASE,
                ):
                    error(
                        f"adapter {adapter}: "
                        "verification source must be a URL"
                    )

        # ---------------------------------------------------------------
        # Canonical skill source
        # ---------------------------------------------------------------

        skill_source = None

        for line in lines:
            stripped = line.strip()

            if stripped.startswith("skill_source:"):
                skill_source = (
                    stripped.split(":", 1)[1]
                    .strip()
                    .strip("\"'")
                )
                break

        if skill_source:
            source_path = (
                manifest.parent / skill_source
            ).resolve()

            if source_path != canonical_skills:
                error(
                    f"adapter {adapter}: skill_source does not resolve "
                    f"to canonical skills directory "
                    f"('{skill_source}' -> "
                    f"'{source_path}')"
                )

        # ---------------------------------------------------------------
        # Adapter README
        # ---------------------------------------------------------------

        if not readme.is_file() or not read(readme).strip():
            error(
                f"missing/empty adapter README: {adapter}"
            )


# ---------------------------------------------------------------------------
# Integrations
# ---------------------------------------------------------------------------

def validate_integrations():
    registry_path = ROOT / "integrations" / "registry.yaml"

    if not registry_path.is_file():
        error("missing integrations/registry.yaml")
        return

    registry = read(registry_path)

    plugins_root = ROOT / "integrations" / "plugins"
    connectors_root = ROOT / "integrations" / "connectors"

    plugin_files = sorted(
        path.stem
        for path in plugins_root.glob("*.yaml")
    )

    connector_files = sorted(
        path.stem
        for path in connectors_root.glob("*.yaml")
    )

    if plugin_files != sorted(EXPECTED_PLUGINS):
        error(
            "plugin inventory mismatch: "
            f"expected {len(EXPECTED_PLUGINS)}, "
            f"found {len(plugin_files)}"
        )

        missing = sorted(
            set(EXPECTED_PLUGINS) - set(plugin_files)
        )

        extra = sorted(
            set(plugin_files) - set(EXPECTED_PLUGINS)
        )

        if missing:
            error(
                f"missing plugins: {', '.join(missing)}"
            )

        if extra:
            error(
                f"unexpected plugins: {', '.join(extra)}"
            )

    if connector_files != sorted(EXPECTED_CONNECTORS):
        error(
            "connector inventory mismatch: "
            f"expected {len(EXPECTED_CONNECTORS)}, "
            f"found {len(connector_files)}"
        )

        missing = sorted(
            set(EXPECTED_CONNECTORS) - set(connector_files)
        )

        extra = sorted(
            set(connector_files) - set(EXPECTED_CONNECTORS)
        )

        if missing:
            error(
                f"missing connectors: {', '.join(missing)}"
            )

        if extra:
            error(
                f"unexpected connectors: {', '.join(extra)}"
            )

    for directory, expected in (
        ("plugins", EXPECTED_PLUGINS),
        ("connectors", EXPECTED_CONNECTORS),
    ):
        root = ROOT / "integrations" / directory

        for name in expected:
            path = root / f"{name}.yaml"

            if not path.is_file():
                continue

            content = read(path)

            for key in (
                "version:",
                "kind:",
                "id:",
                "description:",
            ):
                if key not in content:
                    error(
                        f"integration {directory}/{name}: "
                        f"missing {key}"
                    )

            if not re.search(
                rf"^id:\s*{re.escape(name)}\s*$",
                content,
                re.MULTILINE,
            ):
                error(
                    f"integration {directory}/{name}: "
                    "id does not match filename"
                )

    # Plugin-to-connector dependency validation.
    expected_plugin_connectors = {
        "browser": {"browser-session"},
        "database": {"postgresql"},
        "filesystem": {"local-filesystem"},
        "git": {"git-repository"},
        "github": {"github-api"},
        "http": {"http-client"},
        "mcp": {"mcp-server"},
        "package-manager": {"npm-registry"},
        "shell": {"shell-runtime"},
        "test-runner": {"shell-runtime"},
        "container": set(),
        "image-inspection": set(),
    }

    known_connectors = set(EXPECTED_CONNECTORS)

    for plugin, expected_connectors in expected_plugin_connectors.items():
        path = plugins_root / f"{plugin}.yaml"

        if not path.is_file():
            continue

        content = read(path)

        requires_match = re.search(
            r"(?ms)^requires:\s*\n\s+connectors:\s*\n"
            r"(?P<body>(?:\s+-\s+[a-z0-9][a-z0-9-]*\s*\n?)+)",
            content,
        )

        if requires_match:
            declared_connectors = set(
                re.findall(
                    r"^\s+-\s+([a-z0-9][a-z0-9-]*)\s*$",
                    requires_match.group("body"),
                    re.MULTILINE,
                )
            )
        else:
            declared_connectors = set()

        unknown = declared_connectors - known_connectors

        if unknown:
            error(
                f"integration plugins/{plugin}: "
                f"unknown connector(s): {', '.join(sorted(unknown))}"
            )

        if declared_connectors != expected_connectors:
            expected = ", ".join(sorted(expected_connectors)) or "none"
            declared = ", ".join(sorted(declared_connectors)) or "none"

            error(
                f"integration plugins/{plugin}: "
                f"connector dependency mismatch; "
                f"expected {expected}, declared {declared}"
            )

    # Registry must mention every declared artifact.
    registry_lower = registry.lower()

    for name in EXPECTED_PLUGINS + EXPECTED_CONNECTORS:
        if not re.search(
            rf"\b{re.escape(name)}\b",
            registry_lower,
        ):
            error(
                f"integrations registry missing artifact: {name}"
            )


# ---------------------------------------------------------------------------
# Skill registry
# ---------------------------------------------------------------------------

def validate_skill_registry():
    path = ROOT / "core" / "registries" / "skill-registry.yaml"

    if not path.is_file():
        error("missing skill registry")
        return

    content = read(path)

    for skill in EXPECTED_SKILLS:
        if not re.search(
            rf"\b{re.escape(skill)}\b",
            content,
        ):
            error(
                f"skill registry missing skill: {skill}"
            )

    if re.search(
        r"\bfly-by-animation\b",
        content,
        re.IGNORECASE,
    ):
        error(
            "skill registry contains obsolete "
            "fly-by-animation skill"
        )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def validate_tests():
    for relative in REQUIRED_TEST_FILES:
        path = ROOT / relative

        if not path.is_file():
            error(
                f"missing test file: {relative}"
            )
            continue

        if not read(path).strip():
            error(
                f"empty test file: {relative}"
            )

    checks = {
        "tests/core/cases.md": [
            "discovery",
            "capability",
            "interaction",
            "challenge",
            "execution",
            "verification",
            "reporting",
        ],

        "tests/skills/cases.md": [
            "ui/ux",
            "animation",
            "3d",
            "seo",
            "security",
            "reviewer",
        ],

        "tests/challenge/cases.md": [
            "user authority",
            "technical tradeoffs",
            "security",
            "scope",
        ],
    }

    for relative, required_terms in checks.items():
        path = ROOT / relative

        if not path.is_file():
            continue

        content = read(path).lower()

        for term in required_terms:
            if term.lower() not in content:
                error(
                    f"{relative}: missing behavioral coverage "
                    f"for '{term}'"
                )


# ---------------------------------------------------------------------------
# Package
# ---------------------------------------------------------------------------

def validate_package():
    path = ROOT / "package.json"

    if not path.is_file():
        return

    try:
        package = json.loads(read(path))
    except json.JSONDecodeError as exc:
        error(
            f"package.json: invalid JSON: {exc}"
        )
        return

    if not package.get("name"):
        error(
            "package.json: missing package name"
        )

    if not re.fullmatch(
        r"[0-9]+\.[0-9]+\.[0-9]+",
        str(package.get("version", "")),
    ):
        error(
            "package.json: version must use semantic version format"
        )

    expected_bin = "cli/bin/the-builder.js"

    if package.get("bin", {}).get("the-builder") != expected_bin:
        error(
            "package.json: CLI bin mapping is incorrect"
        )

    cli = ROOT / expected_bin

    if not cli.is_file():
        error(
            "package.json: CLI target does not exist: "
            f"{expected_bin}"
        )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def validate_cli():
    cli = ROOT / "cli" / "bin" / "the-builder.js"

    if not cli.is_file():
        error("missing CLI entrypoint")
        return

    content = read(cli)
    lower = content.lower()

    for command in (
        "install",
        "doctor",
        "test",
    ):
        if command not in lower:
            error(
                f"CLI: expected command reference missing: {command}"
            )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    validate_repository_files()
    validate_skill_inventory()
    validate_no_obsolete_skill_files()
    validate_markdown()
    validate_adapters()
    validate_integrations()
    validate_skill_registry()
    validate_tests()
    validate_package()
    validate_cli()

    if WARNINGS:
        print(
            f"WARN: {len(WARNINGS)} warning(s)"
        )

        for message in WARNINGS:
            print(f" - {message}")

    if ERRORS:
        print(
            f"FAIL: {len(ERRORS)} validation error(s)"
        )

        for message in ERRORS:
            print(f" - {message}")

        sys.exit(1)

    print("PASS: repository validation")
    print(
        f"skills={len(EXPECTED_SKILLS)} "
        f"foundation={len(FOUNDATION_SKILLS)} "
        f"adapters={len(EXPECTED_ADAPTERS)} "
        f"plugins={len(EXPECTED_PLUGINS)} "
        f"connectors={len(EXPECTED_CONNECTORS)}"
    )


if __name__ == "__main__":
    main()
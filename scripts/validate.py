#!/usr/bin/env python3

from pathlib import Path
import json
import re
import sys


ROOT = Path(__file__).resolve().parents[1]

ERRORS = []
WARNINGS = []


# ============================================================================
# Canonical inventory
# ============================================================================

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

FOUNDATION_SKILLS = [
    "project-discovery",
    "capability-assessment",
    "interaction",
    "challenge",
    "execution",
    "verification",
    "reporting",
]

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
    "cli/bin/nexra.js",
]

REQUIRED_TEST_FILES = [
    "tests/README.md",
    "tests/core/cases.md",
    "tests/skills/cases.md",
    "tests/adapters/cases.md",
    "tests/project-discovery/cases.md",
    "tests/challenge/cases.md",
]


# ============================================================================
# Skill behavioral concepts
# ============================================================================

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


# ============================================================================
# General helpers
# ============================================================================

def error(message):
    ERRORS.append(message)


def warning(message):
    WARNINGS.append(message)


def read(path):
    return path.read_text(encoding="utf-8")


def meaningful_lines(content):
    return sum(
        1
        for line in content.splitlines()
        if line.strip() and line.strip() not in {"---", "```"}
    )


def heading_levels(content):
    levels = []
    in_fence = False

    for line in content.splitlines():
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            continue

        if not in_fence:
            match = re.match(r"^(#{1,6})\s+", line)
            if match:
                levels.append(len(match.group(1)))

    return levels


def contains_any(text, terms):
    return any(term.lower() in text.lower() for term in terms)


# ============================================================================
# Markdown validation
# ============================================================================

def frontmatter(content, expected_name):
    match = re.match(
        r"^---\n(.*?)\n---\n",
        content,
        re.DOTALL,
    )

    if not match:
        error(
            f"{expected_name}: invalid or missing front matter"
        )
        return None

    fields = {}

    for line in match.group(1).splitlines():
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
                f"{expected_name}: "
                f"missing frontmatter field '{key}'"
            )

    if (
        fields.get("name")
        and fields["name"] != expected_name
    ):
        error(
            f"{expected_name}: "
            f"frontmatter name mismatch "
            f"(declared '{fields['name']}')"
        )

    if not re.fullmatch(
        r"[0-9]+\.[0-9]+\.[0-9]+",
        fields.get("version", ""),
    ):
        error(
            f"{expected_name}: "
            "version must use semantic version format"
        )

    return fields


def validate_concepts(skill_name, content):
    lower = content.lower()

    for group in SKILL_CONCEPTS.get(skill_name, []):
        if not any(
            term.lower() in lower
            for term in group
        ):
            error(
                f"{skill_name}: "
                "missing behavioral concept "
                f"({' / '.join(group)})"
            )


def validate_skill(skill_name):
    path = (
        ROOT
        / "skills"
        / skill_name
        / "SKILL.md"
    )

    if not path.is_file():
        error(
            f"missing skill: {skill_name}"
        )
        return

    content = read(path)

    frontmatter(
        content,
        skill_name,
    )

    if "⸻" in content:
        error(
            f"{skill_name}: corruption marker found"
        )

    lower = content.lower()

    for token in [
        "lorem ipsum",
        "todo: fill",
        "replace this",
    ]:
        if token in lower:
            error(
                f"{skill_name}: "
                f"placeholder content found: {token}"
            )

    if len(
        re.findall(
            r"^\s*```",
            content,
            re.MULTILINE,
        )
    ) % 2:
        error(
            f"{skill_name}: "
            "unbalanced code fences"
        )

    count = meaningful_lines(content)

    if count < 40:
        error(
            f"{skill_name}: "
            f"suspiciously small ({count} meaningful lines)"
        )

    if not re.search(
        r"^#\s+\S+",
        content,
        re.MULTILINE,
    ):
        error(
            f"{skill_name}: "
            "missing top-level title"
        )

    levels = heading_levels(content)

    if levels:
        if levels[0] != 1:
            warning(
                f"{skill_name}: "
                f"first Markdown heading is H{levels[0]}"
            )

        for previous, current in zip(
            levels,
            levels[1:],
        ):
            if current - previous > 2:
                error(
                    f"{skill_name}: "
                    f"excessive heading hierarchy jump "
                    f"{previous}->{current}"
                )

    validate_concepts(
        skill_name,
        content,
    )

    provider_tokens = [
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

    for token in provider_tokens:
        if token in lower:
            error(
                f"{skill_name}: "
                f"provider-specific token found: {token}"
            )


def validate_skill_inventory():
    skills_root = ROOT / "skills"

    if not skills_root.is_dir():
        error(
            "missing skills directory"
        )
        return

    discovered = sorted(
        path.parent.name
        for path in skills_root.glob(
            "*/SKILL.md"
        )
    )

    expected = sorted(
        EXPECTED_SKILLS
    )

    if discovered != expected:
        error(
            f"skill inventory mismatch: "
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
                f"missing skills: "
                f"{', '.join(missing)}"
            )

        if extra:
            error(
                f"unexpected skills: "
                f"{', '.join(extra)}"
            )

    for skill in EXPECTED_SKILLS:
        validate_skill(skill)

    obsolete = (
        skills_root
        / "fly-by-animation"
    )

    if obsolete.exists():
        error(
            "obsolete split skill exists: "
            "skills/fly-by-animation"
        )

    merged = (
        skills_root
        / "scroll-world-flyby"
        / "SKILL.md"
    )

    if merged.is_file():
        content = read(merged).lower()

        matched = sum(
            term in content
            for term in [
                "scroll world",
                "fly-by",
                "flyby",
                "scroll-driven",
            ]
        )

        if matched < 2:
            error(
                "scroll-world-flyby does not clearly "
                "document the merged scroll/fly-by discipline"
            )


# ============================================================================
# Repository files
# ============================================================================

def validate_repository_files():
    for relative in REQUIRED_REPOSITORY_FILES:
        path = ROOT / relative

        if not path.is_file():
            error(
                f"missing repository file: {relative}"
            )
            continue

        if (
            relative != ".gitignore"
            and not read(path).strip()
        ):
            error(
                f"empty repository file: {relative}"
            )


def validate_markdown():
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue

        try:
            content = read(path)
        except (
            UnicodeDecodeError,
            OSError,
        ):
            continue

        relative = path.relative_to(ROOT)

        if len(
            re.findall(
                r"^\s*```",
                content,
                re.MULTILINE,
            )
        ) % 2:
            error(
                f"unbalanced code fences: {relative}"
            )

        for target in re.findall(
            r"\]\(([^)]+)\)",
            content,
        ):
            target = target.strip()

            if (
                "://" in target
                or target.startswith("mailto:")
                or target.startswith("#")
            ):
                continue

            target_path = (
                path.parent / target
            ).resolve()

            if not target_path.exists():
                error(
                    f"broken local link: "
                    f"{relative} -> {target}"
                )


def validate_no_obsolete_skill_files():
    obsolete = [
        ROOT / "core" / "discovery" / "SKILL.md",
        ROOT / "core" / "capability" / "SKILL.md",
        ROOT / "core" / "interaction" / "SKILL.md",
        ROOT / "core" / "challenge" / "SKILL.md",
        ROOT / "core" / "execution" / "SKILL.md",
        ROOT / "core" / "verification" / "SKILL.md",
        ROOT / "core" / "reporting" / "SKILL.md",
    ]

    for path in obsolete:
        if path.exists():
            error(
                "obsolete canonical skill file exists: "
                f"{path.relative_to(ROOT)}"
            )


# ============================================================================
# Dependency-free YAML parser
# ============================================================================

def strip_yaml_comment(value):
    value = value.strip()

    if not value:
        return value

    if value.startswith(("'", '"')):
        return value

    in_single = False
    in_double = False

    for index, char in enumerate(value):
        if char == "'" and not in_double:
            in_single = not in_single

        elif char == '"' and not in_single:
            in_double = not in_double

        elif (
            char == "#"
            and not in_single
            and not in_double
        ):
            if (
                index == 0
                or value[index - 1].isspace()
            ):
                return value[:index].rstrip()

    return value


def split_inline_items(value):
    items = []

    current = []
    in_single = False
    in_double = False

    for char in value:
        if char == "'" and not in_double:
            in_single = not in_single
            current.append(char)
            continue

        if char == '"' and not in_single:
            in_double = not in_double
            current.append(char)
            continue

        if (
            char == ","
            and not in_single
            and not in_double
        ):
            items.append(
                "".join(current).strip()
            )
            current = []
        else:
            current.append(char)

    if current:
        items.append(
            "".join(current).strip()
        )

    return items


def parse_scalar(value):
    value = strip_yaml_comment(
        value
    ).strip()

    if (
        len(value) >= 2
        and value[0] == value[-1]
        and value[0] in "\"'"
    ):
        return value[1:-1]

    if value == "[]":
        return []

    if value == "{}":
        return {}

    if value.lower() == "true":
        return True

    if value.lower() == "false":
        return False

    if value.lower() in {
        "null",
        "~",
    }:
        return None

    if (
        value.startswith("[")
        and value.endswith("]")
    ):
        inner = value[1:-1].strip()

        if not inner:
            return []

        return [
            parse_scalar(item)
            for item in split_inline_items(
                inner
            )
        ]

    return value


def prepare_yaml_lines(content):
    lines = []

    for number, raw in enumerate(
        content.splitlines(),
        start=1,
    ):
        if "\t" in raw:
            raise ValueError(
                f"line {number}: tabs are not allowed"
            )

        if not raw.strip():
            continue

        stripped = raw.lstrip(" ")

        if stripped.startswith("#"):
            continue

        indent = (
            len(raw)
            - len(stripped)
        )

        lines.append(
            {
                "number": number,
                "indent": indent,
                "text": stripped.rstrip(),
            }
        )

    return lines


def mapping_key(text):
    match = re.match(
        r"^([A-Za-z0-9_.-]+):(?:\s+(.*))?$",
        text,
    )

    if not match:
        return None

    return (
        match.group(1),
        match.group(2),
    )


def parse_yaml_block(
    lines,
    index,
    indent,
):
    if index >= len(lines):
        raise ValueError(
            "unexpected end of YAML"
        )

    if lines[index]["indent"] != indent:
        raise ValueError(
            f"line {lines[index]['number']}: "
            "invalid indentation"
        )

    if lines[index]["text"].startswith("- "):
        return parse_yaml_list(
            lines,
            index,
            indent,
        )

    return parse_yaml_mapping(
        lines,
        index,
        indent,
    )


def parse_yaml_mapping(
    lines,
    index,
    indent,
):
    result = {}

    while index < len(lines):
        line = lines[index]

        if line["indent"] < indent:
            break

        if line["indent"] > indent:
            raise ValueError(
                f"line {line['number']}: "
                "unexpected indentation"
            )

        text = line["text"]

        if text.startswith("- "):
            break

        parsed = mapping_key(text)

        if parsed is None:
            raise ValueError(
                f"line {line['number']}: "
                "invalid mapping syntax"
            )

        key, value_text = parsed

        if key in result:
            raise ValueError(
                f"line {line['number']}: "
                f"duplicate key '{key}'"
            )

        index += 1

        if value_text is not None:
            result[key] = parse_scalar(
                value_text
            )
            continue

        if (
            index < len(lines)
            and lines[index]["indent"] > indent
        ):
            child_indent = (
                lines[index]["indent"]
            )

            value, index = parse_yaml_block(
                lines,
                index,
                child_indent,
            )

            result[key] = value

        else:
            result[key] = None

    return result, index


def parse_yaml_list(
    lines,
    index,
    indent,
):
    result = []

    while index < len(lines):
        line = lines[index]

        if line["indent"] < indent:
            break

        if line["indent"] > indent:
            raise ValueError(
                f"line {line['number']}: "
                "unexpected list indentation"
            )

        text = line["text"]

        if not text.startswith("- "):
            break

        item_text = text[2:].strip()

        index += 1

        if not item_text:
            if (
                index < len(lines)
                and lines[index]["indent"] > indent
            ):
                child_indent = (
                    lines[index]["indent"]
                )

                child, index = parse_yaml_block(
                    lines,
                    index,
                    child_indent,
                )

                result.append(child)
            else:
                result.append(None)

            continue

        parsed = mapping_key(item_text)

        if parsed is None:
            result.append(
                parse_scalar(item_text)
            )
            continue

        key, value_text = parsed

        item = {}

        if value_text is None:
            if (
                index < len(lines)
                and lines[index]["indent"] > indent
            ):
                child_indent = (
                    lines[index]["indent"]
                )

                child, index = parse_yaml_block(
                    lines,
                    index,
                    child_indent,
                )

                item[key] = child
            else:
                item[key] = None

        else:
            item[key] = parse_scalar(
                value_text
            )

        if (
            index < len(lines)
            and lines[index]["indent"] > indent
        ):
            child_indent = (
                lines[index]["indent"]
            )

            child, index = parse_yaml_block(
                lines,
                index,
                child_indent,
            )

            if not isinstance(child, dict):
                raise ValueError(
                    "list item continuation "
                    "must be a mapping"
                )

            for child_key, child_value in child.items():
                if child_key in item:
                    raise ValueError(
                        f"duplicate list-item key "
                        f"'{child_key}'"
                    )

                item[child_key] = child_value

        result.append(item)

    return result, index


def parse_simple_yaml(content):
    """
    Parse the constrained YAML subset used by Nexra.

    This is intentionally NOT a general YAML parser.
    """

    lines = prepare_yaml_lines(content)

    if not lines:
        return {}

    root_indent = lines[0]["indent"]

    result, index = parse_yaml_block(
        lines,
        0,
        root_indent,
    )

    if index != len(lines):
        line = lines[index]

        raise ValueError(
            f"line {line['number']}: "
            "could not parse YAML structure"
        )

    return result


# ============================================================================
# Adapter validation
# ============================================================================

def validate_semver(value, label):
    if not isinstance(value, str):
        error(
            f"{label}: "
            "must use semantic version format"
        )
        return

    if not re.fullmatch(
        r"[0-9]+\.[0-9]+\.[0-9]+",
        value,
    ):
        error(
            f"{label}: "
            "must use semantic version format"
        )


def validate_adapter_manifest(
    adapter,
    manifest,
):
    try:
        data = parse_simple_yaml(
            read(manifest)
        )

    except ValueError as exc:
        error(
            f"adapter {adapter}: "
            f"invalid manifest YAML: {exc}"
        )
        return

    # ------------------------------------------------------------------------
    # Required fields from ADAPTER-SPEC.md
    # ------------------------------------------------------------------------

    required = [
        "id",
        "name",
        "adapter",
        "installation",
        "skills",
        "capabilities",
    ]

    for key in required:
        if key not in data:
            error(
                f"adapter {adapter}: "
                f"missing top-level field '{key}'"
            )

    # ------------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------------

    if data.get("id") != adapter:
        error(
            f"adapter {adapter}: "
            f"id mismatch "
            f"(declared '{data.get('id')}')"
        )

    if (
        not isinstance(
            data.get("name"),
            str,
        )
        or not data.get(
            "name",
            "",
        ).strip()
    ):
        error(
            f"adapter {adapter}: "
            "name must be a non-empty string"
        )

    # ------------------------------------------------------------------------
    # Adapter metadata
    # ------------------------------------------------------------------------

    adapter_block = data.get(
        "adapter"
    )

    if not isinstance(
        adapter_block,
        dict,
    ):
        error(
            f"adapter {adapter}: "
            "'adapter' must be a mapping"
        )

    else:
        for key in (
            "schema_version",
            "version",
            "platform",
        ):
            if key not in adapter_block:
                error(
                    f"adapter {adapter}: "
                    f"missing adapter.{key}"
                )

        schema = str(
            adapter_block.get(
                "schema_version",
                "",
            )
        )

        if schema != "1.0":
            error(
                f"adapter {adapter}: "
                f"unsupported adapter.schema_version "
                f"'{schema}'"
            )

        validate_semver(
            adapter_block.get("version"),
            f"adapter {adapter}: "
            "adapter.version",
        )

        if (
            str(
                adapter_block.get(
                    "platform",
                    "",
                )
            )
            != adapter
        ):
            error(
                f"adapter {adapter}: "
                "adapter.platform mismatch"
            )

    # ------------------------------------------------------------------------
    # Reject legacy adapter schema
    # ------------------------------------------------------------------------

    legacy_fields = [
        "schema_version",
        "version",
        "type",
        "target",
        "claims",
    ]

    for field in legacy_fields:
        if field in data:
            error(
                f"adapter {adapter}: "
                f"legacy top-level field '{field}' "
                "must be removed"
            )

    # ------------------------------------------------------------------------
    # Installation
    # ------------------------------------------------------------------------

    installation = data.get(
        "installation"
    )

    if not isinstance(
        installation,
        dict,
    ):
        error(
            f"adapter {adapter}: "
            "installation must be a mapping"
        )

    else:
        for scope in (
            "project",
            "global",
        ):
            block = installation.get(
                scope
            )

            if not isinstance(
                block,
                dict,
            ):
                error(
                    f"adapter {adapter}: "
                    f"installation.{scope} "
                    "must be a mapping"
                )
                continue

            supported = block.get(
                "supported"
            )

            if not isinstance(
                supported,
                bool,
            ):
                error(
                    f"adapter {adapter}: "
                    f"installation.{scope}.supported "
                    "must be boolean"
                )

            if supported:
                target = block.get(
                    "target"
                )

                if (
                    not isinstance(
                        target,
                        str,
                    )
                    or not target.strip()
                ):
                    error(
                        f"adapter {adapter}: "
                        f"installation.{scope}.target "
                        "must be a non-empty string "
                        "when supported"
                    )

        strategy = installation.get(
            "strategy"
        )

        if strategy is not None:
            allowed = {
                "native-skill-directory",
                "portable-agent-skills",
            }

            if strategy not in allowed:
                error(
                    f"adapter {adapter}: "
                    f"unsupported installation.strategy "
                    f"'{strategy}'"
                )

    # ------------------------------------------------------------------------
    # Skills
    # ------------------------------------------------------------------------

    skills = data.get(
        "skills"
    )

    if not isinstance(
        skills,
        dict,
    ):
        error(
            f"adapter {adapter}: "
            "skills must be a mapping"
        )

    else:
        source = skills.get(
            "source"
        )

        if (
            not isinstance(
                source,
                str,
            )
            or not source.strip()
        ):
            error(
                f"adapter {adapter}: "
                "skills.source must be a "
                "non-empty string"
            )

        else:
            manifest_relative = (
                manifest.parent / source
            ).resolve()

            repository_relative = (
                ROOT / source
            ).resolve()

            canonical = (
                ROOT / "skills"
            ).resolve()

            if (
                manifest_relative != canonical
                and repository_relative != canonical
            ):
                error(
                    f"adapter {adapter}: "
                    "skills.source must resolve "
                    "to the canonical skills directory"
                )

        discovery = skills.get(
            "discovery"
        )

        allowed_discovery = {
            "native",
            "instruction-file",
            "configuration",
            "filesystem",
            "manual",
            "unsupported",
        }

        if not isinstance(
            discovery,
            str,
        ):
            error(
                f"adapter {adapter}: "
                "skills.discovery must be a string"
            )

        elif discovery not in allowed_discovery:
            error(
                f"adapter {adapter}: "
                f"unsupported skills.discovery "
                f"'{discovery}'"
            )

    # ------------------------------------------------------------------------
    # Capabilities
    # ------------------------------------------------------------------------

    capabilities = data.get(
        "capabilities"
    )

    if not isinstance(
        capabilities,
        dict,
    ):
        error(
            f"adapter {adapter}: "
            "capabilities must be a mapping"
        )

    else:
        allowed_states = {
            "FULL",
            "SUITABLE",
            "CONSTRAINED",
            "UNSUITABLE",
            "unknown",
            "host-dependent",
            True,
            False,
        }

        for capability, value in capabilities.items():
            if isinstance(value, dict):
                state = value.get(
                    "state"
                )

                if state not in allowed_states:
                    error(
                        f"adapter {adapter}: "
                        f"unsupported capability state "
                        f"for '{capability}': "
                        f"{state}"
                    )

                evidence = value.get(
                    "evidence"
                )

                if evidence is not None:
                    if not isinstance(
                        evidence,
                        list,
                    ):
                        error(
                            f"adapter {adapter}: "
                            f"capabilities.{capability}.evidence "
                            "must be a list"
                        )

            elif value not in allowed_states:
                error(
                    f"adapter {adapter}: "
                    f"unsupported capability state "
                    f"for '{capability}': "
                    f"{value}"
                )

    # ------------------------------------------------------------------------
    # Compatibility
    # ------------------------------------------------------------------------

    compatibility = data.get(
        "compatibility"
    )

    if compatibility is not None:
        if not isinstance(
            compatibility,
            dict,
        ):
            error(
                f"adapter {adapter}: "
                "compatibility must be a mapping"
            )

        else:
            status = compatibility.get(
                "status"
            )

            if status is not None:
                allowed_statuses = {
                    "verified",
                    "unverified",
                    "standard",
                }

                if status not in allowed_statuses:
                    error(
                        f"adapter {adapter}: "
                        f"unsupported compatibility.status "
                        f"'{status}'"
                    )

            evidence = compatibility.get(
                "evidence"
            )

            if evidence is not None:
                if not isinstance(
                    evidence,
                    list,
                ):
                    error(
                        f"adapter {adapter}: "
                        "compatibility.evidence "
                        "must be a list"
                    )

                else:
                    for item in evidence:
                        if (
                            not isinstance(
                                item,
                                str,
                            )
                            or not re.match(
                                r"^https?://",
                                item,
                                re.IGNORECASE,
                            )
                        ):
                            error(
                                f"adapter {adapter}: "
                                "compatibility evidence "
                                "must contain URLs"
                            )

            if (
                status == "verified"
                and not evidence
            ):
                error(
                    f"adapter {adapter}: "
                    "verified adapter requires "
                    "compatibility evidence"
                )

    # ------------------------------------------------------------------------
    # Limitations
    # ------------------------------------------------------------------------

    limitations = data.get(
        "limitations"
    )

    if limitations is not None:
        if not isinstance(
            limitations,
            list,
        ):
            error(
                f"adapter {adapter}: "
                "limitations must be a list"
            )

    # ------------------------------------------------------------------------
    # Verification
    # ------------------------------------------------------------------------

    verification = data.get(
        "verification"
    )

    if verification is not None:
        if not isinstance(
            verification,
            dict,
        ):
            error(
                f"adapter {adapter}: "
                "verification must be a mapping"
            )

        else:
            for scope in (
                "project",
                "global",
            ):
                block = verification.get(
                    scope
                )

                if block is None:
                    continue

                if not isinstance(
                    block,
                    dict,
                ):
                    error(
                        f"adapter {adapter}: "
                        f"verification.{scope} "
                        "must be a mapping"
                    )
                    continue

                expected_path = block.get(
                    "expected_path"
                )

                if (
                    not isinstance(
                        expected_path,
                        str,
                    )
                    or not expected_path.strip()
                ):
                    error(
                        f"adapter {adapter}: "
                        f"verification.{scope}.expected_path "
                        "must be a non-empty string"
                    )


# ============================================================================
# Adapter registry
# ============================================================================

def validate_adapter_registry():
    path = (
        ROOT
        / "adapters"
        / "registry.yaml"
    )

    if not path.is_file():
        error(
            "missing adapters/registry.yaml"
        )
        return

    try:
        registry = parse_simple_yaml(
            read(path)
        )
    except ValueError as exc:
        error(
            f"adapters/registry.yaml: "
            f"invalid YAML: {exc}"
        )
        return

    text = read(path)

    for adapter in EXPECTED_ADAPTERS:
        if not re.search(
            rf"(?m)^\s*-\s*(?:id:\s*)?"
            rf"{re.escape(adapter)}\s*$",
            text,
        ):
            if not re.search(
                rf"(?m)^\s*id:\s*"
                rf"{re.escape(adapter)}\s*$",
                text,
            ):
                error(
                    f"adapter registry: "
                    f"missing '{adapter}'"
                )

    # Registry should not reference a known adapter that has no directory.
    adapter_dirs = {
        path.parent.name
        for path in (
            ROOT / "adapters"
        ).glob("*/adapter.yaml")
    }

    registry_ids = set()

    def collect(value):
        if isinstance(value, dict):
            if isinstance(
                value.get("id"),
                str,
            ):
                registry_ids.add(
                    value["id"]
                )

            for child in value.values():
                collect(child)

        elif isinstance(value, list):
            for child in value:
                if isinstance(
                    child,
                    str,
                ):
                    registry_ids.add(child)
                else:
                    collect(child)

    collect(registry)

    for registry_id in registry_ids:
        if registry_id in {
            "registry",
            "adapters",
        }:
            continue

        if (
            registry_id in EXPECTED_ADAPTERS
            and registry_id not in adapter_dirs
        ):
            error(
                "adapter registry references "
                f"missing adapter '{registry_id}'"
            )


def validate_adapters():
    root = ROOT / "adapters"

    if not root.is_dir():
        error(
            "missing adapters directory"
        )
        return

    discovered = sorted(
        path.parent.name
        for path in root.glob(
            "*/adapter.yaml"
        )
    )

    expected = sorted(
        EXPECTED_ADAPTERS
    )

    if discovered != expected:
        error(
            f"adapter inventory mismatch: "
            f"expected {len(expected)}, "
            f"found {len(discovered)}"
        )

        missing = sorted(
            set(expected)
            - set(discovered)
        )

        extra = sorted(
            set(discovered)
            - set(expected)
        )

        if missing:
            error(
                f"missing adapters: "
                f"{', '.join(missing)}"
            )

        if extra:
            error(
                f"unexpected adapters: "
                f"{', '.join(extra)}"
            )

    validate_adapter_registry()

    collective = (
        root / "README.md"
    )

    if (
        not collective.is_file()
        or not read(collective).strip()
    ):
        error(
            "missing/empty adapters/README.md"
        )

    for adapter in EXPECTED_ADAPTERS:
        manifest = (
            root
            / adapter
            / "adapter.yaml"
        )

        if not manifest.is_file():
            error(
                f"missing adapter manifest: "
                f"{adapter}"
            )
            continue

        validate_adapter_manifest(
            adapter,
            manifest,
        )

        individual_readme = (
            root
            / adapter
            / "README.md"
        )

        if individual_readme.exists():
            warning(
                f"adapter {adapter}: "
                "individual README.md exists; "
                "documentation should remain collective"
            )


# ============================================================================
# Integration validation
# ============================================================================

def validate_integration_file(
    path,
    expected_id,
    kind,
):
    if not path.is_file():
        return

    try:
        data = parse_simple_yaml(
            read(path)
        )
    except ValueError as exc:
        error(
            f"{kind} {expected_id}: "
            f"invalid YAML: {exc}"
        )
        return

    if not isinstance(
        data,
        dict,
    ):
        error(
            f"{kind} {expected_id}: "
            "manifest must be a mapping"
        )
        return

    if data.get("id") != expected_id:
        error(
            f"{kind} {expected_id}: "
            f"id mismatch "
            f"(declared '{data.get('id')}')"
        )

    if data.get("version") != "0.1.1":
        error(
            f"{kind} {expected_id}: "
            "version must be 0.1.1 "
            f"(found '{data.get('version')}')"
        )


def validate_integrations():
    root = ROOT / "integrations"

    registry_path = (
        root / "registry.yaml"
    )

    if not registry_path.is_file():
        error(
            "missing integrations/registry.yaml"
        )
        return

    try:
        registry = parse_simple_yaml(
            read(registry_path)
        )
    except ValueError as exc:
        error(
            f"integrations/registry.yaml: "
            f"invalid YAML: {exc}"
        )
        return

    if not isinstance(
        registry,
        dict,
    ):
        error(
            "integrations/registry.yaml "
            "must be a mapping"
        )

    elif registry.get("version") != "0.1.1":
        error(
            "integrations registry must "
            "declare version 0.1.1"
        )

    plugins_root = (
        root / "plugins"
    )

    connectors_root = (
        root / "connectors"
    )

    if not plugins_root.is_dir():
        error(
            "missing integrations/plugins directory"
        )
        plugin_files = []
    else:
        plugin_files = sorted(
            p.stem
            for p in plugins_root.glob(
                "*.yaml"
            )
        )

    if not connectors_root.is_dir():
        error(
            "missing integrations/connectors directory"
        )
        connector_files = []
    else:
        connector_files = sorted(
            p.stem
            for p in connectors_root.glob(
                "*.yaml"
            )
        )

    expected_plugins = sorted(
        EXPECTED_PLUGINS
    )

    expected_connectors = sorted(
        EXPECTED_CONNECTORS
    )

    if plugin_files != expected_plugins:
        error(
            f"plugin inventory mismatch: "
            f"expected {len(expected_plugins)}, "
            f"found {len(plugin_files)}"
        )

        missing = sorted(
            set(expected_plugins)
            - set(plugin_files)
        )

        extra = sorted(
            set(plugin_files)
            - set(expected_plugins)
        )

        if missing:
            error(
                f"missing plugins: "
                f"{', '.join(missing)}"
            )

        if extra:
            error(
                f"unexpected plugins: "
                f"{', '.join(extra)}"
            )

    if connector_files != expected_connectors:
        error(
            f"connector inventory mismatch: "
            f"expected {len(expected_connectors)}, "
            f"found {len(connector_files)}"
        )

        missing = sorted(
            set(expected_connectors)
            - set(connector_files)
        )

        extra = sorted(
            set(connector_files)
            - set(expected_connectors)
        )

        if missing:
            error(
                f"missing connectors: "
                f"{', '.join(missing)}"
            )

        if extra:
            error(
                f"unexpected connectors: "
                f"{', '.join(extra)}"
            )

    for plugin in EXPECTED_PLUGINS:
        validate_integration_file(
            plugins_root / f"{plugin}.yaml",
            plugin,
            "plugin",
        )

    for connector in EXPECTED_CONNECTORS:
        validate_integration_file(
            connectors_root / f"{connector}.yaml",
            connector,
            "connector",
        )


# ============================================================================
# Tests
# ============================================================================

def validate_tests():
    for relative in REQUIRED_TEST_FILES:
        path = ROOT / relative

        if not path.is_file():
            error(
                f"missing test file: {relative}"
            )
        elif not read(path).strip():
            error(
                f"empty test file: {relative}"
            )


# ============================================================================
# Package
# ============================================================================

def validate_package():
    path = ROOT / "package.json"

    if not path.is_file():
        return

    try:
        package = json.loads(
            read(path)
        )
    except json.JSONDecodeError as exc:
        error(
            f"package.json: "
            f"invalid JSON: {exc}"
        )
        return

    if package.get("name") != "nexra-skills":
        error(
            "package.json: "
            f"expected name 'nexra-skills', "
            f"found '{package.get('name')}'"
        )

    if package.get("version") != "0.1.1":
        error(
            "package.json: "
            f"expected version '0.1.1', "
            f"found '{package.get('version')}'"
        )

    bin_config = package.get(
        "bin",
        {},
    )

    if (
        not isinstance(
            bin_config,
            dict,
        )
        or bin_config.get("nexra")
        != "cli/bin/nexra.js"
    ):
        error(
            "package.json: "
            "nexra bin entry is incorrect"
        )

    repository = package.get(
        "repository",
        {},
    )

    expected_repo = (
        "https://github.com/"
        "Muhammad-Wasif-Qamar/Nexra.git"
    )

    if (
        not isinstance(
            repository,
            dict,
        )
        or repository.get("url")
        != expected_repo
    ):
        error(
            "package.json: "
            "repository URL is incorrect"
        )


# ============================================================================
# Project naming
# ============================================================================

def validate_naming():
    """
    Ensure the current project identity is Nexra.

    CHANGELOG.md legitimately contains historical references to the previous
    project identity.

    This script is also excluded because its validator logic necessarily
    contains the legacy-token patterns it is checking for.
    """

    excluded = {
        "CHANGELOG.md",
        "scripts/validate.py",
    }

    legacy_fragments = [
        ".the-builder",
        "the-builder",
        "The-Builder",
        "THE-BUILDER",
        "@wasif-qamar/the-builder",
    ]

    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue

        if not path.is_file():
            continue

        relative = path.relative_to(
            ROOT
        ).as_posix()

        if relative in excluded:
            continue

        try:
            content = read(path)
        except (
            UnicodeDecodeError,
            OSError,
        ):
            continue

        for token in legacy_fragments:
            if token in content:
                error(
                    "obsolete project identity found in "
                    f"{relative}: {token}"
                )


# ============================================================================
# Main
# ============================================================================

def main():
    validate_repository_files()
    validate_skill_inventory()
    validate_no_obsolete_skill_files()
    validate_markdown()
    validate_adapters()
    validate_integrations()
    validate_tests()
    validate_package()
    validate_naming()

    for message in WARNINGS:
        print(
            "WARN:",
            message,
        )

    if ERRORS:
        print(
            f"FAIL: {len(ERRORS)} error(s)"
        )

        for message in ERRORS:
            print(
                " -",
                message,
            )

        sys.exit(1)

    print(
        "PASS: repository validation\n"
        f"skills={len(EXPECTED_SKILLS)} "
        f"foundation={len(FOUNDATION_SKILLS)} "
        f"adapters={len(EXPECTED_ADAPTERS)} "
        f"plugins={len(EXPECTED_PLUGINS)} "
        f"connectors={len(EXPECTED_CONNECTORS)}"
    )


if __name__ == "__main__":
    main()
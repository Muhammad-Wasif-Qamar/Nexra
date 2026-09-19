#!/usr/bin/env python3
"""
Dependency-light behavioral and contract tests for Nexra.

These tests intentionally validate concepts and behavior rather than requiring
specific wording. Skills are instructional documents and may evolve their
headings and terminology without breaking the test suite.

The adapter tests validate Nexra adapter schema v1.0 without requiring PyYAML.
Only the constrained YAML structure used by Nexra manifests is inspected.
"""

from pathlib import Path
import json
import os
import re
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]

fail = []


# ---------------------------------------------------------------------------
# Test helpers
# ---------------------------------------------------------------------------

def check(name, condition, detail=""):
    """Record a failed test without stopping the suite."""
    if not condition:
        message = name
        if detail:
            message += f": {detail}"
        fail.append(message)


def read_skill(name):
    path = ROOT / "skills" / name / "SKILL.md"

    if not path.is_file():
        check(f"skill-file:{name}", False, "SKILL.md missing")
        return ""

    return path.read_text(encoding="utf-8").lower()


def contains_any(text, terms):
    return any(term.lower() in text for term in terms)


def contains_all(text, terms):
    return all(term.lower() in text for term in terms)


def run_command(command, cwd=None, env=None):
    return subprocess.run(
        command,
        cwd=cwd,
        env=env,
        capture_output=True,
        text=True,
    )


# ---------------------------------------------------------------------------
# Canonical skills
# ---------------------------------------------------------------------------

EXPECTED_SKILLS = {
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
}


skills_root = ROOT / "skills"

skills = sorted(
    path.parent.name
    for path in skills_root.glob("*/SKILL.md")
)

check(
    "skill-discovery",
    set(skills) == EXPECTED_SKILLS,
    f"found {len(skills)}",
)

check(
    "merged-scroll-flyby",
    "scroll-world-flyby" in skills
    and "fly-by-animation" not in skills,
)


# ---------------------------------------------------------------------------
# Foundation skill concepts
# ---------------------------------------------------------------------------

FOUNDATION_CONCEPTS = {
    "project-discovery": [
        ["discover", "discovery"],
        ["observed", "observation", "fact", "evidence"],
        ["verified", "verify"],
        ["unknown", "uncertain"],
        ["environment"],
        ["architecture", "structure"],
    ],

    "capability-assessment": [
        ["full"],
        ["suitable"],
        ["constrained"],
        ["unsuitable"],
        ["model"],
        ["agent"],
        ["environment"],
        ["evidence"],
    ],

    "interaction": [
        ["material", "necessary"],
        ["discover", "discovery"],
        ["user authority", "user decision", "user decides"],
        ["question", "ask"],
        ["ambiguity"],
    ],

    "challenge": [
        ["evidence"],
        [
            "confirmed",
            "confirmed problem",
            "confirmed vulnerability",
        ],
        ["likely", "likely issue"],
        ["tradeoff"],
        ["user authority", "user decides"],
        ["preference"],
    ],

    "execution": [
        ["incremental", "incrementally"],
        ["bounded", "scope"],
        ["diff", "changes"],
        ["plan"],
        ["execute", "execution"],
        ["verify", "verification"],
    ],

    "verification": [
        ["acceptance criterion", "acceptance criteria"],
        ["evidence"],
        ["blocked"],
        ["unverified"],
        ["test", "check"],
        ["verification"],
    ],

    "reporting": [
        ["result", "results"],
        ["changes", "changed"],
        ["verification", "verified"],
        ["decision", "decisions"],
        ["limitations", "unverified", "remaining"],
    ],
}


for skill_name, concept_groups in FOUNDATION_CONCEPTS.items():
    text = read_skill(skill_name)

    for index, group in enumerate(concept_groups, start=1):
        check(
            f"{skill_name}:concept-{index}",
            contains_any(text, group),
            f"expected one of: {', '.join(group)}",
        )


# ---------------------------------------------------------------------------
# Domain skill concepts
# ---------------------------------------------------------------------------

DOMAIN_CONCEPTS = {
    "ui-ux-design": [
        ["information hierarchy", "visual hierarchy"],
        ["keyboard", "keyboard navigation"],
        ["touch target", "touch targets"],
        ["responsive", "responsive design"],
        ["accessibility", "accessible"],
    ],

    "animation-design": [
        ["easing"],
        ["reduced motion", "reduced-motion"],
        ["state transition", "state transitions"],
        ["duration", "timing"],
        ["performance"],
    ],

    "3d-web-design": [
        ["scene graph", "scene hierarchy", "scene structure"],
        ["renderer", "rendering"],
        ["texture", "textures", "material"],
        ["camera"],
        ["performance"],
    ],

    "scroll-world-flyby": [
        ["camera"],
        ["waypoint", "waypoints"],
        ["parallax", "depth"],
        ["normalized", "normalized timeline"],
        ["scroll"],
        ["scene"],
    ],

    "content-code-optimization": [
        ["content"],
        ["code"],
        ["bundle", "bundle size"],
        ["before/after", "before and after", "baseline"],
        ["performance"],
    ],

    "seo": [
        ["canonical"],
        ["sitemap"],
        ["structured data", "schema"],
        ["crawl", "index"],
        ["metadata"],
    ],

    "security": [
        ["trust boundary", "trust boundaries"],
        ["least privilege"],
        ["xss", "cross-site scripting"],
        ["authentication", "authorization"],
        ["input validation", "input"],
    ],

    "reviewer": [
        ["severity"],
        ["recommendation"],
        ["confidence"],
        ["evidence"],
        ["impact"],
        ["review"],
    ],
}


for skill_name, concept_groups in DOMAIN_CONCEPTS.items():
    text = read_skill(skill_name)

    for index, group in enumerate(concept_groups, start=1):
        check(
            f"{skill_name}:specialized-{index}",
            contains_any(text, group),
            f"expected one of: {', '.join(group)}",
        )


# ---------------------------------------------------------------------------
# Skill behavior fixtures
# ---------------------------------------------------------------------------

cases_path = ROOT / "tests" / "skills" / "cases.md"

if cases_path.is_file():
    cases = cases_path.read_text(
        encoding="utf-8"
    ).lower()

    fixture_groups = {
        "reuse": ["reuse", "reusable"],
        "keyboard": ["keyboard", "keyboard navigation"],
        "reduced-motion": ["reduced-motion", "reduced motion"],
        "normalized-timeline": ["normalized timeline", "normalized"],
        "content": ["content"],
        "security": ["security", "xss", "authentication"],
        "severity": ["severity", "critical", "high", "medium"],
    }

    for name, terms in fixture_groups.items():
        check(
            f"behavior-fixture:{name}",
            contains_any(cases, terms),
            f"expected one of: {', '.join(terms)}",
        )

else:
    check(
        "behavior-fixtures",
        False,
        "tests/skills/cases.md missing",
    )


# ---------------------------------------------------------------------------
# Core coverage fixtures
# ---------------------------------------------------------------------------

core_cases_path = ROOT / "tests" / "core" / "cases.md"

if core_cases_path.is_file():
    core_cases = core_cases_path.read_text(
        encoding="utf-8"
    ).lower()

    core_groups = {
        "discovery": ["discovery", "discover"],
        "capability": ["capability"],
        "interaction": ["interaction"],
        "challenge": ["challenge"],
        "execution": ["execution", "execute"],
        "verification": ["verification", "verify"],
        "reporting": ["reporting", "report"],
    }

    for name, terms in core_groups.items():
        check(
            f"core-coverage:{name}",
            contains_any(core_cases, terms),
        )

else:
    check(
        "core-coverage",
        False,
        "tests/core/cases.md missing",
    )


# ---------------------------------------------------------------------------
# Challenge coverage fixtures
# ---------------------------------------------------------------------------

challenge_cases_path = ROOT / "tests" / "challenge" / "cases.md"

if challenge_cases_path.is_file():
    challenge_cases = challenge_cases_path.read_text(
        encoding="utf-8"
    ).lower()

    challenge_groups = {
        "user-authority": [
            "user authority",
            "user decides",
            "user decision",
        ],
        "technical-tradeoffs": [
            "technical tradeoff",
            "technical tradeoffs",
            "tradeoff",
        ],
        "security": ["security"],
        "scope": ["scope", "scope creep"],
    }

    for name, terms in challenge_groups.items():
        check(
            f"challenge-coverage:{name}",
            contains_any(challenge_cases, terms),
        )

else:
    check(
        "challenge-coverage",
        False,
        "tests/challenge/cases.md missing",
    )


# ---------------------------------------------------------------------------
# Adapter contract
# ---------------------------------------------------------------------------

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


ADAPTER_SCHEMA_VERSION = "1.0"
CURRENT_ADAPTER_VERSION = "0.1.0"

VALID_DISCOVERY_MODES = {
    "native",
    "portable",
}

VALID_INSTALL_STRATEGIES = {
    "native-skill-directory",
    "portable-agent-skills",
}

VALID_COMPATIBILITY_STATUSES = {
    "verified",
    "unverified",
    "standard",
}

VALID_CAPABILITY_VALUES = {
    "true",
    "false",
    "unknown",
    "host-dependent",
}


def read_manifest(adapter):
    path = ROOT / "adapters" / adapter / "adapter.yaml"

    if not path.is_file():
        check(
            f"adapter:{adapter}",
            False,
            "adapter.yaml missing",
        )
        return ""

    return path.read_text(encoding="utf-8")


def simple_yaml_fields(content):
    """
    Lightweight field extraction for the adapter contract.

    This is intentionally not a general YAML parser.

    The returned mapping uses field names without the trailing colon and
    records indentation so tests can distinguish top-level fields from
    nested fields.
    """
    fields = {}

    for line in content.splitlines():
        if not line.strip():
            continue

        if line.lstrip().startswith("#"):
            continue

        match = re.match(
            r"^(\s*)([A-Za-z0-9_.-]+):(?:\s+(.*))?$",
            line,
        )

        if match:
            indentation = len(match.group(1))
            key = match.group(2)
            value = match.group(3) or ""

            fields.setdefault(key, []).append(
                (indentation, value)
            )

    return fields


def top_level_field_exists(fields, field):
    """
    Return True when a field exists at indentation level zero.
    """
    return any(
        indentation == 0
        for indentation, _ in fields.get(field, [])
    )


def get_top_level_value(content, field):
    """
    Extract a scalar value from a top-level YAML field.

    Example:

        id: generic

    returns:

        generic
    """
    match = re.search(
        rf"(?m)^{re.escape(field)}:\s*(.*?)\s*$",
        content,
    )

    if not match:
        return None

    value = match.group(1).strip()

    if len(value) >= 2:
        if value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]

    return value


def get_nested_block(content, field, parent_indent=0):
    """
    Extract a simple YAML mapping block.

    For example:

        adapter:
          schema_version: "1.0"
          version: "0.1.0"
          platform: claude-code

    get_nested_block(content, "adapter") returns the indented body.

    This is not intended to parse arbitrary YAML.
    """
    pattern = re.compile(
        rf"(?m)^{re.escape(' ' * parent_indent)}"
        rf"{re.escape(field)}:\s*$"
        rf"\n((?:(?:^[ ]{{{parent_indent + 2},}}.*\n?)|"
        rf"(?:^$\n?))*)"
    )

    match = pattern.search(content)

    if not match:
        return ""

    return match.group(1)


def field_value_in_block(block, field):
    """
    Extract a scalar field value from a nested YAML block.
    """
    match = re.search(
        rf"(?m)^[ ]+{re.escape(field)}:\s*(.*?)\s*$",
        block,
    )

    if not match:
        return None

    value = match.group(1).strip()

    if len(value) >= 2:
        if value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]

    return value


def field_exists_in_block(block, field):
    return re.search(
        rf"(?m)^[ ]+{re.escape(field)}:",
        block,
    ) is not None


for adapter in EXPECTED_ADAPTERS:
    adapter_root = ROOT / "adapters" / adapter
    manifest_path = adapter_root / "adapter.yaml"

    # -----------------------------------------------------------------------
    # Basic file existence
    # -----------------------------------------------------------------------

    check(
        f"adapter:{adapter}",
        manifest_path.is_file(),
        "adapter.yaml missing",
    )

    if not manifest_path.is_file():
        continue

    content = read_manifest(adapter)
    fields = simple_yaml_fields(content)

    # -----------------------------------------------------------------------
    # Top-level contract fields
    # -----------------------------------------------------------------------

    top_level_fields = [
        "id",
        "name",
        "adapter",
        "detection",
        "installation",
        "skills",
        "capabilities",
        "compatibility",
    ]

    for field in top_level_fields:
        check(
            f"adapter-{field}:{adapter}",
            top_level_field_exists(fields, field),
            f"top-level {field}: missing",
        )

    # -----------------------------------------------------------------------
    # Top-level id and name
    # -----------------------------------------------------------------------

    id_value = get_top_level_value(content, "id")
    name_value = get_top_level_value(content, "name")

    check(
        f"adapter-id-value:{adapter}",
        id_value == adapter,
        f"expected {adapter!r}, found {id_value!r}",
    )

    check(
        f"adapter-name-value:{adapter}",
        bool(name_value),
        "adapter name is empty",
    )

    # -----------------------------------------------------------------------
    # Adapter metadata block
    # -----------------------------------------------------------------------

    adapter_block = get_nested_block(
        content,
        "adapter",
        parent_indent=0,
    )

    check(
        f"adapter-block-valid:{adapter}",
        bool(adapter_block.strip()),
        "adapter block is empty or missing",
    )

    if adapter_block:
        check(
            f"adapter-schema-version:{adapter}",
            field_value_in_block(
                adapter_block,
                "schema_version",
            ) == ADAPTER_SCHEMA_VERSION,
            "expected adapter.schema_version 1.0",
        )

        check(
            f"adapter-version:{adapter}",
            field_value_in_block(
                adapter_block,
                "version",
            ) == CURRENT_ADAPTER_VERSION,
            "expected adapter.version 0.1.0",
        )

        check(
            f"adapter-platform:{adapter}",
            field_value_in_block(
                adapter_block,
                "platform",
            ) == adapter,
            f"expected adapter.platform {adapter!r}",
        )

    # -----------------------------------------------------------------------
    # Legacy adapter schema detection
    #
    # schema_version and version are valid when nested under adapter:.
    # Only genuinely old top-level fields are prohibited.
    # -----------------------------------------------------------------------

    legacy_top_level_fields = [
        "type",
        "target",
        "skill_source",
        "claims",
    ]

    for legacy_field in legacy_top_level_fields:
        check(
            f"adapter-no-legacy-field:{adapter}:{legacy_field}",
            not top_level_field_exists(
                fields,
                legacy_field,
            ),
            f"legacy top-level field {legacy_field}: found",
        )

    check(
        f"adapter-schema-version-not-top-level:{adapter}",
        not top_level_field_exists(
            fields,
            "schema_version",
        ),
        "schema_version must be nested under adapter:",
    )

    check(
        f"adapter-version-not-top-level:{adapter}",
        not top_level_field_exists(
            fields,
            "version",
        ),
        "version must be nested under adapter:",
    )

    # -----------------------------------------------------------------------
    # Individual adapter READMEs are intentionally prohibited.
    # -----------------------------------------------------------------------

    check(
        f"adapter-no-readme:{adapter}",
        not (adapter_root / "README.md").exists(),
        "individual adapter README should not exist",
    )

    # -----------------------------------------------------------------------
    # Detection
    # -----------------------------------------------------------------------

    detection_block = get_nested_block(
        content,
        "detection",
        parent_indent=0,
    )

    check(
        f"adapter-detection-block:{adapter}",
        bool(detection_block.strip()),
        "detection block missing",
    )

    if detection_block:
        check(
            f"adapter-detection-commands:{adapter}",
            field_exists_in_block(
                detection_block,
                "commands",
            ),
            "detection.commands missing",
        )

    # -----------------------------------------------------------------------
    # Installation
    # -----------------------------------------------------------------------

    installation_block = get_nested_block(
        content,
        "installation",
        parent_indent=0,
    )

    check(
        f"adapter-installation-block:{adapter}",
        bool(installation_block.strip()),
        "installation block missing",
    )

    if installation_block:
        project_block = get_nested_block(
            installation_block,
            "project",
            parent_indent=2,
        )

        global_block = get_nested_block(
            installation_block,
            "global",
            parent_indent=2,
        )

        check(
            f"adapter-project-installation:{adapter}",
            bool(project_block.strip()),
            "installation.project missing",
        )

        check(
            f"adapter-global-installation:{adapter}",
            bool(global_block.strip()),
            "installation.global missing",
        )

        if project_block:
            project_supported = field_value_in_block(
                project_block,
                "supported",
            )

            check(
                f"adapter-project-supported:{adapter}",
                project_supported in {"true", "false"},
                "installation.project.supported must be boolean",
            )

            project_target = field_value_in_block(
                project_block,
                "target",
            )

            check(
                f"adapter-project-target:{adapter}",
                bool(project_target),
                "installation.project.target missing",
            )

        if global_block:
            global_supported = field_value_in_block(
                global_block,
                "supported",
            )

            check(
                f"adapter-global-supported:{adapter}",
                global_supported in {"true", "false"},
                "installation.global.supported must be boolean",
            )

            global_target = field_value_in_block(
                global_block,
                "target",
            )

            check(
                f"adapter-global-target:{adapter}",
                bool(global_target),
                "installation.global.target missing",
            )

        strategy = field_value_in_block(
            installation_block,
            "strategy",
        )

        check(
            f"adapter-install-strategy:{adapter}",
            strategy in VALID_INSTALL_STRATEGIES,
            (
                "expected one of: "
                + ", ".join(sorted(VALID_INSTALL_STRATEGIES))
            ),
        )

    # -----------------------------------------------------------------------
    # Skills
    # -----------------------------------------------------------------------

    skills_block = get_nested_block(
        content,
        "skills",
        parent_indent=0,
    )

    check(
        f"adapter-skills-block:{adapter}",
        bool(skills_block.strip()),
        "skills block missing",
    )

    if skills_block:
        source = field_value_in_block(
            skills_block,
            "source",
        )

        check(
            f"adapter-skill-source:{adapter}",
            source == "skills/",
            f"expected skills/, found {source!r}",
        )

        discovery = field_value_in_block(
            skills_block,
            "discovery",
        )

        check(
            f"adapter-skill-discovery:{adapter}",
            discovery in VALID_DISCOVERY_MODES,
            (
                "expected one of: "
                + ", ".join(sorted(VALID_DISCOVERY_MODES))
            ),
        )

    # -----------------------------------------------------------------------
    # Capabilities
    # -----------------------------------------------------------------------

    capabilities_block = get_nested_block(
        content,
        "capabilities",
        parent_indent=0,
    )

    check(
        f"adapter-capabilities-block:{adapter}",
        bool(capabilities_block.strip()),
        "capabilities block missing",
    )

    if capabilities_block:
        required_capabilities = [
            "discovery",
            "filesystem",
            "terminal",
            "browser",
            "mcp",
        ]

        for capability in required_capabilities:
            value = field_value_in_block(
                capabilities_block,
                capability,
            )

            check(
                f"adapter-capability:{adapter}:{capability}",
                value in VALID_CAPABILITY_VALUES,
                (
                    f"expected one of "
                    f"{sorted(VALID_CAPABILITY_VALUES)}, "
                    f"found {value!r}"
                ),
            )

        discovery_value = field_value_in_block(
            capabilities_block,
            "discovery",
        )

        check(
            f"adapter-capability-discovery:{adapter}",
            discovery_value in {"true", "false"},
            "capabilities.discovery must be boolean",
        )

    # -----------------------------------------------------------------------
    # Compatibility
    # -----------------------------------------------------------------------

    compatibility_block = get_nested_block(
        content,
        "compatibility",
        parent_indent=0,
    )

    check(
        f"adapter-compatibility-block:{adapter}",
        bool(compatibility_block.strip()),
        "compatibility block missing",
    )

    if compatibility_block:
        status = field_value_in_block(
            compatibility_block,
            "status",
        )

        check(
            f"adapter-compatibility-status:{adapter}",
            status in VALID_COMPATIBILITY_STATUSES,
            (
                "expected one of: "
                + ", ".join(sorted(VALID_COMPATIBILITY_STATUSES))
            ),
        )

        check(
            f"adapter-compatibility-evidence:{adapter}",
            field_exists_in_block(
                compatibility_block,
                "evidence",
            ),
            "compatibility.evidence missing",
        )

        check(
            f"adapter-compatibility-notes:{adapter}",
            field_exists_in_block(
                compatibility_block,
                "notes",
            ),
            "compatibility.notes missing",
        )

    # -----------------------------------------------------------------------
    # Optional verification block
    # -----------------------------------------------------------------------

    verification_block = get_nested_block(
        content,
        "verification",
        parent_indent=0,
    )

    if verification_block:
        project_verification = get_nested_block(
            verification_block,
            "project",
            parent_indent=2,
        )

        global_verification = get_nested_block(
            verification_block,
            "global",
            parent_indent=2,
        )

        if project_verification:
            check(
                f"adapter-project-verification-path:{adapter}",
                bool(
                    field_value_in_block(
                        project_verification,
                        "expected_path",
                    )
                ),
                "verification.project.expected_path missing",
            )

        if global_verification:
            check(
                f"adapter-global-verification-path:{adapter}",
                bool(
                    field_value_in_block(
                        global_verification,
                        "expected_path",
                    )
                ),
                "verification.global.expected_path missing",
            )


# ---------------------------------------------------------------------------
# Adapter registry
# ---------------------------------------------------------------------------

registry_path = ROOT / "adapters" / "registry.yaml"

check(
    "adapter-registry",
    registry_path.is_file(),
    "adapters/registry.yaml missing",
)


if registry_path.is_file():
    registry = registry_path.read_text(
        encoding="utf-8"
    )

    for adapter in EXPECTED_ADAPTERS:
        # Support the structured registry representation:
        #
        # adapters:
        #   - id: generic
        #
        # and the simpler:
        #
        # - generic
        #
        # This keeps the test resilient to registry formatting while still
        # requiring every canonical adapter to be registered.

        structured_pattern = re.compile(
            rf"(?m)^\s*-\s*id:\s*{re.escape(adapter)}\s*$"
        )

        simple_pattern = re.compile(
            rf"(?m)^\s*-\s*{re.escape(adapter)}\s*$"
        )

        key_value_pattern = re.compile(
            rf"(?m)^\s*{re.escape(adapter)}:\s*$"
        )

        registered = (
            structured_pattern.search(registry) is not None
            or simple_pattern.search(registry) is not None
            or key_value_pattern.search(registry) is not None
        )

        check(
            f"adapter-registry:{adapter}",
            registered,
            "adapter not found in adapters/registry.yaml",
        )


# ---------------------------------------------------------------------------
# Collective adapter documentation
# ---------------------------------------------------------------------------

collective_readme = ROOT / "adapters" / "README.md"

check(
    "adapter-collective-readme",
    collective_readme.is_file(),
    "adapters/README.md missing",
)


if collective_readme.is_file():
    adapter_readme_text = collective_readme.read_text(
        encoding="utf-8"
    )

    check(
        "adapter-collective-readme-content",
        bool(adapter_readme_text.strip()),
        "adapters/README.md is empty",
    )

    readme_lower = adapter_readme_text.lower()

    for adapter in EXPECTED_ADAPTERS:
        check(
            f"adapter-readme-reference:{adapter}",
            adapter in readme_lower,
            f"{adapter} not documented in collective README",
        )


# ---------------------------------------------------------------------------
# Integration inventory
# ---------------------------------------------------------------------------

plugins_root = ROOT / "integrations" / "plugins"
connectors_root = ROOT / "integrations" / "connectors"

check(
    "plugins",
    len(list(plugins_root.glob("*.yaml"))) == 12,
    f"found {len(list(plugins_root.glob('*.yaml')))}",
)

check(
    "connectors",
    len(list(connectors_root.glob("*.yaml"))) == 9,
    f"found {len(list(connectors_root.glob('*.yaml')))}",
)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

CLI = ROOT / "cli" / "bin" / "nexra.js"

check(
    "cli-entrypoint",
    CLI.is_file(),
)


if CLI.is_file():

    for command in [
        ["list"],
        ["doctor"],
        ["validate"],
    ]:
        result = run_command(
            ["node", str(CLI), *command]
        )

        check(
            f"cli-{command[0]}",
            result.returncode == 0,
            result.stderr.strip(),
        )

    # -----------------------------------------------------------------------
    # CLI list count
    # -----------------------------------------------------------------------

    result = run_command(
        ["node", str(CLI), "list"]
    )

    if result.returncode == 0:
        output_lines = [
            line
            for line in result.stdout.splitlines()
            if line.strip()
        ]

        skill_lines = [
            line.strip()
            for line in output_lines
            if line.startswith("  ")
            and not "—" in line
            and not line.endswith("skills available.")
            and not line.endswith("adapters available.")
        ]

        check(
            "cli-list-skills",
            all(skill in result.stdout for skill in EXPECTED_SKILLS),
            "one or more canonical skills missing from list output",
        )

        check(
            "cli-list-adapters",
            all(adapter in result.stdout for adapter in EXPECTED_ADAPTERS),
            "one or more adapters missing from list output",
        )


# ---------------------------------------------------------------------------
# Installer behavior
# ---------------------------------------------------------------------------

with tempfile.TemporaryDirectory() as td:
    temp_root = Path(td)

    env = dict(os.environ)
    env["HOME"] = str(temp_root / "home")
    env["USERPROFILE"] = str(temp_root / "home")

    project = temp_root / "project"
    project.mkdir(parents=True)

    # -----------------------------------------------------------------------
    # Project installation
    # -----------------------------------------------------------------------

    result = run_command(
        [
            "node",
            str(CLI),
            "install",
            "--project",
            "--all",
        ],
        cwd=project,
        env=env,
    )

    check(
        "installer-project-exit",
        result.returncode == 0,
        result.stderr.strip(),
    )

    project_manifest_path = (
        project
        / ".nexra"
        / "manifest.json"
    )

    check(
        "installer-project-manifest",
        project_manifest_path.is_file(),
    )

    if project_manifest_path.is_file():
        try:
            project_manifest = json.loads(
                project_manifest_path.read_text(
                    encoding="utf-8"
                )
            )

            check(
                "installer-project-manifest-schema",
                project_manifest.get("schema") == 1,
            )

            check(
                "installer-project-manifest-scope",
                project_manifest.get("scope") == "project",
            )

            check(
                "installer-project-skill-list",
                len(
                    project_manifest.get(
                        "skills",
                        [],
                    )
                ) == 15,
            )

            project_installations = project_manifest.get(
                "installations",
                [],
            )

            check(
                "installer-project-installations",
                len(project_installations) == len(EXPECTED_ADAPTERS),
                f"found {len(project_installations)}",
            )

            for installation in project_installations:
                target = installation.get("target", "")
                target_path = project / target

                managed_files = installation.get(
                    "managed_files",
                    [],
                )

                check(
                    (
                        "installer-project-managed-files:"
                        f"{installation.get('adapter', 'unknown')}"
                    ),
                    len(managed_files) == 15,
                    f"found {len(managed_files)}",
                )

                installed_count = len(
                    list(
                        target_path.glob(
                            "*/SKILL.md"
                        )
                    )
                )

                check(
                    (
                        "installer-project-skills:"
                        f"{installation.get('adapter', 'unknown')}"
                    ),
                    installed_count == 15,
                    f"found {installed_count}",
                )

        except (
            json.JSONDecodeError,
            OSError,
        ) as exc:
            check(
                "installer-project-manifest-readable",
                False,
                str(exc),
            )

    # -----------------------------------------------------------------------
    # Global installation
    # -----------------------------------------------------------------------

    result = run_command(
        [
            "node",
            str(CLI),
            "install",
            "--global",
            "--all",
        ],
        cwd=project,
        env=env,
    )

    check(
        "installer-global-exit",
        result.returncode == 0,
        result.stderr.strip(),
    )

    home = Path(env["HOME"]) / ".nexra"

    global_manifest_path = (
        home / "manifest.json"
    )

    check(
        "installer-global-manifest",
        global_manifest_path.is_file(),
    )

    if global_manifest_path.is_file():
        try:
            global_manifest = json.loads(
                global_manifest_path.read_text(
                    encoding="utf-8"
                )
            )

            check(
                "installer-global-manifest-schema",
                global_manifest.get("schema") == 1,
            )

            check(
                "installer-global-manifest-scope",
                global_manifest.get("scope") == "global",
            )

            check(
                "installer-global-skill-list",
                len(
                    global_manifest.get(
                        "skills",
                        [],
                    )
                ) == 15,
            )

            global_installations = global_manifest.get(
                "installations",
                [],
            )

            check(
                "installer-global-installations",
                len(global_installations) == len(EXPECTED_ADAPTERS),
                f"found {len(global_installations)}",
            )

            for installation in global_installations:
                target = installation.get("target", "")

                target_path = Path(
                    target.replace("~/", str(Path(env["HOME"]) / ""), 1)
                    if target.startswith("~/")
                    else Path(env["HOME"]) / target
                )

                managed_files = installation.get(
                    "managed_files",
                    [],
                )

                check(
                    (
                        "installer-global-managed-files:"
                        f"{installation.get('adapter', 'unknown')}"
                    ),
                    len(managed_files) == 15,
                    f"found {len(managed_files)}",
                )

                installed_count = len(
                    list(
                        target_path.glob(
                            "*/SKILL.md"
                        )
                    )
                )

                check(
                    (
                        "installer-global-skills:"
                        f"{installation.get('adapter', 'unknown')}"
                    ),
                    installed_count == 15,
                    f"found {installed_count}",
                )

        except (
            json.JSONDecodeError,
            OSError,
        ) as exc:
            check(
                "installer-global-manifest-readable",
                False,
                str(exc),
            )


# ---------------------------------------------------------------------------
# Final result
# ---------------------------------------------------------------------------

if fail:
    print(f"FAIL: {len(fail)} test(s)")

    for failure in fail:
        print(" -", failure)

    sys.exit(1)


print("PASS: behavioral and contract tests")
print("skills=15 adapters=12 plugins=12 connectors=9")
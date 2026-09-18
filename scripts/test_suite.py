#!/usr/bin/env python3
"""
Dependency-light behavioral and contract tests for The-Builder.

These tests intentionally validate concepts and behavior rather than requiring
specific wording. Skills are instructional documents and may evolve their
headings and terminology without breaking the test suite.
"""

from pathlib import Path
import json
import os
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]

fail = []


def check(name, condition, detail=""):
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
# Canonical skill inventory
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

skills = sorted(
    path.parent.name
    for path in (ROOT / "skills").glob("*/SKILL.md")
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
# Foundation behavioral invariants
#
# These are concept groups rather than exact phrases.
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
        ["confirmed", "confirmed problem", "confirmed vulnerability"],
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
# Domain specialization
#
# The purpose here is to detect generic/copied skills. We require concepts
# that are materially specific to each domain, but do not require exact
# wording.
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
# Behavioral fixtures
#
# Test cases should demonstrate behavioral coverage without forcing a single
# exact sentence or formatting convention.
# ---------------------------------------------------------------------------

cases_path = ROOT / "tests" / "skills" / "cases.md"

if cases_path.is_file():
    cases = cases_path.read_text(encoding="utf-8").lower()

    fixture_groups = {
        "reuse": [
            "reuse",
            "reusable",
        ],
        "keyboard": [
            "keyboard",
            "keyboard navigation",
        ],
        "reduced-motion": [
            "reduced-motion",
            "reduced motion",
        ],
        "normalized-timeline": [
            "normalized timeline",
            "normalized",
        ],
        "content": [
            "content",
        ],
        "security": [
            "security",
            "xss",
            "authentication",
        ],
        "severity": [
            "severity",
            "critical",
            "high",
            "medium",
        ],
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
# Core test coverage
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
# Challenge test coverage
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
        "security": [
            "security",
        ],
        "scope": [
            "scope",
            "scope creep",
        ],
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
# Adapters
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

for adapter in EXPECTED_ADAPTERS:
    adapter_root = ROOT / "adapters" / adapter

    check(
        f"adapter:{adapter}",
        (
            (adapter_root / "adapter.yaml").is_file()
            and (adapter_root / "README.md").is_file()
        ),
    )

    manifest = adapter_root / "adapter.yaml"

    if not manifest.is_file():
        continue

    content = manifest.read_text(encoding="utf-8")

    check(
        f"adapter-target:{adapter}",
        f"target: {adapter}" in content
        or f"target:{adapter}" in content,
    )

    check(
        f"adapter-skill-source:{adapter}",
        "skill_source:" in content,
    )

    check(
        f"adapter-installation:{adapter}",
        "installation:" in content,
    )


# ---------------------------------------------------------------------------
# Integrations
# ---------------------------------------------------------------------------

plugins_root = ROOT / "integrations" / "plugins"
connectors_root = ROOT / "integrations" / "connectors"

check(
    "plugins",
    len(list(plugins_root.glob("*.yaml"))) == 12,
)

check(
    "connectors",
    len(list(connectors_root.glob("*.yaml"))) == 9,
)


# ---------------------------------------------------------------------------
# CLI smoke tests
# ---------------------------------------------------------------------------

CLI = ROOT / "cli" / "bin" / "the-builder.js"

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

    result = run_command(
        ["node", str(CLI), "list"]
    )

    if result.returncode == 0:
        output_lines = [
            line
            for line in result.stdout.splitlines()
            if line.strip()
        ]

        check(
            "cli-list-count",
            len(output_lines) == 15,
            f"found {len(output_lines)} lines",
        )


# ---------------------------------------------------------------------------
# Installer smoke tests
#
# Run installation inside isolated temporary project/home directories so
# tests cannot modify the user's real agent configuration.
# ---------------------------------------------------------------------------

with tempfile.TemporaryDirectory() as td:
    temp_root = Path(td)

    env = dict(os.environ)
    env["HOME"] = str(temp_root / "home")

    project = temp_root / "project"
    project.mkdir(parents=True)

    # ---------------------------------------------------------------
    # Project installation
    # ---------------------------------------------------------------

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
        project / ".the-builder" / "manifest.json"
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

            project_skills = project_manifest.get(
                "skills",
                [],
            )

            check(
                "installer-project-skill-list",
                len(project_skills) == 15,
            )

            project_targets = project_manifest.get(
                "targets",
                [],
            )

            check(
                "installer-project-targets",
                len(project_targets) == 4,
            )

            for target in project_targets:
                target_path = Path(
                    target.get("path", "")
                )

                installed_count = len(
                    list(
                        target_path.glob(
                            "*/SKILL.md"
                        )
                    )
                )

                check(
                    f"installer-project-skills:{target.get('target', 'unknown')}",
                    installed_count == 15,
                    f"found {installed_count}",
                )

        except (json.JSONDecodeError, OSError) as exc:
            check(
                "installer-project-manifest-readable",
                False,
                str(exc),
            )

    # ---------------------------------------------------------------
    # Global installation
    # ---------------------------------------------------------------

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

    home = Path(env["HOME"]) / ".the-builder"

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

            global_skills = global_manifest.get(
                "skills",
                [],
            )

            check(
                "installer-global-skill-list",
                len(global_skills) == 15,
            )

            global_targets = global_manifest.get(
                "targets",
                [],
            )

            check(
                "installer-global-targets",
                len(global_targets) == 4,
            )

            for target in global_targets:
                target_path = Path(
                    target.get("path", "")
                )

                installed_count = len(
                    list(
                        target_path.glob(
                            "*/SKILL.md"
                        )
                    )
                )

                check(
                    f"installer-global-skills:{target.get('target', 'unknown')}",
                    installed_count == 15,
                    f"found {installed_count}",
                )

        except (json.JSONDecodeError, OSError) as exc:
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
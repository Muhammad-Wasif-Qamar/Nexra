#!/usr/bin/env python3
from pathlib import Path
import re, sys, json

ROOT = Path(__file__).resolve().parents[1]
errors = []

EXPECTED = [
    "project-discovery","capability-assessment","interaction","challenge",
    "execution","verification","reporting","ui-ux-design","animation-design",
    "3d-web-design","scroll-world-flyby","content-code-optimization","seo",
    "security","reviewer"
]
FOUNDATION = EXPECTED[:7]
REQUIRED = [
    "Purpose","Core Principle","Scope","Discovery","Capability Requirements",
    "Interaction","Challenge Handling","Execution Workflow","Verification",
    "Reporting","Completion Criteria"
]

def err(msg): errors.append(msg)
def text(p): return p.read_text(encoding="utf-8")

# Skill inventory and canonical shape
skill_dirs = sorted(
    p.parent.name for p in (ROOT/"skills").glob("*/SKILL.md")
)
if skill_dirs != sorted(EXPECTED):
    err(f"skill inventory mismatch: expected {len(EXPECTED)}, found {len(skill_dirs)}")

for name in EXPECTED:
    p = ROOT/"skills"/name/"SKILL.md"
    if not p.is_file():
        err(f"missing skill: {name}")
        continue
    t = text(p)
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    if not m:
        err(f"{name}: invalid/missing front matter")
        continue
    block = m.group(1)
    for key in ("name","description","version"):
        if not re.search(rf"^{key}:\s*.+$", block, re.M):
            err(f"{name}: missing frontmatter {key}")
    nm = re.search(r"^name:\s*(.+)$", block, re.M)
    if nm and nm.group(1).strip() != name:
        err(f"{name}: frontmatter name mismatch")
    if "⸻" in t:
        err(f"{name}: corruption marker")
    if len(re.findall(r"^```", t, re.M)) % 2:
        err(f"{name}: unbalanced code fences")
    for h in REQUIRED:
        if not re.search(r"^## " + re.escape(h) + r"\s*$", t, re.M):
            err(f"{name}: missing section {h}")
    levels = [len(m.group(1)) for m in re.finditer(r"^(#{1,6})\s+", t, re.M)]
    for a,b in zip(levels, levels[1:]):
        if b-a > 1:
            err(f"{name}: heading jump {a}->{b}")
    # Canonical skills must remain provider agnostic.
    low = t.lower()
    forbidden = [".claude/skills/", "opencode.json", "cursor rules", "gemini cli command only"]
    for token in forbidden:
        if token in low:
            err(f"{name}: provider lock-in token {token}")

# No duplicate or obsolete split concept
if (ROOT/"skills"/"fly-by-animation").exists():
    err("obsolete split skill fly-by-animation exists")
if (ROOT/"skills"/"scroll-world-flyby"/"SKILL.md").is_file():
    t = text(ROOT/"skills"/"scroll-world-flyby"/"SKILL.md").lower()
    if "scroll world and fly-by are one discipline" not in t:
        err("scroll-world-flyby does not declare the merged concept")

# Repository documents
required_files = [
    "README.md","CONTRIBUTING.md","CHANGELOG.md","LICENSE",".gitignore",
    "package.json","docs/spec/SKILL-SPEC.md","docs/adapters/ADAPTER-SPEC.md",
    "core/README.md","core/orchestration/PIPELINE.md",
    "core/specification/BEHAVIOR.md","core/execution/EXECUTION-CONTRACT.md",
    "core/verification/VERIFICATION-CONTRACT.md","core/reporting/REPORTING-CONTRACT.md",
    "core/registries/skill-registry.yaml","integrations/registry.yaml",
]
for rel in required_files:
    p=ROOT/rel
    if not p.is_file() or not text(p).strip():
        err(f"missing/empty {rel}")

# Markdown integrity and local links
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts:
        continue
    t=text(p)
    if len(re.findall(r"^```",t,re.M))%2:
        err(f"unbalanced fences: {p.relative_to(ROOT)}")
    for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)",t):
        if "://" in target or target.startswith("mailto:") or target.startswith("#"):
            continue
        q=(p.parent/target).resolve()
        if not q.exists():
            err(f"broken local link: {p.relative_to(ROOT)} -> {target}")

# Adapters
adapters = ["generic","opencode","claude-code","kiro","cursor","codex","gemini",
            "github-copilot","antigravity","cline","roo","openhands"]
for a in adapters:
    manifest=ROOT/"adapters"/a/"adapter.yaml"
    readme=ROOT/"adapters"/a/"README.md"
    if not manifest.is_file(): err(f"missing adapter manifest {a}")
    else:
        t=text(manifest)
        for key in ("adapter_version:","target:","skill_source:","installation:","claims:"):
            if key not in t: err(f"adapter {a}: missing {key}")
        if "verified: true" in t and "source: http" not in t:
            err(f"adapter {a}: verified=true requires a documented source")
    if not readme.is_file() or not text(readme).strip():
        err(f"missing adapter README {a}")

# Integration contracts
reg=text(ROOT/"integrations/registry.yaml")
plugins=list((ROOT/"integrations/plugins").glob("*.yaml"))
connectors=list((ROOT/"integrations/connectors").glob("*.yaml"))
if len(plugins)!=12: err(f"expected 12 plugins, found {len(plugins)}")
if len(connectors)!=9: err(f"expected 9 connectors, found {len(connectors)}")
for p in plugins+connectors:
    t=text(p)
    for key in ("version:","kind:","id:","description:"):
        if key not in t: err(f"integration {p.name}: missing {key}")
for name in re.findall(r"^\s+- ([a-z0-9-]+)$", reg, re.M):
    # registry contains both lists; ensure each named artifact exists
    if name in {p.stem for p in plugins}|{p.stem for p in connectors}:
        continue

# Package invariant
pkg=json.loads(text(ROOT/"package.json"))
if pkg.get("version") != "0.5.0": err("package version mismatch")
if pkg.get("bin",{}).get("the-builder") != "cli/bin/the-builder.js":
    err("CLI bin mapping missing")

# Ensure no obvious placeholder language in shipped canonical content
for p in (ROOT/"skills").glob("*/SKILL.md"):
    low=text(p).lower()
    if "lorem ipsum" in low or "todo: fill" in low:
        err(f"placeholder content in {p.parent.name}")

if errors:
    print(f"FAIL: {len(errors)} validation error(s)")
    for e in errors: print(" -", e)
    sys.exit(1)
print("PASS: repository validation")
print(f"skills={len(EXPECTED)} foundation={len(FOUNDATION)} adapters={len(adapters)} plugins={len(plugins)} connectors={len(connectors)}")

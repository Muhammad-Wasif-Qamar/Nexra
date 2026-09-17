#!/usr/bin/env python3
"""Dependency-light behavioral and contract tests for The-Builder."""
from pathlib import Path
import subprocess, sys, re

ROOT=Path(__file__).resolve().parents[1]
fail=[]
def check(name, cond, detail=""):
    if not cond: fail.append(f"{name}: {detail}")

skills=sorted(p.parent.name for p in (ROOT/"skills").glob("*/SKILL.md"))
expected={"project-discovery","capability-assessment","interaction","challenge","execution",
"verification","reporting","ui-ux-design","animation-design","3d-web-design",
"scroll-world-flyby","content-code-optimization","seo","security","reviewer"}
check("skill-discovery",set(skills)==expected,f"found {len(skills)}")
check("merged-scroll-flyby","scroll-world-flyby" in skills and "fly-by-animation" not in skills)

# Foundation behavioral invariants
checks={
"project-discovery":["Discover before asking","observed","verified","unknown"],
"capability-assessment":["FULL","SUITABLE","CONSTRAINED","UNSUITABLE"],
"interaction":["material","discover","user authority"],
"challenge":["evidence","CONFIRMED PROBLEM","LIKELY ISSUE"],
"execution":["incremental","bounded","diff"],
"verification":["acceptance criterion","evidence","BLOCKED"],
"reporting":["Result","Changes","Verification","Limitations"],
}
for name,terms in checks.items():
    t=(ROOT/"skills"/name/"SKILL.md").read_text(encoding="utf8").lower()
    for term in terms:
        check(f"{name}:{term}",term.lower() in t)

# Domain specialization checks: these terms make generic cloning detectable.
special={
"ui-ux-design":["information hierarchy","keyboard","touch targets"],
"animation-design":["easing","reduced motion","state transitions"],
"3d-web-design":["scene graph","renderer","texture"],
"scroll-world-flyby":["camera","waypoints","parallax","normalized"],
"content-code-optimization":["content","bundle","before/after"],
"seo":["canonical","sitemap","structured data"],
"security":["trust boundaries","least privilege","xss"],
"reviewer":["severity","recommendation","confidence"],
}
for name,terms in special.items():
    t=(ROOT/"skills"/name/"SKILL.md").read_text(encoding="utf8").lower()
    for term in terms:
        check(f"{name}:specialized:{term}",term.lower() in t)

# Behavioral fixtures
cases=(ROOT/"tests/skills/cases.md").read_text(encoding="utf8").lower()
for phrase in ["reuse","keyboard","reduced-motion","normalized timeline","content","security","severity"]:
    check(f"behavior-fixture:{phrase}",phrase in cases)

# Adapters
adapters=["generic","opencode","claude-code","kiro","cursor","codex","gemini","github-copilot","antigravity","cline","roo","openhands"]
for a in adapters:
    check(f"adapter:{a}",(ROOT/"adapters"/a/"adapter.yaml").is_file() and (ROOT/"adapters"/a/"README.md").is_file())

# Integrations
check("plugins",len(list((ROOT/"integrations/plugins").glob("*.yaml")))==12)
check("connectors",len(list((ROOT/"integrations/connectors").glob("*.yaml")))==9)

# CLI smoke tests
for command in [["list"],["doctor"],["validate"]]:
    r=subprocess.run(["node",str(ROOT/"cli/bin/the-builder.js"),*command],capture_output=True,text=True)
    check("cli-"+command[0],r.returncode==0,r.stderr.strip())
r=subprocess.run(["node",str(ROOT/"cli/bin/the-builder.js"),"list"],capture_output=True,text=True)
check("cli-list-count",len(r.stdout.strip().splitlines())==15)

# Installer smoke tests in isolated HOME/project directories.
import tempfile, os, json
with tempfile.TemporaryDirectory() as td:
    env=dict(os.environ)
    env["HOME"]=str(Path(td)/"home")
    project=Path(td)/"project"; project.mkdir()
    r=subprocess.run(["node",str(ROOT/"cli/bin/the-builder.js"),"install","--project","--all"],cwd=project,env=env,capture_output=True,text=True)
    check("installer-project-exit",r.returncode==0,r.stderr)
    check("installer-project-manifest",(project/".the-builder/manifest.json").is_file())
    pm=json.loads((project/".the-builder/manifest.json").read_text())
    check("installer-project-skills",sum(len(list(Path(t["path"]).glob("*/SKILL.md"))) for t in pm["targets"])==15)
    r=subprocess.run(["node",str(ROOT/"cli/bin/the-builder.js"),"install","--global","--all"],cwd=project,env=env,capture_output=True,text=True)
    home=Path(env["HOME"])/".the-builder"
    check("installer-global-exit",r.returncode==0,r.stderr)
    check("installer-global-manifest",(home/"manifest.json").is_file())
    gm=json.loads((home/"manifest.json").read_text())
    check("installer-global-skills",sum(len(list(Path(t["path"]).glob("*/SKILL.md"))) for t in gm["targets"])==15)
    manifest=json.loads((project/".the-builder/manifest.json").read_text())
    check("installer-manifest-scope",manifest.get("scope")=="project")

if fail:
    print(f"FAIL: {len(fail)} test(s)")
    for x in fail: print(" -",x)
    sys.exit(1)
print("PASS: behavioral and contract tests")
print("skills=15 adapters=12 plugins=12 connectors=9")

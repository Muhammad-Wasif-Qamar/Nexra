#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const SKILLS = path.join(ROOT, "skills");
const args = process.argv.slice(2);
const cmd = args[0] || "install";
const EXPECTED_SKILLS = fs.readdirSync(SKILLS, { withFileTypes: true })
  .filter(e => e.isDirectory() && fs.existsSync(path.join(SKILLS, e.name, "SKILL.md")))
  .map(e => e.name).sort();

const AGENTS = [
  { id: "claude-code", label: "Claude Code", commands: ["claude"], project: ".claude/skills", global: ".claude/skills", macApps: [] },
  { id: "opencode", label: "OpenCode", commands: ["opencode"], project: ".opencode/skills", global: path.join(".config", "opencode", "skills") },
  { id: "kiro", label: "Kiro", commands: ["kiro", "kiro-cli"], project: ".kiro/skills", global: ".kiro/skills" },
  { id: "cursor", label: "Cursor", commands: ["cursor"], project: ".cursor/skills", global: ".cursor/skills", macApps: ["/Applications/Cursor.app"], windowsPaths: [path.join(process.env.LOCALAPPDATA || "", "Programs", "cursor")], linuxPaths: [path.join(os.homedir(), ".local", "share", "applications", "cursor.desktop")] },
  { id: "codex", label: "Codex", commands: ["codex"], project: ".agents/skills", global: path.join(".agents", "skills") },
  { id: "gemini", label: "Gemini CLI", commands: ["gemini"], project: ".gemini/skills", global: ".gemini/skills" },
  { id: "github-copilot", label: "GitHub Copilot CLI", commands: ["copilot"], project: ".github/skills", global: path.join(".copilot", "skills") },
  { id: "cline", label: "Cline", commands: ["cline"], project: ".cline/skills", global: ".cline/skills" },
  { id: "roo", label: "Roo", commands: ["roo"], project: ".agents/skills", global: path.join(".agents", "skills") },
  { id: "openhands", label: "OpenHands", commands: ["openhands"], project: ".agents/skills", global: path.join(".agents", "skills") },
  { id: "antigravity", label: "Antigravity", commands: ["antigravity"], project: ".agents/skills", global: path.join(".agents", "skills"), macApps: ["/Applications/Antigravity.app"] },
];

function hasCommand(command) {
  const r = spawnSync(process.platform === "win32" ? "where" : "which", [command], { stdio: "ignore" });
  return r.status === 0;
}
function appExists(paths) { return paths.some(p => fs.existsSync(p)); }
function agentDetected(a) {
  if (a.commands.some(hasCommand)) return true;
  if (process.platform === "darwin" && a.macApps) return appExists(a.macApps);
  if (process.platform === "linux" && a.linuxPaths) return appExists(a.linuxPaths);
  if (process.platform === "win32" && a.windowsPaths) return appExists(a.windowsPaths);
  return false;
}
function detectAgents() { return AGENTS.filter(agentDetected); }
function skills() { return EXPECTED_SKILLS; }
function usage() {
  console.log(`The-Builder\n\nCommands:\n  install              Interactive installation wizard (default)\n  install --project    Install into the current project\n  install --global     Install into the user home\n  install --all        Install all skills without prompting\n  detect               Detect supported coding agents and environment\n  list                 List canonical skills\n  show <skill>         Print a skill path\n  doctor               Check installation/repository health\n  validate             Run repository validation\n  test                 Run repository tests\n\nExamples:\n  npx @wasif-qamar/the-builder\n  npx @wasif-qamar/the-builder install --project --all\n  npx @wasif-qamar/the-builder detect`);
}
function run(program, argv, cwd = ROOT) {
  return spawnSync(program, argv, { cwd, stdio: "inherit" });
}
function copySkills(destination, selected) {
  fs.mkdirSync(destination, { recursive: true });
  for (const name of selected) {
    const src = path.join(SKILLS, name);
    const dst = path.join(destination, name);
    fs.rmSync(dst, { recursive: true, force: true });
    fs.cpSync(src, dst, { recursive: true });
    console.log(`  ✓ ${name}`);
  }
}
function targetForAgent(agent, scope, project) {
  const rel = scope === "global" ? agent.global : agent.project;
  return scope === "global" ? path.join(os.homedir(), rel) : path.join(project, rel);
}
function writeManifest(dir, scope, detected, targets) {
  fs.mkdirSync(dir, { recursive: true });
  const manifest = {
    schema: 1,
    version: "0.5.0",
    scope,
    installed_at: new Date().toISOString(),
    skills: EXPECTED_SKILLS,
    detected_agents: detected.map(a => a.id),
    agent_adapters: detected.map(a => `adapters/${a.id}`),
    targets,
    note: "Skills are copied only to documented native skill directories or the portable .agents/skills fallback. Host configuration is not guessed or overwritten."
  };
  fs.writeFileSync(path.join(dir, "manifest.json"), JSON.stringify(manifest, null, 2) + "\n");
  fs.writeFileSync(path.join(dir, "AGENTS.md"), `# The-Builder installation\n\nDetected agents at install time: ${detected.length ? detected.map(a => a.label).join(", ") : "none"}.\n\nCanonical skills are under \\.the-builder/skills/. Use the corresponding adapter in the The-Builder distribution when a host requires a provider-specific discovery location.\n`);
}
async function install() {
  const project = process.cwd();
  const detected = detectAgents();
  console.log("The-Builder\n");
  console.log(`Environment: ${process.platform} / Node ${process.version}`);
  console.log(`Project: ${project}`);
  console.log(`Detected agents: ${detected.length ? detected.map(a => a.label).join(", ") : "none"}`);

  const hasProject = args.includes("--project");
  const hasGlobal = args.includes("--global");
  const all = args.includes("--all");
  let scope = hasGlobal ? "global" : hasProject ? "project" : null;
  const rl = (!scope || !all) ? readline.createInterface({ input, output }) : null;
  try {
    if (!scope) {
      const answer = await rl.question("\nInstall scope? [1] Project  [2] Global: ");
      scope = answer.trim() === "2" ? "global" : "project";
    }
    let selected = skills();
    if (!all) {
      const answer = await rl.question("Install all skills? [Y/n]: ");
      if (/^n/i.test(answer.trim())) {
        const list = await rl.question(`Enter skill names separated by commas:\n${skills().join(", ")}\n> `);
        selected = list.split(",").map(s => s.trim()).filter(Boolean);
        const invalid = selected.filter(s => !skills().includes(s));
        if (invalid.length) throw new Error(`Unknown skill(s): ${invalid.join(", ")}`);
      }
    }
    const root = scope === "global" ? path.join(os.homedir(), ".the-builder") : path.join(project, ".the-builder");
    const targets = (detected.length ? detected : [{ id: "generic", label: "Generic Agent Skills", project: ".agents/skills", global: path.join(".agents", "skills") }])
      .map(agent => ({ agent: agent.id, path: targetForAgent(agent, scope, project) }));
    console.log(`\nInstalling ${selected.length} skill(s) for ${targets.length} target(s)`);
    for (const target of targets) {
      console.log(`\n→ ${target.agent}: ${target.path}`);
      copySkills(target.path, selected);
    }
    writeManifest(root, scope, detected, targets);
    console.log(`\n✓ Installed ${selected.length} skill(s) to ${targets.length} target(s).`);
    console.log(`✓ Scope: ${scope}`);
    console.log(`✓ Manifest: ${path.join(root, "manifest.json")}`);
    if (detected.length) console.log("✓ Agent detection recorded; no unsupported host configuration was modified.");
    else console.log("  No supported coding-agent executable was detected. Generic installation is still available.");
    console.log("\nRun `npx @wasif-qamar/the-builder doctor` to verify the installation.");
  } finally { rl?.close(); }
}
function doctor() {
  const cwd = process.cwd();
  const candidates = [path.join(cwd, ".the-builder"), path.join(os.homedir(), ".the-builder")];
  const found = candidates.filter(p => fs.existsSync(path.join(p, "manifest.json")));
  console.log(`Node: ${process.version}`);
  console.log(`Platform: ${process.platform}`);
  console.log(`Agents detected: ${detectAgents().map(a => a.id).join(", ") || "none"}`);
  console.log(`Installed The-Builder locations: ${found.length ? found.join(", ") : "none"}`);
  for (const root of found) {
    const manifest = JSON.parse(fs.readFileSync(path.join(root, "manifest.json"), "utf8"));
    const missing = [];
    for (const target of (manifest.targets || [])) {
      for (const skill of (manifest.skills || [])) {
        if (!fs.existsSync(path.join(target.path, skill, "SKILL.md"))) missing.push(`${target.agent}:${skill}`);
      }
    }
    if (missing.length) { console.error(`✗ ${root}: missing ${missing.join(", ")}`); process.exitCode = 1; }
    else console.log(`✓ ${root}: ${manifest.skills.length} skills present across ${manifest.targets.length} target(s)`);
  }
  if (!found.length) {
    const required = ["README.md","LICENSE","CONTRIBUTING.md","CHANGELOG.md","package.json",".gitignore"];
    const missing = required.filter(p => !fs.existsSync(path.join(ROOT,p)));
    if (missing.length) { console.error(`Missing repository files: ${missing.join(", ")}`); process.exitCode = 1; }
    else console.log("✓ Repository structure is healthy");
  }
}
async function main() {
  if (cmd === "list") skills().forEach(s => console.log(s));
  else if (cmd === "show") {
    const name = args[1];
    if (!name || !skills().includes(name)) { console.error("Unknown skill. Run: the-builder list"); process.exitCode = 2; return; }
    console.log(path.join(SKILLS, name, "SKILL.md"));
  } else if (cmd === "detect") {
    console.log(`Platform: ${process.platform}\nNode: ${process.version}`);
    for (const a of AGENTS) console.log(`${agentDetected(a) ? "✓" : "✗"} ${a.label}`);
  } else if (cmd === "install") await install();
  else if (cmd === "doctor") doctor();
  else if (cmd === "validate") process.exitCode = run("python3", ["scripts/validate.py"]).status ?? 1;
  else if (cmd === "test") process.exitCode = run("python3", ["scripts/test_suite.py"]).status ?? 1;
  else usage();
}

main().catch(error => { console.error(`Error: ${error.message}`); process.exitCode = 1; });

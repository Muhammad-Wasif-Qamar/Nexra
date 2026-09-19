#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

const ROOT = path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  "../.."
);

const SKILLS_DIR = path.join(ROOT, "skills");
const ADAPTERS_DIR = path.join(ROOT, "adapters");
const ADAPTER_REGISTRY = path.join(ADAPTERS_DIR, "registry.yaml");

const NEXRA_DIR = ".nexra";
const MANIFEST_FILE = "manifest.json";
const MANIFEST_VERSION = 1;

const args = process.argv.slice(2);
const command = args[0] || "install";

const hasFlag = (flag) => args.includes(flag);

const cliOptions = {
  project: hasFlag("--project"),
  global: hasFlag("--global"),
  all: hasFlag("--all"),
  yes: hasFlag("--yes"),
  generic: hasFlag("--generic"),
};

const requestedAgent = (() => {
  const index = args.indexOf("--agent");

  if (index === -1) {
    return null;
  }

  return args[index + 1] || null;
})();

const requestedSkill = (() => {
  const index = args.indexOf("--skill");

  if (index === -1) {
    return null;
  }

  return args[index + 1] || null;
})();


/* -------------------------------------------------------------------------- */
/* Nexra branding                                                              */
/* -------------------------------------------------------------------------- */

const NEXRA_LOGO = `
  ███╗   ██╗███████╗██╗  ██╗██████╗  █████╗
  ████╗  ██║██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗
  ██╔██╗ ██║█████╗   ╚███╔╝ ██████╔╝███████║
  ██║╚██╗██║██╔══╝   ██╔██╗ ██╔══██╗██╔══██║
  ██║ ╚████║███████╗██╔╝ ██╗██║  ██║██║  ██║
  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═╝

  Capability-aware skill system for AI coding agents
`;

function printNexraBanner() {
  console.log(NEXRA_LOGO);
}

/* -------------------------------------------------------------------------- */
/* Utilities                                                                  */
/* -------------------------------------------------------------------------- */

function fail(message, code = 1) {
  console.error(`✗ ${message}`);
  process.exitCode = code;
}

function hasCommand(commandName) {
  const checker = process.platform === "win32" ? "where" : "which";

  const result = spawnSync(checker, [commandName], {
    stdio: "ignore"
  });

  return result.status === 0;
}

function expandHome(value) {
  if (typeof value !== "string") return value;

  if (value === "~") {
    return os.homedir();
  }

  if (value.startsWith("~/")) {
    return path.join(os.homedir(), value.slice(2));
  }

  return value;
}

function resolveFrom(base, target) {
  const expanded = expandHome(target);

  if (path.isAbsolute(expanded)) {
    return expanded;
  }

  return path.resolve(base, expanded);
}

function readText(file) {
  return fs.readFileSync(file, "utf8");
}

function fileExists(file) {
  return fs.existsSync(file);
}

function directoryExists(dir) {
  return fs.existsSync(dir) && fs.statSync(dir).isDirectory();
}

function parseScalar(value) {
  const trimmed = value.trim();

  if (trimmed === "") return "";

  if (trimmed === "true") return true;
  if (trimmed === "false") return false;
  if (trimmed === "null") return null;

  if (
    (trimmed.startsWith('"') && trimmed.endsWith('"')) ||
    (trimmed.startsWith("'") && trimmed.endsWith("'"))
  ) {
    return trimmed.slice(1, -1);
  }

  if (/^-?\d+(?:\.\d+)?$/.test(trimmed)) {
    return Number(trimmed);
  }

  if (trimmed.startsWith("[") && trimmed.endsWith("]")) {
    const body = trimmed.slice(1, -1).trim();

    if (!body) return [];

    return body
      .split(",")
      .map(item => parseScalar(item));
  }

  return trimmed;
}

/* -------------------------------------------------------------------------- */
/* Constrained YAML parser                                                    */
/* -------------------------------------------------------------------------- */

/*
 * Nexra intentionally does not depend on PyYAML or another YAML package.
 *
 * This parser supports the subset used by Nexra's adapter manifests and
 * registry:
 *
 * - mappings
 * - nested mappings
 * - block lists
 * - inline lists
 * - quoted scalars
 * - booleans
 * - numbers
 * - null
 * - comments
 *
 * It is NOT intended to be a general-purpose YAML implementation.
 */

function stripComment(line) {
  let quote = null;

  for (let i = 0; i < line.length; i += 1) {
    const char = line[i];

    if (char === "'" || char === '"') {
      if (quote === null) {
        quote = char;
      } else if (quote === char) {
        quote = null;
      }
    }

    if (char === "#" && quote === null) {
      if (i === 0 || /\s/.test(line[i - 1])) {
        return line.slice(0, i).trimEnd();
      }
    }
  }

  return line;
}

function indentation(line) {
  return line.match(/^ */)[0].length;
}

function parseYaml(content) {
  const rawLines = content.replace(/\r\n/g, "\n").split("\n");

  const lines = rawLines
    .map(stripComment)
    .filter(line => line.trim() !== "")
    .map(line => ({
      indent: indentation(line),
      text: line.trim()
    }));

  if (lines.length === 0) {
    return {};
  }

  function parseBlock(start, indent) {
    if (start >= lines.length) {
      return [{}, start];
    }

    const isList = lines[start].indent === indent &&
      lines[start].text.startsWith("- ");

    const result = isList ? [] : {};

    let index = start;

    while (
      index < lines.length &&
      lines[index].indent === indent
    ) {
      const line = lines[index].text;

      if (isList) {
        if (!line.startsWith("- ")) {
          break;
        }

        const itemText = line.slice(2).trim();

        if (itemText === "") {
          const next = index + 1;

          if (
            next < lines.length &&
            lines[next].indent > indent
          ) {
            const [value, nextIndex] = parseBlock(
              next,
              lines[next].indent
            );

            result.push(value);
            index = nextIndex;
          } else {
            result.push(null);
            index += 1;
          }

          continue;
        }

        const colon = itemText.indexOf(":");

        if (colon !== -1) {
          const key = itemText.slice(0, colon).trim();
          const rawValue = itemText.slice(colon + 1).trim();

          const item = {};

          if (rawValue !== "") {
            item[key] = parseScalar(rawValue);
            index += 1;
          } else {
            const next = index + 1;

            if (
              next < lines.length &&
              lines[next].indent > indent
            ) {
              const [value, nextIndex] = parseBlock(
                next,
                lines[next].indent
              );

              item[key] = value;
              index = nextIndex;
            } else {
              item[key] = {};
              index += 1;
            }
          }

          if (
            index < lines.length &&
            lines[index].indent > indent
          ) {
            const [extra, nextIndex] = parseBlock(
              index,
              lines[index].indent
            );

            if (
              extra &&
              typeof extra === "object" &&
              !Array.isArray(extra)
            ) {
              Object.assign(item, extra);
            }

            index = nextIndex;
          }

          result.push(item);
          continue;
        }

        result.push(parseScalar(itemText));
        index += 1;
        continue;
      }

      const colon = line.indexOf(":");

      if (colon === -1) {
        throw new Error(`Invalid YAML mapping line: ${line}`);
      }

      const key = line.slice(0, colon).trim();
      const rawValue = line.slice(colon + 1).trim();

      if (rawValue !== "") {
        result[key] = parseScalar(rawValue);
        index += 1;
        continue;
      }

      const next = index + 1;

      if (
        next < lines.length &&
        lines[next].indent > indent
      ) {
        const [value, nextIndex] = parseBlock(
          next,
          lines[next].indent
        );

        result[key] = value;
        index = nextIndex;
      } else {
        result[key] = {};
        index += 1;
      }
    }

    return [result, index];
  }

  return parseBlock(0, lines[0].indent)[0];
}

/* -------------------------------------------------------------------------- */
/* Adapter registry                                                            */
/* -------------------------------------------------------------------------- */

function loadRegistry() {
  if (!fileExists(ADAPTER_REGISTRY)) {
    throw new Error(
      `Adapter registry not found: ${path.relative(ROOT, ADAPTER_REGISTRY)}`
    );
  }

  const registry = parseYaml(readText(ADAPTER_REGISTRY));

  if (!registry || !Array.isArray(registry.adapters)) {
    throw new Error("Adapter registry does not contain an adapters list.");
  }

  return registry;
}

function loadAdapters() {
  const registry = loadRegistry();

  return registry.adapters.map(entry => {
    if (!entry.id || !entry.manifest) {
      throw new Error(
        "Every adapter registry entry requires id and manifest."
      );
    }

    const manifestPath = path.resolve(
      ADAPTERS_DIR,
      entry.manifest
    );

    if (!manifestPath.startsWith(`${ADAPTERS_DIR}${path.sep}`)) {
      throw new Error(
        `Adapter manifest escapes adapters directory: ${entry.id}`
      );
    }

    if (!fileExists(manifestPath)) {
      throw new Error(
        `Adapter manifest not found: ${entry.manifest}`
      );
    }

    const manifest = parseYaml(readText(manifestPath));

    validateAdapterManifest(manifest, entry.id);

    return {
      ...manifest,
      registry: entry,
      manifestPath
    };
  });
}

function validateAdapterManifest(adapter, registryId) {
  const required = [
    "id",
    "name",
    "adapter",
    "detection",
    "installation",
    "skills",
    "capabilities",
    "compatibility"
  ];

  for (const field of required) {
    if (
      adapter[field] === undefined ||
      adapter[field] === null
    ) {
      throw new Error(
        `Adapter ${registryId} is missing required field: ${field}`
      );
    }
  }

  if (adapter.id !== registryId) {
    throw new Error(
      `Adapter registry id '${registryId}' does not match manifest id '${adapter.id}'.`
    );
  }

  if (!adapter.adapter.version) {
    throw new Error(
      `Adapter ${adapter.id} is missing adapter.version.`
    );
  }

  if (!adapter.adapter.platform) {
    throw new Error(
      `Adapter ${adapter.id} is missing adapter.platform.`
    );
  }

  if (
    !adapter.detection ||
    !Array.isArray(adapter.detection.commands)
  ) {
    throw new Error(
      `Adapter ${adapter.id} has invalid detection.commands.`
    );
  }

  if (
    !adapter.installation.project ||
    !adapter.installation.global
  ) {
    throw new Error(
      `Adapter ${adapter.id} must define project and global installation scopes.`
    );
  }

  return true;
}

/* -------------------------------------------------------------------------- */
/* Skills                                                                      */
/* -------------------------------------------------------------------------- */

function getSkills() {
  if (!directoryExists(SKILLS_DIR)) {
    throw new Error("Canonical skills directory does not exist.");
  }

  return fs.readdirSync(SKILLS_DIR, { withFileTypes: true })
    .filter(
      entry =>
        entry.isDirectory() &&
        fileExists(
          path.join(SKILLS_DIR, entry.name, "SKILL.md")
        )
    )
    .map(entry => entry.name)
    .sort();
}

/* -------------------------------------------------------------------------- */
/* Detection                                                                   */
/* -------------------------------------------------------------------------- */

function detectAdapter(adapter) {
  const commands = adapter.detection.commands || [];

  if (commands.length === 0) {
    return {
      detected: false,
      evidence: []
    };
  }

  const evidence = commands
    .filter(command => hasCommand(command))
    .map(command => ({
      type: "command",
      value: command
    }));

  return {
    detected: evidence.length > 0,
    evidence
  };
}

function detectAgents(adapters) {
  return adapters
    .filter(adapter => adapter.id !== "generic")
    .map(adapter => ({
      adapter,
      ...detectAdapter(adapter)
    }));
}

/* -------------------------------------------------------------------------- */
/* Installation target safety                                                  */
/* -------------------------------------------------------------------------- */

function validateTarget(target, scope) {
  if (typeof target !== "string" || target.trim() === "") {
    throw new Error(
      `Invalid ${scope} installation target.`
    );
  }

  if (target.includes("\0")) {
    throw new Error(
      `Invalid ${scope} installation target: null byte detected.`
    );
  }

  if (target.includes("..")) {
    const normalized = target.replace(/\\/g, "/");

    const segments = normalized.split("/");

    if (segments.includes("..")) {
      throw new Error(
        `Unsafe ${scope} installation target: path traversal detected.`
      );
    }
  }

  if (path.isAbsolute(target) && !target.startsWith("~")) {
    throw new Error(
      `Unsafe ${scope} installation target: absolute paths are not permitted in adapter manifests.`
    );
  }

  return true;
}

function getInstallationTarget(adapter, scope) {
  const configuration = adapter.installation?.[scope];

  if (!configuration || configuration.supported !== true) {
    return null;
  }

  const target = configuration.target;

  validateTarget(target, scope);

  return target;
}

function resolveInstallationTarget(adapter, scope, projectRoot) {
  const target = getInstallationTarget(adapter, scope);

  if (!target) {
    return null;
  }

  if (target.startsWith("~/")) {
    return resolveFrom(os.homedir(), target.slice(2));
  }

  if (scope === "global") {
    return resolveFrom(os.homedir(), target);
  }

  return resolveFrom(projectRoot, target);
}

/* -------------------------------------------------------------------------- */
/* Safe installation                                                           */
/* -------------------------------------------------------------------------- */

function ensureInsideRoot(root, candidate) {
  const relative = path.relative(root, candidate);

  if (
    relative === "" ||
    relative.startsWith(`..${path.sep}`) ||
    path.isAbsolute(relative)
  ) {
    throw new Error(
      `Unsafe installation path outside allowed root: ${candidate}`
    );
  }
}

function copyDirectoryNonDestructive(source, destination) {
  if (!directoryExists(source)) {
    throw new Error(`Skill source does not exist: ${source}`);
  }

  fs.mkdirSync(destination, {
    recursive: true
  });

  const entries = fs.readdirSync(source, {
    withFileTypes: true
  });

  const managedFiles = [];

  for (const entry of entries) {
    const sourcePath = path.join(source, entry.name);
    const destinationPath = path.join(destination, entry.name);

    if (entry.isDirectory()) {
      copyDirectoryNonDestructive(
        sourcePath,
        destinationPath
      );

      continue;
    }

    if (!entry.isFile()) {
      continue;
    }

    if (fileExists(destinationPath)) {
      const sourceContent = fs.readFileSync(sourcePath);
      const destinationContent = fs.readFileSync(destinationPath);

      if (!sourceContent.equals(destinationContent)) {
        throw new Error(
          `Refusing to overwrite existing user file: ${destinationPath}`
        );
      }

      managedFiles.push(destinationPath);
      continue;
    }

    fs.copyFileSync(
      sourcePath,
      destinationPath
    );

    managedFiles.push(destinationPath);
  }

  return managedFiles;
}

function installSkills({
  projectRoot,
  adapter,
  scope,
  selectedSkills
}) {
  const targetRoot = resolveInstallationTarget(
    adapter,
    scope,
    projectRoot
  );

  if (!targetRoot) {
    throw new Error(
      `${adapter.name} does not support ${scope} installation.`
    );
  }

  const allowedRoot =
    scope === "global"
      ? os.homedir()
      : projectRoot;

  ensureInsideRoot(
    allowedRoot,
    targetRoot
  );

  const managedFiles = [];

  for (const skill of selectedSkills) {
    if (!EXPECTED_SKILLS.includes(skill)) {
      throw new Error(
        `Unknown skill: ${skill}`
      );
    }

    const source = path.join(
      SKILLS_DIR,
      skill
    );

    const destination = path.join(
      targetRoot,
      skill
    );

    ensureInsideRoot(
      targetRoot,
      destination
    );

    const files = copyDirectoryNonDestructive(
      source,
      destination
    );

    for (const file of files) {
      managedFiles.push({
        path: path.relative(
          projectRoot,
          file
        ),
        adapter: adapter.id,
        scope,
        skill
      });
    }

    console.log(`  ✓ ${skill}`);
  }

  return {
    targetRoot,
    managedFiles
  };
}

/* -------------------------------------------------------------------------- */
/* Nexra state                                                                  */
/* -------------------------------------------------------------------------- */

function stateDirectory(scope, projectRoot) {
  if (scope === "global") {
    return path.join(
      os.homedir(),
      NEXRA_DIR
    );
  }

  return path.join(
    projectRoot,
    NEXRA_DIR
  );
}

function writeManifest({
  projectRoot,
  scope,
  adapters,
  installations,
  selectedSkills
}) {
  const stateDir = stateDirectory(
    scope,
    projectRoot
  );

  fs.mkdirSync(stateDir, {
    recursive: true
  });

  const manifest = {
    schema: MANIFEST_VERSION,
    version: "0.1.1",
    scope,
    installed_at: new Date().toISOString(),
    skills: selectedSkills,
    detected_agents: adapters
      .filter(item => item.detected)
      .map(item => item.adapter.id),
    installations,
    note:
      "Nexra installs canonical skills through adapter-defined locations. Existing user files are never overwritten."
  };

  const manifestPath = path.join(
    stateDir,
    MANIFEST_FILE
  );

  fs.writeFileSync(
    manifestPath,
    JSON.stringify(manifest, null, 2) + "\n",
    "utf8"
  );

  return manifestPath;
}

function writeAgentsFile({
  projectRoot,
  scope,
  adapters
}) {
  const stateDir = stateDirectory(
    scope,
    projectRoot
  );

  const detected = adapters
    .filter(item => item.detected)
    .map(item => item.adapter.name);

  const lines = [
    "# Nexra installation",
    "",
    `Installation scope: ${scope}`,
    "",
    "Detected agents at install time:",
    "",
    ...(detected.length
      ? detected.map(name => `- ${name}`)
      : ["- None"]),
    "",
    "Skills are installed through the adapter-defined discovery locations.",
    "Installation does not prove runtime discovery or execution.",
    ""
  ];

  fs.writeFileSync(
    path.join(stateDir, "AGENTS.md"),
    lines.join("\n"),
    "utf8"
  );
}

/* -------------------------------------------------------------------------- */
/* Interactive UI                                                              */
/* -------------------------------------------------------------------------- */

async function ask(question) {
  const rl = readline.createInterface({
    input,
    output
  });

  try {
    return await rl.question(question);
  } finally {
    rl.close();
  }
}

async function chooseScope() {
  const answer = (
    await ask(
      "\nInstallation scope [project/global] (project): "
    )
  )
    .trim()
    .toLowerCase();

  if (!answer || answer === "project") {
    return "project";
  }

  if (answer === "global") {
    return "global";
  }

  throw new Error(
    "Invalid scope. Choose project or global."
  );
}

async function chooseSkills(available) {
  console.log("\nAvailable skills:\n");

  available.forEach((skill, index) => {
    console.log(
      `  ${index + 1}. ${skill}`
    );
  });

  const answer = (
    await ask(
      "\nInstall [all/numbers] (all): "
    )
  ).trim();

  if (!answer || answer.toLowerCase() === "all") {
    return available;
  }

  const indexes = answer
    .split(",")
    .map(value => Number(value.trim()))
    .filter(Number.isInteger);

  const selected = indexes.map(index => available[index - 1]);

  if (
    selected.length === 0 ||
    selected.some(skill => !skill)
  ) {
    throw new Error(
      "Invalid skill selection."
    );
  }

  return [...new Set(selected)];
}

async function chooseAdapters(detected, adapters) {
  const detectedAdapters = detected
    .filter(item => item.detected);

  console.log("\nDetected agents:\n");

  if (detectedAdapters.length === 0) {
    console.log("  No supported agent executables detected.");
  } else {
    detectedAdapters.forEach(item => {
      console.log(
        `  ✓ ${item.adapter.name}`
      );
    });
  }

  const fallback = adapters.find(
    adapter => adapter.id === "generic"
  );

  const answer = (
    await ask(
      "\nUse detected agents, generic fallback, or choose adapters? [detected/generic/select] (detected): "
    )
  )
    .trim()
    .toLowerCase();

  if (!answer || answer === "detected") {
    if (detectedAdapters.length > 0) {
      return detectedAdapters;
    }

    if (fallback) {
      return [{
        adapter: fallback,
        detected: false,
        evidence: []
      }];
    }

    throw new Error(
      "No detected agents and no generic adapter is available."
    );
  }

  if (answer === "generic") {
    if (!fallback) {
      throw new Error(
        "Generic adapter is not registered."
      );
    }

    return [{
      adapter: fallback,
      detected: false,
      evidence: []
    }];
  }

  if (answer === "select") {
    console.log("\nAdapters:\n");

    adapters.forEach((adapter, index) => {
      const state =
        detected.some(
          item =>
            item.adapter.id === adapter.id &&
            item.detected
        )
          ? "detected"
          : "not detected";

      console.log(
        `  ${index + 1}. ${adapter.name} [${state}]`
      );
    });

    const selection = (
      await ask(
        "\nSelect adapter numbers (comma-separated): "
      )
    ).trim();

    const indexes = selection
      .split(",")
      .map(value => Number(value.trim()))
      .filter(Number.isInteger);

    const selected = indexes
      .map(index => adapters[index - 1])
      .filter(Boolean);

    if (selected.length === 0) {
      throw new Error(
        "Invalid adapter selection."
      );
    }

    return selected.map(adapter => {
      const detection = detected.find(
        item =>
          item.adapter.id === adapter.id
      );

      return {
        adapter,
        detected: detection?.detected ?? false,
        evidence: detection?.evidence ?? []
      };
    });
  }

  throw new Error(
    "Invalid adapter selection."
  );
}

/* -------------------------------------------------------------------------- */
/* Commands                                                                    */
/* -------------------------------------------------------------------------- */

const EXPECTED_SKILLS = getSkills();

function commandList(adapters) {
  console.log("\nNexra skills:\n");

  for (const skill of EXPECTED_SKILLS) {
    console.log(`  ${skill}`);
  }

  console.log(
    `\n${EXPECTED_SKILLS.length} skills available.`
  );

  console.log("\nAdapters:\n");

  for (const adapter of adapters) {
    console.log(
      `  ${adapter.id} — ${adapter.name}`
    );
  }

  console.log(
    `\n${adapters.length} adapters available.`
  );
}

function commandValidate() {
  const validator = path.join(
    ROOT,
    "scripts",
    "validate.py"
  );

  if (!fileExists(validator)) {
    throw new Error("Validation script not found.");
  }

  const result = spawnSync(
    "python3",
    [validator],
    {
      cwd: ROOT,
      stdio: "inherit"
    }
  );

  if (result.error) {
    throw result.error;
  }

  if (result.status !== 0) {
    process.exitCode = result.status || 1;
  }
}

function commandDetect(adapters) {
  console.log(
    `Platform: ${process.platform}`
  );

  console.log(
    `Node: ${process.version}`
  );

  console.log("");

  for (const adapter of adapters) {
    if (adapter.id === "generic") {
      continue;
    }

    const result = detectAdapter(adapter);

    console.log(
      `${result.detected ? "✓" : "✗"} ${adapter.name}`
    );
  }
}

function commandShow(adapters, id) {
  if (!id) {
    throw new Error(
      "Usage: nexra show <skill-or-adapter>"
    );
  }

  const skillPath = path.join(
    SKILLS_DIR,
    id,
    "SKILL.md"
  );

  if (fileExists(skillPath)) {
    console.log(readText(skillPath));
    return;
  }

  const adapter = adapters.find(
    item => item.id === id
  );

  if (adapter) {
    console.log(
      JSON.stringify(adapter, null, 2)
    );
    return;
  }

  throw new Error(
    `Skill or adapter not found: ${id}`
  );
}

function commandDoctor(adapters) {
  console.log(
    `Node: ${process.version}`
  );

  console.log(
    `Platform: ${process.platform}`
  );

  const detected = detectAgents(adapters);

  console.log(
    `Agents detected: ${
      detected
        .filter(item => item.detected)
        .map(item => item.adapter.id)
        .join(", ") || "none"
    }`
  );

  const locations = [];

  const projectState = path.join(
    process.cwd(),
    NEXRA_DIR
  );

  const globalState = path.join(
    os.homedir(),
    NEXRA_DIR
  );

  if (directoryExists(projectState)) {
    locations.push(projectState);
  }

  if (
    globalState !== projectState &&
    directoryExists(globalState)
  ) {
    locations.push(globalState);
  }

  console.log(
    `Installed Nexra locations: ${
      locations.length
        ? locations.join(", ")
        : "none"
    }`
  );

  let repositoryHealthy = true;

  if (!directoryExists(SKILLS_DIR)) {
    console.error(
      "✗ Missing skills directory"
    );

    repositoryHealthy = false;
  }

  if (!fileExists(ADAPTER_REGISTRY)) {
    console.error(
      "✗ Missing adapter registry"
    );

    repositoryHealthy = false;
  }

  for (const adapter of adapters) {
    if (!fileExists(adapter.manifestPath)) {
      console.error(
        `✗ Missing manifest: ${adapter.id}`
      );

      repositoryHealthy = false;
    }
  }

  for (const location of locations) {
    const manifestPath = path.join(
      location,
      MANIFEST_FILE
    );

    if (!fileExists(manifestPath)) {
      console.error(
        `✗ Missing manifest: ${manifestPath}`
      );

      repositoryHealthy = false;
      continue;
    }

    let manifest;

    try {
      manifest = JSON.parse(
        readText(manifestPath)
      );
    } catch {
      console.error(
        `✗ Invalid manifest: ${manifestPath}`
      );

      repositoryHealthy = false;
      continue;
    }

    const installations =
      manifest.installations || [];

    for (const installation of installations) {
      for (const managedFile of installation.managed_files || []) {
        const absolutePath = path.resolve(
          process.cwd(),
          managedFile.path
        );

        if (!fileExists(absolutePath)) {
          console.error(
            `✗ Missing managed file: ${managedFile.path}`
          );

          repositoryHealthy = false;
        }
      }
    }
  }

  if (repositoryHealthy) {
    console.log(
      "✓ Repository structure is healthy"
    );
  }
}

async function commandInstall(adapters) {
  const projectRoot = process.cwd();

  printNexraBanner();

  const detected = detectAgents(adapters);

  let selectedAdapters;

  if (cliOptions.generic) {
    const generic = adapters.find(
      item => item.id === "generic"
    );

    if (!generic) {
      fail("Generic adapter is not available.");
      return;
    }

    selectedAdapters = [generic];
  } else if (requestedAgent) {
    const requested = adapters.find(
      item => item.id === requestedAgent
    );

    if (!requested) {
      fail(`Unknown adapter: ${requestedAgent}`);
      return;
    }

    selectedAdapters = [requested];
  } else if (cliOptions.all) {
    selectedAdapters = adapters;
  } else {
    selectedAdapters =
      await chooseAdapters(
        detected,
        adapters
      );
  }

  // chooseAdapters() returns detection records shaped as
  // { adapter, detected, evidence }. Normalize those records
  // to the actual adapter objects expected by the installer.
  selectedAdapters = selectedAdapters.map(item =>
    item &&
    item.adapter &&
    item.adapter.id
      ? item.adapter
      : item
  );

  let scope;

  if (cliOptions.global && cliOptions.project) {
    fail("Use either --project or --global, not both.");
    return;
  }

  if (cliOptions.global) {
    scope = "global";
  } else if (cliOptions.project) {
    scope = "project";
  } else {
    scope = await chooseScope();
  }

  let selectedSkills;

  if (requestedSkill) {
    if (!EXPECTED_SKILLS.includes(requestedSkill)) {
      fail(`Unknown skill: ${requestedSkill}`);
      return;
    }

    selectedSkills = [requestedSkill];
  } else if (cliOptions.all) {
    selectedSkills = EXPECTED_SKILLS;
  } else {
    selectedSkills =
      await chooseSkills(
        EXPECTED_SKILLS
      );
  }

  console.log("\nInstallation plan:\n");

  console.log(
    `  Scope: ${scope}`
  );

  console.log(
    `  Skills: ${selectedSkills.length}`
  );

  console.log(
    `  Adapters: ${
      selectedAdapters
        .map(item => item.name)
        .join(", ")
    }`
  );

  let confirmed = true;

  if (!cliOptions.yes && !cliOptions.all) {
    const confirm = (
      await ask(
        "\nContinue? [y/N]: "
      )
    )
      .trim()
      .toLowerCase();

    confirmed = confirm === "y" || confirm === "yes";
  }

  if (!confirmed) {
    console.log(
      "\nInstallation cancelled."
    );

    return;
  }

  const installations = [];

  for (const adapter of selectedAdapters) {

    console.log(
      `\nInstalling for ${adapter.name}...`
    );

    const result = installSkills({
      projectRoot,
      adapter,
      scope,
      selectedSkills
    });

    installations.push({
      adapter: adapter.id,
      scope,
      target: path.relative(
        projectRoot,
        result.targetRoot
      ) || ".",
      managed_files: result.managedFiles
    });
  }

  const manifestPath = writeManifest({
    projectRoot,
    scope,
    adapters: detected,
    installations,
    selectedSkills
  });

  writeAgentsFile({
    projectRoot,
    scope,
    adapters: detected
  });

  console.log(
    `\n✓ Installation complete`
  );

  console.log(
    `✓ Manifest: ${manifestPath}`
  );

  console.log(
    "\nRun `nexra doctor` to verify the installation."
  );
}

/* -------------------------------------------------------------------------- */
/* Help                                                                        */
/* -------------------------------------------------------------------------- */

function usage() {
  console.log(`
Nexra — capability-aware skills for AI coding agents

Usage:
  nexra
  nexra install
  nexra list
  nexra detect
  nexra validate
  nexra show <skill|adapter>
  nexra doctor

Commands:
  install     Install Nexra skills
  list        List skills and adapters
  detect      Detect supported coding agents
  validate    Validate the Nexra repository
  show        Show a skill or adapter manifest
  doctor      Diagnose repository and installation state
`);
}

/* -------------------------------------------------------------------------- */
/* Main                                                                        */
/* -------------------------------------------------------------------------- */

async function main() {
  let adapters;

  try {
    adapters = loadAdapters();
  } catch (error) {
    fail(error.message);
    return;
  }

  try {
    switch (command) {
      case "install":
        await commandInstall(adapters);
        break;

      case "list":
        commandList(adapters);
        break;

      case "detect":
        commandDetect(adapters);
        break;

      case "validate":
        commandValidate();
        break;

      case "show":
        commandShow(
          adapters,
          args[1]
        );
        break;

      case "doctor":
        commandDoctor(adapters);
        break;

      case "help":
      case "--help":
      case "-h":
        usage();
        break;

      case "version":
      case "--version":
      case "-v":
        console.log("0.1.1");
        break;

      default:
        usage();
        process.exitCode = 1;
    }
  } catch (error) {
    fail(error.message);
  }
}

await main();
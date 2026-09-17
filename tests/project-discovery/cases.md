# Project Discovery Cases

## 1. Simple UI tweak

Request: "Change the homepage button to brown."

Expected behavior:
- locate the homepage and existing button styles;
- do not ask what framework is used if inspection reveals it;
- make only the requested change;
- verify the relevant result.

## 2. Broad redesign

Request: "Redesign the landing page."

Expected behavior:
- inspect stack, routes, components, assets, content, and existing design conventions;
- ask only for missing decisions that materially affect the redesign;
- do not begin a wholesale rewrite without scope.

## 3. Contradictory request

Existing project is React; request says "rebuild using React."

Expected behavior:
- identify that React already exists;
- clarify whether the user wants a redesign/rebuild or merely a change;
- do not silently replace the application.

## 4. Missing visual capability

Request: "Reproduce this animation exactly" when no browser/visual inspection is available.

Expected behavior:
- classify visual verification as constrained/unsuitable;
- implement only what can be justified;
- do not claim exact visual verification.

## 5. Discoverable fact

Request: "What framework does this project use?"

Expected behavior:
- inspect manifests/source;
- answer from evidence;
- do not ask the user.

## 6. Necessary unknown

Request: "Redesign this page for our target audience" when the audience is not represented anywhere in the project.

Expected behavior:
- identify audience as a material unknown;
- ask a focused question.

## 7. Preference

Request: "Make the animation slower."

Expected behavior:
- treat this as an explicit preference;
- implement it unless a concrete technical/accessibility problem exists.

## 8. Technical tradeoff

Request: "Use a different animation library for every section."

Expected behavior:
- identify dependency, bundle, maintenance, and consistency tradeoffs;
- present alternatives;
- preserve the user's final decision.

## 9. Unknown application

Request: "Add authentication."

Expected behavior:
- discover frontend/backend/auth/database/deployment boundaries first;
- ask only for missing decisions such as identity provider when not discoverable.

## 10. Stop discovery

Request: "Fix this spelling mistake."

Expected behavior:
- locate the text;
- change it;
- run the smallest relevant verification;
- do not perform a full architecture audit.

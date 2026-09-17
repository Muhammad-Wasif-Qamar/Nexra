# Verification Contract

## Evidence matrix

Every material acceptance criterion maps to one or more methods:

| Method | Suitable evidence |
|---|---|
| static | source/config structure |
| unit | isolated behavior |
| integration | component boundaries |
| build | compilation/bundling integrity |
| runtime | exercised behavior |
| browser | rendered and interactive behavior |
| visual | appearance/composition |
| measurement | performance or size |
| security | targeted control/risk validation |

## Result states

- PASS — evidence supports the criterion.
- FAIL — evidence contradicts it.
- BLOCKED — required evidence capability was unavailable.
- NOT APPLICABLE — criterion does not apply.

Never convert BLOCKED into PASS.

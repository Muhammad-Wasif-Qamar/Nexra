# Execution Contract

## Inputs

- requested outcome;
- discovered project facts;
- capability states;
- user decisions;
- acceptance criteria;
- bounded change set.

## Rules

- preserve existing conventions unless there is a justified reason to change them;
- prefer minimal coherent diffs;
- avoid unrelated refactors;
- validate risky increments;
- update tests when behavior changes;
- keep migrations explicit and reversible where practical;
- inspect the final diff.

## Output

An execution result contains:

```text
changed
checks_run
decisions
unverified
remaining_work
```

Execution does not imply verification.

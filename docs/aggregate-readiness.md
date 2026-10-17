# Aggregate Readiness Gate

Numerical publication is a gate, not an aspiration.

## Required checks

A first aggregate table may be published only when all are true:

- [ ] collection window is explicitly defined;
- [ ] every counted row has passed privacy review;
- [ ] every counted row has explicit normalized fields or `UNKNOWN`;
- [ ] duplicate candidates are resolved for the counted occurrence set;
- [ ] denominator is disclosed;
- [ ] unknown/missing counts are disclosed;
- [ ] self-selected-sample warning is adjacent to the table;
- [ ] no cell creates a reasonable re-identification risk;
- [ ] provenance remains in the ledger, not the aggregate row;
- [ ] aggregate output passes schema validation/readback;
- [ ] sample is large/diverse enough that publishing the table adds information rather than false precision.

## Current decision

**GATE = NOT PASSED.** V4.5 does not retroactively guess missing fields from historical narrative reports. Therefore no first numerical aggregate is published by this release.

## Minimum-size principle

There is deliberately no universal magic `N`. Readiness depends on deduplication quality, missingness, cell sparsity, independence/diversity and re-identification risk. A reviewer must document why publication is informative and safe.

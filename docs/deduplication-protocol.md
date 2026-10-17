# Deduplication Protocol

Deduplication reduces double counting without erasing materially different failure paths.

## Compare in this order

1. Same public source or obvious resubmission.
2. Same contributor explicitly states it is the same occurrence.
3. Same symptom family **and** same terminal outcome **and** same state transition **and** same coarse occurrence window.
4. Material discriminators: platform, direct 429 vs cancellation/timeout/5xx, visibility state, retry/backoff signal, recovery behaviour.

## Outcomes

- **EXACT/RESUBMISSION** -> one occurrence, multiple submissions noted.
- **LIKELY DUPLICATE** -> `DUPLICATE_CANDIDATE`; human/reviewer confirmation required before counts change.
- **SAME SYMPTOM / DIFFERENT DISCRIMINATOR** -> keep separate.
- **INSUFFICIENT INFORMATION** -> keep separate or `UNKNOWN`; do not force a merge.

## Safety rule

Fuzzy or semantic similarity may surface duplicate candidates, but it may never delete, merge or change counts automatically. Similar UI wording does not prove the same mechanism or occurrence.

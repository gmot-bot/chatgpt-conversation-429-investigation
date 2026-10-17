# Periodic Community Triage

Use this checklist for a bounded review of new public contributions. It is a process specification, not a claim that background monitoring is continuously running.

See also the V4.5 [Community Operations](community-operations.md), [Triage Ledger](triage-ledger.md), [Deduplication Protocol](deduplication-protocol.md), and [Freshness Policy](freshness-policy.md).

## Review cycle

1. Read new Discussions and Issues since the previous recorded checkpoint.
2. Remove/flag exposed private information before deeper analysis.
3. Route help questions to the closest Error Library page or safe workaround.
4. Detect duplicates and aggregate “me too” observations.
5. Extract only explicitly supplied structured fields; missing values remain `UNKNOWN`.
6. Grade candidate evidence S0-S3 when justified.
7. Re-evaluate H0-H12 only for discriminating evidence.
8. Update `Other People Are Seeing This`, Workarounds/Solutions and Community Intelligence when there is a real delta.
9. Check official OpenAI Status for relevant acknowledged incidents, recording it as context only.
10. Record review timestamp, items reviewed, privacy actions, material deltas and next review trigger.

## Immediate escalation triggers

- new vendor/server telemetry;
- a new independent S2/S3 reproduction that discriminates hypotheses;
- a confirmed mechanism-specific fix;
- privacy/security exposure requiring moderation;
- evidence that invalidates a frozen public claim.

A substantive causal delta reactivates the 429 investigation from `STANDBY_EXTERNAL / MONITORING` to P0.

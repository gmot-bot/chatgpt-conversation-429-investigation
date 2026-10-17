# Controlled Community Status Update Protocol

This protocol prevents a fast-moving community page from turning unverified anecdotes into incident claims.

## Inputs

Only use public Discussions/Issues, already-public independent evidence, official OpenAI status notices, and public release/change records. Do not ingest private support material into community status.

V4.5 operational details are defined in [Community Operations](community-operations.md) and [Candidate Promotion Rules](candidate-promotion-rules.md). Automatic rules may create candidates only; they cannot promote causal conclusions.

## Pipeline

`NEW CONTRIBUTION -> PRIVACY -> DEDUP -> CLASSIFY -> VERIFY -> UPDATE CANDIDATE -> READBACK -> PUBLISH`

## Allowed state transitions

- `REPORTED` -> `INVESTIGATING` when the report is sufficiently clear to compare.
- `INVESTIGATING` -> `WORKAROUND AVAILABLE` when a bounded safe mitigation has useful repeated observations.
- `INVESTIGATING` -> `MULTIPLE POSSIBLE MECHANISMS` when discriminating evidence demonstrates materially different terminal paths.
- Any state -> `CONFIRMED FIX` only with mechanism-specific evidence strong enough to support that wording.
- Missing or ambiguous evidence -> `UNKNOWN`, never inferred.

## Official-status linkage

Official OpenAI incidents are shown in a separate context field. Never automatically change a community problem to `RESOLVED` because an official incident closed unless the evidence establishes that the community problem belongs to that incident.

## Freshness

Every status page should display its last project review date. `Last reviewed` means the project checked its inputs; it does not mean continuous monitoring or that no newer incident exists.

## Causal escalation

A substantive vendor/server telemetry delta, discriminating independent reproduction, or mechanism-specific confirmed fix automatically reactivates the causal investigation from `STANDBY_EXTERNAL / MONITORING` to P0 review.

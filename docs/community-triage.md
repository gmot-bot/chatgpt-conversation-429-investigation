# Community Triage Protocol

The community-help layer must remain useful without lowering the evidence standard of the technical investigation.

## Funnel

`HELP -> symptom page -> safe troubleshooting -> Discussion -> structured report -> privacy review -> S0/S1/S2/S3 -> H0-H12/engineering evidence when justified`

## Triage rules

1. Treat a visitor's wording first as a **symptom report**, not a causal diagnosis.
2. Search for an existing Discussion/Issue before opening a duplicate.
3. Aggregate “same symptom” reports unless a new report adds a material discriminator.
4. Never pressure a user to reproduce a failure, repeatedly retry, open DevTools, or publish logs.
5. Remove or ask the contributor to remove exposed private data before technical analysis.
6. Promote a report into the technical evidence set only when its provenance/directness/specificity justify it.
7. A workaround that helped is recorded as a mitigation observation, not proof of root cause.
8. Mark a solution/fix as confirmed only when the evidence supports the specific mechanism and outcome.
9. Keep `FACT / INFERENCE / HYPOTHESIS / NOT PROVED` distinct.
10. New substantive vendor/server telemetry reactivates the causal P0 workstream automatically.

## Duplicate policy

Prefer a reply or reaction on the closest existing Discussion for “me too” reports. Create a separate structured Issue when there is a discriminating delta such as a different terminal HTTP outcome, reproducible state transition, authoritative backoff signal, clearly different client behaviour, or useful sanitized technical evidence.

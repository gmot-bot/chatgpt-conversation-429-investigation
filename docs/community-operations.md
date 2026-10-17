# V4.5 — Community Operations & Contribution Pipeline

**Operational state:** ACTIVE SPECIFICATION. This is a bounded public-community workflow, not a claim of continuous autonomous monitoring.

## Purpose

Turn natural public contributions into useful help, maintained status, and — only after gates — aggregate community intelligence without converting anecdotes into causal claims.

## Operational pipeline

`DISCOVER -> INTAKE -> PRIVACY -> DEDUP -> NORMALIZE -> TRIAGE -> CANDIDATE -> VERIFY -> HELP/STATUS UPDATE -> AGGREGATE GATE -> PUBLISH -> CHECKPOINT`

### 1. Discover
Use new public repository Discussions/Issues and already-public evidence. Do not generate ChatGPT failures or traffic to create evidence.

### 2. Intake
Assign an internal public-safe contribution key. Preserve the source link in the ledger; do not copy secrets or private identifiers into aggregate records.

### 3. Privacy
Stop promotion when a contribution exposes credentials, cookies, tokens, email, unique account/conversation/request IDs, IP addresses, precise location, private chat content, private support correspondence, or unsanitized HAR material.

### 4. Deduplicate
Compare symptom family, platform family, terminal outcome, state transition, time window at coarse granularity, and semantic description. Never merge merely because two users saw similar wording.

### 5. Normalize
Extract only explicit values. Missing/ambiguous values become `UNKNOWN`. Never infer `NO` from silence.

### 6. Triage
Route to HELP, KNOWN_PROBLEM, WORKAROUND, EVIDENCE_CANDIDATE, DUPLICATE, PRIVACY_HOLD, or OUT_OF_SCOPE.

### 7. Candidate promotion
Automation/rules may promote an item only to **CANDIDATE** status. Candidacy means “worth human/evidence review”, never “true”, “causal”, “confirmed”, or “representative”.

### 8. Verify
Apply provenance/directness/specificity/independence and S0-S3 evidence rules where appropriate.

### 9. Update
Update help/status/known-problem pages only when wording remains inside the evidence boundary.

### 10. Aggregate
Counts remain gated until normalization, deduplication, privacy, denominator/unknown disclosure and minimum-sample safeguards pass.

### 11. Publish and checkpoint
Read back changed public surfaces, record review time, source count, holds, candidate promotions and material deltas.

## Non-goals

- no automatic root-cause promotion;
- no automatic H0-H12 closure;
- no ChatGPT-wide prevalence estimate;
- no private support-data ingestion;
- no automated retries or failure generation;
- no automatic `RESOLVED` from temporal proximity to an official incident.

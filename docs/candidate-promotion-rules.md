# Candidate Promotion Rules

Rules may automatically **surface** candidates. They may not establish causality.

## Candidate types

### STATUS_CANDIDATE
Surface when a new public contribution clearly maps to an existing symptom family or introduces a new reproducible user-visible state.

### WORKAROUND_CANDIDATE
Surface when a bounded, low-risk mitigation is explicitly reported as helping. Repetition by independent reports increases review priority but does not prove mechanism.

### EVIDENCE_CANDIDATE
Surface when a report contains a discriminating terminal outcome, authoritative backoff signal, sanitized direct request/response evidence, reproducible state transition, or other material discriminator.

### AGGREGATE_CANDIDATE
Surface only after explicit fields can be normalized and the contribution has passed privacy and duplicate review.

## Forbidden automatic promotions

Automation must never assign:

- `ROOT CAUSE CONFIRMED`;
- `CONFIRMED FIX`;
- H0-H12 true/false closure;
- `GLOBAL OUTAGE` / global prevalence;
- causal linkage to an OpenAI incident;
- `RESOLVED` for a community family solely because an official incident closed.

## Priority signals

Higher review priority is appropriate for S2/S3-quality direct evidence, a novel terminal class, a falsifier for a current hypothesis, independent repeated observations with the same discriminator, or authoritative vendor/server telemetry.

A substantive causal/vendor delta reactivates the causal investigation to P0 review; the rule itself does not decide the causal conclusion.

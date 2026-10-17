# Evidence Dashboard — Community Sample

<p align="center"><a href="../README.md"><img src="../assets/chatgpt-community-hero-social-preview.jpg" alt="ChatGPT Conversation Errors — return to project home" width="420"></a></p>


**Status: SCHEMA READY / NUMERICAL PUBLICATION GATED.**

This dashboard is intentionally conservative. It will show aggregate tables only after enough public reports can be normalized without guessing, deduplicated, and privacy-reviewed.

> **Community frequency != global prevalence.** This repository receives a self-selected sample and cannot estimate the percentage of ChatGPT users affected.

## Current dashboard

| Metric | Current publication state |
|---|---|
| Total deduplicated community reports | NOT YET PUBLISHED |
| Reports by error/symptom family | SCHEMA READY; DATA GATED |
| Reports by platform family | SCHEMA READY; DATA GATED |
| Intermittent / persistent / unknown | SCHEMA READY; DATA GATED |
| Recovered after normal waiting | SCHEMA READY; DATA GATED |
| Remained visible/searchable | SCHEMA READY; DATA GATED |
| Terminal class: 429/4xx/5xx/cancel/timeout/unknown | SCHEMA READY; DATA GATED |
| Evidence grade S0/S1/S2/S3 | SCHEMA READY; DATA GATED |

## Why there are no charts yet

Charts would imply quantitative precision before the sample has passed normalization and deduplication gates. Tables come first. Charts are allowed only when denominators, missing-data rates, duplicate handling and collection period are disclosed.

## V4.5 operational gate

The publication decision is now tracked in [Aggregate Readiness](aggregate-readiness.md). Candidate rows must first pass the [Community Operations](community-operations.md) pipeline and deduplication/privacy review.

## Publication gate

Before a numerical table is published:

1. define the collection window;
2. normalize only explicit fields;
3. preserve missing values as `UNKNOWN`;
4. remove obvious duplicate submissions;
5. perform privacy review;
6. disclose denominator and unknown count;
7. state that the sample is self-selected;
8. retain provenance in the evidence ledger, not in aggregate rows;
9. check that no count can identify an individual;
10. obtain a readback/checkpoint before promotion.

## Future table format

| Symptom family | Deduplicated reports | Unknown platform | Recovered after wait | Direct 429 | Evidence S2/S3 |
|---|---:|---:|---:|---:|---:|
| *Published only after gate* | — | — | — | — | — |

See [Community Intelligence](community-intelligence.md) for the data dictionary.

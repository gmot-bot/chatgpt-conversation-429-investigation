# Community Intelligence — Privacy-Preserving Aggregate View

**Purpose:** summarize public, voluntarily submitted observations without identifying contributors and without presenting repository frequency as ChatGPT-wide prevalence.

## Critical interpretation rule

> **Community frequency != global prevalence.**

This repository is a self-selected sample. Counts can be affected by discoverability, duplicate reporting, contributor behaviour, platform mix, moderation and changing issue forms. They must not be used to estimate the percentage of ChatGPT users affected.

## Aggregate dimensions

When enough public reports exist, maintain only non-identifying counts for:

- symptom/error family;
- broad platform family;
- intermittent vs persistent vs unknown;
- recovered after normal waiting: yes/no/unknown;
- conversation remained visible/searchable: yes/no/unknown;
- directly observed terminal class: 429 / other 4xx / 5xx / cancellation / timeout / unknown;
- evidence grade S0 / S1 / S2 / S3;
- number of reports grouped into the same symptom family.

## Current baseline

The V4.2 baseline is **schema-first**. It does not invent counts from narrative evidence and does not backfill missing fields. Historical reports remain in their existing evidence tables until they can be classified without inference.

## Minimum aggregation safeguards

- no usernames or contributor ranking;
- no precise geography;
- no unique timestamps in aggregate tables;
- no account/conversation/request identifiers;
- no private support data;
- no inferred values for missing fields;
- label unknown as `UNKNOWN`, never silently convert it to `NO`;
- deduplicate obvious duplicates before counting;
- retain provenance separately in the evidence ledger, not in the public aggregate row.

## Data dictionary

| Field | Allowed aggregate values |
|---|---|
| symptom_family | controlled non-identifying label |
| platform_family | web / windows / macos / android / ios-ipados / work-project / other / unknown |
| intermittent | yes / no / unknown |
| recovered_after_wait | yes / no / unknown |
| remained_visible | yes / no / unknown |
| terminal_class | 429 / other-4xx / 5xx / cancellation / timeout / other / unknown |
| evidence_grade | S0 / S1 / S2 / S3 |
| report_count | integer after deduplication |

## Publication gate

Publish numerical community statistics only after the underlying public reports can be normalized without guessing and the deduplication/privacy review passes. Until then, use qualitative `YES / NOT YET ESTABLISHED` summaries.

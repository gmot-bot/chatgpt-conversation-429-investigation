# Latest Community Changes

This page answers: **What changed since the previous project checkpoint?**

## 2026-10-17 — V4.5 Community Operations

- Added the operational contribution pipeline from public intake through checkpoint.
- Added a public-safe triage ledger schema without inventing historical rows.
- Added conservative duplicate detection and confirmation rules.
- Added freshness/status-review semantics.
- Added automatic **candidate-only** promotion rules; causality can never be auto-promoted.
- Added a statistical readiness gate for first aggregates.
- Added a machine-readable aggregate schema and validation script.

## Current causal status

`STANDBY_EXTERNAL / MONITORING` — root cause **NOT DETERMINED**.

## Current aggregate status

`NOT READY FOR NUMERICAL PUBLICATION` until the gate in [Aggregate Readiness](aggregate-readiness.md) passes with real normalized, deduplicated, privacy-reviewed contributions.

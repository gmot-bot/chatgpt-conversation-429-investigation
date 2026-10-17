# What We Know — and What We Do Not Know

## Confirmed from the public evidence set

- Existing/historical conversations can remain visible or searchable while failing to open normally.
- Some public cases directly show HTTP 429 on conversation/history retrieval paths.
- Some public cases show automatic or overlapping retrieval/refetch/recovery activity near the failure.
- At least one reviewed history-loading failure is associated with cancellation/state handling without a demonstrated 429 on that operation.
- Similar user-visible symptoms therefore do not establish one universal technical mechanism.

## Plausible but not proved as the root cause

Client request amplification, retry/backoff coordination defects, stale-state recovery loops, insufficient request coalescing/single-flight, limiter coupling and rate-limit feedback are among the hypotheses under test.

## Not established

- A global ChatGPT outage or global overload as the cause of these reports.
- One common root cause for every conversation/history loading failure.
- That WebSocket/realtime activity causes the 429 responses.
- That affected users necessarily generated excessive manual traffic.
- A specific server-side limiter scope or policy.

**Root cause remains NOT DETERMINED.**

# Private OpenAI Engineering Escalation — Sanitised Companion

This document is a public-safe companion to a private engineering escalation. Identifying correlation material belongs only in the private support/vendor channel.

## Problem statement
Existing/historical ChatGPT conversations can remain represented in the interface while failing to open. In the maintainer case, preserved client-side evidence includes conversation/history retrieval HTTP 429, server-provided backoff headers, successful realtime WebSocket establishment during history-retrieval failure, `conversation-update` / `refetch-conversation` events, and recovery-linked retrieval attempts.

## Independently reproduced discriminators
Public reports now independently document: (1) HTTP 429 on conversation-detail retrieval routes; (2) `Retry-After` / history backoff signals followed by later successful retrieval; (3) automatic recovery/refetch polling associated with `Too many requests`; (4) overlapping conversation-list requests and retries; and (5) cross-client cases where the same conversation can remain unavailable on one client while loading on another.

## Requested engineering correlation
Please correlate the privately supplied request/timestamp identifiers against server telemetry and determine, where possible:

1. the rate-limit scope/key and endpoint-specific policy involved;
2. whether automatic client recovery/refetch/list refresh contributes materially to request volume during the affected state;
3. whether retries are deduplicated and respect the authoritative backoff interval;
4. whether realtime recovery events can trigger redundant conversation-detail retrieval while a prior retrieval/backoff is outstanding;
5. whether a failed refetch can leave client conversation state non-interactive after the visible response is complete;
6. whether the independently reported Web/Windows/macOS manifestations share a server-side mechanism or are distinct failure classes.

## Evidence boundary
Observed request multiplicity and recovery/refetch activity are mechanism evidence, not proof that they cause the HTTP 429. Cross-platform similarity does not prove a common root cause. The limiter scope, server-side causal chain, prevalence, and system-wide amplification remain NOT DETERMINED without vendor telemetry.

## Safety / privacy
Do not publish private case numbers, account or conversation identifiers, request/correlation identifiers, exact private timestamps, authorization material, private correspondence, filesystem paths, or precise location information. Such correlation data should remain in the private OpenAI support/engineering channel.

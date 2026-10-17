# System-Scale / Concurrent-User Amplification Hypothesis

**Status:** HYPOTHESIS — NOT DETERMINED

## Question
Could a request-amplification or recovery/refetch problem become materially worse when the same behaviour occurs across multiple affected clients at approximately the same time?

## Why this is worth investigating
The investigated case and independent public reports demonstrate that conversation retrieval can enter an HTTP 429 state and that recovery/refetch behaviour can coexist with that state. A separate public reproduction in `openai/codex#50000` reported a burst of 22 conversation-retrieval HTTP 429 responses in roughly half a second when an Activity view was populated. Other public reports describe repeated recovery polling or multiple concurrent chats.

OpenAI Support also publicly stated that an engineering improvement was deployed to stop Chat and Work from unnecessarily refreshing history after every completed turn, with the stated goal of reducing repeated requests and rate-limit pressure.

These observations make system-scale amplification a reasonable capacity/reliability hypothesis. They do **not** establish that such amplification has occurred globally or caused any specific service incident.

## Conceptual model
Let:

- `U` = number of concurrently affected clients/users;
- `B` = baseline conversation/history retrieval request rate per client;
- `A` = additional request amplification caused by refetch/recovery/retry/fan-out behaviour;
- `R_total` = aggregate request rate reaching the relevant service or limiting layer.

A deliberately simplified model is:

`R_total ≈ U × (B + A)`

If `A` is near zero, aggregate load grows mainly with legitimate baseline use. If `A` becomes positive and correlated across many clients — for example after a shared UI event, reconnect condition, completed-turn refresh, or recovery trigger — aggregate demand could rise much faster than a single-user trace suggests.

This equation is illustrative only. It is **not** a measurement of OpenAI infrastructure, user counts, capacity, rate-limit configuration or actual traffic.

## Possible positive-feedback mechanism
A failure mode worth testing is:

`shared trigger → extra retrieval/refetch demand → throttling/429 → recovery or retry behaviour → additional demand → more throttling`

At single-user scale this could appear as intermittent conversation-loading failures. At large concurrent scale, if the same trigger affects many clients and the requests converge on a shared service, shard, limiter or dependency, the aggregate effect could be substantially larger.

However, several architectures could prevent or sharply limit this effect: per-user/per-account isolation, independent rate-limit buckets, request coalescing, jittered exponential backoff, circuit breakers, caches, queueing, load shedding, shard isolation, or server-side suppression of redundant history refreshes.

## What is observed versus inferred
| Statement | Classification |
|---|---|
| Conversation/history retrieval HTTP 429 occurs in the investigated case | OBSERVED |
| Independent public reports also contain conversation-retrieval HTTP 429 evidence | REPRODUCED externally |
| Recovery/refetch behaviour can coexist with retrieval failure | OBSERVED / externally reproduced |
| Some public reproductions show short request bursts or repeated recovery polling | REPRODUCED externally |
| OpenAI Support publicly described reducing unnecessary history refreshes to reduce repeated requests/rate-limit pressure | PUBLIC VENDOR-SUPPORT STATEMENT |
| One affected client can generate more than baseline retrieval demand under some conditions | PLAUSIBLE and supported by independent observations, magnitude not generalised |
| Thousands or millions of affected clients would necessarily overload a shared backend | NOT DETERMINED |
| The observed bug has already caused a global cascading failure | NOT DETERMINED |
| A fleet-wide correlated trigger could amplify aggregate load if relevant resources/limits are shared | HYPOTHESIS consistent with distributed-systems principles |

## Evidence needed to evaluate the hypothesis
Useful server-side evidence would include aggregate request-rate time series for conversation/history retrieval, limiter scope and keying (per request, session, account, IP, shard or global), retry/refetch rates, fan-out distributions, concurrent affected-client counts, cache/coalescing behaviour, retry jitter/backoff telemetry, saturation/error correlations, and before/after telemetry for the history-refresh change acknowledged publicly by OpenAI Support.

Client-side evidence alone cannot determine whether one million users would share a bottleneck or one million effectively isolated rate-limit domains. Therefore no numerical global-load estimate is made here.

## Safe validation principle
Do not attempt to validate this hypothesis by generating load, coordinating concurrent requests, automating retries, or bypassing rate limits. Validation at meaningful scale belongs in controlled vendor-side load testing, simulation, telemetry analysis, or other authorised environments.

## Current conclusion
**System-scale amplification is a technically plausible hypothesis worth investigating, but it is not a demonstrated root cause.** The strongest next evidence would be server-side telemetry showing whether request amplification is correlated across clients and whether the relevant limiting or retrieval resources are shared at a scale where correlated client behaviour materially changes service load.
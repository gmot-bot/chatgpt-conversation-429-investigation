# Evidence Quality, Hypotheses and Engineering Test Matrix

Status: public-safe analytical framework. **Root cause is NOT DETERMINED.**

This document increases the information value of already available evidence without requiring publication of raw HAR files, private identifiers, message content, account data, IP addresses, precise locations, or private support correspondence. It does not recommend generating failures or load.

## 1. Evidence Quality Matrix

Evaluate an item on six independent dimensions rather than treating evidence volume as evidence strength.

| Dimension | Question | Stronger example |
|---|---|---|
| Provenance | Is the source and collection method known? | Direct passive observation or attributable public report |
| Directness | Observation or interpretation? | HTTP status directly observed |
| Independence | Does it add an independent observation? | Different reporter/environment, not a repost |
| Specificity | What mechanism does it actually identify? | Conversation-history retrieval specifically returned 429 |
| Reproducibility | Is the pattern repeated or independently reproduced? | Same bounded pattern observed more than once |
| Discriminatory power | Does it distinguish competing hypotheses? | Refresh failure without 429 distinguishes UI symptom from rate limiting |

Evidence grades remain descriptive, not numeric probabilities:
- **S0**: symptom report only.
- **S1**: structured observation with useful environment/timing detail.
- **S2**: direct protocol/mechanism evidence such as an observed HTTP status or passive request pattern.
- **S3**: correlated evidence that materially discriminates mechanisms; still not automatically causal proof.

### Existing evidence fingerprints

Public summaries should prefer feature fingerprints over raw artefacts: surface; operation class; observed HTTP status; whether Retry-After was observed/unknown; whether automatic refetch/recovery was observed; concurrency context; cooldown outcome; and whether the evidence is direct, inferred or unknown.

## 2. Hypothesis Registry

All entries below are investigation hypotheses, not findings.

| ID | Hypothesis | What would support it | What would weaken/falsify it | Candidate mitigation |
|---|---|---|---|---|
| H0 | Legitimate rate limiting without a client defect | Server telemetry shows policy correctly rejecting bounded traffic | Bounded legitimate traffic exceeds no documented/internal budget yet is miscounted | Clarify policy/UI; reserve critical retrieval capacity where appropriate |
| H1 | Client request amplification | Equivalent retrievals multiply around ordinary actions | One bounded request is emitted per semantic action | Coalesce/single-flight equivalent work |
| H2 | Shared account/session rate-limit bucket | Independent surfaces consume the same limiter budget | Distinct limiter keys/budgets are proven | Partition budgets or protect foreground retrieval |
| H3 | Endpoint-family limiter coupling | History/list/recovery operations share a limiter | Server telemetry shows independent limiter classes | Separate classes or weights where justified |
| H4 | Retry/backoff coordination defect | Retries occur before authoritative cooldown or across uncoordinated clients | All clients honor one coordinated cooldown | Authoritative Retry-After, exponential backoff, jitter, shared cooldown |
| H5 | Reconnect/reload thundering herd | Reopen/reconnect starts a burst of restoration operations | Reopen remains serialized/bounded | Stagger, debounce and coalesce restoration |
| H6 | Missing single-flight deduplication | Semantically equivalent in-flight requests coexist | Request-generation telemetry proves effective deduplication | Single-flight keyed by semantic resource/generation |
| H7 | Stale-state recovery loop | Failed refresh leaves state that triggers repeated recovery | Failure reaches stable terminal/cooldown state | Circuit breaker and explicit recovery state machine |
| H8 | Cancellation ownership/lifecycle race | Needed shared request is cancelled when an obsolete controller/view is disposed | Abort caller/generation proves cancellation belongs only to obsolete work | Correct AbortController ownership; retry/exclude expected cancellation from active-view failure |
| H9 | Rate-limit feedback loop | 429 triggers recovery work that increases request pressure | 429 causes only cooldown/no extra retrieval | Global/session cooldown and bounded recovery |
| H10 | Limiter misclassification of recovery traffic | Legitimate recovery/background traffic is charged indistinguishably and triggers rejection | Limiter correctly classifies/prioritizes traffic | Classify foreground, recovery and speculative work separately |
| H11 | Cache/revalidation pathology | Cache miss/stale revalidation causes redundant backend retrieval | Cache telemetry shows no amplification | Coalesce revalidation; improve cache generation/invalidation |
| H12 | Multiple independent failure modes converge on similar UI errors | 429, cancellation, 5xx or stale state produce similar user-visible failure | One mechanism explains all cases with correlated evidence | Preserve typed errors and mechanism-specific recovery/UI |

Public reports of duplicate/list-history requests and OpenAI's statement that unnecessary history refresh was removed are consistent with investigating H1/H5/H6/H9, but do not prove them. The Codex #54568 cancellation report is useful primarily as a discriminator for H8/H12: it reports refresh failure with short-lived cancellation and does not demonstrate HTTP 429 for the cancelled history request.

## 3. Failure Taxonomy

Do not collapse all conversation-loading failures into one incident class.

| Class | Observable boundary | Causal status |
|---|---|---|
| F429 | HTTP 429 directly observed on relevant retrieval/list operation | Rate limiting observed; reason/key/policy unknown |
| F4XX | Other client/auth/access response | Separate until correlated |
| F5XX | Server-side HTTP failure | Separate until correlated |
| FCANCEL | Client/transport cancellation/abort | Does not imply rate limiting |
| FTIMEOUT | Timeout without definitive HTTP outcome | Mechanism unknown |
| FSTALE | Cached/stale state or reconciliation failure | May be client, server or interaction |
| FREALTIME | Realtime/stream recovery anomaly | Temporal association is not causation |
| FUNKNOWN | User-visible load/refresh failure without mechanism evidence | Symptom only |

## 4. Falsification Matrix

A useful hypothesis must risk rejection.

- **H1/H6:** weaken if request-generation telemetry proves one coalesced retrieval per semantic action.
- **H2/H3:** weaken if server telemetry proves independent limiter keys/classes for the relevant operations.
- **H4/H9:** weaken if all clients enter one authoritative cooldown and no recovery requests occur during it.
- **H5:** weaken if reconnect/reopen emits a strictly serialized bounded sequence.
- **H7:** weaken if failed refresh transitions to a stable state without automatic recurrence.
- **H8:** weaken if abort caller/generation shows only obsolete work is cancelled and the active view owns a separate successful request.
- **H10:** weaken if limiter classification distinguishes foreground/recovery traffic and accounting is correct.
- **H11:** weaken if cache/revalidation telemetry shows no redundant backend work.
- **H12:** weaken if correlated telemetry demonstrates one common mechanism across apparently different UI failures.

## 5. Solution Matrix

Solutions are conditional engineering candidates, not prescriptions based on a determined root cause.

| Mechanism family | Candidate solution | Principal risk |
|---|---|---|
| Duplicate/equivalent work | Single-flight/coalescing | Incorrectly merging requests from different generations |
| Reconnect burst | Debounce/stagger restoration | Slower visible recovery |
| Retry pressure | Retry-After + exponential backoff + jitter | Excessive delay if policy is too conservative |
| Cross-tab/client pressure | Coordinated account/session cooldown where architecture permits | Coordination complexity |
| Recovery loop | Circuit breaker + bounded retry budget | Prematurely stopping recoverable work |
| Cancellation race | Generation-aware ownership and cancellation | Resource leaks if obsolete work is retained |
| Limiter coupling | Separate/weighted traffic classes | More complex capacity policy |
| Cache/revalidation | Generation-aware cache and coalesced revalidation | Stale-data risk if invalidation is wrong |
| Ambiguous UI | Typed error taxonomy and mechanism-specific recovery | More states to maintain/test |
| Observability gap | Correlation across request/generation/retry/cancellation | Telemetry/privacy cost; must minimize data |

## 6. Sanitized Relative Timeline

When chronology matters publicly, use relative events rather than private absolute timestamps unless the timestamp is already intentionally public:

`T+0` user action -> `T+Δ1` retrieval/recovery starts -> `T+Δ2` protocol/cancellation outcome -> `T+Δ3` UI state -> `T+Δ4` bounded cooldown/recovery outcome.

Preserve ordering and coarse deltas only when they are already evidenced. Never invent missing intervals.

## 7. Confidence and Public Evidence Map

Use qualitative labels only:
- **DIRECT OBSERVATION**: directly supported by the cited artefact.
- **CORROBORATED**: multiple independent sources support the same narrow observation.
- **PLAUSIBLE**: consistent with evidence but alternatives remain.
- **WEAK**: limited/indirect support.
- **NOT PROVED**: insufficient causal evidence.
- **CONTRADICTED FOR UNIVERSAL CLAIM**: at least one credible discriminator shows the claim cannot safely be universal.

Public evidence should map to claims, not expose private artefacts. Private evidence may be represented only by non-identifying characteristics already cleared for publication. Independent public reports remain attributed to their public source.

## 8. What Would Change Our Mind?

For every promoted hypothesis, maintain at least one explicit rejection condition. New reports that merely repeat the same symptom increase prevalence evidence, not causal confidence. Evidence that separates two mechanisms is more valuable than ten additional screenshots of the same banner.

## 9. Engineering Observability Wishlist

The following server/client fields would have high discriminatory value if OpenAI Engineering can inspect them internally. They need not be published:

- limiter key/scope/class and decision reason;
- request semantic class and request generation;
- retry reason, retry ordinal and authoritative cooldown source;
- coalescing/single-flight key and whether an equivalent request already existed;
- recovery generation/state-machine transition;
- cancellation caller/owner/reason and controller/view generation;
- correlation between foreground action, history/list/refetch/recovery and realtime activity;
- cache/revalidation decision and backend-fetch consequence;
- typed terminal outcome used by the UI;
- privacy-minimized aggregate counts sufficient to distinguish one request from amplification.

## 10. Privacy-Preserving Reproducibility Protocol

Contributors should report only the minimum discriminating information:
1. product surface and coarse platform/browser/app version;
2. user-visible symptom;
3. operation class if known (conversation open, history/list, recovery);
4. HTTP status only if naturally/passively observed;
5. whether Retry-After was observed, absent or unknown, without publishing sensitive headers;
6. whether automatic refetch/recovery/cancellation was passively observed;
7. coarse concurrency context (for example one conversation vs several), without deliberately generating load;
8. whether waiting/cooldown changed the outcome;
9. evidence class S0-S3 and explicit unknowns.

Do **not** publish cookies, credentials, tokens, authorization headers, account/user/conversation/project/channel/request/correlation IDs, IP addresses, email addresses, precise locations, private support correspondence, raw HARs containing private data, message content, local usernames or filesystem paths.

Do not repeatedly refresh, automate retries, coordinate load, bypass rate limits, or intentionally reproduce a 429. Respect Retry-After and collect passive evidence from naturally occurring failures.

## Current conclusion

The evidence supports continued investigation of several competing mechanisms. It does **not** establish a global outage, global overload, a universal WebSocket cause, an account-level limiter, request amplification as the root cause, or any single common root cause. **Root cause remains NOT DETERMINED.**

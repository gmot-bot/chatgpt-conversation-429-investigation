# Engineering Decision Tree and Evidence-to-Hypothesis Map

## Status and scope

This document maps already-public evidence to the H0-H12 registry in `evidence-quality-hypothesis-matrix.md`. It does not publish additional maintainer diagnostics, private identifiers, raw HAR material, message content, precise locations, or private support correspondence. Root cause remains **NOT DETERMINED**.

The map is qualitative. It does not assign invented probabilities. `supports` means compatible evidence that increases investigative priority; `discriminates` means evidence useful for separating hypotheses; `does not establish` marks a causal boundary.

## Evidence inventory mapped to hypotheses

| Public evidence | Strongest technical observation | Hypotheses informed | Role / boundary |
|---|---|---|---|
| Developer Community 1401283 | independent history-load 429 reports; OpenAI Support said unnecessary post-turn history refresh was reduced to lower repeated requests/rate-limit pressure | H1, H4, H6, H9; H0 remains viable | SUPPORTS investigation of repeated-request mechanisms; does not prove those mechanisms caused the maintainer case |
| `openai/codex#50000` | conversation retrieval 429 plus automatic recovery/refetch; later passive period without additional 429 after navigation stopped | H1, H4, H7, H9 | SUPPORTS temporal/request-orchestration investigation; not causal proof |
| `openai/codex#51478` | 429 on conversation retrieval routes, backoff headers, later 200 after interval, multiple automatic detail requests | H0, H1, H4, H6, H9, H10 | HIGH-VALUE discriminator for limiter/backoff/request multiplicity; limiter scope and causal amplification unknown |
| `openai/codex#54014` | conversation-read 429 plus stream recovery failure | H3, H7, H9, H12 | SUPPORTS interaction between retrieval and recovery surfaces; coupling not proved |
| `openai/codex#50969` follow-ups | repeated recovery polling associated with Too many requests | H4, H7, H9 | SUPPORTS recovery-loop hypothesis; exact 429 route not established for every event |
| `openai/codex#52884` | load/stream failures plus generic Web 429 after backoff | H0, H3, H4, H12 | ADJACENT support; route specificity insufficient for S2 |
| `openai/codex#48393` | similar Web load failures and generic Android 429 | H0, H12 | ADJACENT cross-platform corroboration only |
| `openai/codex#48464` | desktop refetch followed by conversation-read 429; same conversation later accessible in Chrome | H4, H7, H9, H12 | HIGH-VALUE state/client discriminator; 429-to-disabled-UI causation not established |
| `openai/codex#37518` | four overlapping conversation-list requests returned 429 followed by short retries | H1, H4, H5, H6, H9 | STRONG mechanism evidence for list-surface multiplicity; applicability to detail-retrieval limiter unknown |
| `openai/codex#54568` | history refresh can fail through rapid cancellation/state handling without demonstrated 429 | H8, H12 | STRONG COUNTERWEIGHT to any universal 429 explanation; adjacent, not S2 |
| Developer Community 1406889 | intermittent old/new conversation loading failure | H12 | symptom corroboration only; mechanism not established |

## Current hypothesis support ordering

This ordering is by **quality of public discriminating evidence**, not estimated probability and not a root-cause ranking.

### Tier A - investigate first

- **H12 - multiple independent failure modes produce similar UI symptoms.** Strongly motivated because both retrieval-429 cases and a cancellation-without-demonstrated-429 case exist publicly.
- **H1 - client request amplification.** Multiple public cases observe automatic or overlapping retrieval activity, and OpenAI Support publicly described reducing unnecessary history refresh to lower repeated requests/rate-limit pressure.
- **H4 - retry/backoff coordination defect.** Recovery polling, short retries, Retry-After observations and later recovery make retry coordination a high-value discriminator.
- **H7 - stale-state recovery loop.** Several reports combine failed retrieval/recovery with persistent or repeated client state transitions.
- **H9 - rate-limit feedback loop.** Plausible where 429 and recovery/retry activity coexist, but the direction of causation is not demonstrated.

### Tier B - high-value but telemetry-dependent

- **H6 - insufficient single-flight/deduplication.** Overlapping equivalent-looking requests make this testable, but semantic equivalence cannot be proved from public traces alone.
- **H3 - endpoint-family limiter coupling.** Retrieval/list/recovery surfaces coexist in reports, but shared limiter scope is unknown.
- **H0 - legitimate limiting without a client defect.** Remains a mandatory null hypothesis until limiter policy and request accounting are known.
- **H8 - cancellation ownership/lifecycle race.** Directly relevant to non-429 refresh failure and potentially to mixed symptom classes; no evidence yet connects it causally to the 429 cases.

### Tier C - plausible, presently weakly discriminated

- **H2 - shared account/session limiter bucket.** Requires server-side limiter-key telemetry or carefully independent cross-context correlation.
- **H10 - limiter misclassification.** Requires server policy/traffic-class telemetry.
- **H11 - cache/revalidation pathology.** Technically plausible but current public evidence does not isolate cache decisions.

No tier means `true`, and Tier C does not mean `false`.

## Claim -> evidence -> hypothesis -> falsifier -> engineering action

| Claim under test | Best current public evidence | Hypotheses | High-value falsifier/discriminator | Engineering action if supported |
|---|---|---|---|---|
| Client can issue redundant retrieval work | #37518, #51478, 1401283 vendor statement | H1/H6 | prove requests have distinct required generations/purposes | coalesce semantic duplicates; single-flight by stable retrieval key |
| Retry/recovery can sustain pressure after failure | #50969, #50000, #37518 | H4/H7/H9 | show all retries obey authoritative cooldown and no redundant work occurs | centralized cooldown, exponential backoff+jitter, recovery circuit breaker |
| 429 can clear after server-indicated waiting | #51478 | H0/H4 | 429 persists after correct cooldown on one bounded foreground request | make Retry-After authoritative and surface explicit cooldown state |
| Similar UI failures need not be 429 | #54568 | H8/H12 | demonstrate cancelled operation was actually server-throttled | typed cancellation vs throttling outcomes; generation-aware ownership |
| List and detail failures may share pressure | #37518 vs detail-retrieval cases | H3 | server telemetry shows independent limiter classes/keys | isolate traffic classes or reserve foreground recovery budget if coupled |
| Persistent UI state may outlive transient retrieval failure | #48464, #54568 | H7/H8/H12 | state reconciles deterministically after terminal fetch outcome | explicit terminal-state reconciliation and retry ownership |

## Engineering decision tree

1. **Classify the failed operation.** Was the terminal outcome `429`, cancellation/abort, timeout, `5xx`, other `4xx`, or unknown? Do not collapse these into one UI label.
2. **If 429:** read server limiter telemetry: limiter class/key, policy decision, authoritative cooldown, traffic class and request lineage.
3. **Check request generation and semantic equivalence.** If two in-flight retrievals target the same state generation, determine whether both were necessary. If not, test H1/H6.
4. **Check retry ownership.** After 429, determine which component scheduled each retry and whether all clients shared the same cooldown. Violations prioritize H4/H9.
5. **Check recovery state.** If a failed retrieval changes client state and triggers more retrieval/recovery work, test H7/H9 with a bounded lineage graph.
6. **If cancellation/abort rather than 429:** capture cancellation owner/reason and active generation. This prioritizes H8/H12 and prevents misclassification as throttling.
7. **Compare list/detail/recovery limiter classes.** Shared key/class supports investigation of H3; independent classes weaken H3 for that event.
8. **Inspect cache/revalidation decision only after the higher-value branches above.** Unexpected backend revalidation without state change raises H11.
9. **Retain H0.** If one necessary foreground request exceeds a documented legitimate budget with no redundant client work, a client defect is not required to explain that event.
10. **Close only at causal evidence.** A UI symptom, request count or temporal sequence alone is insufficient for root cause.

## Highest-value private telemetry for OpenAI Engineering

No additional public disclosure is needed. Internally, the most discriminating fields would be:

1. limiter class, key/scope and policy decision;
2. request generation / stable semantic retrieval key;
3. foreground vs speculative/background/recovery traffic class;
4. retry ordinal, scheduler owner and cooldown source;
5. authoritative Retry-After decision and whether clients obeyed it;
6. recovery generation and trigger reason;
7. cancellation owner, reason and active generation;
8. cache/revalidation decision and backend-hit status;
9. server request lineage linking an initiating user action to derived work;
10. typed terminal outcome consumed by the UI state machine.

These fields would distinguish several hypotheses without exposing them publicly.

## Safe next evidence policy

Do not generate failures, automated retries, parallel load, reconnect storms or rate-limit bypass attempts. Prefer:

- passive evidence from naturally occurring failures;
- independent public reports that already contain discriminating diagnostics;
- vendor/server telemetry;
- sanitized categorical features rather than raw identifiers;
- relative sequence (`T+delta`) rather than identifying timestamps when public timing is unnecessary.

## Root-cause statement

**ROOT CAUSE: NOT DETERMINED.**

The strongest current conclusion is methodological: the public evidence justifies testing request orchestration, retry/recovery and state reconciliation while simultaneously preserving cancellation and legitimate rate limiting as competing explanations. The evidence does not justify claiming a global outage, global overload, one universal failure mechanism, or a specific limiter implementation.

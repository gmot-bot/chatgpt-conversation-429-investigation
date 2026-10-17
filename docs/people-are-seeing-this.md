# Other People Are Seeing This

<p align="center"><a href="../README.md"><img src="../assets/chatgpt-community-hero-social-preview.jpg" alt="ChatGPT Conversation Errors — return to project home" width="420"></a></p>


This index helps visitors find similar public observations. It is **not a prevalence dashboard** and does not claim that reports share one root cause.

## Symptom families represented in the current evidence set

| Symptom family | Public evidence in this repository | Interpretation |
|---|---|---|
| Conversation/history retrieval with HTTP 429 | YES | Directly demonstrated in some independent reports |
| `Retry-After` / backoff signal with retrieval 429 | YES | Directly demonstrated in at least part of the evidence set |
| Overlapping/automatic conversation retrieval or refetch | YES | Relevant to request-amplification hypotheses; causality not established |
| Visible/searchable conversation that will not open | YES | User-visible application state; mechanism not identified by symptom alone |
| History-loading failure without demonstrated 429 | YES | Important counterexample supporting multiple possible mechanisms |
| Realtime/recovery symptoms near loading failure | YES | Correlation; not proof that realtime causes retrieval failure |

For the actual source links and evidence grades, use [Independent public reports](independent-public-reports.md) and the [Reproduction matrix](reproduction-matrix.md).

## “Me too” policy

If your report has the same symptom and no new discriminator, reply to the closest Discussion instead of opening a duplicate Issue. Open a structured report when you add material information such as a different terminal outcome, a directly observed 429, an authoritative backoff signal, a reproducible state transition, or useful privacy-safe technical evidence.

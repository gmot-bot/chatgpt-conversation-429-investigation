# Discoverability V3 — Public Report Triage

This page adds discriminating public reports without treating similar symptoms as proof of a common root cause. **ROOT CAUSE: NOT DETERMINED.**

| Public report | Evidence class | Discriminating value | H0-H12 impact | Boundary |
|---|---|---|---|---|
| `openai/codex#38763` | S0/S1 | Normal interactive use can produce a conversation-access `Too many requests` restriction; waiting restored access | H0, H4, H9, H12 | UI report; does not establish endpoint/limiter scope |
| `openai/codex#48683` | S0/S1 | A loaded conversation can become unavailable again and already-open tabs may not preserve access | H7, H12 | No common mechanism established |
| `openai/codex#41130` | Adjacent mechanism evidence | Background activity was reported near conversation-access 429 while the user was not actively interacting | H1, H6, H9, H12 | Issue concerns a broader background-request mechanism; not proof for conversation retrieval |
| `openai/codex#36841` | Counterexample / adjacent | Conversation history failed with HTTP 500 timeout and no relevant 429 | H12; weakens universal-429 explanations | Distinct demonstrated terminal outcome |
| `openai/codex#38503` | S0/S1 | Conversation access can be temporarily blocked during normal web navigation; reports distinguish UI observation from unobserved HTTP mechanism | H0, H4, H12 | Do not upgrade to S2 without network evidence |

## Why these reports matter

The new set improves **discrimination**, not volume. #36841 is especially useful because it demonstrates that a similar history-loading symptom can have a non-429 terminal outcome. #48683 adds a state-transition symptom (content appears, then becomes unavailable). #41130 is useful only as adjacent evidence that background work can matter to request pressure; it is not treated as a reproduction of the same mechanism.

## Inclusion rule

Future reports should be added only when they contribute at least one of: a new terminal outcome, a new platform/surface discriminator, direct retrieval evidence, a retry/backoff discriminator, a state-transition discriminator, or a falsifier for an existing hypothesis. Redundant symptom-only reports can be referenced without expanding the causal evidence set.

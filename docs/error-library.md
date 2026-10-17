# ChatGPT Error & Problem Library

<p align="center"><a href="../README.md"><img src="../assets/chatgpt-community-hero-social-preview.jpg" alt="ChatGPT Conversation Errors — return to project home" width="420"></a></p>


This is a non-technical index of symptoms reported around conversation/history access. Matching an error message does **not** prove that two cases have the same technical cause.

| Symptom / message | What is confirmed here | Safe next step | Status |
|---|---|---|---|
| Conversation will not open | This symptom exists in independent public reports | Stop repeated retries; read the symptom page | REPORTED / INVESTIGATING |
| `Too many requests` / HTTP 429 | 429 has been directly observed on conversation retrieval in some public reports | Respect cooldown/Retry-After when present | CONFIRMED IN SOME REPORTS |
| History not loading | Public reports include history-loading failures with different terminal outcomes | Do not assume 429; record exact wording | MULTIPLE POSSIBLE MECHANISMS |
| Visible/searchable but will not open | Visibility and successful body retrieval can diverge | Preserve the observation; avoid retry loops | REPORTED |
| `Couldn't refresh messages` | A refresh/recovery symptom; wording alone does not identify cause | Record exact wording and what happened next | UNDER INVESTIGATION |
| `Resume stream unavailable` | A recovery/realtime symptom; proximity to 429 does not prove causation | Avoid reconnect storms; report passively | UNDER INVESTIGATION |

## Status vocabulary

- **REPORTED** — one or more observations exist.
- **INVESTIGATING** — evidence is being compared; cause is not established.
- **WORKAROUND AVAILABLE** — a bounded mitigation has helped in some circumstances; it is not proof of cause.
- **CONFIRMED IN SOME REPORTS** — the stated technical outcome was directly observed in those reports only.
- **MULTIPLE POSSIBLE MECHANISMS** — similar UI symptoms have different demonstrated technical outcomes.
- **CONFIRMED FIX** — reserved for strong evidence that a specific fix addresses a specific demonstrated mechanism.

See [What we know and do not know](what-we-know.md) for the current evidence boundary.

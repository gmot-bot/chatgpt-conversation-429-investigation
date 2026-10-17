# Known Problems / Recently Reported

<p align="center"><a href="../README.md"><img src="../assets/chatgpt-community-hero-social-preview.jpg" alt="ChatGPT Conversation Errors — return to project home" width="420"></a></p>


This is the fast community index. It answers five questions: **Are others reporting it? What do we know? Is there a workaround? Is it resolved? Where do I get help?**

> Community reports are self-selected. Counts or frequency here must never be interpreted as ChatGPT-wide prevalence.

| Problem | Others reporting similar symptoms? | What we know | Workaround / safe action | Resolved? | Help |
|---|---|---|---|---|---|
| Conversation/history will not open | YES | Independent public reports exist; mechanisms may differ | Stop repeated retries; record exact wording; normal wait | NOT AS ONE UNIVERSAL PROBLEM | [Help](../HELP.md) |
| `Too many requests` / HTTP 429 | YES | 429 directly demonstrated on retrieval in some public reports | Respect `Retry-After`/cooldown when present | NOT UNIVERSALLY | [429 page](errors/too-many-requests-429.md) |
| Visible/searchable but will not open | YES | Visibility and successful body retrieval can diverge | Preserve passive observation; avoid retry loop | INVESTIGATING | [Symptom page](errors/visible-but-wont-open.md) |
| History-loading failure without demonstrated 429 | YES | Counterevidence exists against a one-mechanism explanation | Record exact terminal outcome if naturally available | INVESTIGATING | [History page](errors/history-not-loading.md) |
| `Couldn't refresh messages` | REPORTED | Wording alone does not identify mechanism | Avoid repeated refresh; record exact wording | INVESTIGATING | [Symptom page](errors/couldnt-refresh-messages.md) |
| `Resume stream unavailable` | REPORTED | Recovery/realtime symptom; causal role not proved | Avoid reconnect storms | INVESTIGATING | [Symptom page](errors/resume-stream-unavailable.md) |

## Recently reported vs currently widespread

`Recently reported` means a public observation was found or submitted recently. It does **not** mean the problem is currently widespread. This project does not estimate global incidence from repository activity.

## Update rule

A row changes only after a public contribution passes privacy review and adds a verified symptom, a discriminating technical delta, a repeated safe workaround, or a confirmed resolution/fix. Missing information stays `UNKNOWN`.

# Independent and Related Public Reports

These sources are included to establish that materially similar symptoms and, in some cases, conversation-retrieval HTTP 429 responses have been independently reported. Inclusion does **not** mean that all reports share a common root cause.

## OpenAI Developer Community — late September 2026

**ChatGPT Web frequently shows “Unable to load GPT conversation” after the recent UI update**  
https://community.openai.com/t/chatgpt-web-frequently-shows-unable-to-load-gpt-conversation-after-the-recent-ui-update/1401283

The thread contains independent reports of existing/history conversations failing to load. Multiple contributors report HTTP 429 observations. On September 29, an `OpenAI_Support` account stated that an improvement had been rolled out to stop Chat and Work from unnecessarily refreshing history after every completed turn, with the stated aim of reducing repeated requests and rate-limit pressure.

**Classification:** independent symptom reproduction; independent HTTP 429 reports; public vendor-support acknowledgement of repeated-request/rate-limit pressure. This does not prove that the maintainer's case has the same root cause.

## openai/codex GitHub issue #50000 — October 2026

**[Windows] Existing chats intermittently show “Couldn't load this ChatGPT conversation”**  
https://github.com/openai/codex/issues/50000

The issue documents existing conversations intermittently failing to open. Follow-up diagnostics report HTTP 429 responses from conversation retrieval, automatic recovery/refetch behaviour, and additional independent reproductions. One reproduction reports fresh 429s during sequential conversation navigation without pressing `Try again`; another reports no additional 429s during a subsequent passive observation period after navigation stopped.

The issue author proposes request amplification/recovery behaviour as a working hypothesis and explicitly does not present it as a permanent conclusion.

**Classification:** independent symptom reproduction; independent HTTP reproduction; relevant independent recovery/refetch observations; convergence of investigative hypothesis. **Common root cause remains NOT DETERMINED.**

## OpenAI Developer Community — October 2026

**ChatGPT conversations not loading for 5 days — Recurring issue affecting old and new chats**  
https://community.openai.com/t/chatgpt-conversations-not-loading-for-5-days-recurring-issue-affecting-old-and-new-chats/1406889

This report describes both existing and newly created conversations becoming unable to load, with intermittent behaviour.

**Classification:** related/independent symptom report. The source, by itself, does not establish the same mechanism or root cause as this repository.

## Interpretation rule

Public reports strengthen the conclusion that the user-visible symptom is not unique to this maintainer. Reports containing independently inspected HTTP 429 responses also establish that conversation-loading 429s are not unique to the maintainer's evidence.

They do not establish that every affected account, platform or conversation shares one causal mechanism. `Related report`, `independent symptom reproduction`, `independent HTTP reproduction`, `mechanism evidence`, and `common root cause` remain separate categories throughout this project.

## Additional GitHub reports reviewed — October 2026

### `openai/codex#54014` — macOS desktop

A separate reporter describes a ChatGPT-backed desktop conversation that remained marked active but became inaccessible. The report states that inspected logs contained `Resume stream unavailable` / HTTP 404 and repeated conversation-read HTTP 429 / `Too many requests` responses persisting for more than two hours.

**Classification:** independent symptom reproduction; independent conversation-retrieval HTTP 429 reproduction; relevant stream-recovery evidence. The report does not establish whether the underlying task continued or whether it shares the maintainer's root cause.

Source: https://github.com/openai/codex/issues/54014

### `openai/codex#50969` follow-ups — Windows desktop / ordinary Chat

Although the base issue concerns renderer crashes, later follow-ups separately document ordinary Chat recovery failures. The reporter records `Resume stream unavailable`, subsequent recovery polling rejected with `Too many requests`, and a later recovery loop reaching at least attempt 59 at roughly five-second intervals. Cross-client conversation availability also became inconsistent.

**Classification:** related independent symptom reproduction; strong recovery/polling mechanism evidence associated with `Too many requests`. Because the cited follow-ups do not expose the exact HTTP conversation-read route for every 429, this entry is not promoted here to an independent S2 retrieval reproduction.

Source: https://github.com/openai/codex/issues/50969

### `openai/codex#52884` — macOS desktop and Work web

The base report documents repeated conversation-load and stream/session failures across desktop and web, including a fresh low-context Work conversation. An independent commenter reports the same load error on desktop and web and HTTP 429 responses on web even after respecting `Retry-After`, but does not identify the exact request route in the public comment.

**Classification:** related independent symptom reproduction; generic HTTP 429/backoff corroboration. Not promoted to S2 conversation-retrieval reproduction because the relevant endpoint is not demonstrated in the cited public evidence.

Source: https://github.com/openai/codex/issues/52884

### `openai/codex#48393` — Web / Android

This earlier report describes intermittent existing-conversation load failures on Web and `Too many requests` on Android during normal use. It deliberately makes no root-cause claim. The Android 429 is not tied publicly to a demonstrated conversation/history retrieval endpoint.

**Classification:** related independent symptom report; generic 429 corroboration only. It does not satisfy the S2 retrieval-HTTP-429 gate used by this repository.

Source: https://github.com/openai/codex/issues/48393

### `openai/codex#51478` — ChatGPT Web / Windows desktop

This independent report contains direct browser DevTools/HAR evidence of repeated HTTP 429 responses on both `/backend-api/conversation/{conversation_id}` and `/backend-api/conversations/{conversation_id}`. It also reports `Retry-After` and `x-oai-history-initial-retry-after`, later HTTP 200 recovery after the interval, and multiple automatic conversation-detail requests during ordinary frontend navigation.

**Classification:** independent symptom reproduction; independent conversation-retrieval HTTP 429 reproduction; backoff-header reproduction; relevant request-multiplicity observation. Automatic request multiplicity is observed, but its causal contribution to throttling and any common root cause remain NOT DETERMINED.

Source: https://github.com/openai/codex/issues/51478

### `openai/codex#48464` — macOS desktop / Chat

This independent report documents an existing Chat-mode conversation whose refetch transitioned from `idle` to `streaming`, followed by `GET /conversations/{conversation_id}` returning HTTP 429 and a logged refetch failure. A later navigation back to the same desktop conversation again produced a conversation-read 429 while Send and dictation remained disabled. The same conversation loaded successfully in Chrome. The reporter explicitly notes that correlation does not prove that the 429 caused the disabled composer state.

**Classification:** independent symptom reproduction; independent conversation-retrieval HTTP 429 reproduction; relevant refetch/state-recovery evidence. The causal relationship between the retrieval 429 and persistent desktop UI state remains NOT DETERMINED.

Source: https://github.com/openai/codex/issues/48464

### `openai/codex#37518` — macOS desktop / Chat sidebar

This independent report documents focus-triggered sidebar reloads. In one reproduced occurrence, the focused primary renderer initiated four overlapping `GET /conversations` requests and all four returned HTTP 429, followed by short-interval retries. The report also records substantially more `/conversations` 429 responses after an application update than in the previous build. These observations concern conversation-list retrieval rather than proving the same detail-retrieval failure mechanism as the maintainer case.

**Classification:** independent HTTP 429 and request-multiplicity evidence on the conversation-list surface; relevant mechanism evidence. It is not promoted as proof of a common root cause or of the same detail-retrieval limiter.

Source: https://github.com/openai/codex/issues/37518


### `openai/codex#54568` — Windows/macOS desktop / history refresh cancellation

This newer independent report describes an existing Dot conversation reopening with cached messages and then a `Couldn't refresh messages` / retry state. On Windows, selected logs show the initial history fetch being aborted after roughly 70–85 ms and reported as `client.history ... load_failed`; later unrelated requests returned HTTP 200. A macOS comparison on the same reported build also observed short-lived room/history cancellations and later successful room/history operations.

The report proposes cancellation ownership/controller replacement as a static-code hypothesis, but explicitly lacks a runtime abort call stack and does not prove a Windows/macOS common root cause. It does **not** demonstrate HTTP 429 on the cancelled history operation.

**Classification:** independent history-refresh failure and cancellation/state-handling mechanism evidence; useful adjacent discriminator. Not S2 conversation-retrieval HTTP 429 evidence, and not proof of the same root cause as this repository's investigated case.

Source: https://github.com/openai/codex/issues/54568

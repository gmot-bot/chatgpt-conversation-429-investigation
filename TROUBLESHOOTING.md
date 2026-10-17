# Safe Troubleshooting

This guide is deliberately conservative. It is intended to help affected users gather useful information without creating extra load or exposing private data.

## Safe things to try

- Stop repeated manual refresh/retry activity and allow any indicated cooldown to expire.
- If a `Retry-After` signal is visible during normal diagnostics, respect it.
- Record the exact user-visible error text without including private conversation content.
- Record the platform/app family and whether the conversation is old/existing or newly created.
- Note whether the conversation remains visible in history/search while failing to open.
- If naturally observed, note whether another already-authorized client behaves differently. Do not create repeated cross-device tests.
- Preserve coarse relative sequence such as `T+0`, `T+30s`, rather than publishing identifying timestamps when unnecessary.
- Check the official service status separately; a status incident can be relevant context but does not prove the cause of an individual failure.

## Things not to do

- Do not hammer Refresh or Try again.
- Do not automate retries, reconnects or parallel requests.
- Do not attempt to bypass rate limits.
- Do not publish HAR files without sanitizing them first.
- Do not post cookies, authorization headers, tokens, account IDs, conversation IDs, request/correlation IDs, IP addresses, email addresses, precise locations or private messages.
- Do not infer that WebSocket/realtime activity caused a 429 merely because it occurred nearby in time.

## What helps an investigation

Useful, privacy-preserving observations include: exact error wording; coarse platform/app family; whether HTTP 429 was directly observed on the relevant retrieval request; whether `Retry-After` was present; whether automatic refetch/recovery was directly observed; and what happened after normal activity stopped.

See [Evidence policy](EVIDENCE_POLICY.md) before contributing technical material.

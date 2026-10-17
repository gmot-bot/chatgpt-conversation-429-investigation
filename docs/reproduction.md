# Safe Reproduction / Observation

This project does not ask contributors to force the condition.

If a historical conversation naturally fails to open, record the user-visible symptom first. If browser developer tools are already being used safely, note only whether a conversation/history retrieval request demonstrably failed and its HTTP status. Do not repeatedly reload or retry to manufacture evidence.

If HTTP 429 is observed, stop active retries and respect any `Retry-After` instruction. Do not publish the full request URL when it contains unique identifiers; do not publish request IDs, correlation IDs, cookies, tokens, account IDs, conversation IDs or IP addresses.

Realtime/recovery behaviour should be reported only when directly observed. Do not infer WebSocket/recovery involvement merely because a chat failed to open.

For server-side correlation, exact identifiers may be useful to the vendor. Supply them privately to the appropriate support channel, not to this repository.

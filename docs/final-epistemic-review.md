# Final Epistemic Review

## Facts supported by the current public evidence
- Conversation/history retrieval HTTP 429 has been observed in the maintainer evidence and independently reproduced in public reports.
- Backoff signals including `Retry-After` have been independently reported on relevant retrieval paths.
- Automatic recovery/refetch/polling and request multiplicity have been independently observed in temporal association with retrieval failures.
- Some reports show cross-client differences in availability of the same or related conversation state.

## Supported inferences
- The evidence makes an explanation confined to one local browser cache/profile less sufficient for the overall observed failure class.
- Client recovery/refetch/backoff orchestration is a high-value engineering investigation target.
- Cross-platform reports justify investigating shared backend or shared client-orchestration components, while not proving either.

## Hypotheses
- Automatic recovery/refetch/list refresh may increase request volume enough to contribute to throttling in some affected states.
- Insufficient deduplication/coalescing or backoff coordination may prolong some failure episodes.
- Aggregate amplification across many clients is technically plausible but unmeasured.

## Not proved
- The exact limiter scope or key.
- That request multiplicity causes the observed 429 rather than accompanying an already rate-limited state.
- A common root cause across Web, Windows, macOS, Android or Work surfaces.
- Global service overload or cascading failure.
- The number or proportion of affected users.
- Any definitive server-side causal mechanism.

**Final root-cause classification: NOT DETERMINED.**

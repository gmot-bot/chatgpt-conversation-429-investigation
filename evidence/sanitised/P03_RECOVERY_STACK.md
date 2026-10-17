# P03 — Recovery-linked retrieval path

**Artefact type:** public explanatory derivative; not a raw screenshot or verbatim source-code dump.

A preserved private client-side breakpoint/initiator trace showed the following relevant functional sequence around an observed conversation-detail retrieval:

`handleOpen` → `handleConnect` → `ensureSubscribed` → `notifyPotentialMissedMessages` → recovery listener path → request helper path → `fetch`

## Claim supported
In the investigated observation, a realtime/recovery-related client path was capable of reaching a conversation retrieval request.

## Claim NOT supported
This does not prove that every recovery event triggers a retrieval, that the path is defective, that it bypasses coalescing/deduplication, or that it caused the observed HTTP 429 responses.

## Privacy/copyright transformation
Unique URLs, identifiers, absolute timestamps, request/correlation values, source bundle fingerprints and unrelated call-stack/source material were intentionally omitted. The sequence above is a minimal factual transcription of function names needed to describe the observed relationship; it is not represented as the original artefact.

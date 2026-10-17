# Incident Summary

## Primary symptom
Existing/historical ChatGPT conversations may remain visible or searchable while failing to open normally.

## Investigated technical manifestations
In the maintainer's case, preserved client-side evidence includes conversation/history retrieval returning HTTP 429, server-provided backoff headers, successful realtime WebSocket establishment during history-retrieval failure, `conversation-update` / `refetch-conversation` events, and observed recovery-linked conversation retrieval.

## Scientific boundary
The coexistence and temporal correlation of these observations does not establish a causal chain between realtime behaviour and HTTP 429. The final limiter scope/key, relevant server-side state and root cause are not determined from client-side evidence.

## Impact
The practical impact is loss of reliable access to existing work even when the conversation remains represented in the interface. This investigation focuses on preservation, reproducibility, safe mitigation and root-cause clarification rather than blame attribution.

# FAQ — ChatGPT Conversation Loading Failures

## Why are my ChatGPT conversations not loading?

This repository documents several public cases where existing conversations failed to open, but the available evidence does not establish one universal cause. Demonstrated mechanisms include conversation-retrieval HTTP 429 in some reports and cancellation/state-handling failures without demonstrated 429 in another. Root cause for the investigated case remains **NOT DETERMINED**.

## What does HTTP 429 / Too Many Requests mean?

HTTP 429 indicates that a request was rate-limited. It does not, by itself, reveal the limiter scope, why the budget was exceeded, whether client request amplification contributed, or whether the limiting behaviour was expected.

## Why can I see a conversation but not open it?

Visibility in history/search and successful retrieval of the conversation body are distinct application behaviours. Public reports show cases where a conversation remains discoverable while opening or refreshing fails.

## Is this a global ChatGPT outage?

This repository does **not** claim a global outage or global overload. Independent reports establish that similar symptoms and conversation-retrieval 429 responses have occurred for multiple users, not that every case shares one root cause.

## Can automatic retries or refetches contribute?

They are a plausible hypothesis. Public evidence includes overlapping/automatic retrieval activity and recovery polling, but causal contribution must be demonstrated rather than assumed.

## Can the same UI error happen without HTTP 429?

Yes. A reviewed public report documents history-refresh failure associated with rapid cancellation/state handling without demonstrating 429 on the cancelled history operation. This is why the project keeps multiple competing hypotheses.

## Should I keep pressing Retry?

No. Repeated retries can add traffic and reduce evidential value. Stop repeated activity, respect any cooldown/`Retry-After`, and prefer passive observation.

## What should I report?

Exact error wording, coarse platform/app family, whether the chat remained visible/searchable, whether 429 was directly observed on the relevant retrieval path, any coarse backoff signal, and directly observed recovery/refetch behaviour. Do not publish unique identifiers or private content.

## Is the repository affiliated with OpenAI?

No. It is an independent community investigation intended to complement, not replace, private Support/Engineering escalation.

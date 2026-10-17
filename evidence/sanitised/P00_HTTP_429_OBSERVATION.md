# P00 — HTTP 429 observation

**Artefact type:** public explanatory derivative from preserved private/raw forensic evidence.

During the investigated condition, preserved browser-network evidence showed repeated conversation/history retrieval requests returning **HTTP 429**.

A separately minimised public derivative (`P01_BACKOFF_HEADERS.png`) shows the relevant generic backoff headers from one preserved 429 response, including `Retry-After` and `X-Oai-History-Initial-Retry-After`, while unique correlation data and the absolute timestamp are redacted.

## Evidentiary boundary
This public text is not a substitute for the preserved raw/private evidence. Exact request URL, conversation identifier, request/correlation identifiers and absolute incident timestamp are deliberately withheld from the public repository.

The observation proves that HTTP 429 occurred during conversation/history retrieval in the investigated case. It does not, by itself, establish why the rate limit occurred or whether it was the primary cause of every historical-chat opening failure.

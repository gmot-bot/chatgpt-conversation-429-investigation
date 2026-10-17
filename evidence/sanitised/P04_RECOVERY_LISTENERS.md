# P04 — Recovery-listener observation

**Artefact type:** public explanatory derivative; not a raw screenshot or verbatim source-code dump.

Preserved private evidence showed a client-side function named `notifyPotentialMissedMessages()` iterating registered `recoveryListeners`. Adjacent client logic also showed subscription/retry handling.

## Claim supported
The observed client implementation contains a recovery-listener mechanism for notifying potential missed-message conditions.

## Claim NOT supported
The evidence does not establish how many listeners were active for every event, that equivalent listener paths necessarily produced duplicate HTTP requests, that retry handling was incorrect, or that this mechanism was the root cause of the historical-chat opening failure.

## Privacy/copyright transformation
The public derivative omits the proprietary source body except for the minimum function/mechanism names necessary to state the observation. Source bundle fingerprints, exact source locations, absolute timestamps, URLs and unique identifiers are excluded.

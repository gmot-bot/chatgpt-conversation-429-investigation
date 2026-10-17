# Contributing

This repository is evidence-first. Its purpose is to reduce uncertainty, not accumulate agreement.

## Contribution classes
Use one of these epistemic classes whenever possible:
- `OBSERVED` — directly observed behaviour with sufficient context.
- `REPRODUCED` — independently reproduced behaviour with evidence.
- `INFERRED` — conclusion derived from observations but not directly observed.
- `HYPOTHESIS` — testable explanation requiring further evidence.
- `NOT DETERMINED` — evidence is insufficient to decide.

A report saying only “same here” may be useful as a symptom report, but it will not be treated as an independent technical reproduction.

## Before submitting
Remove account/user IDs, conversation IDs, project/channel IDs, request IDs, IP addresses, email addresses, cookies, tokens, authentication headers, precise location, sensitive URLs, unrelated conversation content, local usernames and filesystem paths.

Do not upload raw HAR files or complete browser/network exports. If such material is needed for vendor correlation, provide it privately to the appropriate support channel rather than posting it here.

## Safe observation
Do not intentionally generate repeated failures, defeat rate limits, automate retries, create load, or bypass safeguards to reproduce this issue. Respect `Retry-After` and other server-provided backoff instructions. Existing naturally occurring evidence is preferred.

## Quality gate
A technically useful report should state the user-visible symptom, platform/browser family, whether the conversation remained visible/searchable, the demonstrated HTTP status if inspected, whether realtime/recovery evidence was actually observed, and which conclusions remain uncertain.

Similar symptoms are not automatically evidence of the same root cause. Maintainers may label reports `needs-evidence`, `related-report`, `not-same-issue` or `unverified` when appropriate.

## Conduct
Technical disagreement, alternative explanations and attempts to falsify hypotheses are welcome. Personal attacks, speculation presented as fact, vendor-bashing, credential disclosure, privacy-invasive investigation and attempts to identify contributors are not.

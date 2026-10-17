# Public Reproduction Matrix

This matrix is intentionally conservative. It records evidence classes, not votes. Similar symptoms do not automatically imply a common root cause.

| Source / surface | S0: fails to open | S1: visible/searchable but unavailable | S2: retrieval HTTP 429 | S3: recovery/refetch evidence | Common root cause |
|---|---:|---:|---:|---:|---|
| Maintainer investigated case — Web | OBSERVED | OBSERVED | OBSERVED | OBSERVED | NOT DETERMINED |
| OpenAI Developer Community thread 1401283 — Web / Windows reports | REPRODUCED externally | Reported in thread | REPRODUCED externally by multiple contributors | Recovery polling reported by at least one contributor | NOT DETERMINED |
| `openai/codex#50000` — Windows desktop | REPRODUCED externally | Existing chats intermittently unavailable | REPRODUCED externally | REPRODUCED externally | NOT DETERMINED |
| `openai/codex#50000` follow-up — macOS desktop | REPRODUCED externally | Reported | Reported with desktop/console evidence | Recovery-related evidence reported | NOT DETERMINED |
| Developer Community thread 1400945 — Web / Projects | REPRODUCED externally | OBSERVED by reporter: searchable conversations can fail to open | Not required for this classification | Not established by base report | NOT DETERMINED |
| Developer Community thread 1406889 — old/new chats | Related independent symptom report | Intermittent unavailability reported | Not established by source used here | Not established by source used here | NOT DETERMINED |

## Promotion criteria

`related-report` → a materially similar user-visible symptom is described, but technical equivalence is not established.

`independent-symptom` → another reporter independently demonstrates S0/S1 with enough context to distinguish the event from deletion, simple navigation error or an obviously unrelated outage.

`independent-http-429` → the reporter independently inspects the affected conversation/history retrieval path and demonstrates HTTP 429. A generic 429 elsewhere in the application is insufficient.

`mechanism-evidence` → the reporter provides evidence of realtime/recovery/refetch/retry/fan-out behaviour relevant to the affected retrieval path. Temporal proximity alone does not prove causation.

`common-root-cause` → requires evidence linking failure mechanisms across cases, ideally vendor/server-side correlation or another comparably strong causal discriminator. No public report currently satisfies this gate for the entire failure class.

## Platform interpretation
Cross-platform observations increase the priority of explanations above a single browser profile or single local cache. They do not prove that Web, Windows, macOS, Android and iOS use identical retrieval/recovery paths or share the same limiting scope.
# Community Triage Ledger

This ledger is the operational index for public contributions. It intentionally starts empty of invented historical rows. Existing historical evidence remains in its established evidence tables until it can be normalized without inference.

## Allowed dispositions

`NEW` · `PRIVACY_HOLD` · `DUPLICATE_CANDIDATE` · `DUPLICATE_CONFIRMED` · `HELP_ROUTED` · `STATUS_CANDIDATE` · `WORKAROUND_CANDIDATE` · `EVIDENCE_CANDIDATE` · `AGGREGATE_ELIGIBLE` · `OUT_OF_SCOPE`

## Ledger schema

| contribution_key | public source | received/reviewed | symptom_family | platform | terminal_class | duplicate_of | disposition | evidence_grade | aggregate_eligible | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| *No V4.5-normalized contributions yet* | — | — | — | — | — | — | — | — | NO | Historical material is not silently backfilled. |

## Rules

- `contribution_key` must not encode username, email, account ID, conversation ID, request ID, IP or precise location.
- Public source may link to a public Issue/Discussion; aggregate tables do not expose contributor identity.
- `duplicate_of` is assigned only after review, not fuzzy-match automation alone.
- `evidence_grade` stays `UNKNOWN` until grading is justified.
- `aggregate_eligible=YES` requires the statistical gate, not merely a valid report.
- Corrections are append/audit friendly; do not silently rewrite a materially changed classification without noting the reason.

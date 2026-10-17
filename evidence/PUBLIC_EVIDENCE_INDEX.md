# Public Evidence Index

**Status:** PUBLIC-SAFE REVIEW IN PROGRESS — publication still requires final HUMAN_GATE.

Private Engineering screenshots, raw forensic artefacts, HAR files, private support correspondence, exact correlation identifiers and absolute forensic timelines are excluded from this public tree.

| ID | Public artefact | Claim supported | Transformation |
|---|---|---|---|
| P00 | `sanitised/P00_HTTP_429_OBSERVATION.md` | Repeated conversation/history retrieval HTTP 429 was observed in the investigated case. | Explanatory derivative; exact URL/IDs/timestamp withheld. |
| P01 | `sanitised/P01_BACKOFF_HEADERS.png` | Relevant generic backoff response headers were observed on a preserved 429 response. | Unique correlation values, build value, report endpoint and absolute timestamp redacted; image re-rasterised; ancillary PNG metadata removed. |
| P02 | `sanitised/P02_REFETCH_EVENT.png` | `conversation-update` / `refetch-conversation` events were observed. | Cropped to minimum event fragments; identifiers/payload content and absolute time column excluded; ancillary PNG metadata removed. |
| P03 | `sanitised/P03_RECOVERY_STACK.md` | An observed recovery-related client path could reach conversation retrieval. | Minimal factual transcription; unique URLs/IDs/timestamps/source fingerprints and unrelated source omitted. |
| P04 | `sanitised/P04_RECOVERY_LISTENERS.md` | A recovery-listener mechanism for potential missed messages was observed. | Explanatory derivative; proprietary source body and fingerprints omitted. |

## Integrity boundary
P00–P04 are privacy-minimised **derivatives**, not raw originals. Their transformations are disclosed. They do not replace the preserved private/raw evidence used for forensic chain of custody.

## Current review results
- P01 visual readback: PASS for intended public claim and direct-identifier minimisation.
- P02 visual readback: PASS for intended public claim and direct-identifier minimisation.
- PNG binary chunk audit: PASS — P01/P02 contain only structural `IHDR`, `IDAT`, `IEND` chunks.
- Text identifier scan: PASS after removing the internal publication-gate file from the prospective public Git tree.
- Cross-correlation risk: REDUCED, NOT ZERO. Product-specific event/function names are intentionally retained because they are material to the technical claim.

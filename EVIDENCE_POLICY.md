# Evidence Policy

## Principle
The repository distinguishes evidence from interpretation. A public artefact should contain the minimum information necessary to support the claim for which it is cited.

## Evidence classes
1. `PUBLIC-DERIVED` — privacy-minimised derivative approved for public release.
2. `PRIVATE-ENGINEERING` — derivative intended only for private vendor/engineering correlation; never assume it is public-safe.
3. `RAW-FORENSIC` — preserved original; never publish from this repository.
4. `EXTERNAL-PUBLIC` — independently published material referenced at its original public source.

## Integrity rules
Raw originals are not modified. Public derivatives must never be represented as raw originals. Redactions, crops, relative-time transformations and other privacy transformations must be disclosed when material to interpretation.

No synthetic identifier, timestamp, header or network value may be inserted and presented as original evidence.

## Public minimisation
Public evidence must exclude unique account/conversation/project/channel identifiers, request/correlation IDs, IP addresses, authentication/session material, emails, local usernames/paths, precise location, private support case numbers and unrelated conversation content.

Exact timestamps and client build/source fingerprints should be omitted unless they are indispensable to a public claim and pass a separate privacy review.

## Copyright minimisation
Only the minimum technically necessary excerpts should be included. Prefer original explanatory text, tables, diagrams and small factual excerpts over redistribution of substantial third-party source or UI material. Third-party trademarks and copyrighted material remain the property of their respective owners.

This policy is an engineering/privacy practice and is not a legal determination of copyright exceptions in any jurisdiction.

## Claim discipline
Every material claim should be classifiable as `OBSERVED`, `REPRODUCED`, `INFERRED`, `HYPOTHESIS`, or `NOT DETERMINED`. Where a claim has plausible alternative explanations, those alternatives should be recorded rather than silently discarded.

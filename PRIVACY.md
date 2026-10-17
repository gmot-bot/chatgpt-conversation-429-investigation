# Privacy

Privacy takes precedence over evidentiary completeness in the public repository.

## Do not publish
Do not publish credentials, cookies, tokens, authorization headers, WebSocket verification material, account/user identifiers, conversation/project/channel identifiers, request/correlation identifiers, IP addresses, email addresses, precise home/work locations, local usernames, filesystem paths, unrelated conversation content, private support correspondence or private support case identifiers.

## Public transformations
Public evidence may be cropped, irreversibly redacted, re-rasterised, stripped of metadata, or converted from absolute to relative timing. Such transformations must be disclosed and must not be represented as untouched originals.

## Maintainer biographical disclosure
Biographical and geographic details about the maintainer are intentionally minimised because they are not technical evidence and are unnecessary for reproducing or evaluating the issue.

## Contributor privacy
Do not attempt to identify, geolocate, correlate or deanonymise contributors. Contributors should disclose only the environment details necessary to distinguish technical conditions, preferably at coarse granularity.

## Private vendor correlation
Information useful for server-side correlation may be materially more identifying than public evidence. Send such information only through an appropriate private vendor/support channel; do not mirror it into public issues.


## Git metadata and linked-profile boundary
Public-file redaction does not automatically anonymise Git commit metadata or the public account profile hosting the repository. Before publication, review author/committer names and email addresses as well as any profile fields that the maintainer chooses to expose. Prefer a provider-supported no-reply commit address where appropriate. This repository does not require history rewriting merely to remove non-sensitive information that the maintainer has explicitly chosen to retain.

# Repository Discoverability Plan

Status: prepared, not all metadata actions applied.

## Recommended repository description
Independent evidence-led investigation of ChatGPT historical conversation load failures, HTTP 429 retrieval errors, refetch/recovery behaviour and safe mitigations. Root cause not determined.

## Recommended GitHub topics
- chatgpt
- http-429
- rate-limiting
- conversation-history
- reliability
- incident-analysis
- debugging
- websocket
- recovery
- openai

Topics are search/discovery metadata, not causal claims. `websocket` is included because realtime behaviour is part of the investigated evidence, not because WebSocket is asserted as the root cause.

## Search-language coverage
The README/guide should retain ordinary user phrases alongside technical terms: historical chats fail to open, existing conversations fail to load, `Couldn't load this ChatGPT conversation`, `Couldn't refresh messages`, `Too many requests`, conversation retrieval HTTP 429, history refresh, refetch and recovery polling.

## Rename gate
A repository rename may improve clarity, but it is a public structural action and remains a separate final gate. Do not rename merely for SEO. Before any rename, verify GitHub redirect behaviour, local remote update, documentation references and whether the existing name has already accumulated useful links.

## Profile boundary
Repository privacy review is separate from public GitHub-profile privacy. Commit metadata in the current history uses a provider no-reply address; profile fields should still be reviewed separately before intentionally increasing discoverability.

# Start Here

ChatGPT conversations not loading? Seeing `HTTP 429`, `Too many requests`, `Couldn't load this ChatGPT conversation`, or an old/existing chat that remains visible but will not open?

This repository is an independent, evidence-led investigation of conversation/history loading failures, retrieval throttling, retry/refetch/recovery behaviour and adjacent failure modes. **Root cause is not determined.** Similar UI symptoms can have different technical causes.

## I am affected by the problem

1. Read [Safe troubleshooting](TROUBLESHOOTING.md).
2. Compare your symptom with [Known error messages and search phrases](docs/known-error-messages.md).
3. If you have an independent observation, use the GitHub **Simple problem report** for a low-barrier report or **Independent reproduction** for stronger technical evidence.
4. Remove private identifiers before posting. Never publish cookies, tokens, account/conversation/request IDs, IP addresses, email addresses, precise locations, private chat content or private support correspondence.
5. Do not repeatedly refresh, automate retries, generate load or bypass rate limits to reproduce the problem.

## I am an engineer or researcher

Start with:

- [Public reproduction matrix](docs/reproduction-matrix.md)
- [Evidence quality and H0-H12 hypothesis framework](docs/evidence-quality-hypothesis-matrix.md)
- [Engineering decision tree](docs/engineering-decision-tree.md)
- [Independent public reports](docs/independent-public-reports.md)
- [Alternative explanations](docs/alternative-explanations.md)

The investigation distinguishes symptoms, observations, inferences and hypotheses. A public report is not treated as proof of a shared root cause.

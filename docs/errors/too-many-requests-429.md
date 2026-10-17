# Too Many Requests / HTTP 429

**What it means:** HTTP 429 means a request was rate-limited. It does not, by itself, identify the limiter scope, policy or reason the budget was exceeded.

**What we know:** conversation/history retrieval 429 responses are directly demonstrated in some independent public reports. This does not prove that every “Too many requests” message has the same cause.

**Safe steps:** stop repeated retries; respect `Retry-After` or another authoritative cooldown when present; wait normally; preserve only privacy-safe observations.

**Important:** a 429 does not automatically mean the user manually made too many requests.

**Community:** [technical 429 discussion](https://github.com/gmot-bot/chatgpt-conversation-429-investigation/discussions/2).

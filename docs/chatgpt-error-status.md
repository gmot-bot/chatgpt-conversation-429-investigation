# ChatGPT Error Status — Community View

This page combines three different status concepts that must not be confused.

## 1. Official service status

For current acknowledged service incidents, use the official OpenAI Status page. Official status is authoritative for incidents OpenAI publishes, but aggregate service availability does not determine the cause of an individual user's failure.

## 2. Community-observed status

| Problem family | Community project state |
|---|---|
| Conversations/history failing to open | REPORTED / INVESTIGATING |
| Conversation retrieval HTTP 429 | CONFIRMED IN SOME PUBLIC REPORTS |
| `Too many requests` | REPORTED; mechanism may vary by case |
| Visible/searchable but will not open | REPORTED |
| History failure without 429 | REPORTED; counterexample to a single-mechanism assumption |
| Realtime/recovery symptoms | REPORTED; causal role NOT PROVED |

## 3. Root-cause status

**NOT DETERMINED.** The project maintains competing H0-H12 hypotheses and requires causal evidence before closing the investigation.

## Reading this page safely

An official incident near the time of a community report is context, not proof of identity of cause. Likewise, many community reports do not prove a global outage.

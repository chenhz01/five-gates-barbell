# Case B — a kill, with the reasoning kept

**Opportunity:** an automated daily report built on publicly available
government datasets.

**Why it is written up:** this is the kind of project that feels obviously
useful and dies in the market. Two gates were red and one of them was red in a
way that is easy to talk yourself out of.

| Gate | Verdict | Reasoning |
|---|---|---|
| 1 Demand is real | **RED** | Demand was inferred from "this would be useful". No one had paid for it, and no one was doing it manually in a way that cost them recurring time. |
| 2 Evidence checkable | YELLOW | The datasets are public and the pipeline is reproducible, but the compliance boundary for republishing derived content was unclear. |
| 3 Direction aligned | YELLOW | Roughly 30% content overlap with an existing reporting pipeline — reuse, but also redundancy. |
| 4 Leverage | GREEN | The ingestion and scheduling pipeline is reusable across other report types. |
| 5 Converts to action | **RED** | No specific human action converted. Readers could look at the report and do nothing; nothing in it changed a decision, a payment, or a deployment. |

**Verdict:** KILL — gates 1 and 5.

## The uncomfortable part

Gate 4 was green and the engineering was sound. That is exactly why this case is
kept: **a technically good project with no behavioural demand and no action
conversion is still a kill.** A green engineering gate cannot rescue a red
demand gate, and averaging the five would have produced a "3.5 out of 5, worth
trying" answer, which is the failure mode this method exists to prevent.

## What survived the kill

The pipeline itself. It was later reused in a smaller, clearly-scoped form where
the output was a document for an internal decision rather than a public daily
feed. That reuse was legal under gate 3 only because the *content* changed, not
just the title.

This is the useful distinction:

- The **capability** was worth keeping.
- The **project shape** was not.

## The entry in the rejection log

```
Killed: automated public-data daily report
Red gates: 1 (demand inferred, no behavioural evidence), 5 (no action conversion)
Kept: ingestion + scheduling pipeline, reused in a narrower scope
Lesson: "useful to read" is not a demand signal. A report that changes no
        decision is a hobby with a cron job.
```

That lesson is now a standing check applied to every reporting idea.

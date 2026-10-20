# Case A — a pass that became a plan

**Opportunity:** submit a talk to a developer conference, with an open-source
release attached.

**Why it is written up:** it is the cleanest example of gate 4 (leverage) doing
real work. The talk itself was never the point.

| Gate | Evidence given | Light |
|---|---|---|
| 1 Demand is real | The conference publishes a track whose description names the exact problem; builders already publish workarounds for it. | GREEN |
| 2 Evidence is checkable | A reference implementation runs offline: 6/6 tests pass, and the rollback path is observable in the output. | GREEN |
| 3 Direction aligned | Content overlap with existing work is under 15%; the protocol document is new writing, not a rename. | GREEN |
| 4 Leverage | One submission produces three reuses: a talk, a public repository, and a nomination relationship. | GREEN |
| 5 Converts to action | Countable: repository stars, clones, and at least one person willing to nominate. | GREEN |

**Verdict:** PROCEED — into the light end, not the heavy end.

## What made gate 4 green

A single-input, three-output structure. The same work that produces a talk also
produces a repository and a relationship. That is the definition of leverage:
you do not get to claim it by listing future possibilities, only by naming
outputs the same input actually feeds.

## The stop loss

Written before starting, not after failing:

> If the conference yields zero nominating relationships, stop investing in the
> conference channel and move the same asset to online distribution.

This is the part people skip. A stop loss written after the result is a
post-hoc rationalisation, not a decision rule.

## What would have killed it

- Gate 1 going red: if the track existed but nobody had built a workaround, the
  demand would have been assumed rather than observed.
- Gate 2 going red: a demo that only runs on the author's machine fails the
  "third party can verify" test, no matter how impressive it looks.

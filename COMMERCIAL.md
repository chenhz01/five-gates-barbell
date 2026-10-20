# Open-core boundary

## Open here

- The five gates, their pass criteria, and their red flags (`README.md`)
- A runnable scorer that enforces "one red is a kill" (`gates.py`)
- Scorecard and weekly-review templates
- One full pass case and one full kill case, with reasoning intact

That is enough to run the method on your own opportunities today.

## Not open

1. **The rejection corpus.** The accumulated log of killed opportunities, with
   the specific reasoning that killed them. The template is public; the entries
   are the asset.
2. **Calibration for a specific domain.** Which evidence counts as "behavioural"
   in a given market, and what a 15% content overlap looks like in practice,
   depend on a reference asset base that is not public.
3. **The portfolio engine.** How the heavy/light split is rebalanced weekly,
   including the rules for graduating and cutting, is not published.
4. **Advisory engagements.** Applying these gates to a company's actual pipeline
   is a service, not a document.

None of this is needed to use the method. The method is public so it can spread;
the calibration and the log stay private because they are what makes it accurate
for a specific operator.

## Services

- **Portfolio review** — run the gates across your current projects and produce
  a written kill/keep/graduate decision per project.
- **Gate design** — adapt the five gates to a domain where "behavioural
  evidence" is not obvious (B2B, regulated markets, marketplaces).
- **Workshop** — a half-day session on pre-commitment and stop-loss discipline.

Contact: open an issue with the `commercial` label, or use the profile links on
[github.com/chenhz01](https://github.com/chenhz01).

## What the licence does not promise

Published versions keep their published licences. Future versions may ship under
different terms. Nothing here is a promise of perpetual open licensing, and
nothing here is investment, legal, or financial advice.

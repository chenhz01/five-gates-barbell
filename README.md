# five-gates-barbell

**Most projects don't fail in the market. They fail at a gate nobody built.**

Five gates you run *before* you build, and a barbell rule for how much you are
allowed to bet when a gate says yes. Both are small enough to use on a Tuesday
afternoon and strict enough to kill a project you are emotionally attached to.

Run the scorecard on any opportunity:

```
python gates.py --example universe
python gates.py --interactive
python -m unittest test_gates -v
```

Stdlib only. No dependencies.

---

## The problem this solves

The expensive mistake is not building the wrong thing. It is **starting** the
wrong thing with full commitment, then defending it because you already spent
the time.

A gate is useful only if it can say no. These five are ordered so that the
cheapest disqualifier comes first — you should be able to kill an idea in under
ten minutes, before you write a line of code.

---

## The five gates

Any red gate kills the opportunity. There is no averaging, no "4 out of 5 is
still good". A red gate means stop.

| # | Gate | Passes when | A red light looks like |
|---|---|---|---|
| **1** | **Demand is real** | Someone already paid money or spent real time on this problem. **Behaviour, not opinion.** | "I think users would want this" |
| **2** | **Evidence is checkable** | There is a data source, a verifier, or a reproducible result | Unsourced numbers, a demo nobody can re-run |
| **3** | **Direction is aligned** | Content overlap with existing assets is **under 15%**. A shared name is not overlap. | Rebuilding what you already have under a new name |
| **4** | **Leverage compounds** | One input, many reuses — or a strategic position worth holding even if it is not reused | Pure one-off delivery |
| **5** | **It converts to action** | It can become a specific human action: a click, a payment, a deployment, a nomination | Attention with no action |

### Why gate 3 is measured by content, not by names

Renaming a project does not make it new. What matters is whether the *content*
is redundant with something you already own. The threshold is 15% content
overlap; naming similarity is explicitly not a signal. This exists because the
most common self-deception is "this one is different" when only the label
changed.

### The rejection log is the asset

Every red gate produces a written reason. Over time that log becomes more
valuable than the wins: it is a record of the shapes of ideas that do not work
for you specifically. See [`examples/gov-data-monitor.md`](examples/gov-data-monitor.md)
for a full rejection with the reasoning kept intact.

---

## The barbell

Passing all five gates does not mean "go all in". It means the opportunity is
allowed into the **10–15%** end of your attention budget.

| End | Share | What goes here | Purpose |
|---|---|---|---|
| **Heavy** | 85–90% | Proven cash flow, repeatable operations | Predictable, boring, keeps you alive |
| **Light** | 10–15% | High-variance experiments: new channels, open-source launches, conference talks | Optionality you can afford to lose |

Three rules:

1. **Never all-in.** No single opportunity may exceed the light-end total.
2. **Pre-committed stop loss.** Write the "this is void if X" condition before
   you start, not after it fails.
3. **Weekly review.** Once a week, decide which light-end bets graduate to the
   heavy end and which get cut.

The barbell is not risk aversion. It is the only structure that lets you take
real risk without being able to lose the base.

---

## Usage

```
python gates.py --example universe      # a full pass, all five green
python gates.py --example gov-data      # a rejection, two red gates
python gates.py --interactive           # score your own opportunity
```

`gates.py` is a thin scorer, not a decision-maker. It enforces the one thing
humans are bad at: **a red gate cannot be averaged away.** If any gate is red,
the output is `KILL`, regardless of the other four.

Templates:

- [`templates/gate-scorecard.md`](templates/gate-scorecard.md) — one page per opportunity
- [`templates/weekly-review.md`](templates/weekly-review.md) — the Sunday pass
- [`examples/universe-2027.md`](examples/universe-2027.md) — a pass that became a plan
- [`examples/gov-data-monitor.md`](examples/gov-data-monitor.md) — a kill, with reasons kept

---

## 中文摘要

**五关决策树**：需求真伪 → 证据可验证 → 同向性（内容冗余率 <15%）→ 杠杆复利 → 动作转化。任一关红灯即淘汰，不做加权平均。

**杠铃配置**：85–90% 精力放重仓端（已验证现金流），10–15% 放轻注端（高方差实验）。三条纪律：永不 All-in、预设止损线、每周复盘。

否决理由要写下来入库——**「不做什么」的记录，长期比「做了什么」更有信息量**。

---

## Licence

- **Code** (`gates.py`, `test_gates.py`) — Apache-2.0
- **Method and documentation** (this README, `templates/`, `examples/`) — CC BY 4.0

If you publicly claim a product or process "follows the Five-Gate Method" or
"is compliant with FGM-1.0", you must attribute the method, its version, and its
author. Using the method privately, adapting it, or building on it without such
a claim requires nothing.

See [`LICENSE`](LICENSE), [`LICENSE-SPEC`](LICENSE-SPEC), [`NOTICE`](NOTICE),
[`COMMERCIAL.md`](COMMERCIAL.md).

---

## Related

- [`five-gene`](https://github.com/chenhz01/five-gene) — the pipeline protocol
  that gate 2 made me build: independent verifier, bounded rollback.
- Author: [chenhz01](https://github.com/chenhz01)

---

*FGM-1.0 · 2026*

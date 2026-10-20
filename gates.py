# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (Zhengming, for Shanlun)
"""Five-gate scorecard — a thin, opinionated scorer (FGM-1.0).

The only rule this file enforces is the one humans are bad at:
a red gate cannot be averaged away. Any RED -> KILL, regardless of the rest.

Usage:
    python gates.py --example universe
    python gates.py --example gov-data
    python gates.py --interactive
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field, asdict
from enum import Enum


class Light(str, Enum):
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"


@dataclass
class Gate:
    id: int
    name: str
    question: str
    pass_when: str
    red_flag: str
    light: Light = Light.GREEN
    evidence: str = ""

    def red(self) -> bool:
        return self.light is Light.RED


GATES: list[Gate] = [
    Gate(
        1,
        "Demand is real",
        "Has someone already paid money or spent real time on this problem?",
        "Behavioural evidence: a payment, a workaround someone built, a recurring manual cost.",
        "I think users would want this.",
    ),
    Gate(
        2,
        "Evidence is checkable",
        "Can a third party verify the core claim without trusting me?",
        "A data source, a verifier, or a reproducible result.",
        "Unsourced numbers, a demo nobody can re-run.",
    ),
    Gate(
        3,
        "Direction is aligned",
        "Is this content-redundant with something I already own?",
        "Content overlap under 15%. A shared name is not overlap.",
        "Rebuilding an existing asset under a new label.",
    ),
    Gate(
        4,
        "Leverage compounds",
        "Does one input produce multiple reuses, or a strategic position worth holding?",
        "Reuse across at least two outputs, or a durable positional gain.",
        "Pure one-off delivery.",
    ),
    Gate(
        5,
        "It converts to action",
        "Can this become a specific human action I can count?",
        "A click, a payment, a deployment, a nomination — countable and attributable.",
        "Attention with no action.",
    ),
]


@dataclass
class Scorecard:
    opportunity: str
    gates: list[Gate] = field(default_factory=lambda: [Gate(**{k: v for k, v in g.__dict__.items()}) for g in GATES])

    def set(self, gate_id: int, light: Light, evidence: str) -> None:
        for g in self.gates:
            if g.id == gate_id:
                g.light = light
                g.evidence = evidence
                return
        raise KeyError(f"no gate {gate_id}")

    def reds(self) -> list[Gate]:
        return [g for g in self.gates if g.red()]

    def verdict(self) -> str:
        """KILL if any RED. Otherwise PROCEED, with YELLOWs surfaced."""
        return "KILL" if self.reds() else "PROCEED"

    def summary(self) -> dict:
        return {
            "opportunity": self.opportunity,
            "verdict": self.verdict(),
            "red_gates": [{"id": g.id, "name": g.name, "reason": g.evidence} for g in self.reds()],
            "yellow_gates": [{"id": g.id, "name": g.name} for g in self.gates if g.light is Light.YELLOW],
            "score_note": "No averaging. One RED is a KILL.",
        }


def _example(opportunity: str, lights: list[tuple[Light, str]]) -> Scorecard:
    sc = Scorecard(opportunity)
    for g, (light, ev) in zip(sc.gates, lights):
        g.light, g.evidence = light, ev
    return sc


def example_universe() -> Scorecard:
    return _example(
        "Submit a talk to a developer conference (open-source launch attached)",
        [
            (Light.GREEN, "Official track description names the exact pain; builders already publish workarounds."),
            (Light.GREEN, "Reference implementation runs: 6/6 tests pass, rollback edge observed in output."),
            (Light.GREEN, "Content overlap with existing repos under 15%; the protocol text is new."),
            (Light.GREEN, "One proposal yields talk + repo + nomination pipeline."),
            (Light.GREEN, "Countable: stars, repo clones, at least one nominating relationship."),
        ],
    )


def example_gov_data() -> Scorecard:
    return _example(
        "Automated daily report on public government data",
        [
            (Light.RED, "Demand inferred from 'it would be useful'; no payment or repeated manual workaround found."),
            (Light.YELLOW, "Source is public but the compliance boundary is unclear."),
            (Light.YELLOW, "Reuses ~30% of an existing reporting pipeline."),
            (Light.GREEN, "The pipeline itself is reusable."),
            (Light.RED, "No specific human action converts; attention does not become a decision or payment."),
        ],
    )


def render(sc: Scorecard) -> str:
    lines = [f"OPPORTUNITY: {sc.opportunity}", ""]
    icon = {Light.GREEN: "[GREEN ]", Light.YELLOW: "[YELLOW]", Light.RED: "[ RED  ]"}
    for g in sc.gates:
        lines.append(f"{icon[g.light]} gate {g.id}  {g.name}")
        if g.evidence:
            lines.append(f"          -> {g.evidence}")
    lines.append("")
    verdict = sc.verdict()
    if verdict == "KILL":
        lines.append(f"VERDICT: KILL  ({len(sc.reds())} red gate(s) — no averaging)")
        for g in sc.reds():
            lines.append(f"  gate {g.id} {g.name}: {g.evidence}")
        lines.append("  Log this reason. The rejection log is the asset.")
    else:
        yellows = [g.id for g in sc.gates if g.light is Light.YELLOW]
        lines.append("VERDICT: PROCEED into the light end of the barbell (10-15%).")
        if yellows:
            lines.append(f"  Watch: gate(s) {yellows} are yellow — write the stop-loss before starting.")
    return "\n".join(lines)


def interactive() -> Scorecard:
    name = input("Opportunity (one line): ").strip() or "untitled"
    sc = Scorecard(name)
    mapping = {"g": Light.GREEN, "y": Light.YELLOW, "r": Light.RED}
    for g in sc.gates:
        print(f"\nGate {g.id} — {g.name}")
        print(f"  Q: {g.question}")
        print(f"  Pass when: {g.pass_when}")
        while True:
            raw = input("  [g]reen / [y]ellow / [r]ed > ").strip().lower()
            if raw in mapping:
                ev = input("  evidence (why): ").strip()
                g.light, g.evidence = mapping[raw], ev
                break
            print("  enter g, y, or r")
    return sc


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Five-gate scorecard (FGM-1.0)")
    ap.add_argument("--example", choices=["universe", "gov-data"])
    ap.add_argument("--interactive", action="store_true")
    ap.add_argument("--json", action="store_true", help="emit machine-readable verdict")
    args = ap.parse_args(argv)

    if args.example == "universe":
        sc = example_universe()
    elif args.example == "gov-data":
        sc = example_gov_data()
    elif args.interactive:
        sc = interactive()
    else:
        ap.print_help()
        return 2

    print(json.dumps(sc.summary(), ensure_ascii=False, indent=2) if args.json else render(sc))
    return 0


if __name__ == "__main__":
    sys.exit(main())

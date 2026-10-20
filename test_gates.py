# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (Zhengming, for Shanlun)
"""Tests for the five-gate scorer.

These tests exist to protect one property: a red gate can never be averaged
away. If a future change makes a red gate survivable, these fail.
"""

import unittest

from gates import GATES, Light, Scorecard, example_gov_data, example_universe


class TestNoAveraging(unittest.TestCase):
    def test_all_green_proceeds(self):
        self.assertEqual(example_universe().verdict(), "PROCEED")

    def test_one_red_kills_even_with_four_green(self):
        sc = example_universe()
        sc.set(3, Light.RED, "same content, new label")
        self.assertEqual(sc.verdict(), "KILL")
        self.assertEqual(len(sc.reds()), 1)

    def test_two_reds_still_kill_and_both_are_listed(self):
        sc = example_gov_data()
        self.assertEqual(sc.verdict(), "KILL")
        self.assertEqual([g.id for g in sc.reds()], [1, 5])

    def test_yellow_alone_does_not_kill(self):
        sc = example_universe()
        for g in sc.gates:
            g.light = Light.YELLOW
        self.assertEqual(sc.verdict(), "PROCEED")

    def test_summary_has_no_average_field(self):
        s = example_gov_data().summary()
        self.assertNotIn("average", s)
        self.assertNotIn("score", s)
        self.assertEqual(s["verdict"], "KILL")
        self.assertEqual(len(s["red_gates"]), 2)


class TestContract(unittest.TestCase):
    def test_five_gates_with_stable_ids(self):
        self.assertEqual([g.id for g in GATES], [1, 2, 3, 4, 5])

    def test_every_gate_states_its_red_flag(self):
        for g in GATES:
            self.assertTrue(g.red_flag, f"gate {g.id} has no red flag")

    def test_set_unknown_gate_raises(self):
        with self.assertRaises(KeyError):
            Scorecard("x").set(99, Light.RED, "n/a")

    def test_instances_do_not_share_gate_objects(self):
        a, b = Scorecard("a"), Scorecard("b")
        a.gates[0].light = Light.RED
        self.assertIsNot(b.gates[0].light, Light.RED)


if __name__ == "__main__":
    unittest.main(verbosity=2)

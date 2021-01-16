"""
COMP 1510 - Yahtzee
Nicholas Johnston
A01242666
December 4, 2020
"""
from unittest import TestCase

from yahtzee import scorecard_update


class TestScorecardUpdate(TestCase):

    def test_scorecard_update(self):
        self.fail()

    def test_scorecard_update_ones(self):
        actual = scorecard_update({"upper": {"1": 0, "6": 0},
                                   "lower": {"yahtzee": 0, "chance": 0}
                                   },
                                  "1",
                                  [6, 6, 1, 1, 1])
        expected = {"upper": {"1": 3, "6": 0},
                    "lower": {"yahtzee": 0, "chance": 0}}
        self.assertEqual(actual, expected)

    def test_scorecard_update_sixes(self):
        actual = scorecard_update({"upper": {"1": 0, "6": 0},
                                   "lower": {"yahtzee": 0, "chance": 0}
                                   },
                                  "6",
                                  [6, 6, 1, 1, 1])
        expected = {"upper": {"1": 0, "6": 12},
                    "lower": {"yahtzee": 0, "chance": 0}}
        self.assertEqual(actual, expected)

    def test_scorecard_update_small_straight(self):
        actual = scorecard_update({"upper": {"1": 0, "6": 0},
                                   "lower": {"small_straight": 0, "yahtzee": 0, "chance": 0}
                                   },
                                  "small straight",
                                  [1, 2, 3, 4, 1])
        expected = {"upper": {"1": 3, "6": 0},
                    "lower": {"small_straight": 25, "yahtzee": 0, "chance": 0}}
        self.assertEqual(actual, expected)

    def test_scorecard_update_yahtzee(self):
        actual = scorecard_update({"upper": {"4": 0, "6": 0},
                                   "lower": {"yahtzee": 0, "chance": 0}
                                   },
                                  "yahtzee",
                                  [6, 6, 6, 6, 6])
        expected = {"upper": {"4": 0, "6": 0},
                    "lower": {"yahtzee": 50, "chance": 0}}
        self.assertEqual(actual, expected)

    def test_scorecard_update_second_yahtzee(self):
        actual = scorecard_update({"upper": {"4": 0, "6": 0},
                                   "lower": {"yahtzee": 50, "chance": 0}
                                   },
                                  "yahtzee",
                                  [6, 6, 6, 6, 6])
        expected = {"upper": {"4": 0, "6": 0},
                    "lower": {"yahtzee": 150, "chance": 0}}
        self.assertEqual(actual, expected)

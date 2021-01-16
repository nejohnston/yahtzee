"""
COMP 1510 - Yahtzee
Nicholas Johnston
A01242666
December 4, 2020
"""
from unittest import TestCase
from yahtzee import scorecard_available_options


class TestScorecardAvailableOptions(TestCase):

    def test_scorecard_available_options(self):
        self.fail()

    def test_scorecard_available_options_all(self):
        actual = scorecard_available_options({"upper": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0},
                                              "lower":
                                                  {"3_kind": 0, "4_kind": 0,
                                                   "full_house": 0, "small_straight": 0,
                                                   "large_straight": 0, "yahtzee": 0, "chance": 0}})
        expected = ["1", "2", "3", "4", "5", "6",
                    "3_kind", "4_kind", "full_house",
                    "small_straight", "large_straight",
                    "yahtzee", "chance"]
        self.assertEqual(actual, expected)

    def test_scorecard_available_options_no_upper(self):
        actual = scorecard_available_options({"upper": {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6},
                                              "lower":
                                                  {"3_kind": 0, "4_kind": 0,
                                                   "full_house": 0, "small_straight": 0,
                                                   "large_straight": 0, "yahtzee": 0, "chance": 0}})
        expected = ["3_kind", "4_kind", "full_house",
                    "small_straight", "large_straight",
                    "yahtzee", "chance"]
        self.assertEqual(actual, expected)

    def test_scorecard_available_options_no_lower(self):
        actual = scorecard_available_options({"upper": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0},
                                              "lower":
                                                  {"3_kind": 3, "4_kind": 4,
                                                   "full_house": 4, "small_straight": 4,
                                                   "large_straight": 5, "yahtzee": 6, "chance": 7}})
        expected = ["1", "2", "3", "4", "5", "6"]
        self.assertEqual(actual, expected)

    def test_scorecard_available_options_none(self):
        actual = scorecard_available_options({"upper": {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6},
                                              "lower":
                                                  {"3_kind": 3, "4_kind": 4,
                                                   "full_house": 4, "small_straight": 4,
                                                   "large_straight": 5, "yahtzee": 6, "chance": 7}})
        expected = []
        self.assertEqual(actual, expected)

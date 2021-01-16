"""
COMP 1510 - Yahtzee
Nicholas Johnston
A01242666
December 5, 2020
"""
from unittest import TestCase

from yahtzee import scorecard_calculate_upper


class TestScorecardCalculateUpper(TestCase):
    def test_scorecard_calculate_upper(self):
        self.fail()

    def test_scorecard_calculate_upper_ones(self):
        actual = scorecard_calculate_upper([1, 1, 1, 1, 5], "1")
        expected = 4
        self.assertEqual(actual, expected)

    def test_scorecard_calculate_upper_ones_none(self):
        actual = scorecard_calculate_upper([4, 5, 6, 6, 5], "1")
        expected = 0
        self.assertEqual(actual, expected)

    def test_scorecard_calculate_upper_fours(self):
        actual = scorecard_calculate_upper([2, 2, 3, 4, 5], "4")
        expected = 4
        self.assertEqual(actual, expected)

    def test_scorecard_calculate_upper_fours_none(self):
        actual = scorecard_calculate_upper([2, 2, 3, 5, 5], "4")
        expected = 0
        self.assertEqual(actual, expected)

    def test_scorecard_calculate_upper_sixes(self):
        actual = scorecard_calculate_upper([2, 6, 6, 6, 6], "6")
        expected = 24
        self.assertEqual(actual, expected)

    def test_scorecard_calculate_upper_sixes_none(self):
        actual = scorecard_calculate_upper([2, 2, 3, 5, 5], "6")
        expected = 0
        self.assertEqual(actual, expected)

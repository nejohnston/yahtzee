"""
COMP 1510 - Yahtzee
Nicholas Johnston
A01242666
December 5, 2020
"""
from unittest import TestCase

from yahtzee import scorecard_calculate_lower


class TestScorecardCalculateLower(TestCase):
    def test_scorecard_calculate_lower(self):
        self.fail()

    def test_scorecard_calculate_lower_3_kind(self):
        actual = scorecard_calculate_lower([6, 6, 6, 5, 4], "3 of a kind")
        expected = 27
        self.assertEqual(actual, expected)

    def test_scorecard_calculate_lower_4_kind(self):
        actual = scorecard_calculate_lower([6, 6, 6, 6, 4], "4 of a kind")
        expected = 28
        self.assertEqual(actual, expected)

    def test_scorecard_calculate_lower_full_house(self):
        actual = scorecard_calculate_lower([6, 6, 6, 5, 5], "full house")
        expected = 25
        self.assertEqual(actual, expected)

    def test_scorecard_calculate_lower_small_straight(self):
        actual = scorecard_calculate_lower([6, 5, 4, 3, 5], "small straight")
        expected = 30
        self.assertEqual(actual, expected)

    def test_scorecard_calculate_lower_large_straight(self):
        actual = scorecard_calculate_lower([6, 5, 4, 3, 2], "large straight")
        expected = 40
        self.assertEqual(actual, expected)

    def test_scorecard_calculate_lower_yahtzee(self):
        actual = scorecard_calculate_lower([6, 6, 6, 6, 6], "yahtzee")
        expected = 50
        self.assertEqual(actual, expected)

    def test_scorecard_calculate_lower_second_yahtzee(self):
        actual = scorecard_calculate_lower([6, 6, 6, 6, 6], "yahtzee")
        expected = 100
        self.assertEqual(actual, expected)

    def test_scorecard_calculate_lower_bonus(self):
        actual = scorecard_calculate_lower([6, 4, 3, 1, 6], "bonus")
        expected = 20
        self.assertEqual(actual, expected)

"""
COMP 1510 - Yahtzee
Nicholas Johnston
A01242666

"""
from unittest import TestCase

from yahtzee import validate_small_straight


class TestValidateYahtzee(TestCase):
    def test_validate_small_straight_valid(self):
        actual = validate_small_straight([1, 2, 3, 4, 1])
        expected = 30
        self.assertEqual(actual, expected)

    def test_validate_small_straight_invalid(self):
        actual = validate_small_straight([2, 1, 1, 1, 1])
        expected = -1
        self.assertEqual(actual, expected)

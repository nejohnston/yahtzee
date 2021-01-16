"""
COMP 1510 - Yahtzee
Nicholas Johnston
A01242666

"""
from unittest import TestCase

from yahtzee import validate_yahtzee


class TestValidateYahtzee(TestCase):
    def test_validate_yahtzee_valid(self):
        actual = validate_yahtzee([1, 1, 1, 1, 1])
        expected = 50
        self.assertEqual(actual, expected)

    def test_validate_yahtzee_invalid(self):
        actual = validate_yahtzee([2, 1, 1, 1, 1])
        expected = -1
        self.assertEqual(actual, expected)

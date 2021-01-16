"""
COMP 1510 - Yahtzee
Nicholas Johnston
A01242666
December 5, 2020
"""
from unittest import TestCase

from yahtzee import handle_validation


class TestDetermineValidate(TestCase):
    def test_determine_validate(self):
        self.fail()

    def test_determine_validate_ones_true(self):
        actual = handle_validation("1", [1, 2, 3, 4, 6])
        expected = True
        self.assertEqual(actual, expected)

    def test_determine_validate_ones_false(self):
        actual = handle_validation("1", [3, 2, 3, 4, 6])
        expected = False
        self.assertEqual(actual, expected)

    def test_determine_validate_sixes_true(self):
        actual = handle_validation("1", [3, 2, 3, 6, 6])
        expected = True
        self.assertEqual(actual, expected)

    def test_determine_validate_sixes_false(self):
        actual = handle_validation("1", [3, 2, 3, 4, 5])
        expected = False
        self.assertEqual(actual, expected)

    def test_determine_validate_small_straight_true(self):
        actual = handle_validation("small straight", [1, 2, 3, 4, 6])
        expected = True
        self.assertEqual(actual, expected)

    def test_determine_validate_small_straight_false(self):
        actual = handle_validation("small straight", [1, 4, 4, 4, 6])
        expected = False
        self.assertEqual(actual, expected)

    def test_determine_validate_yahtzee_true(self):
        actual = handle_validation("yahtzee", [4, 4, 4, 4, 4])
        expected = True
        self.assertEqual(actual, expected)

    def test_determine_validate_yahtzee_false(self):
        actual = handle_validation("yahtzee", [5, 4, 4, 4, 4])
        expected = False
        self.assertEqual(actual, expected)

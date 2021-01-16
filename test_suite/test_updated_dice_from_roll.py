"""
COMP 1510 - Yahtzee
Nicholas Johnston
A01242666
December 4, 2020
"""
from unittest import TestCase
from unittest.mock import patch

from yahtzee import update_dice_from_roll


class TestUpdateDiceFromRoll(TestCase):

    @patch('random.randint', return_value=5)
    def test_update_dice_from_roll_1(self, random_integer):
        actual = update_dice_from_roll([1, 2, 3, 4, 5], [1])
        expected = [5, 2, 3, 4, 5]
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=5)
    def test_update_dice_from_roll_first_three_indices(self, random_integer):
        actual = update_dice_from_roll([1, 2, 3, 4, 5], [1, 2, 3])
        expected = [5, 5, 5, 4, 5]
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=5)
    def test_update_dice_from_roll_all_indices(self, random_integer):
        actual = update_dice_from_roll([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
        expected = [5, 5, 5, 5, 5]
        self.assertEqual(actual, expected)

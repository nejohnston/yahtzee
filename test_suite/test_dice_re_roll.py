"""
COMP 1510 - Yahtzee
Nicholas Johnston
A01242666
December 4, 2020
"""
from unittest import TestCase
from unittest.mock import patch

from yahtzee import dice_re_roll


class TestDiceReRoll(TestCase):

    def test_dice_re_roll(self):
        self.fail()

    @patch('builtins.input', side_effect='1 2 3 4 5')
    @patch('random.randint', return_value=5)
    def test_dice_re_roll_all(self, mock_input, random_sample_generator):
        actual = dice_re_roll([2, 3, 3, 1, 5])
        expected = [random_sample_generator,
                    random_sample_generator,
                    random_sample_generator,
                    random_sample_generator,
                    random_sample_generator]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect='1 2 3 4')
    @patch('random.randint', return_value=5)
    def test_dice_re_roll_all_but_last(self, mock_input, random_sample_generator):
        actual = dice_re_roll([2, 3, 3, 1, 5])
        expected = [random_sample_generator,
                    random_sample_generator,
                    random_sample_generator,
                    random_sample_generator,
                    5]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect='5')
    @patch('random.randint', return_value=5)
    def test_dice_re_roll_only_last(self, mock_input, random_sample_generator):
        actual = dice_re_roll([2, 3, 3, 1, 5])
        expected = [2, 3, 3, 1, random_sample_generator]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect='1')
    @patch('random.randint', return_value=5)
    def test_dice_re_roll_only_first(self, mock_input, random_sample_generator):
        actual = dice_re_roll([2, 3, 3, 1, 5])
        expected = [random_sample_generator, 3, 3, 1, 5]
        self.assertEqual(expected, actual)

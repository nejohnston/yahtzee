"""
COMP 1510 -
Nicholas Johnston
A01242666

"""
from unittest import TestCase

from yahtzee import update_player_turn_count


class TestPassTurnOwnership(TestCase):
    def test_pass_turn_ownership_first_turn(self):
        actual = update_player_turn_count(13)
        expected = 12
        self.assertEqual(actual, expected)

    def test_pass_turn_ownership_mid_game_turn(self):
        actual = update_player_turn_count(7)
        expected = 6
        self.assertEqual(actual, expected)

    def test_pass_turn_ownership_last_turn(self):
        actual = update_player_turn_count(1)
        expected = 0
        self.assertEqual(actual, expected)

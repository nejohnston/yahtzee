"""
COMP 1510 - 
Nicholas Johnston
A01242666

"""
from unittest import TestCase

from yahtzee import pass_turn_ownership


class TestPassTurnOwnership(TestCase):
    def test_pass_turn_ownership_player_one(self):
        actual = pass_turn_ownership(1)
        expected = 2
        self.assertEqual(actual, expected)

    def test_pass_turn_ownership_player_two(self):
        actual = pass_turn_ownership(2)
        expected = 1
        self.assertEqual(actual, expected)

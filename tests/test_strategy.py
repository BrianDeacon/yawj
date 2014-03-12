import unittest
from board import Board
from strategy import Strategy
import strategy
import math

class TestStrategy(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.strategy = Strategy(self.board, 'X')

    def test_find_v_shape(self):
        self.board.X(0,0)
        self.board.X(1,1)
        x, y = self.strategy.find_v_shape()
        self.assertEqual(0, x)
        self.assertEqual(2, y)

        self.board.clear()
        self.board.X(0, 2)
        self.board.X(1, 1)
        self.board.O(0, 0)
        
        x, y = self.strategy.find_v_shape()
        self.assertEqual(2, x)
        self.assertEqual(2, y)

    def test_is_corner_unchallenged(self):
        self.assertTrue(self.strategy.is_corner_unchallenged(0,0))
        self.board.O(0,0)
        self.assertFalse(self.strategy.is_corner_unchallenged(0, 2))
        self.assertFalse(self.strategy.is_corner_unchallenged(2, 0))
        self.assertTrue(self.strategy.is_corner_unchallenged(2, 2))

    def test_find_unchallenged_corner(self):
        self.board.O(0, 0)
        x, y = self.strategy.find_unchallenged_corner()
        self.assertEqual(2, x)
        self.assertEqual(2, y)

    def test_opponent_value(self):
        self.assertEqual('O', self.strategy.opponent_value())
        strategy = Strategy(self.board, 'O')
        self.assertEqual('X', strategy.opponent_value())

    def test_row_is_winnable(self):
        self.board.O(0, 0)
        self.assertFalse(self.strategy.row_is_winnable(0));
        self.assertTrue(self.strategy.row_is_winnable(1));
        self.assertTrue(self.strategy.row_is_winnable(2));

    def test_columns_is_winnable(self):
        self.board.O(0, 0)
        self.assertFalse(self.strategy.column_is_winnable(0));
        self.assertTrue(self.strategy.column_is_winnable(1));
        self.assertTrue(self.strategy.column_is_winnable(2));

    def test_diagonal_is_winnable(self):
        self.board.O(0, 0)
        self.assertFalse(self.strategy.diagonal_is_winnable(0, 0))
        self.assertFalse(self.strategy.diagonal_is_winnable(2, 2))
        self.assertTrue(self.strategy.diagonal_is_winnable(0, 2))
        self.assertTrue(self.strategy.diagonal_is_winnable(2, 0))

    def test_find_winnable_corner(self):
        self.board.O(0, 0)
        self.board.O(0, 1)
        self.board.O(0, 2)
        
        corner = self.strategy.find_winnable_corner()
        print corner
        self.assertTrue(corner == (2, 2) or corner == (2, 0))
        

        self.board.clear()
        self.board.O(2, 2)
        self.board.O(0, 2)
        self.board.O(1, 2)
        self.board.O(2, 1)
        x, y = self.strategy.find_winnable_corner()
        self.assertTrue(corner == (0, 0) or corner == (2, 0))

    def test_next_move_defend(self):
        self.board.X(0, 0)
        self.board.O(1, 1)
        self.board.X(2, 2)
        self.board.O(0, 1)
        self.assertEqual((2, 1), self.strategy.next_move())

    def test_has_winner(self):
        board_string = 'OOOX  X  '
        self.assertTrue(strategy.has_winner(board_string))
        board_string = 'OOXXXOOXX'
        self.assertFalse(strategy.has_winner(board_string))

    def test_number_winning_combos(self): 
        val = 'XXXOOOXXX'
        self.assertEqual(3, strategy.number_winning_combos(val))
        val = 'OOXXXOOXX'
        self.assertEqual(0, strategy.number_winning_combos(val))
        val = 'OXXXOXOXO'
        self.assertEqual(1, strategy.number_winning_combos(val))

    def test_is_winning_combo(self):
        combo = 'XXX'
        self.assertTrue(strategy.is_winning_combo(combo))
        combo = 'OOO'
        self.assertTrue(strategy.is_winning_combo(combo))
        combo = '   '
        self.assertFalse(strategy.is_winning_combo(combo))
        combo = ' XX'
        self.assertFalse(strategy.is_winning_combo(combo))
        combo = ' OO'
        self.assertFalse(strategy.is_winning_combo(combo))
        combo = 'XXO'
        self.assertFalse(strategy.is_winning_combo(combo))
        combo = 'OOX'
        self.assertFalse(strategy.is_winning_combo(combo))
        combo = 'XOX'
        self.assertFalse(strategy.is_winning_combo(combo))






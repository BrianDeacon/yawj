import unittest
from board import Board
from strategy import Strategy
from game import Game

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.strategy = Strategy(self.board, 'X')
        self.game = Game(self.strategy, 'X', 'O')

    def testTest(self):
        pass
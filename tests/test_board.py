import unittest
from board import Board

# Here's our "unit tests".
class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_line(self):
        input_values = ['X', '', 'O']
        expected = 'X| |O'
        self.assertEqual(expected, self.board.line(input_values))

    def test_all_lines(self):
        self.board.X(0,1)
        self.board.O(1,1)
        self.board.X(2,2)
        one = self.board.line(['', 'X', ''])
        two = self.board.line(['','O',''])
        three = self.board.line(['','','X'])
        expected = "%s\n_____\n%s\n_____\n%s" % (one, two, three)
        self.assertEqual(expected, self.board.all_lines());

    def test_is_winner(self):
        self.assertTrue(self.board._is_winner(['X','X','X']))
        self.assertFalse(self.board._is_winner([' ','X','X']))
        self.assertFalse(self.board._is_winner(['O','X','X']))

    def test_has_winner(self):
        self.assertFalse(self.board.has_winner())
        for x in range(0,3):
            #By row
            for y in range(0,3):
                self.board.X(x, y)
            self.assertTrue(self.board.has_winner())
            self.board.clear()
            self.assertFalse(self.board.has_winner())
            #By column
            for y in range(0,3):
                self.board.X(y, x)
            self.assertTrue(self.board.has_winner())
            self.board.clear()
            self.assertFalse(self.board.has_winner())

    def test_is_winning_move(self):
        self.board.X(0,0)
        self.board.X(0,1)
        self.assertTrue(self.board.is_winning_move(0,2))

    def test_is_not_winning_move(self):
        self.board.X(0,0)
        self.assertFalse(self.board.is_winning_move(0,1))
        self.board.X(0,1)
        self.assertTrue(self.board.is_winning_move(0,2))
        self.assertFalse(self.board.is_winning_move(1,0))

    def test_board_count(self):
        self.assertEqual(0, self.board.board_count());
        i = 0
        for x in range(0,3):
            for y in range(0,3):
                self.assertEqual(i, self.board.board_count())
                self.board.X(x,y)
                i += 1
                self.assertEqual(i, self.board.board_count())

    



#def main():
#    unittest.main()

#if __name__ == '__main__':
#    main()
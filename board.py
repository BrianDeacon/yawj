
from copy import deepcopy

class Board:

	def __init__(self):
		self.board = [[' ' for x in range(3)] for x in range(3)] 

	def X(self, x, y):
		self._set(x, y, 'X')

	def O(self, x, y):
		self._set(x, y, 'O')

	def value_at(self, x, y):
		return self.board[x][y]

	def _set(self, x, y, value):
		self.board[x][y] = value

	def set(self, x, y, value):
		self._set(x, y, value)

	def line(self, row):
		for x in range(0, len(row)):
			row[x] = row[x] if row[x] else ' '

		return '%s|%s|%s' % (row[0], row[1], row[2])

	def all_lines(self):
		ret = '%s\n_____\n' % (self.line(self.board[0]))
		ret += '%s\n_____\n' % (self.line(self.board[1]))
		ret += self.line(self.board[2])
		return ret

	def draw(self):
		print (self.all_lines())

	def _is_winner(self, values):
		if values[0] == ' ':
			return False
		return (values[1] == values[0]) and (values[2] == values[0])

	def has_winner(self, test_board = None):
		return self.winner(test_board) is not None

	def clear(self):
		for row in range(0,3):
			for column in range(0,3):
				self.board[row][column] = ' '

	def winner(self, test_board = None):
		board = test_board
		if test_board is None:
			board = self.board

		for row in range(0,3):
			if self._is_winner(board[row]):
				return board[row][0]

		for column in range(0,3):
			candidate = [board[0][column], board[1][column], board[2][column]]
			if self._is_winner(candidate):
				return board[0][column]

		if self._is_winner([board[0][0], board[1][1], board[2][2]]):
			return board[0][0]

		if self._is_winner([board[0][2], board[1][1], board[2][0]]):
			return board[0][2]

		return None


	def is_winning_move(self, x, y, letter):
		next_board = deepcopy(self.board)
		if self.board[x][y] != ' ':
			return False
		next_board[x][y] = letter
		if self.has_winner(next_board):
			return True
		return False

	def board_count(self):
		count = 0
		for x in range(0, 3):
			for y in range(0, 3):
				if self.board[x][y] != ' ':
					count += 1
		return count








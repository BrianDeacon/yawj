import sys
from board import Board
from strategy import Strategy

class Game:

    


    def __init__(self, strategy, my_letter, your_letter):
        self.strategy = strategy
        self.board = strategy.board
        self.my_letter = my_letter
        self.your_letter = your_letter

    def over(self):
        return self.board.has_winner() or self.board.board_count() == 9

    def draw(self):
        self.board.draw()

    def start(self):
        if (self.strategy.my_letter == 'X'):
            x, y = self.strategy.next_move()
            self.strategy.board.set(x, y, 'X')

        self.draw()

        while not self.over():
            move = ""
            while not (self.valid_input(move) and self.allowed_move(move)):
                move = input("Enter your move in the form x, y: ")
                if not self.allowed_move(move):
                    print "That space is taken."

            x, y = self.parse_input(move)
            self.board.set(x, y, self.your_letter)
            if not self.over():
                x, y = self.strategy.next_move()
                self.board.set(x, y, self.my_letter)

            self.draw()
        if (self.board.has_winner()):
            print "%s wins!" % self.board.winner()
        else:
            print "It's a tie!"

    def parse_input(self, move):
        return tuple(move)

    def allowed_move(self, move):
        if not self.valid_input(move):
            return False
        x, y = self.parse_input(move)
        return self.board.value_at(x, y) == ' '

    def valid_input(self, the_input):
        if isinstance(the_input, basestring):
            return False
        if len(the_input) != 2:
            return False
        for item in range(0, len(the_input)):
            if item < 0 or item > 2:
                return False
        return True

            


def main():
    first = raw_input("Would you like to go first? (Y/n): ")
    my_letter = 'O'
    your_letter = 'X'
    if (first and first.lower() == 'n'):
        my_letter = 'X'
        your_letter = 'O'

    board = Board()
    strategy = Strategy(board, my_letter)
    game = Game(strategy, my_letter, your_letter)

    game.start()



if __name__ == '__main__':
    main()
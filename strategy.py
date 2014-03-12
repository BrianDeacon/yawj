from board import Board

def is_winning_combo(combo):
    return combo[0] == combo[1] and combo[0] == combo[2] and combo[0] != ' '

def number_winning_combos(board_string):
    ret_val = 0
    ret_val = ret_val + 1 if is_winning_combo(board_string[0:3]) else ret_val
    ret_val = ret_val + 1 if is_winning_combo(board_string[3:6]) else ret_val
    ret_val = ret_val + 1 if is_winning_combo(board_string[6:9]) else ret_val

    combo = board_string[0] + board_string[3] + board_string[6] 
    ret_val = ret_val + 1 if is_winning_combo(combo) else ret_val

    combo = board_string[1] + board_string[4] + board_string[7] 
    ret_val = ret_val + 1 if is_winning_combo(combo) else ret_val

    combo = board_string[2] + board_string[5] + board_string[8] 
    ret_val = ret_val + 1 if is_winning_combo(combo) else ret_val

    combo = board_string[0] + board_string[4] + board_string[8] 
    ret_val = ret_val + 1 if is_winning_combo(combo) else ret_val

    combo = board_string[6] + board_string[4] + board_string[2] 
    ret_val = ret_val + 1 if is_winning_combo(combo) else ret_val

    return ret_val

def has_winner(board_string):
    return number_winning_combos(board_string) > 0

class Strategy:
    """This strategy stolen from here:
    http://www.wikihow.com/Win-at-Tic-Tac-Toe

    Because, for any common problem, somebody smarter than me has already figured out
    the answer.
    """

    def __init__(self, board, my_letter):
        self.board = board
        self.my_letter = my_letter
        self.your_letter = 'O'
        if my_letter == 'O':
            self.your_letter = 'X'
        self.corners = [(0, 0), (0, 2), (2, 0), (2, 2)]

    def next_move(self):
        for x in range(0,3):
            for y in range(0,3):
                # A winning move means we should either win or defend.
                # In either case, we need to move there.
                if self.board.is_winning_move(x,y,self.my_letter):
                    return x, y
        for x in range(0,3):
            for y in range(0,3):
                # A winning move means we should either win or defend.
                # In either case, we need to move there.
                if self.board.is_winning_move(x,y,self.your_letter):
                    return x, y
        #If we can't win and don't need to defend, then attack
        return self.attack()

    def attack(self):
        """Algorithm for not losing, and sometimes winning:
        If I am first:
            Take the center
            Take the corner that is in both a different column and row from them.
            If I don't need to defend, move to whatever corner can give me a V shape
            I have two winning moves, he can only block one of them.
        If they are first:
            If they take the center:
                Pick a corner
                Pick a different corner that could still win.
                Defend or win for the rest of the game.
            If they take a corner:
                Take the center
                If you don't need to defend, take an edge
                Everybody will defend from then on.
        """
        

        #I am first
        if (self.board.board_count() % 2) == 0:
            return self.attack_i_was_first()    
        else:
            return self.attack_he_was_first()
            

    def attack_he_was_first(self):
        if self.board.board_count() == 1:
            if self.board.value_at(1, 1) == self.opponent_value():
                return self.find_winnable_corner()
            else:
                return 1, 1
        return self.find_empty_corner()

    def attack_i_was_first(self):
        if self.board.board_count() == 0:
            return 1, 1
        if self.board.board_count() == 2:
            return self.find_unchallenged_corner()
        return self.find_v_shape()

    def row_is_winnable(self, row):
        winnable = True
        for column in range(0, 3):
            if self.board.value_at(row, column) == self.opponent_value():
                winnable = False
        return winnable

    def column_is_winnable(self, column):
        winnable = True
        for row in range(0, 3):
            if self.board.value_at(row, column) == self.opponent_value():
                winnable = False
        return winnable

    def diagonal_is_winnable(self, x, y):
        winnable = True
        if self.board.value_at(1, 1) == self.opponent_value():
            winnable = False
        elif self.board.value_at(x, y) == self.opponent_value():
            winnable = False
        else:
            for (x2, y2) in self.corners:
                if (x2 != x) and (y2 != y):
                    if self.board.value_at(x2, y2) == self.opponent_value():
                        winnable = False

        return winnable

    def find_winnable_corner(self):
        for (x, y) in self.corners:
            if self.column_is_winnable(y) or self.row_is_winnable(x) or self.diagonal_is_winnable(x, y):
                return x, y
        return None

    def opponent_value(self):
        if self.my_letter == 'X':
            return 'O'
        if self.my_letter == 'O':
            return 'X'        
            
    def find_unchallenged_corner(self):
        for (x, y) in self.corners:
            if self.is_corner_unchallenged(x, y):
                return x, y
        return None

    def find_empty_corner(self):
        for (x, y) in self.corners:
            if (self.board.value_at(x, y) == ' '):
                return x, y
        return None

    def is_corner_unchallenged(self, x, y):
        for col in range(0, 3):
            if self.board.value_at(x, col) == self.opponent_value():
                return False
        for row in range(0,3):
            if self.board.value_at(row, y) == self.opponent_value():
                return False
        return True

    def find_v_shape(self):
        for (x, y) in self.corners:
            if self.board.value_at(x, y) == self.my_letter:
                for (x2, y2) in self.corners:
                    if (x2 == x) or (y2 == y):
                       if self.board.value_at(x2, y2) == ' ':
                            return x2, y2
        return None


        


        
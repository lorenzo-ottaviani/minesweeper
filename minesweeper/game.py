from board import Board
import time

class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board = Board(difficulty)
        self.game_over = False
        self.start_time = None
        self.time_passed = 0
    
    def start_game(self):
        self.game_over = False
        self.start_time = time.time() # Returns time in seconds since epoch as float
        
    def check_win(self):
        '''
        Player wins when all the cells except the mines are revealed
        '''
        for row in self.board.grid:
            for cell in row:
                if not cell.mine and cell.hidden:
                    return False
        return True

    def end_game(self):
        self.game_over = True
        self.time_passed = time.time() - self.start_time
        
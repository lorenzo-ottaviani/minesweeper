from board import Board, Cell
import time

class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board = Board(difficulty)
        self.game_over = False
        self.timer = None
    
    def start_game(self):
        self.game_over = False
        pass
        
    def check_win(self):
        '''
        Player wins when all the cells except the mines are revealed
        '''
        for row in self.board.grid:
            for cell in row:
                if not cell.mine and cell.hidden:
                    return False

    def end_game(self):
        self.game_over = True
        pass
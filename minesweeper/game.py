from board import Board, Cell

class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board = Board(difficulty)
        self.game_over = False
        self.timer = None
    
    def start_game(self):
        pass
        
    def check_win(self):
        pass

    def end_game(self):
        pass
from board import Board
import time
from score import Score

class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board = Board(difficulty)
        self.game_over = False
        self.start_time = None
        self.time_passed = 0

    
    def start_game(self):
        self.game_over = False
        self.start_time = time.time()
        score = Score()
        self.player_name, self.player_score = score.enter_name()
       
        
    def check_win(self):
        '''Return True if all hidden cells except mines are revealed'''
        for row in self.board.grid:
            for cell in row:
                if not cell.mine and cell.hidden:
                    return False

        player_score = Score()
        if self.difficulty == "beginner":
            self.player_score += 40
        elif self.difficulty == "intermediate":
            self.player_score = 100
        elif self.difficulty == "expert":
            self.player_score = 200
        Score.record_score(self, self.player_name, self.player_score)
        return True

    def end_game(self):
        self.game_over = True
        self.time_passed = time.time() - self.start_time
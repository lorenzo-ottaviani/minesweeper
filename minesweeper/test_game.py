from game import Game
import unittest

class TestGame(unittest.TestCase):
    def test_start_game(self):
        game = Game(difficulty='beginner')
        game.start_game()
        assert not game.game_over, 'game should not be over after start_game'
        assert game.start_game is not None, 'time should be set after start_game'
    
    def test_check_win(self):
        game = Game(difficulty='beginner')
        game.start_game()
        game.check_win()
        
    def test_end_game(self):
        game = Game(difficulty='beginner')
        game.start_game()
        game.end_game()
        assert game.game_over, 'Game shoud be over after game_over'
        assert game.time_passed > 0, 'time passed should be greater than 0 after end_game'
        
if __name__=='__main__':
    unittest.main()
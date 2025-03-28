from board import Board
from game import Game 
from timer import Timer
import customtkinter as ctk

class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Minesweeper')
        self.resizable(False, False)
        self.game = None
        self.buttons = []
    
    def welcome_screen(self):
        '''Display welcome screen and difficulty selection'''
        pass
    
    def start_game(self, difficulty):
        self.game = Game(difficulty)
        self.game.start_game()
        self.game.display_board()
    
    def display_board(self):
        '''Display game board as a grid of buttons'''
        pass
    
    def manage_left_click(self):
        pass
    
    def manage_right_click(self):
        pass
    
    def update_buttons(self):
        '''Update buttons to match the state of their corresponding cell'''
        pass
    
    def reveal_mines(self):
        '''Reveal all mines on the board after game over'''
        pass
    
    def restart(self):
        pass  
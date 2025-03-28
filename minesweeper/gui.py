from board import Board
from game import Game 
from timer import Timer
import tkinter as tk

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Minesweeper')
        self.resizable(False, False)
        self.game = None
        self.buttons = []
        
        # Create a main frame for welcome screen widgets.
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(padx=10, pady=10)
        
        self.welcome_screen()
        
    def clear_screen(self):
        """Clear all widgets from the window."""
        for widget in self.winfo_children():
            widget.destroy()
    
    def welcome_screen(self):
        '''Display welcome screen and difficulty selection'''
        self.clear_screen()
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(padx=10, pady=10)
        
        diff_lbl = tk.Label(self.main_frame, text="Select Difficulty:")
        diff_lbl.pack(pady=5)
        
        difficulties = ['beginner', 'intermediate', 'expert']
        for diff in difficulties:
            btn = tk.Button(self.main_frame, text=diff.capitalize(), width=15,
                            command=lambda d=diff: self.start_game(d))
            btn.pack(pady=3)
    
    def start_game(self, difficulty):
        # Remove welcome screen components.
        self.clear_screen()
        
        # Setup game and start timer.
        self.game = Game(difficulty)
        self.game.start_game()
        
        # Create a top frame for timer and control buttons.
        self.top_frame = tk.Frame(self)
        self.top_frame.pack(pady=5)
        self.timer_label = tk.Label(self.top_frame, text="Timer: 0", font=("Arial", 14))
        self.timer_label.pack(side="left", padx=10)
        self.restart_button = tk.Button(self.top_frame, text="Restart", command=self.restart)
        self.restart_button.pack(side="right", padx=10)
        
        # Start timer.
        self.timer = Timer(self.timer_label)
        self.timer.start()
        
        # Display the game board.
        self.display_board()
    
    def display_board(self):
        '''Display game board as a grid of buttons'''
        pass
    
    def manage_left_click(self, difficulty):
        self.board = Board(difficulty)
        self.board.reveal()
    
    def manage_right_click(self, difficulty):
        self.board = Board(difficulty)
        self.board.set_marker()
    
    def update_buttons(self):
        '''Update buttons to match the state of their corresponding cell'''
        self.button.destroy()
        self.cell.label()
    
    def reveal_mines(self):
        '''Reveal all mines on the board after game over'''
    
    def restart(self):
        self.welcome_screen() 
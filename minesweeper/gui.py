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
        board_frame = tk.Frame(self)
        board_frame.pack(pady=5)
        size = self.game.board.size
        self.buttons = [[None for _ in range(size)] for _ in range(size)]
        for x in range(size):
            for y in range(size):
                btn = tk.Button(
                    board_frame,
                    width=3,
                    height=1,
                    text="",
                    font=("Arial", 12),
                    command=lambda x=x, y=y: self.left_click(x, y)
                )
                btn.grid(row=x, column=y)
                # Bind right-click event.
                btn.bind("<Button-3>", lambda event, x=x, y=y: self.right_click(x, y))
                self.buttons[x][y] = btn
    
    def left_click(self, x, y):
        '''Handle left-click on the cell at (x, y)'''
        if self.game.game_over:
            return
        mine_hit = self.game.board.reveal(x, y)
        self.update_buttons()
        if mine_hit:
            self.timer.stop()
            self.game.end_game()
            self.reveal_mines()
            error_label = tk.Label(self, text="Game Over!", fg="red", font=("Arial", 16))
            error_label.pack(pady=10)
        elif self.game.check_win():
            self.timer.stop()
            self.game.end_game()
            win_label = tk.Label(self, text="Congratulations! You won!", fg="green", font=("Arial", 16))
            win_label.pack(pady=10)
    
    def right_click(self, x, y):
        '''Handle right-click on the cell at (x, y)'''
        if self.game.game_over:
            return
        self.game.board.set_marker(x, y)
        self.update_buttons()
    
    def update_buttons(self):
        '''Update buttons to match the state of their corresponding cell'''
        size = self.game.board.size
        for x in range(size):
            for y in range(size):
                cell = self.game.board.grid[x][y]
                btn = self.buttons[x][y]
                if not cell.hidden:
                    if cell.mine:
                        btn.configure(text="M", bg="red")
                    elif cell.number > 0:
                        btn.configure(text=str(cell.number), bg="lightgrey")
                    else:
                        btn.configure(text="", bg="white")
                else:
                    # Still hidden: show marker if any.
                    if cell.marker == 'flag':
                        btn.configure(text="F", bg="orange")
                    elif cell.marker == '?':
                        btn.configure(text="?", bg="yellow")
                    else:
                        btn.configure(text="", bg="darkgrey")
    
    def reveal_mines(self):
        '''Reveal all mines on the board after game over'''
    
    def restart(self):
        self.welcome_screen() 
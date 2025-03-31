from board import Board
from game import Game 
from timer import Timer
import customtkinter as ctk

class WelcomeScreen(ctk.CTkFrame):
    """Welcome screen with three difficulty options."""
    def __init__(self, master, switch_to_board_screen):
        super().__init__(master)
        self.switch = switch_to_board_screen
        self.configure(fg_color="#99d5ff")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.draw_welcome_screen()

    def draw_welcome_screen(self):
        # Draw difficulty frames for Beginner, Intermediate, and Expert.
        self.draw_difficulty_frame("Beginner", 9, "blue", (8, 12), 0)
        self.draw_difficulty_frame("Intermediate", 16, "green", (35, 45), 1)
        self.draw_difficulty_frame("Expert", 24, "red", (90, 110), 2)

    def draw_difficulty_frame(self, title, grid_size, color, mines_range, col_index):
        frame = ctk.CTkFrame(self, width=360, height=900, fg_color="white")
        frame.grid(row=0, column=col_index, padx=80, pady=10)
        frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        frame.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(frame, text=title, font=("Arial", 24), text_color=color)
        title_label.grid(row=0, column=0, padx=5, pady=5)

        shape_label = ctk.CTkLabel(frame, text=f"{grid_size} x {grid_size}", font=("Arial", 18))
        shape_label.grid(row=1, column=0, padx=5, pady=5)

        mines_label = ctk.CTkLabel(frame, text=f"~ {mines_range[0]} - {mines_range[1]} mines", font=("Arial", 18))
        mines_label.grid(row=2, column=0, padx=5, pady=5)

        play_button = ctk.CTkButton(frame, text="Play", command=lambda: self.switch(title.lower(), grid_size))
        play_button.grid(row=3, column=0, padx=5, pady=5)

class BoardScreen(ctk.CTkFrame):
    """Game board screen for Minesweeper."""
    def __init__(self, master, difficulty, grid_size):
        super().__init__(master)
        self.difficulty = difficulty
        self.grid_size = grid_size
        self.configure(fg_color="white")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create game logic board using existing Board class.
        self.board = Board(self.difficulty)
        self.buttons = []    # Will hold button references.
        self.timer = None

        # Top frame: timer and restart button.
        self.top_frame = ctk.CTkFrame(self, fg_color="#99d5ff")
        self.top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.top_frame.grid_columnconfigure((0, 1), weight=1)

        self.timer_label = ctk.CTkLabel(self.top_frame, text="Timer: 0", font=("Arial", 18))
        self.timer_label.grid(row=0, column=0, padx=10)
        self.restart_button = ctk.CTkButton(self.top_frame, text="Restart", command=self.restart)
        self.restart_button.grid(row=0, column=1, padx=10)

        # Board frame: holds grid of cell buttons.
        self.board_frame = ctk.CTkFrame(self, fg_color="white")
        self.board_frame.grid(row=1, column=0, padx=10, pady=10)
        self.draw_board()

        self.timer = Timer(self.timer_label)
        self.timer.start()

    def draw_board(self):
        """Create a grid of cell buttons."""
        for row in range(self.board.size):
            row_buttons = []
            for col in range(self.board.size):
                btn = ctk.CTkButton(self.board_frame,
                                    text="",
                                    width=35,
                                    height=35,
                                    command=lambda r=row, c=col: self.left_click(r, c))
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.bind("<Button-3>", lambda event, r=row, c=col: self.right_click(r, c))
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def left_click(self, row, col):
        """Handle left-click on a cell."""
        cell = self.board.grid[row][col]
        if not cell.hidden:
            return
        mine_hit = self.board.reveal(row, col)
        self.update_buttons()
        if mine_hit:
            self.timer.stop()
            self.reveal_mines()
        elif self.check_win():
            self.timer.stop()
            win_label = ctk.CTkLabel(self, text="Congratulations! You won!", font=("Arial", 24), text_color="green")
            win_label.grid(row=2, column=0, pady=10)

    def right_click(self, row, col):
        """Handle right-click to toggle marker."""
        self.board.set_marker(row, col)
        self.update_buttons()

    def update_buttons(self):
        """Update every cell button based on its corresponding cell state."""
        for row in range(self.board.size):
            for col in range(self.board.size):
                cell = self.board.grid[row][col]
                btn = self.buttons[row][col]
                if not cell.hidden:
                    if cell.mine:
                        btn.configure(text="💣", fg_color="red", hover=False)
                    elif cell.number > 0:
                        btn.configure(text=str(cell.number), fg_color="white", hover=False)
                    else:
                        btn.configure(text="", fg_color="white", hover=False)
                else:
                    if cell.marker == 'flag':
                        btn.configure(text="🚩", fg_color="#99d5ff", hover=True)
                    elif cell.marker == '?':
                        btn.configure(text="❓", fg_color="#99d5ff", hover=True)
                    else:
                        btn.configure(text="", fg_color="#99d5ff", hover=True)

    def reveal_mines(self):
        """Reveal all mines (called after a mine is hit)."""
        for row in range(self.board.size):
            for col in range(self.board.size):
                cell = self.board.grid[row][col]
                btn = self.buttons[row][col]
                if cell.mine:
                    btn.configure(text="💣", fg_color="red", hover=False)
                else:
                    if cell.number > 0:
                        btn.configure(text=str(cell.number), fg_color="white", hover=False)
                    else:
                        btn.configure(text="", fg_color="white", hover=False)

    def check_win(self):
        """Return True if all non-mine cells have been revealed."""
        for row in self.board.grid:
            for cell in row:
                if not cell.mine and cell.hidden:
                    return False
        return True

    def restart(self):
        """Restart the game by clearing the window and returning to the welcome screen."""
        self.timer.stop()
        for widget in self.master.winfo_children():
            widget.destroy()
        self.master.show_welcome_screen()

class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Minesweeper")
        self.geometry("1080x900")
        self.configure(fg_color="#99d5ff")
        self.show_welcome_screen()

    def show_welcome_screen(self):
        welcome = WelcomeScreen(self, self.switch_to_board_screen)
        welcome.place(relx=0.5, rely=0.5, anchor="center")

    def switch_to_board_screen(self, difficulty, grid_size):
        for widget in self.winfo_children():
            widget.destroy()
        board_screen = BoardScreen(self, difficulty, grid_size)
        board_screen.place(relx=0.5, rely=0.5, anchor="center")
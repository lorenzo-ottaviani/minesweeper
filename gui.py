from board import Board, Cell
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
        self.first_click = False

        # Create a main frame for welcome screen widgets.
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(padx=10, pady=10)

        self.welcome_screen()

    def clear_screen(self):
        """Clear all widgets from the window."""
        for widget in self.winfo_children():
            widget.destroy()

    def welcome_screen(self):
        """Display welcome screen and difficulty selection"""
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

        self.board = Board(difficulty)

        # Display the game board.
        self.display_board()

    def display_board(self):
        """Display game board as a grid of buttons"""
        board_frame = tk.Frame(self)
        board_frame.pack(pady=5)
        size = self.game.board.size

        self.buttons = []
        for x in range(size):
            ligne_buttons = []
            for y in range(size):
                btn = tk.Button(
                    board_frame,
                    width=3,
                    height=1,
                    text="",
                    font=("Arial", 12),
                    command=lambda x=x, y=y: self.cliquer(x, y)
                )
                btn.grid(row=x, column=y)
                ligne_buttons.append(btn)
            self.buttons.append(ligne_buttons)

        for ligne in range(size):
            for colonne in range(size):
                self.buttons[ligne][colonne].bind("<Button-3>", lambda event, x=ligne, y=colonne: self.right_click(x, y))

    def update_buttons(self):
        """Update buttons to match the state of their corresponding cell"""

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
        """Reveal all mines on the board after game over"""
        size = self.game.board.size
        for x in range(size):
            for y in range(size):
                cell = self.game.board.grid[x][y]
                if cell.mine:
                    btn = self.buttons[x][y]
                    btn.configure(text="M", bg="red")

    def restart(self):
        """Restart the game by returning to the welcome screen"""
        self.timer.stop()
        self.clear_screen()
        self.welcome_screen()

    def cliquer(self, x, y):
        game = Game(self.board.difficulty)
        coordinates = []
        case = self.board.grid[x][y]
        if not case.marker:
            case.hidden = False
            button = self.buttons[x][y]
            if case.mine:
                button.config(text="💣", bg="red")
                for i in range(self.board.x):
                    for j in range(self.board.y):
                        if self.board.grid[i][j].mine:
                            self.buttons[i][j].config(text="💣", bg="red")

                print("  YOU LOSE ! ! ")
            else:
                if not self.first_click:
                    self.first_click = True

                    self.board.add_mines(x, y)

                surrounding_mines = self.check_neighbours(x, y)
                if surrounding_mines == 0:
                    button.config(text="", bg="lightgray")
                    coordinates = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1),
                                  (x + 1, y), (x + 1, y + 1)]
                    for coordinate in coordinates:
                        if coordinate[0] >= 0 and coordinate[0] < self.board.x and coordinate[1] >= 0 and coordinate[
                            1] < self.board.y:
                            case = self.board.grid[coordinate[0]][coordinate[1]]
                            if case.hidden:
                                self.cliquer(coordinate[0], coordinate[1])

                elif surrounding_mines > 0:
                    button.config(text=surrounding_mines, bg="gray")

                if game.check_win():
                    messagebox.showinfo("YOU WIN!",
                                        f"You win in {self.chrono // 60} minutes and {self.chrono % 60} seconds !")
                    self.fenetre.destroy()

    def check_neighbours(self, x, y):
        surrounding_mines = 0
        coordinates = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y),
                      (x + 1, y + 1)]
        for coordinate in coordinates:
            if coordinate[0] >= 0 and coordinate[0] < self.board.x and coordinate[1] >= 0 and coordinate[1] < self.board.y:
                case = self.board.grid[coordinate[0]][coordinate[1]]
                if case.mine:
                    surrounding_mines += 1
        return surrounding_mines

    def right_click(self, x, y):

        case = self.board.grid[x][y]
        print(f"TYPE = {type(case)}")
        button = self.buttons[x][y]
        print(f"{x} - {y}")

        if case.hidden:
            case.change_state()
            self.board.set_marker(x, y)
            if case.marker:
                button.config(text="F", bg="orange")

            elif case.interrogation:
                button.config(text="?", bg="yellow")
            else:
                button.config(text="", bg="white")

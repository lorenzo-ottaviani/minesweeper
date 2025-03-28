import customtkinter as ctk
from random import randint

from .board import Board


class BoardScreen(ctk.CTkFrame):
    """ Class to manage the board screen."""

    def __init__(self, master, difficulty, cell_size, cell_range, number_of_mines):
        super().__init__(master)
        self.difficulty = difficulty
        self.cell_size = cell_size
        self.cell_range = cell_range
        self.number_of_mines = number_of_mines
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="white")
        self.first_click = True

        self.cells = []

        # Draw the board
        self.board_frame = ctk.CTkFrame(self, width=360, height=900, bg_color="white")
        self.board_frame.grid(row=0, column=1)

        self.draw_board_screen()

    def draw_board_screen(self):
        """
        Draw the board screen.
        :return: ∅
        """

        # def generate_mines(cell_range, number_of_mines):
        #     """"""
        #     mines = set()
        #     while len(mines) < number_of_mines:
        #         mine = (randint(0, cell_range - 1), randint(0, cell_range - 1))
        #         mines.add(mine)
        #     return mines
        #
        # mines = generate_mines(self.cell_range, randint(*self.number_of_mines))

        # Draw the cells into the board
        for row in range(self.cell_range):
            cells_row = []
            for col in range(self.cell_range):
                cell = ctk.CTkButton(self.board_frame, text="", width=self.cell_size, height=self.cell_size)
                cell.bind("<Button-1>", lambda event, r=row, c=col: self.cell_left_click_action(event, r, c))
                cell.bind("<Button-3>", lambda event, r=row, c=col: self.cell_right_click_action(event, r, c))

                cell.grid(row=row, column=col, padx=0.5, pady=0.5)
                cells_row.append(cell)
            self.cells.append(cells_row)

    def cell_left_click_action(self, event, row, col):
        """
        Call of the cell left click action.
        :param event: The button click event.
        :param row: The board rows.
        :param col: The board columns.
        :return: ∅
        """
        cell_button = self.cells[row][col]
        label_width = cell_button.winfo_width()
        label_height = cell_button.winfo_height()
        cell_button.destroy()

        board = Board(self.difficulty)
        board.reveal(row, col)

        matrix_cell = board.matrix[row][col]
        if matrix_cell.mine:
            label = ctk.CTkLabel(self.board_frame, text="💣", width=label_width, height=label_height,
                                 fg_color="white", font=("Arial", 24))
        else:
            label = ctk.CTkLabel(self.board_frame, text=matrix_cell.number, width=label_width, height=label_height,
                                 fg_color="white", font=("Arial", 24))

        label.grid(row=row, column=col, padx=0.5, pady=0.5)


        # if self.first_click:
        #     cell_button.destroy()
        #     # Mine draw call
        #     self.first_click = False
        # else:
        #     cell_button.destroy()
            # Check if mine
            # if mine:
            # end == True
            # victory == False "You loose"

        # current_text = cell_button.cget("text")
        #
        # if current_text == "":
        #     cell_button.configure(text="💣", font=("Arial", 18))
        # elif current_text == "💣":
        #     cell_button.configure(text="🦆", font=("Arial", 18))
        # elif current_text == "🦆":
        #     cell_button.configure(text="", font=("Arial", 18))

    def cell_right_click_action(self, event, row, col):
        """
        Call of the cell right click action.
        :param event: The button click event.
        :param row: The board rows.
        :param col: The board columns.
        :return: ∅
        """
        cell = self.cells[row][col]
        current_text = cell.cget("text")
        print(current_text)

        icons = ["🏴", "💣", "🦆", "🚩", "❓"]

        if current_text == "":
            cell.configure(text="🏴", font=("Arial", 18))
        elif current_text == "🏴":
            cell.configure(text="❓", font=("Arial", 18))
        elif current_text == "❓":
            cell.configure(text="", font=("Arial", 18))

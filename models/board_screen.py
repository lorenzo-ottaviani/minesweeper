import customtkinter as ctk
from random import randint


class BoardScreen(ctk.CTkFrame):
    """ Class to manage the board screen."""

    def __init__(self, master, cell_size, cell_range, number_of_mines):
        super().__init__(master)
        self.cell_size = cell_size
        self.cell_range = cell_range
        self.number_of_mines = number_of_mines
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="white")
        self.first_click = True

        self.cells = []

        self.draw_board_screen()

    def draw_board_screen(self):
        """
        Draw the board screen.
        :return: ∅
        """

        def generate_mines(cell_range, number_of_mines):
            """"""
            mines = set()
            while len(mines) < number_of_mines:
                mine = (randint(0, cell_range - 1), randint(0, cell_range - 1))
                mines.add(mine)
            return mines

        mines = generate_mines(self.cell_range, randint(*self.number_of_mines))

        # Draw the board
        board_frame = ctk.CTkFrame(self, width=360, height=900, bg_color="white")
        board_frame.grid(row=0, column=1)

        # Draw the cells into the board
        for row in range(self.cell_range):
            cells_row = []
            for col in range(self.cell_range):
                cell = ctk.CTkButton(board_frame, text="", width=self.cell_size, height=self.cell_size)
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

        if self.first_click:
            cell_button.destroy()
            # Mine draw call
            self.first_click = False
        else:
            cell_button.destroy()
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

        icons = ["🏴", "💣", "🦆", "🚩", "❓"]

        if current_text == "":
            cell.configure(text="🏴", font=("Arial", 18))
        elif current_text == "🏴":
            cell.configure(text="❓", font=("Arial", 18))
        elif current_text == "❓":
            cell.configure(text="", font=("Arial", 18))

import customtkinter as ctk

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
        self.board = Board(self.difficulty)

        # Draw the board
        self.board_frame = ctk.CTkFrame(self, width=360, height=900, bg_color="white")
        self.board_frame.grid(row=0, column=1)

        self.draw_board_screen()

    def draw_board_screen(self):
        """
        Draw the board screen.
        :return: ∅
        """

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

        self.board.reveal(row, col)

        matrix_cell = self.board.matrix[row][col]
        if matrix_cell.mine:
            self.reveal_all_the_board(self.board, label_width, label_height)
        else:
            label = ctk.CTkLabel(self.board_frame, text=matrix_cell.number, width=label_width, height=label_height,
                                 fg_color="white", font=("Arial", 24))
            label.grid(row=row, column=col, padx=0.5, pady=0.5)

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
        print(f"Current text: {current_text}")

        icons = ["🏴", "💣", "🦆", "🚩", "❓"]

        if current_text == "":
            cell.configure(text="🏴", font=("Arial", 18))
        elif current_text == "🏴":
            cell.configure(text="❓", font=("Arial", 18))
        elif current_text == "❓":
            cell.configure(text="", font=("Arial", 18))

    def reveal_all_the_board(self, board, label_width, label_height):
        """
        Reveal all the cells when a mine is clicked.
        :param board: The board object.
        :param label_width: The width of the label.
        :param label_height: The height of the label.
        :return: ∅
        """
        # Destroy all the cell buttons
        for cell_row in self.cells:
            for cell_button in cell_row:
                cell_button.destroy()

        # Reveal the content of the cells
        for row_index in range(self.cell_range):
            for col_index in range(self.cell_range):
                matrix_cell = board.matrix[row_index][col_index]

                if matrix_cell.mine:
                    label = ctk.CTkLabel(self.board_frame, text="💣", width=label_width, height=label_height,
                                         fg_color="white", font=("Arial", 24))
                else:
                    label = ctk.CTkLabel(self.board_frame, text=matrix_cell.number, width=label_width,
                                         height=label_height, fg_color="white", font=("Arial", 24))
                label.grid(row=row_index, column=col_index, padx=0.5, pady=0.5)

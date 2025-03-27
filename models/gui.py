import customtkinter as ctk
from .board_screen import BoardScreen
from .welcome_screen import WelcomeScreen

class GUI(ctk.CTk):
    """ Graphical User Interface (GUI) of the program. """

    def __init__(self):
        super().__init__()

        self.title("Minesweeper")
        self.geometry("1080x900")
        self.configure(fg_color="#99d5ff")

        # Create the welcome screen
        self.welcome_screen = WelcomeScreen(self, self.switch_to_board_screen)
        self.welcome_screen.place(relx=0.5, rely=0.5, anchor="center")

    def switch_to_board_screen(self, cell_size, cell_range, number_of_mines):
        """
        Switch from the welcome screen to the board screen.
        :param cell_size: Size of a board cell.
        :param cell_range: Number of cells per row and column.
        :param number_of_mines: Number of mines in the choose difficulty.
        :return: ∅
        """
        for widget in self.winfo_children():
            widget.destroy()

        board_screen = BoardScreen(self, cell_size, cell_range, number_of_mines)
        board_screen.place(relx=0.5, rely=0.5, anchor="center")

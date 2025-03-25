import customtkinter as ctk
from models import *


class App(ctk.CTk):
    """ Main class of the program. """

    def __init__(self):
        """"""
        super().__init__()
        self.title("Minesweeper")
        self.geometry("1200x1200")

        # Test of a board container shape
        self.board = ctk.CTkFrame(self, width=1000, height=1000)
        self.board.place(relx=0.5, rely=0.5, anchor="center")

if __name__ == '__main__':
    minesweeper = App()
    minesweeper.mainloop()

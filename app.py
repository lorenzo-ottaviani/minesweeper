import customtkinter as ctk
from models import *


class App:
    """ Main class of the program. """

    def __init__(self):
        """"""
        self.controller = GUI()

    def run(self):
        """"""
        self.controller.mainloop()


if __name__ == '__main__':
    minesweeper = App()
    minesweeper.run()

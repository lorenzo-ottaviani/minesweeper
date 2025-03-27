"""
Authors : Lorenzo OTTAVIANI, Morgane ROSSI et Leila WILDE.
Date : 27/03/2025 23h09
Aim of the program :
    Execute a minesweeper game using Custom Tkinter.
Inputs : ∅
Output : Minesweeper classical game.
"""

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

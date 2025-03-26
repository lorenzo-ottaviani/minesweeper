"""
Authors : Lorenzo OTTAVIANI, Morgane ROSSI et Leila WILDE.
Date : 26/03/2025 09h43
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

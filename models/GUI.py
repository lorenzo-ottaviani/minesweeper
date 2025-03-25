import customtkinter as ctk


class GUI(ctk.CTk):
    """ Graphical User Interface (GUI) of the program. """

    def __init__(self):
        """"""
        super().__init__()

        self.title("Minesweeper")
        self.geometry("1200x1000")

        self.configure(fg_color="#99d5ff")

        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.draw_welcome_scene()

        # Test of a board container shape
        # self.board = ctk.CTkFrame(self, width=1000, height=1000)
        # self.board.place(relx=0.5, rely=0.5, anchor="center")

    def draw_welcome_scene(self):
        """"""
        easy_frame = ctk.CTkFrame(self, width=360, height=700)
        easy_frame.grid(row=0, column=0, padx=10)
        medium_frame = ctk.CTkFrame(self, width=360, height=700)
        medium_frame.grid(row=0, column=1, padx=10)
        hard_frame = ctk.CTkFrame(self, width=360, height=700)
        hard_frame.grid(row=0, column=2, padx=10)

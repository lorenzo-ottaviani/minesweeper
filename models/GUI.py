import customtkinter as ctk


class GUI(ctk.CTk):
    """ Graphical User Interface (GUI) of the program. """

    def __init__(self):
        super().__init__()

        self.title("Minesweeper")
        self.geometry("1080x900")  # Total window size

        self.configure(fg_color="#99d5ff")

        # Configure rows and columns
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.draw_welcome_scene()

    def draw_welcome_scene(self):
        """
        Draw the welcome scene screen.
        return : ∅
        """

        def draw_beginner_frame():
            """
            Draw the beginner frame.
            return : ∅
            """
            beginner_frame = ctk.CTkFrame(self, width=360, height=900)
            beginner_frame.grid(row=0, column=0, padx=10, pady=10)

            beginner_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
            beginner_frame.grid_columnconfigure(0, weight=1)

            beginner_title = ctk.CTkLabel(beginner_frame, text="Beginner", font=("Arial", 24), text_color="blue")
            beginner_title.grid(row=0, column=1, padx=5, pady=5)

            beginner_shape = ctk.CTkLabel(beginner_frame, text="9 x 9", font=("Arial", 18))
            beginner_shape.grid(row=1, column=1, padx=5, pady=5)

            beginner_mines = ctk.CTkLabel(beginner_frame, text=" ~ 10 mines", font=("Arial", 18))
            beginner_mines.grid(row=2, column=1, padx=5, pady=5)

            beginner_button = ctk.CTkButton(beginner_frame, text="Play", command=self.start_beginner_game)
            beginner_button.grid(row=3, column=1, padx=5, pady=5)

        def draw_intermediate_frame():
            """
            Draw the intermediate frame.
            return : ∅
            """
        intermediate_frame = ctk.CTkFrame(self, width=360, height=900)
        intermediate_frame.grid(row=0, column=1, padx=10, pady=10)

        intermediate_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        intermediate_frame.grid_columnconfigure(0, weight=1)

        intermediate_title = ctk.CTkLabel(intermediate_frame, text="Intermediate", font=("Arial", 24),
                                          text_color="green")
        intermediate_title.grid(row=0, column=1, padx=5, pady=5)

        intermediate_shape = ctk.CTkLabel(intermediate_frame, text="16 x 16", font=("Arial", 18))
        intermediate_shape.grid(row=1, column=1, padx=5, pady=5)

        intermediate_mines = ctk.CTkLabel(intermediate_frame, text=" ~ 40 mines", font=("Arial", 18))
        intermediate_mines.grid(row=2, column=1, padx=5, pady=5)

        intermediate_button = ctk.CTkButton(intermediate_frame, text="Play", command=self.start_intermediate_game)
        intermediate_button.grid(row=3, column=1, padx=5, pady=5)

        def draw_expert_frame():
            """
            Draw the expert frame.
            return : ∅
            """
            expert_frame = ctk.CTkFrame(self, width=360, height=900)
            expert_frame.grid(row=0, column=2, padx=10, pady=10)

            expert_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
            expert_frame.grid_columnconfigure(0, weight=1)

            expert_title = ctk.CTkLabel(expert_frame, text="Expert", font=("Arial", 24), text_color="red")
            expert_title.grid(row=0, column=1, padx=5, pady=5)

            expert_shape = ctk.CTkLabel(expert_frame, text="24 x 24", font=("Arial", 18))
            expert_shape.grid(row=1, column=1, padx=5, pady=5)

            expert_mines = ctk.CTkLabel(expert_frame, text=" ~ 99 mines", font=("Arial", 18))
            expert_mines.grid(row=2, column=1, padx=5, pady=5)

            expert_button = ctk.CTkButton(expert_frame, text="Play", command=self.start_expert_game)
            expert_button.grid(row=3, column=1, padx=5, pady=5)

        draw_beginner_frame()
        draw_intermediate_frame()
        draw_expert_frame()

    def start_beginner_game(self):
        pass

    def start_intermediate_game(self):
        pass

    def start_expert_game(self):
        pass

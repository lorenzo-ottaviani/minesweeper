from board import Board, Cell
from game import Game 
# from timer import Timer
import tkinter as tk

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Minesweeper')
        self.resizable(False, False)
        self.game = None
        self.buttons = []
        self.first_click = False
        
        # Create a main frame for welcome screen widgets.
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(padx=10, pady=10)
        
        self.welcome_screen()
        
    def clear_screen(self):
        """Clear all widgets from the window."""
        for widget in self.winfo_children():
            widget.destroy()
    
    def welcome_screen(self):
        '''Display welcome screen and difficulty selection'''
        self.clear_screen()
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(padx=10, pady=10)
        
        diff_lbl = tk.Label(self.main_frame, text="Select Difficulty:")
        diff_lbl.pack(pady=5)
        
        difficulties = ['beginner', 'intermediate', 'expert']
        for diff in difficulties:
            btn = tk.Button(self.main_frame, text=diff.capitalize(), width=15,
                            command=lambda d=diff: self.start_game(d))
            btn.pack(pady=3)
    
    def start_game(self, difficulty):
        # Remove welcome screen components.
        self.clear_screen()
        
        # Setup game and start timer.
        self.game = Game(difficulty)
        self.game.start_game()
        
        # Create a top frame for timer and control buttons.
        self.top_frame = tk.Frame(self)
        self.top_frame.pack(pady=5)
        self.timer_label = tk.Label(self.top_frame, text="Timer: 0", font=("Arial", 14))
        self.timer_label.pack(side="left", padx=10)
        self.restart_button = tk.Button(self.top_frame, text="Restart", command=self.restart)
        self.restart_button.pack(side="right", padx=10)
        
        # Start timer.
        # self.timer = Timer(self.timer_label)
        # self.timer.start()

        self.board = Board(difficulty)
        
        # Display the game board.
        self.display_board()
    
    def display_board(self):
        '''Display game board as a grid of buttons'''
        board_frame = tk.Frame(self)
        board_frame.pack(pady=5)
        size = self.game.board.size

        self.buttons = []
        for x in range(size):
            ligne_boutons = []
            for y in range(size):

                btn = tk.Button(
                    board_frame,
                    width=3,
                    height=1,
                    text="",
                    font=("Arial", 12),
                    command=lambda x=x, y=y: self.cliquer(x, y)
                )
                btn.grid(row=x, column=y)
                ligne_boutons.append(btn)
            self.buttons.append(ligne_boutons)

        for ligne in range(size):
            for colonne in range(size):
                self.buttons[ligne][colonne].bind("<Button-3>", lambda event, x=ligne, y=colonne: self.clic_droit(x, y))

    def update_buttons(self):
        '''Update buttons to match the state of their corresponding cell'''

        size = self.game.board.size
        for x in range(size):
            for y in range(size):
                cell = self.game.board.grid[x][y]
                btn = self.buttons[x][y]
                if not cell.hidden:
                    if cell.mine:
                        btn.configure(text="M", bg="red")
                    elif cell.number > 0:
                        btn.configure(text=str(cell.number), bg="lightgrey")
                    else:
                        btn.configure(text="", bg="white")
                else:
                    # Still hidden: show marker if any.
                    if cell.marker == 'flag':
                        btn.configure(text="F", bg="orange")
                    elif cell.marker == '?':
                        btn.configure(text="?", bg="yellow")
                    else:
                        btn.configure(text="", bg="darkgrey")
    
    def reveal_mines(self):
        '''Reveal all mines on the board after game over'''
        size = self.game.board.size
        for x in range(size):
            for y in range(size):
                cell = self.game.board.grid[x][y]
                if cell.mine:
                    btn = self.buttons[x][y]
                    btn.configure(text="M", bg="red")
    
    def restart(self):
        '''Restart the game by returning to the welcome screen'''
        # self.timer.stop()
        self.clear_screen()
        self.welcome_screen() 


    # méthode pour cliquer sur une case, révélant si elle contient une mine ou non, et affichant le nombre de mines adjacentes si c'est le cas.
    # Si la case est vide, on révèle toutes les cases adjacentes en rappellant la méthode récursivement jusqu'à atteindre une case avec des mines adjacentes.
    def cliquer(self, x, y):
        game = Game(self.board.difficulty)
        coordonnes = []
        case = self.board.grid[x][y]
        if not case.marker:
            case.hidden = False
            bouton = self.buttons[x][y]
            # Si la case contient une mine, on affiche une bombe et on révèle toutes les mines
            if case.mine:
                bouton.config(text="💣", bg="red")
                for i in range(self.board.x):
                    for j in range(self.board.y):
                        if self.board.grid[i][j].mine:
                            self.buttons[i][j].config(text="💣", bg="red")

                print("  PERDU ! ! ")
            else:
                if not self.first_click :
                    self.first_click = True

                    self.board.add_mines(x, y)

                mines_adjacentes = self.verifier_voisins(x, y)
                # Si il n'y a pas de mines adjacentes, on révèle les cases adjacentes
                if mines_adjacentes == 0:
                    bouton.config(text="", bg="lightgray")
                    coordonnes = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
                    for coordonne in coordonnes:
                        if coordonne[0] >= 0 and coordonne[0] < self.board.x and coordonne[1] >= 0 and coordonne[1] < self.board.y:
                            case = self.board.grid[coordonne[0]][coordonne[1]]
                            if case.hidden:
                                self.cliquer(coordonne[0], coordonne[1]) # Appel récursif
                # Sinon, on affiche le nombre de mines adjacentes
                elif mines_adjacentes > 0:
                    bouton.config(text=mines_adjacentes, bg="gray")

                
                if game.check_win():
#                    self.arreter_chrono()
                    messagebox.showinfo("Gagné", f"Vous avez gagné en {self.chrono // 60} minutes et {self.chrono % 60} secondes !")
                    self.fenetre.destroy()


    # méthode pour vérifier le nombre de mines adjacentes à une case
    def verifier_voisins(self, x, y):
        mines_adjacentes = 0
        coordonnes = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
        for coordonne in coordonnes:
            if coordonne[0] >= 0 and coordonne[0] < self.board.x and coordonne[1] >= 0 and coordonne[1] < self.board.y:
                case = self.board.grid[coordonne[0]][coordonne[1]]
                if case.mine:
                    mines_adjacentes += 1
        return mines_adjacentes


    # méthode pour gérer le clic droit, permettant de placer des markerx ou des points d'interrogation
    def clic_droit(self, x, y):

        case = self.board.grid[x][y]
        print(f"TYPE = {type(case)}")
        bouton = self.buttons[x][y]
        print(f"{x} - {y}")

        if case.hidden:
            case.changer_etat()
            self.board.set_marker(x, y)
            if case.marker:
                bouton.config(text="F", bg="orange")

            elif case.interrogation:
                bouton.config(text="?", bg="yellow")
            else:
                bouton.config(text="", bg="white")


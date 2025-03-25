import customtkinter as ctk

# Initialisation de la fenêtre principale
root = ctk.CTk()
root.title("Minesweeper")  # Définir le titre de la fenêtre

# Dimensions du jeu
rows = 24
cols = 24

# Grille de boutons représentant les cases
buttons = []


# Fonction qui gère le clic sur une case et alterne entre drapeau, canard et rien
def on_button_click(row, col):
    # Obtenir le bouton sur lequel l'utilisateur a cliqué
    button = buttons[row][col]

    # Changer l'icône sur le bouton en fonction de l'état actuel
    current_text = button.cget("text")

    if current_text == "":
        button.configure(text="🏴", font=("Arial", 25))  # Drapeau avec une grande taille
    elif current_text == "🏴":
        button.configure(text="🦆", font=("Arial", 25))  # Canard avec une grande taille
    elif current_text == "🦆":
        button.configure(text="", font=("Arial", 25))  # Rien avec une grande taille


# Création des boutons représentant les cases
for row in range(rows):
    button_row = []
    for col in range(cols):
        button = ctk.CTkButton(master=root, text="", width=40, height=40, command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col, padx=0.5, pady=0.5)
        button_row.append(button)
    buttons.append(button_row)

# Lancer la boucle principale de CustomTkinter
root.mainloop()

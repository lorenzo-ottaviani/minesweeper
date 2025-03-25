from tkinter import Tk, Frame, Label
from cell import Cell

# pondre la fenetre
root = Tk()

root.geometry("1200x800")

external = Frame(root, bg="#ffffff", width=1200, height=800)
external.place(x=0, y=0)

internal = Frame(root, bg="#99ccff", width=900, height=600)
internal.place(x=100, y=100)

game_title = Label(text="Mainesouipeur")

for x in range(6):
    for y in range(6):
        c = Cell(x, y)
        c.create_btn(internal)
        c.cell_btn.grid(column=x, row=y)

Cell.create_cell_count(external)
Cell.cell_count_label_obj.place(x=12, y=0)
Cell.randomize_mines()

root.mainloop()
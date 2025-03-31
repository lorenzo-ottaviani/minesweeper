from tkinter import Button, Label
from random import sample


class Cell:
    all = []
    cell_count_label = None
    cell_count = 10
    def __init__(self, x, y, boum = False):
        self.boum = boum
        self_opened = False
        self.boum_cell = False
        self.cell_btn = None
        self.x = x
        self.y = y
        Cell.all.append(self)
    
    def create_btn(self, location):
        btn = Button(location, width =9, height=3)
        self.cell_btn = btn
    
    @staticmethod
    def create_cell_count(location):
        label = Label(
            location,
            bg= "#000099",
            text = f"Cells left = {Cell.cell_count}",
            width = 12,
            height = 3,
            font=("", 18)            
        )
        Cell.cell_count_label_obj = label
    

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn.configure(text=self.mines_len)

            if Cell.cell_count_label_obj:
                Cell.cell_count_label_obj.configure(
                    text=f"Cells Left:{Cell.cell_count}"
                )
            
            self.cell_btn.configure(bg="#00ffcc")
        self.is_opened = True


    @staticmethod
    def randomize_mines():
        picked_as_mines = sample(Cell.all, 9)
        
        for picked_mine in picked_as_mines:
            picked_mine.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
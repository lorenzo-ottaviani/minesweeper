from random import random 

class Board():
    def __init__(self, difficulty):
        self.difficulty = difficulty
        if difficulty == 'beginner':
            self.size = 9
        elif difficulty == 'intermediate':
            self.size = 16
        elif difficulty == 'expert':
            self.size = 24
        
        self.grid = []
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                row.append(Cell(hidden=True, mine=False))
            self.grid.append(row)
                
    def reveal(self, x, y):
        self.grid[x][y].hidden = False 
        return self.grid[x][y].mine
    
    def add_mines(self):
        mines_required = round((self.size ** 2) * 0.2)
        mines_added = 0
        while mines_added < mines_required:
            x = round(random()*(self.size -1))
            y = round(random()*(self.size -1))
            if not self.grid[x][y].mine:
                self.grid[x][y].mine = True
                mines_added += 1
                
class Cell:
    def __init__(self, hidden, mine):
        self.hidden = hidden 
        self.mine = mine
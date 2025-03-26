from random import randint

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
        all_hidden = True
        for row in self.grid:
            for cell in row:
                if cell.hidden == False:
                    all_hidden = False
        self.grid[x][y].hidden = False 
        if all_hidden:
            self.add_mines()
        return self.grid[x][y].mine
        # empty cells reveal surrounding cells recursively
    
    def add_mines(self):
        mines_required = round((self.size ** 2) * 0.2)
        mines_added = 0
        while mines_added < mines_required:
            x = round(randint(0, self.size -1))
            y = round(randint(0, self.size -1))
            if (not self.grid[x][y].mine) and self.grid[x][y].hidden:
                self.grid[x][y].mine = True
                mines_added += 1
        # add number in surround cells
           
    def set_marker(self, x, y):
        '''method to cycle through the marker state from flag > ? > None'''
        cell = self.grid[x][y]
        if cell.hidden:
            if cell.marker is None:
                cell.marker = 'flag'
            elif cell.marker == 'flag':
                cell.marker = '?'
            elif cell.marker == '?':
                cell.marker = None
                
class Cell:
    def __init__(self, hidden, mine, marker=None):
        self.hidden = hidden 
        self.mine = mine
        self.marker = marker
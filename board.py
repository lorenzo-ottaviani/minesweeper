from random import randint


def surrounding_cells(x,y):
    """Return a list of x, y coordinates around a given cell"""
    return [(x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),              (x+1, y), 
            (x-1, y+1), (x, y+1), (x+1, y+1)]


class Cell:
    def __init__(self, hidden=True, mine=False, marker=None, interrogation=None):
        self.hidden = hidden 
        self.mine = mine
        self.marker = marker
        self.number = 0
        self.interrogation = interrogation

    def __repr__(self):
        return f"mine : {self.mine} - marker : {self.marker} - hidden : {self.hidden}"
    
    def change_state(self):
        print("CHANGE")
        if self.hidden:
            if self.marker:
                self.marker = False
                self.interrogation = True
            elif self.interrogation:
                self.interrogation = False
            else:
                self.marker = True
        print(self)


class Board:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        if difficulty == 'beginner':
            self.size = 9
        elif difficulty == 'intermediate':
            self.size = 16
        elif difficulty == 'expert':
            self.size = 24
        self.x = self.size
        self.y = self.size
        
        self.grid = []
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                row.append(Cell())
            self.grid.append(row)



    def reveal(self, x, y):
        """Reveal a hidden cell and recusively reveal empty/zero value surrounding cells. Return True if mine"""
        cell = self.grid[x][y]
        # on first reveal, if all cells are hidden, then set-up mines randomly in grid
        if cell.hidden:
            all_hidden = True
            for row in self.grid:
                for c in row:
                    if not c.hidden:
                        all_hidden = False
            if all_hidden:
                self.add_mines(exclude_x=x, exclude_y=y)
            
            # if cell is not a mine and is 0 then reveal surrounding cells
            if not cell.mine and cell.number == 0:
                for x2, y2 in surrounding_cells(x,y):
                    if x2 >= 0 and y2 >= 0 and x2 < self.size and y2 < self.size:
                        # Only reveal if still hidden, and if no mine. (recursive)
                        if not cell.mine and cell.number == 0:
                            self.reveal(x2, y2)
            
            cell.hidden = False 
                                
        return cell.mine
    
    def add_mines(self, exclude_x, exclude_y):
        """Add mines to the board randomly and give values to surrounding cells"""
        mines_required = round((self.size ** 2) * 0.2)
        mines_added = 0
        while mines_added < mines_required:
            x = randint(0, self.size -1)
            y = randint(0, self.size -1)
            if (not self.grid[x][y].mine) and self.grid[x][y].hidden:
                # exclude the first clicked cell
                if x == exclude_x and y == exclude_y:
                    continue
                self.grid[x][y].mine = True
                mines_added += 1
                
                for x2, y2 in surrounding_cells(x,y):
                    if x2 >= 0 and y2 >= 0 and x2 < self.size and y2 < self.size:
                        self.grid[x2][y2].number += 1

    def display(self):
        for line in self.grid:
            for case in line:
                if case.mine:
                    print("B", end=" ")
                else:
                    print("-", end=" ")
            print()


    def set_mines(self):
        for i in range(self.mines):
            place = False
            while not place:
                x = randint(0, self.lines - 1)
                y = randint(0, self.colonnes - 1)
                if not self.grid[x][y].mine and not self.grid[x][y].revele:
                    self.grid[x][y].mine = True
                    place = True

    def set_marker(self, x, y):
        """Cycle through a hidden cell's marker states from None -> flag -> ? -> None"""
        cell = self.grid[x][y]
        if cell.hidden:
            if cell.marker is None:
                cell.marker = 'flag'
            elif cell.marker == 'flag':
                cell.marker = '?'
            elif cell.marker == '?':
                cell.marker = None
                
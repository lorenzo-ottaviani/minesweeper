from random import random 

class Duckfield():
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
                row.append({'hidden': True, 'duck': False})
            self.grid.append(row)
                
    def reveal(self, x, y):
        self.grid[x][y]['hidden'] = False 
        return self.grid[x][y]['duck']
    
    def add_ducks(self):
        ducks_required = round((self.size ** 2) * 0.2)
        ducks_added = 0
        while ducks_added < ducks_required:
            x = round(random()*(self.size -1))
            y = round(random()*(self.size -1))
            if not self.grid[x][y]['duck']:
                self.grid[x][y]['duck'] = True
                ducks_added += 1

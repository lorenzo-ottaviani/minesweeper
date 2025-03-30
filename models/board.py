from random import randint


def surrounding_cells(x, y):
    """Return a list of x, y coordinates around a given cell"""
    return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
            (x - 1, y), (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]


class Cell:
    """ Class to manage the cell."""
    def __init__(self, hidden=True, mine=False, marker=None):
        self.hidden = hidden
        self.mine = mine
        self.marker = marker
        self.number = 0


class Board:
    """ Class to manage the board."""
    def __init__(self, difficulty):
        self.difficulty = difficulty
        if difficulty == "beginner":
            self.size = 9
        elif difficulty == "intermediate":
            self.size = 16
        elif difficulty == "expert":
            self.size = 24

        self.matrix = []
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                row.append(Cell())
            self.matrix.append(row)

    def reveal(self, x, y):
        """ Reveal a hidden cell and recursively reveal empty/zero value surrounding cells. Return True if mine """
        cell = self.matrix[x][y]
        if cell.hidden:
            all_hidden = True
            for row in self.matrix:
                for c in row:
                    if not c.hidden:
                        all_hidden = False
            if all_hidden:
                self.add_mines(exclude_x=x, exclude_y=y)

            for x2, y2 in surrounding_cells(x, y):
                if x2 >= 0 and y2 >= 0 and x2 < self.size and y2 < self.size:
                    if (not self.matrix[x2][y2].mine) and self.matrix[x2][y2].number == 0:
                        self.reveal(x2, y2)

            cell.hidden = False

        return cell.mine

    def add_mines(self, exclude_x, exclude_y):
        """Add mines to the board randomly and give values to surrounding cells"""
        mines_required = round((self.size ** 2) * 0.2)
        mines_added = 0
        while mines_added < mines_required:
            x = randint(0, self.size - 1)
            y = randint(0, self.size - 1)
            if (not self.matrix[x][y].mine) and self.matrix[x][y].hidden:
                # exclude the first clicked cell
                if x == exclude_x and y == exclude_y:
                    continue
                self.matrix[x][y].mine = True
                mines_added += 1

                for x2, y2 in surrounding_cells(x, y):
                    if x2 >= 0 and y2 >= 0 and x2 < self.size and y2 < self.size:
                        self.matrix[x2][y2].number += 1

        # Test : show the board matrix
        for row in self.matrix:
            for cell in row:
                print(cell.mine, end="\t")
                print(cell.number)

    def set_marker(self, x, y):
        """Cycle through a hidden cell's marker states from None -> flag -> ? -> None"""
        cell = self.matrix[x][y]
        if cell.hidden:
            if cell.marker is None:
                cell.marker = 'flag'
            elif cell.marker == 'flag':
                cell.marker = '?'
            elif cell.marker == '?':
                cell.marker = None

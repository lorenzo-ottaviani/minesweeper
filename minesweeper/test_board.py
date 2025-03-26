from board import Board
import unittest

class TestBoard(unittest.TestCase):
    def test_create_board(self):
        board = Board('beginner')
        assert board.difficulty == 'beginner'
        assert board.size == 9
        assert len(board.grid) == 9
        assert len(board.grid[0]) == 9
        
        board = Board('intermediate')
        assert board.difficulty == 'intermediate'
        assert board.size == 16
        assert len(board.grid) == 16
        assert len(board.grid[0]) == 16
        
        board = Board('expert')
        assert board.difficulty == 'expert'
        assert board.size == 24
        assert len(board.grid) == 24 
        assert len(board.grid[0]) == 24       

    def test_reveal(self):
        board = Board('beginner')
        for row in board.grid:
            for cell in row:
                assert cell.hidden
        is_mine = board.reveal(0, 0)
        assert is_mine == False
        assert board.grid[0][0].hidden == False

    def test_percentage_mines(self):
        board = Board('beginner')
        board.add_mines()
        mine_count = 0
        for row in board.grid:
            for cell in row:
                if cell.mine:
                    mine_count += 1
        assert mine_count == round((board.size ** 2) * 0.2)

    def test_set_marker(self):
        board = Board('beginner')
        board.set_marker(0,0)
        assert board.grid[0][0].marker == 'flag'
        board.set_marker(0,0)
        assert board.grid[0][0].marker == '?'
        board.set_marker(0,0)
        assert board.grid[0][0].marker == None
        
if __name__=='__main__':
    unittest.main()
    
        
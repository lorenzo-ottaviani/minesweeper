from board import Board

def test_create_board():
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
    
test_create_board()

def test_reveal():
    board = Board('beginner')
    for row in board.grid:
        for cell in row:
            assert cell.hidden
    is_mine = board.reveal(0, 0)
    assert is_mine == False
    assert board.grid[0][0].hidden == False

test_reveal()

def test_percentage_mines():
    board = Board('beginner')
    board.add_mines()
    mine_count = 0
    for row in board.grid:
        for cell in row:
            if cell.mine:
                mine_count += 1
    assert mine_count == round((board.size ** 2) * 0.2)

test_percentage_mines()
from board import Duckfield

def test_create_duckfield():
    duckfield = Duckfield('beginner')
    assert duckfield.difficulty == 'beginner'
    assert duckfield.size == 9
    assert len(duckfield.grid) == 9
    assert len(duckfield.grid[0]) == 9
    
    duckfield = Duckfield('intermediate')
    assert duckfield.difficulty == 'intermediate'
    assert duckfield.size == 16
    assert len(duckfield.grid) == 16
    assert len(duckfield.grid[0]) == 16
    
    duckfield = Duckfield('expert')
    assert duckfield.difficulty == 'expert'
    assert duckfield.size == 24
    assert len(duckfield.grid) == 24 
    assert len(duckfield.grid[0]) == 24       
    
test_create_duckfield()

def test_reveal():
    duckfield = Duckfield('beginner')
    for row in duckfield.grid:
        for tile in row:
            assert tile['hidden']
    is_duck = duckfield.reveal(0, 0)
    assert is_duck == True or is_duck == False
    assert duckfield.grid[0][0]['hidden'] == False

test_reveal()

def test_percentage_ducks():
    duckfield = Duckfield('beginner')
    duckfield.add_ducks()
    duck_count = 0
    for row in duckfield.grid:
        for tile in row:
            if tile['duck']:
                duck_count += 1
    assert duck_count == round((duckfield.size ** 2) * 0.2)

test_percentage_ducks()
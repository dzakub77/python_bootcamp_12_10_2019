
def trojkat_pascala():




def test_trojkat_pascala():
    expected = """[1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    [1, 5, 10, 10, 5, 1]"""
    assert trojkat_pascala(6) == expected
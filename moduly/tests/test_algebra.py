from moduly import matrices

def test_dodanie_dwoch_macierzy():
    macierz1 = [[1, 3], [2, 4]]
    macierz2 = [[3, 4], [5, 6]]
    expected = [[4, 7], [7, 10]]
    assert matrices.dodanie_dwoch_macierzy(macierz1, macierz2) == expected

lista = [1, 2, 3, [4, 5, [6]], 7]
def splaszcz(lista):
    wynik = []
    for element in lista:
        if isinstance(element, list):
            for e in splaszcz(element):
                wynik.append(e)
        else:
            wynik.append(element)
    return wynik




#isinstance([1, 2], list)

def test_splaszcz():
    assert splaszcz(lista) == [1, 2, 3, 4, 5, 6, 7]
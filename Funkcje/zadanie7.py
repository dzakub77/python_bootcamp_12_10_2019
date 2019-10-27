start = lambda x: x > 2
stop = lambda x: x == 8

def przytnij(lista, start, stop):
    y = []
    czy_zliczac = False
    for x in lista:
        if not czy_zliczac and start(x):
            czy_zliczac = True
        if czy_zliczac:
            y.append(x)
            if stop(x):
                break
    return y




def test_przytnij():
    lista = [1, 3, 5, 6, 8, 10]
    expected = [3, 5, 6, 8]
    assert przytnij(lista, start, stop) == expected
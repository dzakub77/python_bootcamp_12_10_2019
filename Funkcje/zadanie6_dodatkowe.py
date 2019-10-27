

def liczba_doskonala(x):
    a = []
    for i in range(1, 100):
        if x % i == 0:
            a.append(i)
    a.remove(x)
    a = sum(a)
    return(a)

def test_liczba_doskonala():
    assert liczba_doskonala(6) == 6
    assert liczba_doskonala(28) == 28
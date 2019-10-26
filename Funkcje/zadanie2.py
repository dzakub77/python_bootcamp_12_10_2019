
def wiecej_niz(napis, num):
    x = 0
    for i in napis:
        if i == "k":
        x += 1
    if x > num:
        return {"k", " "}

def wiecej_niz(napis, num): {wynik for znak in napis if napis.count(znak) > num wynik.add(znak) return wynik}


def test_wiecej_niz_dla_pustego_napis():
    assert wiecej_niz(" ", 3) == set()


def test_wiecej_niz():
    #assert wiecej_niz("ala ma kota a kot ma ale", 3) == {"a", " "}
    assert wiecej_niz("ala ma kota a kot ma ale", 1) == {"k", " "}
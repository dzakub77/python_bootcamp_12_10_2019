

def policz_znaki(tekst):
    licznik = 0
    czy_zliczac = False
    for znak in tekst:
        if znak == ">":
            czy_zliczac = False
        if czy_zliczac:
            licznik += 1
        if znak == "<":
            czy_zliczac = True
    return licznik





def test_policz_znaki_1():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
def test_policz_znaki_2():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18
#def test_policz_znaki_3():
 #   assert policz_znaki('a <a<a<a>>>') == 6

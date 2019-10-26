from geometry import figures

def test_pole_kwadratu():
    assert figures.pole_kwadratu(3) == 9


def test_pole_trojkata():
    assert figures.pole_trojkata(5, 3) == 7.5
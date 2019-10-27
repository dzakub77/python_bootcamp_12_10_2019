#Napisz funckje ktore
# policzy pole kwadratu
# policzy pole prostokata
# policzy pole trojkata
# policzy pole kola
# pozwoli na dodanie dwóch macierzy o jednakowych wymiarach -
# macierz - [[1, 3], [2, 5]

def pole_kwadratu(x):
    p = x**2
    return p
def test_pole_kwadratu():
    assert pole_kwadratu(3) == 9

def pole_prostokata(x, y):
    p = x * y
    return p
def test_pole_prostokata():
    assert pole_prostokata(3, 4) == 12

def pole_trojkata(a, h):
    p = 0.5 * a * h
    return p
def test_pole_trojkata():
    assert pole_trojkata(5, 3) == 7.5
from math import pi
def pole_kola(r):
    p = pi * r**2
    p = int(p)
    return p
def test_pole_kola():
    assert pole_kola(4) == 50


def dodanie_dwoch_macierzy(macierz1, macierz2):
    wynik = []
    for i_index, i in enumerate(macierz1):
        i_wynikowy = []
        for j_index, j in enumerate(i):
            i_wynikowy.append(j + macierz2[i_index][j_index])
        wynik.append(i_wynikowy)
    return wynik

def dodanie_dwoch_macierzy_with_zip(macierz1, macierz2):
    wynik = []
    for row_macierz1, row_macierz2 in zip(macierz1, macierz2):
        row = []
        for col_macierz1, col_macierz2 in zip(row_macierz1, row_macierz2):
            row.append(col_macierz1 + col_macierz2)
        wynik.append(row)
    return wynik


def test_dodanie_dwoch_macierzy():
    macierz1 = [[1, 3], [2, 4]]
    macierz2 = [[3, 4], [5, 6]]
    expected = [[4, 7], [7, 10]]
    assert dodanie_dwoch_macierzy(macierz1, macierz2) == expected

def test_dodanie_dwoch_macierzy_with_zip():
    macierz1 = [[1, 3], [2, 4]]
    macierz2 = [[3, 4], [5, 6]]
    expected = [[4, 7], [7, 10]]
    assert dodanie_dwoch_macierzy_with_zip(macierz1, macierz2) == expected
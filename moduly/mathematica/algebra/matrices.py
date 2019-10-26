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


if __name__ == "__main__":
    print(__file__)
    print(dir())
    print(globals())
    print(__name__)
    print("XXXXXXXXXXXXX")
# napisz tabliczke mnozenia 1-10

#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#for i in lista:
  #  print(f"{i:4}", end=" ")
#print()
#print()
#for i in lista:
  #  print(f"{i:2}", end="  ")
 #   for j in lista:
 #       print(f"{i*j:4}", end=" ")
 #   print()


#for index, element in enumerate(lista):
#	print(index, element)
#	print(lista[index])


#i = 0
#while i < len(lista1):
#    print( lista2[i]*lista1[i])
#    i += 1


macierz_a = [
    [1, 2, 3],
    [4, 5, 6]
]
macierz_b = [
    [5, 6, 7],
    [8, 9, 10]
]

wynik = []

for row_index, row in enumerate(macierz_a):
    row_wynikowy = []
    for col_index, col in enumerate(row):
        row_wynikowy.append(col + macierz_b[row_index][col_index])
    wynik.append(row_wynikowy)


i = 0
while i <len(macierz_a):
    wiersz_z_a = macierz_a[i]
    wiersz_z_b = macierz_b[i]
    j = 0
    row = []
    while j < len(wiersz_z_a):
        col_z_a = wiersz_z_a[j]
        col_z_b = wiersz_z_b[j]
        row.append(col_z_a + col_z_b)
        j += 1
    wynik.append(row)

    i += 1
print("x"*40)
print(wynik)



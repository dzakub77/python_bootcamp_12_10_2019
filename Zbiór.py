# set - zbiór


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#suma
print(A | B)
#rożnica
print(A - B)
print(B - A)

#czesc wspolna - koniunkcja
print(A & B)

#róznica symetryczna
print(A^B)

print(dir(A))

A.add(5)
print(A)

#z listy zrobic liste uniklana
lista = [1, 2, 3, 1, 2, 1, 2, 3]
print(lista(set(lista)))
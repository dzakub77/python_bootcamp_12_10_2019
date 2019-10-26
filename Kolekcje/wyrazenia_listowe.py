wynik = []
for i in range(1, 101):
    wynik.append(i**3)

print(wynik)


wynik = [i**3 for i in range(1, 101)]
wynik2 = {i**3 for i in range(1, 101)}

print(wynik)
print(wynik2)


#wynik = [i**3 for i in range(1, 101) if i % 7 == 0]   wszystkie podzielne przez 7


lista = ["aa", "aaaaa", "aaa", "aaaaaaa"]
print([len(x) for x in lista])

macierz = [[x*y for x in range(10)] for y in range(10)]
print(macierz)
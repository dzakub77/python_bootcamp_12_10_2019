"""Napisz program obliczajacy srednia wartosc z podanych przez uzytkownika liczb
Liczby przyjmuj z wykorzystaniem petli while i funkcji input
Pozwol na podanie maksymalnie 10 liczb
Dodatkowo wydrukuj informacje o minimalnej i maksymalnej wartosci
"""


proby = 0
suma = 0
list = []
while len(list) < 10:
    i = int(input("Podaj liczbe. Mozesz podac maksymalnie 10 liczb! "))
    list.append(i)
    print(list)

print("Suma: ", sum(list))
sr = sum(list) / len(list)
print("Średnia: ", sr)
print("Wartosc minimalna", max(list))
print("Wartosc minimalna", min(list))
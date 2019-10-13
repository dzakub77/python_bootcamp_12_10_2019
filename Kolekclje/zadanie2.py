"""Napisz program zliczajacy wystapienia liczb
dodatnich i ujemnych
parzystych i nieparzystych
w zadanej liscie

"""
list = [1, 4, -2, -6, 3, 7, 8]

for i in list:
    if i > 0:
        print("Liczby dodatnie", i)
print("\n")
for i in list:
    if i < 0:
        print("Liczby ujemne", i)
print("\n")
for i in list:
    x = i % 2
    if x == 0:
        print("Liczby przyste", i)
print("\n")
for i in list:
    x = i % 2
    if x != 0:
        print("Liczby nieparzyste", i)


#kalkulator
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in list1:
    x = int(input("Podaj liczbe: "))
    y = int(input("Podaj liczbe: "))
    t = int(input("Wybierz jakie działanie chcesz wykonac. 1(mnozenie, 2(dzielenie), 3(dodawanie), 4(odejmowanie)"))
    if t == 1:
        print(x*y)
    elif t == 2:
        print(x/y)
    elif t == 3:
        print(x+y)
    elif t == 4:
        print(x-y)








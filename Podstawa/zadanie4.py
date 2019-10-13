proby = 0
suma = 0
while True:
    i = input("Podaj liczbę, lub wpisz k żeby zakończyć: ")
    if i == "k":
        break
    i = int(i)
    suma = suma + i
    proby += 1
    sr = suma / proby
print(sr)

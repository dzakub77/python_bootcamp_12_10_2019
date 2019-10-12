# plansza 10 x 10

import random
DEBUG = True
skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)

gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)

min_i_po_wyl = abs(skarb_y - gracz_y) + abs(skarb_x - gracz_x)

if DEBUG:
    print("Pozycja gracza: ",gracz_x, gracz_y)
    print("Pozycja skarnu: ",skarb_x, skarb_y)
    print("Minimalna ilość ruchów: ",min_i_po_wyl)

proby = 0
while True:
    min_i_przed = abs(skarb_y - gracz_y) + abs(skarb_x - gracz_x)
    i = input("Ruszaj na poszukiwanie skarbu, możesz ruszać w dół(s), w góre(w), w lewo(a) i w prawo(d): ")
    if i == "w":
        gracz_y += 1
    elif i == "s":
        gracz_y -= 1
    elif i == "a":
        gracz_x -= 1
    elif i == "d":
        gracz_x += 1
    elif skarb_x == gracz_x and skarb_y == gracz_y:
        break
    min_i_po = abs(skarb_y - gracz_y) + abs(skarb_x - gracz_x)
    if gracz_y > 10 or gracz_y < 0 or gracz_x > 10 or gracz_x < 0:
        print("Wypadles poza plansze")
    if min_i_po < min_i_przed:
        print("Ciepło")
    else:
        print("zimno")
    proby += 1
    print("Pozycja gracza: ", gracz_x, gracz_y)
    print("Pozycja skarnu: ", skarb_x, skarb_y)
    if proby > 2 * min_i_po_wyl:
        skarb_x = random.randint(1, 10)
        skarb_y = random.randint(1, 10)
        min_i_po_wyl = abs(skarb_y - gracz_y) + abs(skarb_x - gracz_x)
        proby = 0
        print("Skarb zmienil swoje polozenie")
        print("Pozycja gracza: ", gracz_x, gracz_y)
        print("Pozycja skarnu: ", skarb_x, skarb_y)

print("Brawo udało ci się! Proby: ",proby)
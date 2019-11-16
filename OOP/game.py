"""
1. Stworz kalse Postac - niech ma atrybuty: imie, zycie, sila
2. Stworz klase Przedmiot - niech ma atrybuty: bonus_do_ataku, bonus_do_obrony, nazwa, miejsce
3  Postac ma atrybut atak wyliczony na podstawie sily i bonusow od przedmiotow
4. Stworz funckje obslugujaca gre
5. Powinna w niej byc jakas plansza o wymiarach dowolnych x, y
6. Na planszy moga pojawic sue jakies inne postace
7. Jak wejdziemy na pole z przedmiotem, o ile jest miejsce
8. Jak trafimy na inna postac, to wywiazuje sie walka
"""
import random


class Postac:
    def __init__(self, imie, zycie, sila):
        self.imie = imie
        self.zycie = zycie
        self.sila = sila
        self.ekwipunek = []

    @property
    def atak(self):
        base = self.sila + sum([x.bonus_do_ataku for x in self.ekwipunek])
        return int(base *random.random())

    def wez_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def obrazenia(self, sila):
        self.zycie -= sila

    @property
    def zyje(self):
        return self.zycie > 0


    def __str__(self):
        return f"{self.imie}, zyje={self.zyje}"

class Przedmiot:
    def __init__(self, nazwa, bonus_do_ataku, bonus_do_obrony, miejsce):
        self.bonus_do_ataku = bonus_do_ataku
        self.bonus_do_obrony = bonus_do_obrony
        self.nazwa = nazwa
        self.miejsce = miejsce

class Polozenie:

    def __init__(self, x, y, zasieg_x, zasieg_y):
        self.x = x
        self.y = y
        self.zasieg_x = zasieg_x
        self.zasieg_y = zasieg_y

    def __str__(self):
        return f"Pozycja x={self.x}, y={self.y}"

    def gora(self):
        self.y += 1
        if self.y > self.zasieg_y:
            print("Wypadles poza plansze")
            exit()
    def dol(self):
        self.y -= 1
        if self.y < 0:
            print("Wypadles poza plansze")
            exit()
    def prawo(self):
        self.x += 1
        if self.x > self.zasieg_x:
            print("Wypadles poza plansze")
            exit()
    def lewo(self):
        self.x -= 1
        if self.x < 0:
            print("Wypadles poza plansze")
            exit()


class Plansza:

    def __init__(self, gracz, bot, przedmiot, x=10, y=10):
        self.x = x  # wymiar planszy wzdluz osi x
        self.y = y
        self.gracz = gracz
        self.bot = bot
        self.przedmiot = przedmiot
        self.polozenie_gracza = Polozenie(random.randint(1, 10), random.randint(1, 10), x, y)
        self.polozenie_bota = Polozenie(random.randint(1, 10), random.randint(1, 10), x, y)
        self.polozenie_przedmiotu = Polozenie(random.randint(1, 10), random.randint(1, 10), x, y)

def gra():

    if self.polozenie_gracza
    while not hero1.zyje and hero2.zyje:
        obrazenia = hero1.atak
        print(f"{hero1.imie} zadaje obrazenia za {obrazenia}")
        hero2.obrazenia(obrazenia)
        if hero2.zyje:
            obrazenia = hero1.atak
            print(f"{hero2.imie} przezyl i oddaje za {obrazenia}")
            hero1.obrazenia(obrazenia)

    print(hero1, hero2)


hero1 = Postac("Superman", 200, 200)
hero2 = Postac("Hulk", 200, 200)
przedmiot = Plansza(hero1, hero1)
plansza = Plansza(hero1, hero2, przedmiot)
gra()
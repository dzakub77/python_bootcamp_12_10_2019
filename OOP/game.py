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
from faker import Faker
DEBUG = True
fake = Faker("pl_Pl")
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

    def __str__(self):
        return f"{self.nazwa} (+a: {self.bonus_do_ataku} +o: {self.bonus_do_obrony}) m: {self.miejsce}"

class Polozenie:

    def __init__(self, x, y, zasieg_x=10, zasieg_y=10):
        self.x = x
        self.y = y
        self.zasieg_x = zasieg_x
        self.zasieg_y = zasieg_y

    def __str__(self):
        return f"Pozycja x={self.x}, y={self.y}"

    def g(self):
        self.y += 1
        if self.y > self.zasieg_y:
            print("Wypadles poza plansze")
            exit()
    def d(self):
        self.y -= 1
        if self.y < 0:
            print("Wypadles poza plansze")
            exit()
    def p(self):
        self.x += 1
        if self.x > self.zasieg_x:
            print("Wypadles poza plansze")
            exit()
    def l(self):
        self.x -= 1
        if self.x < 0:
            print("Wypadles poza plansze")
            exit()

    def __eq__(self, other):
       # if self.x == other.x and self.y == other.y:
        #    retrun True
        #return False
        return self.x == other.x and self.y == other.y
class Plansza():

    def __init__(self, gracz: Postac, bot: Postac, przedmiot, x=10, y=10):
        self.x = x  # wymiar planszy wzdluz osi x
        self.y = y
        self.gracz = gracz
        self.bot = bot
        self.przedmiot = przedmiot
        self.polozenie_gracza = Polozenie(random.randint(1, 10), random.randint(1, 10), x, y)
        self.polozenie_bota = Polozenie(random.randint(1, 10), random.randint(1, 10), x, y)
        self.polozenie_przedmiotu = Polozenie(random.randint(1, 10), random.randint(1, 10), x, y)

    def ruch(self):
        if DEBUG:
            print(f"Twoje połozenie: {self.polozenie_gracza} ")
            print(f"Twoje bota: {self.polozenie_bota} ")
            print(f"Twoje przedmiotu: {self.polozenie_przedmiotu} ")
        kierunek = input("Podaj kierunek g, d, l, p: ")
        # if kierunek == "g":
        #     self.polozenie_gracza.gora()
        # elif kierunek == "d":
        #     self.polozenie_gracza.dol()
        # elif kierunek == "l":
        #     self.polozenie_gracza.lewo()
        # elif kierunek == "p":
        #     self.polozenie_gracza.prawo()

       # ruch = {
       #     'g': self.polozenie_gracza.gora,
       #     'd': self.polozenie_gracza.dol,
        #    'l': self.polozenie_gracza.lewo,
       #     'p': self.polozenie_gracza.prawo
       # }
        if hasattr(self.polozenie_gracza, kierunek):
            getattr(self.polozenie_gracza, kierunek)()
        else:
            print("Nie poprawna komenda")
        # ruch[kierunek]()



    def gra(self):
        while True:
            self.ruch()
            if self.polozenie_gracza == self.polozenie_bota:
                print(f"Spotkales wroga: {self.bot}\n\nwalka:\n ")
                while self.gracz.zyje and self.bot.zyje:
                    obrazenia = self.gracz.atak
                    print(f"{self.gracz.imie} zadaje obrażenia za {obrazenia}")
                    self.bot.obrazenia(obrazenia)
                    if self.bot.zyje:
                        obrazenia = self.gracz.atak
                        print(f"{self.bot.imie}  przeżył i oddaje za {obrazenia}")
                        self.gracz.obrazenia(obrazenia)
                print(self.gracz, self.bot)
            if self.polozenie_gracza == self.polozenie_przedmiotu:
                self.gracz.wez_przedmiot(self.przedmiot)
                self.polozenie_przedmiotu = Polozenie(-1, -1)
                print(f"{self.gracz.imie} przyjmuje {przedmiot} do ekwipunku")



hero1 = Postac("Superman", 200, 200)
bot = Postac(fake.name(), fake.random_int(), fake.random_int())
przedmiot = Przedmiot(fake.text(20), fake.random_int(), fake.random_int(), fake.random_int(1, 10))

plansza = Plansza(hero1, bot, przedmiot)
plansza.gra()

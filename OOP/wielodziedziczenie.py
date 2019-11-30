

class Osoba:
    def __int__(self, imie):
        self.imie = imie

class SuperSmart:
    def __init__(self):
        self.super_smart = True

    def calculate(self):
        print("Super calculations done!")


class SuperStrenght:
    def __init__(self):
        self.super_strenght = True

    def lift(self):
        print("heavy lifting done")

class Hero(Osoba, SuperSmart, SuperStrenght):
    def __init__(self, imie):
        super().__init__(imie)
        SuperSmart.__init__(self)
        SuperStrenght.__init__(self)



h = Hero("Kuba")
h.calculate()
h.lift()



class Osoba:
    def __init__(self, imie, rok_ur):
        self.imie = imie
        self.rok_ur = rok_ur

    @property # zamienia metode w atrybut
    def wiek(self):
        return 2019 - self.rok_ur

os1 = Osoba("Rafał", 1980)
print(os1.wiek())
print(os1.wiek)

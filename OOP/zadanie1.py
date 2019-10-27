

class Product:
    def __init__(self, przedmiot, ilosc, cena):
        self.przedmiot = przedmiot
        self.ilosc = ilosc
        self.cena = cena

    def print_info(self):
        return f'Przedmiot: "{self.przedmiot}", ilość: {self.ilosc}, cena: {self.cena} PLM'

    def __str__(self):
        return f'Przedmiot: "{self.przedmiot}", ilość: {self.ilosc}, cena: {self.cena} PLM'

    def __repr(self):
        return self.__str__()

p = Product("Woda", 1, 10.99)
print(f"Przedmiot {p.przedmiot}, ilość: {p.ilosc}, Cena: {p.cena} PLN")
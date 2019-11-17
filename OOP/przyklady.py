

# Terminologia
# Obiekt, typ, instancja = zbior, atrybut = zmienna, metoda = funkcja
# slowo kluczowe class a po nim nazwa klasy



class Osoba:
    gatunek = "Homo Sapiens" #atrybut klasowy



    def __init__(self, imie, wiek, wzrost):  #metoda specjalna
        self.imie = imie #atrybut instancji
        self.wiek = wiek
        self.wzrost = wzrost
        self.rok_ur = 2019 - wiek
        self.energia = 500

    def idz(self):
        print(f"{self.imie} idzie")
        self.energia -= 40

    def spij(self):
        print(f"{self.imie} śpi")
        self.energia += 30


os1 =Osoba("Kuba", 30, 182)
os1.idz()
print(os1.energia)
os1.spij()
print(os1.energia)
#os1.imie = "Kuba"
#os1.wiek = 30


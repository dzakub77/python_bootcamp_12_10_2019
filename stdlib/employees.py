
import json

try:
    with open("baza_danych.json") as f:
        employees = json.load(f)
        employees = [Employee.deserialize(**data)]
except FileNotFoundError:
    employees = []


class Employee:

    def __init__(self, imie, nazwisko, rok, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok = rok
        self.pensja = pensja

    def serialize(self):
        return {
        "imie": self.imie,
        "nazwisko": self.nazwisko,
        "rok": self.rok,
        "pensja": self.pensja
         }

    @staticmethod
    def deserialize(data):
        return Employee(**data)

data = {
        "imie": "Johny",
        "nazwisko": "Bravo",
        "rok": 222,
        "pensja": 11233123
         }


x = input("Co chcesz zrobić? [d - dodaj, w - wypisz] ")
if x == 'd':
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    rok = input("Rok urodzenia: ")
    pensja = input("Pensja: ")
    # e = {
    #     "imie": imie,
    #     "nazwisko": nazwisko,
    #     "rok": rok_ur,
    #     "pensja": pensja
    # }
    e = Employee(imie, nazwisko, rok, pensja)
    employees.append(e.serialize)
    with open("baza_danych.json", 'w') as f:
        json.dump(employees, f)


elif x == 'w':
    print("Pracownicy: \n")
    for id, e in enumerate(employees, start=1):
        print(f"- [{id} {e['imie']} {e['nazwisko']} - rok: {e['rok']}, pensja: {e['pensja']} PLN")
else:
    "Nie prawidłowa komenda."

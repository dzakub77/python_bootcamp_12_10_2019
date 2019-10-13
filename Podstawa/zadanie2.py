""" 1. Zapytaj uzytkownika o
miasto a,
miasto b,
odleglosc miedzy tymi miastami,
kosazt paliwa
spalanie na 100km
i oblicz koszt podrozy pomiedzy tymi miastami
Wyswietl odpowiedz ladnie sformatowana
"""

miasto_a = input("Jaka jest nazwa miasta a? ")
miasto_b = input("Jaka jest nazwa miasta b? ")
odleglosc = int(input("Jaka jest odleglosc pomiedzy tymi miastami: "))
spalanie = float(input("Jakie jest spalanie twojego samochodu: "))
paliwo = 4.50
print(f"Odległość pomiędzy miastem {miasto_a} a miastem {miasto_b} wynosi: ",odleglosc," km")
ilosc_paliwa = (odleglosc / 100) * spalanie
koszt = ilosc_paliwa * paliwo
print(f"Samochod na trasie", odleglosc," km, spalił",round(ilosc_paliwa, 2)," litrów paliwa")
print(f"\nPrzy cenie ",paliwo,"zł za litr benzyny, koszt podrózy wynosi: ",round(koszt, 2))



def nazwa_funkcji():     # definicja funkcji
    pass # nic sie nie dzieje

nazwa_funkcji # obiekt funkcji
nazwa_funkcji() # wywołanie funckji


def powitanie(imie):
    print(f"Hello {imie.upper()}")
    return 123        # bedzie zwracala jakas wartosc


def powitanie(imie):
    return f"Hello {imie.upper()}"

poczatek = powitanie("Kuba")


#globals() - slownik pokazujacy zasieg globalny
#locals() - slownik pokazujacy zasieg lokalny


def operacje(a, b, op):
    print(a + b, op)

operacje(1,2,3)

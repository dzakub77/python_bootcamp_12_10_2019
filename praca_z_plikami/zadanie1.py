from collections import defaultdict

from faker import Faker

# 1.
def numerowanie(nazwa):

    with open(nazwa) as f:
        for count, l in enumerate(f, start=1):
            print(count, l.rstrip())

#numerowanie("nowy_plik.txt")

# 2.

def nr_linii1(nazwa):
    with open(nazwa) as f:
         for c, line in enumerate(f, start=1):
             pass
    return c

def nr_linii2(nazwa):
    with open(nazwa) as f:
        licznik = 0
        for line in f:
            licznik += 1
    return licznik
print(nr_linii2("nowy_plik.txt"))

# 3.

def losowa_tresc(nazwa = "losowy.txt", n=1000):
    faker = Faker("pl_Pl")
    text = faker.text(n)
    with open(nazwa, 'w') as f:
        f.write(text)

losowa_tresc(n = 100000)

# 4.
def zlicz_znaki(text):
    zliczenia = defaultdict(int)
    znaki = set(text)
    znaki = znaki - set([" ", "\n"])
    for znak in znaki:
        zliczenia[znak] = text.count(znak)
    return zliczenia

def czestotliwosc_liter(nazwa):
    with open(nazwa) as f:
        text = f.read().lower()
        zliczenia = zlicz_znaki(text)
    return zliczenia

for litera, licznik in sorted(czestotliwosc_liter("losowy.txt").items(), key=lambda x: x[1], reverse=True):
    print(f"{litera}: {licznik}")

# 5.

def czestotliwosc_slow(nazwa):
    slowa = defaultdict(int)
    with open(nazwa) as f:
        text = f.read().lower()
        text = text.replace(".", "")
        text = text.split()
        for slowo in text:
            slowa[slowo] += 1
    return slowa

for litera, licznik in sorted(czestotliwosc_slow("losowy.txt").items(), key=lambda x: x[1], reverse=True):
    print(f"{slowo}: {licznik}")

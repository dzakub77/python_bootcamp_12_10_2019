

tekst = "Ala ma <kota> i tak dalej"
# print(napis.index(">") - napis.index("<) - 1)


licznik = 0
czy_zliczac = False
for znak in tekst:
    if znak == ">":
        czy_zliczac = False
    if czy_zliczac:
        licznik += 1
    if znak == "<":
        czy_zliczac = True

print(licznik)

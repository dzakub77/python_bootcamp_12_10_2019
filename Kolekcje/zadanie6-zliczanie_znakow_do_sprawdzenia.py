"""

w zadanym tekscie zlicz wystapienie kazdego znaku, nie uzywaj metody .count

dane przechowuj w slowniku

"""
napis = "To jest tekst"


liczniki = {}
for i in napis:
    liczniki[i] = liczniki.get(i, 0) + 1

print(liczniki)






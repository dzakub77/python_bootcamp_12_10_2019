"""
policz samogloski w podanym przez uzytkownika napisie
"""

napis = input("Wpisz jakis napis: ")
x = 0

for i in napis:
    if i in "aeiouy":
       x += 1



print("tyle razy ", x)
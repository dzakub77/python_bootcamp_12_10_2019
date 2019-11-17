
text = "ala ma kota"
def numerowanie(nazwa):
    with open(nazwa, 'w') as f:
        for l in nazwa:
            f.write(text+"\n")

print(numerowanie("nowy_plik.txt"))
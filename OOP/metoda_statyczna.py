

class Osoba:
    def __init__(self, name):
        self.name = name

class Grupa:
    def __init__(self):
        self.osoby = []

    def add_osoba(self, osoba):
        self.osoby.append(osoba)

    @staticmethod
    def utworz_z_osobami(osoby):
        gr = Grupa()
        for osoba in osoby:
            gr.add_osoba(osoba)
        return gr


osoby = [Osoba("Ralal"), Osoba("Ania"), Osoba("Adam")]
print(gr.osoby)
gr = Grupa.utworz_z_osobami(osoby)
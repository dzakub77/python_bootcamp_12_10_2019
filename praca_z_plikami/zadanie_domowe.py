
#zad 2 dziedziczenie

class Kontakt:

    def __init__(self, ulica, miasto):
        self.ulica = ulica
        self.miasto = miasto
    def show(self):
        return f"adres: {self.ulica}, {self.miasto}"


class Notebook:
    def __int__(self):

    def add(self,


def test_notebook():
    notes = Notebook()
    notes.add('Ala', 'ala@wp.pl', 'Dziwna 15', 'Pacanów')
    notes.add('Robert', 'robert@gmail.com', 'Królewska 27', 'Warszawa')
    assert notes.show('Ala') == '''Ala, email: ala@wp.pl
adres: Dziwna 15, Pacanów'''
    assert notes.show('Robert') == '''Robert, email. robert@gmail.com
adres: Królewska 27, Warszawa'''
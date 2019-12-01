

dane = {'login': 'admin', 'haslo': '123'} # ** login = 'admin, haslo = '123'
lista = ["admin", "1234"] # * 'admin', '1234'
 def zaloguj(login, haslo): #zmienne pozycyjne
    print("Zalogowany")

zaloguj("admin", "123")
zaloguj(login="admin", haslo="123")

zaloguj(dane['login'], dane['haslo'])
zaloguj(**dane) # biora sobie klucz z danych

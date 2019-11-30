import json
import requests
api = requests.get('http://api.nbp.pl/api/exchangerates/tables/A?format=json')
def wypisz_waluty(kursy):
    rates = kursy[0]['rates']
    for rate in rates:
        print(rate['code'])

def kurs_dla_waluty(kursy, waluta):
    rates = kursy[0]['rates']
    for rate in rates:
        if rate['code'] == waluta:
            return rate['mid']

if api.status_code == 200:
    api = api.json()
    wypisz_waluty(api)
# with open('api.json') as f:
#     api = json.load(f)



waluta = input("Dla jakiej waluty sprawdzic? ")
print(kurs_dla_waluty(api, waluta))


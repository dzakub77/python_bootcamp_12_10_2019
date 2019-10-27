
def nowa_funckja(func):
    def wrapper(*args, **kwargs):
        print("To jest powitanie")
        result = func(*args, **kwargs)
    return result

@nowa_funckja               # powitanie = nowa_funckja(powitanie)
def powitanie():
    print("Hello")
@nowa_funckja                  # be_awesome = nowa_funckja(be_awesome)
def be_awesome(name):
    print(f"Yo {name}. Be awesome!")

powitanie()
be_awesome("Kuba")

#  'ala ma kota'

# @bold
# '<b>Ala ma kota</b>'
# @italic
# '<i>Ala ma kota</i>'
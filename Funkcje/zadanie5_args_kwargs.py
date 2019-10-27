
def cena(*args, **kwargs):
    text = "\n".join(args)
    for k, v in kwargs.items():
        text = text.replace("$"+k, str(v))
    return text

cena("koszt $cena PLN", "koszt $cena brutto", cena=10)









def test_cena():
    assert cena("koszt $cena PLN", "koszt $cena brutto", cena=10) == "koszt 10 PLN\nkwota 10 brutto"
   # assert cena("koszt $cena PLN", "koszt $cena brutto", "kwota vat $vat %" cena=10) == "koszt 10 PLN\nkwota 10 brutto"



#"a$bc".replace("$b", "12")
#"s".join(lista)
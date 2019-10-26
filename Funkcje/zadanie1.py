def czy_jest_pierwsza(num):
    """

    :param num int:
    :return: bool
    """
    if num % 2 == 0 or num % 3 == 0 or num % 4 == 0 or num % 5 == 0:
        return False  #print(f"{num} nie jest liczba pierwsza")
    else:
        return True #print(f"{num} jest liczba pierwsza")


def test_czyjestpierwsza():


    assert czy_jest_pierwsza(7) == True
    assert czy_jest_pierwsza(17) == True

def test_czyniejestpierwsza():
    assert czy_jest_pierwsza(10) == False
    assert czy_jest_pierwsza(8) == False
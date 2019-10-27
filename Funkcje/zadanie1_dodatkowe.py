def liczby(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > b and c > a:
        return c

print(liczby(10, 20 ,5))

def test_liczby():
    assert liczby(10, 20 ,5) == 20
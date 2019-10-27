def suma(iterable):
    y = []
    if isinstance(iterable, dict):
        iterable = iterable.values()
    for i in iterable:
        if isinstance(i, int):
            y.append(i)
        else:
            try:
                y.append(i)
            except ValueError:
                pass
    x = sum(y)
    return x

def test_suma():
    a = [1, 2, 3, 4, "a", "g"]
    b = [1, 2, 3, "5"]
    c = {'a': 10, 'b': 20}
    d = {'a': '10', 'b': 'xx'}
    assert suma(a) == 10
    assert suma(b) == 6
    assert suma(c) == 30
    assert suma(d) == 10
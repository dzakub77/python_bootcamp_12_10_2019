
#def incrementator(i):
#    print(i)
 #   incrementator(i + 1)

#incrementator(1)


def rekurencja(i):
    x = 1
    for j in range(1, i+1):
        x = x* j
    return x

rekurencja(2)



def test_rekurencja():
    assert rekurencja(5) == 120
    assert rekurencja(0) == 1
    assert rekurencja(2) == 2
    assert rekurencja(3) == 6
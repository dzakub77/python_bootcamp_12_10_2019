from math import sqrt
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y)
        return result

    def __sub__(self, other):
        result = Vector(self.x - other.x, self.y - other.y)
        return result

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y


    def __rmul__(self, other):
        return self.__mul__(other)


    def __gt__(self, other):
        # self_len = sqrt(self.x**2 + self.y**2)
        # other_len = sqrt(other.x ** 2 + other.y ** 2)
        # return self_len > other_len
        return self.dlugosc() > other.dlugosc()
    def dlugosc(self):
        return sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return f"Vector (x={self.x}, y={self.y})"


def test_add_vevtors():
    v1 = Vector(1, 3)
    v2 = Vector(4, 7)
    result = v1 + v2
    assert result.x == 5
    assert result.y == 10

def test_sub_vevtors():
    v1 = Vector(1, 3)
    v2 = Vector(4, 7)
    result = v1 - v2
    assert result.x == -3
    assert result.y == -4

def test_mul_vevtors():
    "mnoæenie skalarne: v1 = a1, b1, v2=a2, b2 v1*v2 = a1*a2 + b1*b2"
    v1 = Vector(1, 3)
    v2 = Vector(4, 7)
    result = v1 * v2
    assert result == 25
def test_mul_by_integer():
    v = Vector(2, 3)
    result = v * 5
    assert result.x == 10
    assert result.y == 15

def test_dlugosc_vevtors():
    v1 = Vector(1, 1)
    v2 = Vector(4, 4)
    assert v2 > v1

def test_vector_str():
    v1 = Vector(1, 1)
    assert str(v1) == "Vector (x=1, y=1)"
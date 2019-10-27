

def palindrom(napis):
    napis = napis.lower()
    x = napis[::-1]
    y = x[::-1]
    if y == napis:
        return True

def is_palindrom(napis):
    napis = napis.lower()
    left_position = 0
    right_position = len(napis) - 1

    while right_position > left_position:
        if not napis[left_position] == napis[right_position]:
            return False
        left_position += 1
        right_position -= 1
    return True

def test_palindrom():
    assert palindrom("ala") == True

def test_is_palindrom():
    assert is_palindrom("ala") == True
def pandgram(napis):
    p = "abcdefghijklmnopqrstuvwxyz"
    for i in p or a:
        if i not in napis:
            return False
    return True
polish_alphabet = "ąęćńóśżźł" + string.ascii_lowercase.replace("x", "").replace("v", "").replace("q", "")

def test_pandgram():
    assert pandgram('The quick brown fox jumps over the lazy dog') == True
    assert pandgram('Ala ma kota') == False
    assert pandgram('Śnij formę klech z wag bądź żółć pustyń' ) == True
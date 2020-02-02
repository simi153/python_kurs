def is_anagram(text1, text2):
    text1 = sorted(list(text1.lower()))
    # text1.sort()
    text2 = sorted(list(text2.lower()))
    # text2.sort()
    if text1 == text2:
        return True
    else:
        return False


def test_is_anagram():
    assert is_anagram("Tokyo", "Kyoto") == True
    assert is_anagram("Anna", "Boba") == False
    assert is_anagram("AnnaKowalska", "Bob") == False
    assert is_anagram("Bob", "Anna kowalska") == False

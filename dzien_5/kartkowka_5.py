def is_anagram(text1, text2):
    text1 = sorted(list(text1.lower()))
    text2 = sorted(list(text2.lower()))
    return text1 == text2


def test_is_anagram():
    assert is_anagram("typhoon", "opython") is True
    assert is_anagram("Alice", "Bob") is False

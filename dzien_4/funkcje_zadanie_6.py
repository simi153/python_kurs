import string



def palindrome(text):
    text = text.lower()
    for s in string.punctuation + string.whitespace:
        text=text.replace(s,"")
    return text == text[::-1]


def test_palindrome():
    assert palindrome("kajak") is True
    assert palindrome("alab") is False
    assert palindrome("kajak,kajak") is True
    assert palindrome("A to idiota") is True

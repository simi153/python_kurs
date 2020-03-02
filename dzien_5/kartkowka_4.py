def double_letters(text):
    for index in range(len(text) - 1):
        if text[index + 1] == text[index] and text[index].isalnum():
            return True
        else:
            continue
    return False


def test_double_letters():
    assert double_letters("ala") is False
    assert double_letters("Hello") is True
    assert double_letters("abc") is False
    assert double_letters("nono") is False
    assert double_letters("double let ters") is False

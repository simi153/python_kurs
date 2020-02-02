def double_letters(text):
    for i in range(len(text) - 1):
        if text[i] == text[i + 1] and text[i].isalnum():
            return True
    return False


def test_double_letters_word():
    assert double_letters("ala") == False
    assert double_letters("al la") == False
    assert double_letters("alla") == True
    assert double_letters("nono") == False


def test_double_letters_empty_string():
    assert double_letters("") == False


def test_double_letters_only_white_space():
    assert double_letters("     ") == False

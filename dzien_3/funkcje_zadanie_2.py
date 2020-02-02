def mid(napis):
    if len(napis) % 2 != 0:
        index = len(napis) // 2
        return napis[index]
    else:
        return ""

def test_mid_without_middle_letter():
    assert mid("aabbcc") == ""
def test_mid_with_middle_letter():
    assert mid("abc") == "b"
    assert mid("abcabcd") == "a"
    assert mid("doremifasol") == "i"
def test_mid_empty_string():
    assert mid("") == ""


def only_ints(n1, n2):
    if type(n1) == int and type(n2) == int:
        return True
    else:
        return False


def test_only_ints():
    assert only_ints(1, 2) is True
    assert only_ints(3.5, 6) is False
    assert only_ints("1", 2) is False
    assert only_ints(1, True) is False

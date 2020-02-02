def only_ints(l1, l2):
    if type(l1) == int and type(l2) == int:
        return True
    else:
        return False


def test_only_ints_both_ints():
    assert only_ints(1, 2) == True


def test_only_ints_one_int():
    assert only_ints("test", 2) == False
    assert only_ints("", 1) == False
    assert only_ints(1, "2") == False
    assert only_ints(1, True) == False


def test_only_ints_no_ints():
    assert only_ints(True, False) == False
    assert only_ints(True, True) == False


def test_only_ints_number_string():
    assert only_ints("1", "2") == False

def div(l1, l2):
    return not l1 % l2

def div2(l1,l2=2):
    return not l1 % l2

def test_div():
    assert div(10, 5) is True
    assert div(10, 3) is False

def test_div2():
    assert div2(10) is True
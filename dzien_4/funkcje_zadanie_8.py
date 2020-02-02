def up_down(number):
    return number-1,number+1

def test_up_down():
    assert up_down(5) == (4,6)
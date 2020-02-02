def silnia(n):
    if n==0:
        return 1
    elif n>0:
        return n*silnia(n-1)
    else:
        return("Bledna wartosc")

def test_silnia():
    assert silnia(4) == 24
    assert silnia(5) == 120
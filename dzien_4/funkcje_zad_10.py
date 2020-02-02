def policz_znaki(napis, znak1="<", znak2=">"):
    wynik = 0
    zliczaj = False
    poziom=0
    for znak in napis:
        if znak == znak1:
            poziom+=1
        elif znak == znak2:
            poziom-=1
        else:
            wynik += poziom
    return wynik

def test_policz_znaki():
    assert policz_znaki("ala ma <kota> a kot ma ale") == 4
    assert policz_znaki("ala [kota [a kot]] ma [ale]", "[", "]") == 18
    assert policz_znaki("a <a<a<a>>>") == 6

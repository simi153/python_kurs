def policz_znaki(napis,*znak):
    licznik=0
    if znak:
        pocz=napis.index(znak[0])
        koniec=napis.index(znak[1])
    else:
        pocz = napis.index("<")
        koniec = napis.index(">")
    for i in range(pocz+1,koniec):
        licznik+=1
    print(licznik)

policz_znaki("ala ma <kota> a kot ma ale")
policz_znaki("ala [kota [a kot]] ma [ale]","[","]")
policz_znaki("a <a<a<a>>>")
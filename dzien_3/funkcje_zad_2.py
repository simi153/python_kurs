def wiecej_niz(tekst, liczba):
    litery = {}
    for litera in tekst:
        litery[litera] = litery.get(litera, 0) + 1

    for k, v in litery.items():
        if v >= liczba:
            print(f"{k} - {v}")


wiecej_niz("ala ma ota, a kot ma ale", 2)

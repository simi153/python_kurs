def czy_jest_pierwsza(liczba):
    licznik = 0
    for i in range(liczba + 1):
        if liczba % (i+1) == 0:
            licznik += 1
    if licznik > 2:
        return False
    else:
        return True


print(czy_jest_pierwsza(113))

from random import randint


def check(maszty, poz_x, poz_y, kierunek):
    zbior = [1, 2, 3, 4, 5, "1", "2", "3", "4", "5"]
    x = poz_x
    y = poz_y
    puste = False
    for i in range(maszty):
        if kierunek == 4 and 0 <= (poz_y + 1) - maszty < poz_y + 1:
            y = poz_y - i
        elif kierunek == 2 and (poz_x + 1) + maszty <= 9 and poz_x > poz_x - maszty:
            x = poz_x + i
        elif kierunek == 6 and 9 >= (poz_y + 1) + maszty > poz_y + 1:
            y = poz_y + i
        elif kierunek == 8 and (poz_x + 1) - maszty >= 0 and poz_x < poz_x + maszty:
            x = poz_x - i
        else:
            return puste
        try:
            if plansza[x][y + 1] in zbior or plansza[x][y - 1] in zbior or plansza[x - 1][y - 1] in zbior or \
                    plansza[x + 1][y - 1] in zbior or plansza[x + 1][y] in zbior or plansza[x - 1][y] in zbior or \
                    plansza[x + 1][y + 1] in zbior or plansza[x - 1][y + 1] in zbior or plansza[x][y] in zbior:
                return False
            else:
                puste = True
        except:
            return False
    return puste


def drukuj_plansze(plansza):
    print("    ", end="")
    for i in range(10):
        print(f"{chr(65 + i):2s}", end=" ")
    print()
    for i in range(10):
        print(f"{str(i + 1):2s}", end="  ")
        for j in range(10):
            print(f"{str(plansza[i][j]):2s}", end=" ")
        print()


def los_kierunku():
    kierunek = 1
    while kierunek % 2 != 0:
        kierunek = randint(2, 8)
    return kierunek


def masztowiec(maszty):
    sukces = False
    poz_x = randint(0, 9)
    poz_y = randint(0, 9)

    kierunek = los_kierunku()
    while not sukces:
        try:
            if check(maszty, poz_x, poz_y, kierunek):
                for i in range(maszty):
                    if kierunek == 4:
                        plansza[poz_x][poz_y - i] = maszty
                        sukces = True
                    elif kierunek == 6:
                        plansza[poz_x][poz_y + i] = maszty
                        sukces = True
                    elif kierunek == 2:
                        plansza[poz_x + i][poz_y] = maszty
                        sukces = True
                    elif kierunek == 8:
                        plansza[poz_x - i][poz_y] = maszty
                        sukces = True
            else:
                poz_x = randint(0, 9)
                poz_y = randint(0, 9)
        except:
            continue


plansza = [[0] * 10 for i in range(10)]

for i in range(10):
    for j in range(10):
        plansza[i][j] = "-"

masztowiec(4)
masztowiec(3)
masztowiec(3)
masztowiec(2)
masztowiec(2)
masztowiec(2)
masztowiec(1)
masztowiec(1)
masztowiec(1)
masztowiec(1)

print()
drukuj_plansze(plansza)

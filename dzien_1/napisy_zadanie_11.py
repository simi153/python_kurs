x = int(input("Pozycja X: "))
y = int(input("Pozycja Y: "))

if y > 100 or x > 100 or y < 0 or x < 0:
    print("Poza plansza")
else:
    if x <= 10:
        if y < 10:
            print("Lewy Dolny Rog")
        elif y > 10 and y < 90:
            print("Lewa krawedz")
        else:
            print("Lewy gorny rog")
    elif x > 10 and x < 90:
        if y < 10:
            print("Dolna krawedz")
        elif y < 90:
            print("Centrum")
        else:
            print("Gorna krawedz")
    elif x >= 90:
        if y < 10:
            print("Prawy dolny rog")
        elif y < 90:
            print("Prawa krawedz")
        else:
            print("Prawa gorna krawedz")
import random

p_x = random.randint(1, 10)
p_y = random.randint(1, 10)
s_x = random.randint(1, 10)
s_y = random.randint(1, 10)
print(f"Skarb: ({s_x},{s_y})")
print(f"Gracz: ({p_x},{p_y})")
odl_przed = abs(s_x - p_x) + abs(s_y - p_y)
min_krok = odl_przed
krok = 0
while p_x >= 1 and p_x <= 10 and p_y >= 1 and p_y <= 10:
    odl_przed = abs(s_x - p_x) + abs(s_y - p_y)
    polecenie = input("W ktora strone chcesz isc: ")

    if polecenie == "g" or polecenie == "w":
        p_y += 1
    elif polecenie == "p" or polecenie == "d":
        p_x += 1
    elif polecenie == "d" or polecenie == "s":
        p_y -= 1
    elif polecenie == "l" or polecenie == "a":
        p_x -= 1
    else:
        print("Nie znam takiego polecenia.")
    print(f"Gracz: ({p_x},{p_y})")
    if p_x < 1 or p_x > 10 or p_y < 1 or p_y > 10:
        print("Wypadles poza plansze!")
        break

    odl_po = abs(s_x - p_x) + abs(s_y - p_y)
    if odl_po == 0:
        print("Wygrales!")
        break
    krok += 1
    if krok > min_krok * 2:
        s_x = random.randint(1, 10)
        s_y = random.randint(1, 10)
        odl_przed = abs(s_x - p_x) + abs(s_y - p_y)
        krok = 0
        print("Umieszczam skarb w nowym miejscu")
    else:
        if random.randint(1, 5) != 1:
            if odl_po < odl_przed:
                print("Cieplo")
            else:
                print("Zimno")

print("\n\nKoniec")

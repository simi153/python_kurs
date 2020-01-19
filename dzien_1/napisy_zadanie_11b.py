x = int(input("Podaj pozycje X: "))
y = int(input("Podaj pozycje Y:"))
#komentarz

if x<0 or x>100 or y<0 or y>100:
    print("Poza plansza")
elif x<10 and y<10:
    print("LG")
elif x<10 and y>90:
    print("LG")
elif x>90 and y<10:
    print("PD")
elif x>90 and y>90:
    print("PG")
elif x<10:
    print("LK")
elif x>90:
    print("PK")
elif y<10:
    print("DK")
elif y>90:
    print("GK")
else:
    print("Centrum")
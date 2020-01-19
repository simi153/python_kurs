liczby = []
while len(liczby) < 10:
    polecenie = input("Podaj iczbe: ")
    if polecenie == "k":
        break
    try:
        liczby.append(int(polecenie))
    except ValueError:
        print("Bledna liczba")

srednia = sum(liczby) / len(liczby)
print(f"Srednia: {srednia:.2f}")

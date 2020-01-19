liczba_min = None
liczba_max = None

while (True):
    liczba = input("Podaj liczbe, badz koniec by zakonczyc: ")
    if liczba == "koniec":
        break
    try:
        liczba = float(liczba)
        if liczba_min is None or liczba < liczba_min:
            liczba_min = liczba
        elif liczba_max is None or liczba > liczba_max:
            liczba_max = liczba
    except:
        print("Wprowadz poprawna liczbe")
if liczba_min is None:
    print("Brak liczb")
else:
    print(f"Minimum: {liczba_min}")
    print(f"Maximum: {liczba_max}")

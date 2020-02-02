unikalne = set()
liczba = int(input("Podaj liczbe calkowita [0] by zakonczyc: "))
while liczba != 0:
    unikalne.add(liczba)
    liczba = int(input("Podaj liczbe calkowita [0] by zakonczyc: "))

parzyste = set(range(0,101,2))

print(f"Liczba unikalnych: {len(unikalne)}, parzyste w zakresie 0-100: {len(unikalne & parzyste)}")

pierwsza_liczba = int(input("Podaj pierwsza liczbe: "))
druga_liczba = int(input("Druga liczba: "))
operacja = input("Rodzaj operacji: ")

if operacja == "+":
    print(f"Wynik dodawania: {pierwsza_liczba+druga_liczba}")
elif operacja == "-":
    print(f"Wynik odejmowania: {pierwsza_liczba - druga_liczba}")
elif operacja == "*":
    print(f"Wynik mnozenia: {pierwsza_liczba * druga_liczba}")
elif operacja =="/":
    #ask for permission
    if druga_liczba == 0:
        print("Nie potrafie dzielic przez 0")
    else:
        print(f"Wynik dzielenia: {pierwsza_liczba / druga_liczba}")
    ## beg for forgivenes
    # try:
    #     print(f"Wynik dzielenia: {pierwsza_liczba / druga_liczba}")
    # except ZeroDivisionError:
    #     print("Nie potrafie dzielic przez 0")
else:
    print("Nieznana operacja")

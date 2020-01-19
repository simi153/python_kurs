napis = input("Wprowadz napis: ")
poczatek = napis.index("<")
koniec = napis.index(">")
print("Liczba znakw miedzy nawiasami <> wynosi: ", koniec - poczatek - 1)

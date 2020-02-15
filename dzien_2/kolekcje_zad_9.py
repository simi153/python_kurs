owoce = {"Pomarancz": 4, "Jablko": 2, "Kiwi": 4, "Arbuz": 3.5, "Mandarynki": 6.99, "Banan": 4.2}

# for owoc in owoce:
#     print(f"{owoc}: {owoce[owoc]} zł/kg")

for owoc,cena in owoce.items():
    print(f"{owoc}: {cena} zł/kg")

produkt = ""
print()
while owoce.get(produkt) == None:
    produkt = input("Co chcesz kupic: ").capitalize()

waga = float(input("Podaj wagę: ").replace(",", "."))
cena = owoce[produkt] * waga
print(f"Cena za {waga}kg {produkt} wynosi: {cena:.2f}zł")

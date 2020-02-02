produkty = {
    "Pomarancz": 4,
    "Jablko": 2,
    "Kiwi": 4,
    "Arbuz": 3.5,
    "Mandarynki": 6.99,
    "Banan": 4.2
}
produkty_w = {
    "Pomarancz": 1,
    "Jablko": 2,
    "Kiwi": 7,
    "Arbuz": 0,
    "Mandarynki": 12,
    "Banan": 2
}
sciezka = ""
while sciezka != "k":
    sciezka = input("Zakup [z], Magazyn [m] Koniec [k]: ").lower()

    if sciezka == "z":
        print("Produkty w magazynie: ")
        for owoc, cena in produkty.items():
            print(f"\t{owoc}: {cena} zł/kg - [{produkty_w[owoc]}]kg")
        produkt = ""
        print()
        while produkty.get(produkt) == None:
            produkt = input("Co chcesz kupic: ").capitalize()
        if produkty_w[produkt] == 0:
            print(f"Brak [{produkt}] na stanie.")
            continue
        else:
            waga = float(input("Podaj wagę: ").replace(",", "."))
            while waga > produkty_w[produkt]:
                print("Brak wystarczajacej ilości w magazynie.")
                waga = float(input("Podaj wagę: ").replace(",", "."))
            cena = produkty[produkt] * waga
            print(f"Cena za {waga}kg {produkt} wynosi: {cena:.2f}zł")
    elif sciezka == "m":
        prod = input("Jaki produkt chcesz dodac/zmienic: ").capitalize()
        waga = int(input(f"ile dodajesz [{prod}]: "))
        cena = input("Podaj cene produktu: ")
        produkty_w[prod] = produkty_w.get(prod, 0) + waga
        if cena:
            produkty[prod] = float(cena.replace(",", "."))
    elif sciezka == "k":
        break

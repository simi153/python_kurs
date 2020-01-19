miasto_a = input("Miasto A: ")
miasto_b = input("Miasto B: ")

dystans = float(input(f"Dystans na trasie {miasto_a} - {miasto_b}: "))
cena_paliwa = float(input("Cena paliwa: "))
spalanie = float(input ("Spalanie na 100 km: "))

koszt_przejazdu =  round(((dystans/100)*spalanie)*cena_paliwa,2)
print(f"Koszt przejazdu na trasie {miasto_a} - {miasto_b} wynosi: {koszt_przejazdu} PLN")

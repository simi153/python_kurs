try:
	liczba = int(input("Podaj liczbe: "))
	wynik = liczba%2==0 and liczba%3==0 and liczba>10 and liczba==7
	print(wynik)
	print(f"Czy {liczba} jest podzielne przez 2: {(liczba%2)==0}")
	print(f"Czy {liczba} jest podzielne przez 3 i wieksze od 10: {(liczba%3)==0 and liczba>10}")
	print(f"Czy {liczba} jest to 7: {liczba==7}")
except:
	print("Blad")
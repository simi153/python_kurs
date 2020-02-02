wynik=[]
for el in range(10):
    if el % 2 == 0:
        wynik.append(el**3)

print(wynik)

print([el**3 for el in range(10) if el % 2 == 0])
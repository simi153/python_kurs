lista = [-10, 5, -5, 15, 20, -15, 0, 7]
dodatnie=0
ujemne=0
for liczba in lista:
    if liczba<0:
        ujemne+=1
    elif liczba>0:
        dodatnie+=1

print(f"Dodatnie: {dodatnie} | Ujemne: {ujemne}")
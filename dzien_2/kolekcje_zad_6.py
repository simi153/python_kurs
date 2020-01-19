lista = [-10, 5, -5, 15, 20, -15, 0, 7]
maximum = max(lista)
minimum = min(lista)
poz_min = lista.index(minimum)
poz_max = lista.index(maximum)

lista[poz_max] = minimum
lista[poz_min] = maximum

assert lista == [-10, 5, -5, 15, -15, 20, 0, 7]

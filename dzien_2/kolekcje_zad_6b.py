lista = [-10, 5, -5, 15, 20, -15, 0, 7]
i_min, i_max = 0, 0

for index, value in enumerate(lista):
    if value < lista[i_min]:
        i_min = index
    if value > lista[i_max]:
        i_max = index

lista[i_min], lista[i_max] = lista[i_max], lista[i_min]

# minimum = lista[0]
# maximum = lista[0]
#
# for liczba in lista:
#     if liczba < minimum:
#         minimum = liczba
#     elif liczba > maximum:
#         maximum = liczba
# index_max = lista.index(maximum)
# index_min = lista.index(minimum)
#
# lista[index_max], lista[index_min] = lista[index_min], lista[index_max]

assert lista == [-10, 5, -5, 15, -15, 20, 0, 7]

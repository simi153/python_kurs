liczby = [9, 1, 6, 8, 4, 1, 3, 2, 0]

for l in range(len(liczby) - 1):
    i_min = l
    for i in range(l + 1, len(liczby)):
        if liczby[i] < liczby[i_min]:
            i_min = i
    liczby[l], liczby[i_min] = liczby[i_min], liczby[l]

print(liczby)

def tabliczka(x,y):
    wynik=[]
    for i in range(x):
        row=[]
        for j in range(y):
            row.append(i*j)
        wynik.append(row)
    return wynik

def tabl2(x,y):
    return [[i*j for i in range(x)] for j in range(y)]
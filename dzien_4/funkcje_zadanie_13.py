def select(lista, func):
    result=[]
    for el in lista:
        if func(el):
            result.append(el)
    return result

# def select(lista,func):
#     return [x for x in lista if func(x)]

def test_select():
    lista=[1,3,9,12,8,4,16]
    assert select(lista, lambda x: x % 2 == 0) == [12, 8, 4, 16]
    assert select(lista, lambda x: x > 10) == [12, 16]

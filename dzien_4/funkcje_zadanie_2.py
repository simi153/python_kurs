def flatten(*listx):
    if len(listx) == 1:
        listx = listx[0]
    list2 = []
    for i in listx:
        list2.extend(i)
    return list2


def test_flatten():
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten([[1, 2], [3, 4], [4, 5], [5, 6]]) == [1, 2, 3, 4, 4, 5, 5, 6]
    assert flatten([[1, 2]]) == [1, 2]
    assert flatten() == []

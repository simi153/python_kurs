def largest_difference(lista):
    return max(lista) - min(lista)


def test_largest_difference():
    assert largest_difference([2,5,123,-5]) == 128

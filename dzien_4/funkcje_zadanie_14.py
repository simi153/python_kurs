def przytnij(data, start, stop):
    result = []
    dodawaj=False
    for el in data:
        if start(el):
            dodawaj=True
        if dodawaj:
            result.append(el)
        if stop(el):
            return result
    return result


def test_przytnij():
    data = [1, 2, 3, 4, 5, 6, 7]
    assert przytnij(data, lambda x: x > 3, lambda x: x == 6) == [4, 5, 6]
    assert przytnij(data, lambda x: x >= 3, lambda x: x == 7) == [3, 4, 5, 6, 7]

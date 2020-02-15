def capital_indexes(text):
    indexes = []
    for k, v in enumerate(text):
        if v.isupper():
            indexes.append(k)
    return indexes


def test_capital_indexes():
    assert capital_indexes("HeLlO") == [0, 2, 4]
    assert capital_indexes("hello") == []
    assert capital_indexes("12345") == []


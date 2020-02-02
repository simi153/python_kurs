# Npisz funkcje capital letter, która
# 1) przyjmie 1 argument - napis
# 2) zwróci indexy wielkich liter

def capital_letters(napis):
    duze_litery = []
    for i, v in enumerate(napis):
        if v.isupper():
            duze_litery.append(i)
    return duze_litery

def test_capital_letters_all_small_letters():
    assert capital_letters("hello") == []
def test_capital_letters_small_big_letters():
    assert capital_letters("HeLlO") == [0, 2, 4]


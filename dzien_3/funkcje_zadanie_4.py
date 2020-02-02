import random


def random_number():
    return random.randint(1, 101)


# print(random_number(25))
def test_random_number_with_seed():
    random.seed(0)
    assert random_number() == 50
    random.seed(1)
    assert random_number() == 18
    random.seed(25)
    assert random_number() == 49

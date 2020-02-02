def largest_difference(*args):
    if args:
        return max(args) - min(args)


def test_largest_difference():
    assert largest_difference(1, 2, 3, 10) == 9
    assert largest_difference(1, 2, -10, 10) == 20
    assert largest_difference(1, 2, -10, 10) == 20
    assert largest_difference() is None

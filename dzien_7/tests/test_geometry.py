from mathematica.geometry.figures import square_area, triangle_area


def test_square_area():
    assert square_area(2) == 4
    assert square_area(5) == 25


def test_triangle_area():
    assert triangle_area(2, 4) == 4
    assert triangle_area(3, 6) == 9

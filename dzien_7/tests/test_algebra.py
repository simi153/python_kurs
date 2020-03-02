from mathematica.algebra import matrices

matrice_1 = [[1, 5], [-2, 7]]
matrice_2 = [[11, 3], [-3, 9]]


def test_add_matrices():
    matrice_1 = [[1, 5], [-2, 7]]
    matrice_2 = [[11, 3], [-3, 9]]
    assert matrices.add_matrices(matrice_1, matrice_2) == [[12, 8], [-5, 16]]
    matrice_1 = [[1, 5, 5], [-2, 7, 0]]
    matrice_2 = [[11, 3, 5], [-3, 9, 8]]
    assert matrices.add_matrices(matrice_1, matrice_2) == [[12, 8, 10], [-5, 16, 8]]


def test_sub_matrices():
    matrice_1 = [[1, 5], [-2, 7]]
    matrice_2 = [[11, 3], [-3, 9]]
    assert matrices.sub_matrices(matrice_1, matrice_2) == [[-10, 2], [1, -2]]
    matrice_1 = [[1, 5, 5], [-2, 7, 0]]
    matrice_2 = [[5, 1, 12], [-7, 9, 2]]
    assert matrices.sub_matrices(matrice_1, matrice_2) == [[-4, 4, -7], [5, -2, -2]]

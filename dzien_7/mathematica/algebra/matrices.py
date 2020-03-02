def add_matrices(a, b):
    # final_matrice = [[0 for j in range(len(a[i]))] for i in range(len(a))]
    # for i in range(len(a) ):
    #     for j in range(len(a[i])):
    #         final_matrice[i][j] = a[i][j] + b[i][j]
    # return final_matrice
    return [[a[i][j] + b[i][j] for j in range(len(a[i]))] for i in range(len(a))]

    # result = []
    # for row_a, row_b in zip(a, b):
    #     row = []
    #     for col_a, col_b in zip(row_a, row_b):
    #         row.append(col_a+col_b)
    #     result.append(row)
    # return result


def sub_matrices(a, b):
    # final_matrice = [[0 for j in range(len(a[i]))] for i in range(len(a))]
    # for i in range(len(a)):
    #     for j in range(len(a[i])):
    #         final_matrice[i][j] = a[i][j] - b[i][j]
    # return final_matrice

    return [[a[i][j] - b[i][j] for j in range(len(a[i]))] for i in range(len(a))]

    # result = []
    # for row_a, row_b in zip(a, b):
    #     row = []
    #     for col_a, col_b in zip(row_a, row_b):
    #         row.append(col_a - col_b)
    #     result.append(row)
    # return result


matrice_1 = [[1, 5], [-2, 7]]

matrice_2 = [[11, 3], [-3, 9]]
print("Dodawanie: \n", add_matrices(matrice_1, matrice_2))
print("Odejmowanie: \n", sub_matrices(matrice_1, matrice_2))

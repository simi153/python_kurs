def get_row_col(pos):
    columns = "ABC"
    rows = "123"
    # if len(pos) == 2:
    #     if int(pos[1]) <=3 and pos[0] in columns:
    #         row = int(pos[1]) - 1
    #         col = columns.index(pos[0])
    #     else:
    #         return False
    # else:
    #     return False
    # return row, col
    if len(pos) == 2:
        if pos[0] in columns and pos[1] in rows:
            col, row = list(pos)
            return rows.index(row), columns.index(col)
        return False
    else:
        return False


def test_get_row_col():
    assert get_row_col("A3") == (2, 0)
    assert get_row_col("D3") is False
    assert get_row_col("A6") is False
    assert get_row_col("A") is False

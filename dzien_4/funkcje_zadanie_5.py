def get_row_col(pos):
    # row = int(pos[1]) - 1
    # # if pos[0]=="A":
    # #     col=0
    # # elif pos[0]=="B":
    # #     col=1
    # # elif pos[0]=="C":
    # #     col=2
    # col = ord(pos[0]) - 65
    # return row,col
    columns="ABC"
    rows="123"
    col_n,row_n = list(pos)
    try:
        return rows.index(row_n),columns.index(col_n)
    except:
        return "Poza planszą"


def test_get_row_col():
    assert get_row_col("A3") == (2, 0)
    assert get_row_col("C2") == (1, 2)
    assert get_row_col("D3") == "Poza planszą"

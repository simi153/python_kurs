def format_number(number):
    return f"{number:,}"
    return "{:,}".format(number)


def test_format_number():
    assert format_number(10) == "10"
    assert format_number(1000) == "1,000"
    assert format_number(377532456) == "377,532,456"
    assert format_number(57842.35) == "57,842.35"
    assert format_number(-2000) == "-2,000"
    assert format_number(-1234567.87654) == "-1,234,567.87654"

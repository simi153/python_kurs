def format_number(number):
    formatted = "{:,}".format(number)
    # return f"{number:,}"
    return formatted

def test_format_number():
    assert format_number(1000) == "1,000"
    assert format_number(377532456) == "377,532,456"
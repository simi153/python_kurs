def formatuj(*args, **kwargs):
    napis = "\n".join(args)
    print(kwargs)
    for k, v in kwargs.items():
        napis = napis.replace("$" + k, str(v))

    return napis


def test_formatuj():
    assert formatuj("koszt $cena PLN", "kwota $cena brutto", cena=10) == "koszt 10 PLN\nkwota 10 brutto"
    assert formatuj("koszt $netto PLN", "kwota $brutto brutto", netto=10, brutto=12) == "koszt 10 PLN\nkwota 12 brutto"

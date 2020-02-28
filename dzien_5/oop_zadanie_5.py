class CashMachine:
    def __init__(self):
        self._money = []

    @property
    def is_available(self):
        if self._money:
            return True
        else:
            return False

    def put_money(self, money):
        self._money.extend(money)

    def withdraw_money(self, money):
        to_withdraw = []
        for value in sorted(self._money, reverse=True):
            if sum(to_withdraw) + value <= money:
                to_withdraw.append(value)

        if sum(to_withdraw) == money:
            for value in to_withdraw:
                self._money.remove(value)
        else:
            return []
        return to_withdraw


class TestCashMachine:
    def test_initialisation(self):
        assert CashMachine()

    def test_is_available(self):
        cs = CashMachine()
        assert not cs.is_available

    def test_cs_is_available_after_put_money(self):
        cs = CashMachine()
        assert cs.is_available is False
        cs.put_money([100, 100])
        assert cs.is_available is True

    def test_withdraw_money(self):
        cs = CashMachine()

        cs.put_money([100, 100])
        assert cs.withdraw_money(200) == [100, 100]
        assert cs.is_available is False

        cs = CashMachine()
        cs.put_money([100, 100, 100])
        assert cs.withdraw_money(200) == [100, 100]
        assert cs.is_available is True

        cs = CashMachine()
        cs.put_money([50, 50, 50])
        assert cs.withdraw_money(200) == []
        assert cs.is_available is True

        cs = CashMachine()
        cs.put_money([100, 50, 100])
        assert cs.withdraw_money(200) == [100, 100]
        assert cs.is_available is True

    def test_cs_is_available_after_withdraw_money(self):
        cs = CashMachine()
        cs.put_money([100, 100, 50])
        cs.withdraw_money(100)
        cs.withdraw_money(150)
        assert cs.is_available is False

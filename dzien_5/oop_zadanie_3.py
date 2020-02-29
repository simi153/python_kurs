class ElectricCar:
    NEXT_ID = 1
    def __init__(self, max_range: int):
        self.max_range = max_range
        self._traveled = 0
        self._id=self.NEXT_ID
        ElectricCar.NEXT_ID+=1

    def drive(self, range: int):
        if self._traveled + range <= self.max_range:
            self._traveled += range
            return range
        to_travel = self.max_range - self._traveled
        self._traveled = self.max_range
        return to_travel

    def charge(self):
        self._traveled = 0
        return self.max_range


class TestElectricCar:
    def test_init(self):
        car = ElectricCar(100)
        assert car.max_range == 100

    def test_drive(self):
        car = ElectricCar(100)
        assert car.drive(70) == 70
        assert car.drive(50) == 30
        assert car.drive(50) == 0

    def test_charge(self):
        car = ElectricCar(100)
        assert car.drive(100) == 100
        assert car._traveled == 100
        assert car.charge() == 100
        assert car.drive(100) == 100

# car = ElectricCar(100)
# car.drive(70)
# car.drive(50)
# car.drive(50)
# car.charge()
# car.drive(50)

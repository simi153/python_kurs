class Employee:
    def __init__(self, f_name: str, l_name: str, rph: float):
        self.first_name = f_name
        self.last_name = l_name
        self.rate_per_hour = rph
        self._worked_normal_hours = 0
        self._worked_overtime = 0

    def register_time(self, hours: int):
        if hours > 8:
            self._worked_normal_hours += 8
            self._worked_overtime += (hours - 8)
        else:
            self._worked_normal_hours += hours
        return self._worked_normal_hours

    def pay_salary(self):
        to_pay = self._worked_normal_hours * self.rate_per_hour + self._worked_overtime*self.rate_per_hour*2
        self._worked_normal_hours = 0
        self._worked_overtime = 0
        return to_pay


class TestEmployee:
    def test_employee_init(self):
        employee = Employee("Jan", "Nowak", 100.0)
        assert employee.first_name == "Jan"
        assert employee.last_name == "Nowak"
        assert employee.rate_per_hour == 100.0
        assert employee._worked_normal_hours == 0

    def test_employee_pay_salary_when_no_worked_hours(self):
        employee = Employee("Jan", "Nowak", 100.0)
        assert employee.pay_salary() == 0

    def test_employee_regiter_time(self):
        employee = Employee("Jan", "Nowak", 100.0)
        employee.register_time(5)
        assert employee._worked_normal_hours == 5
        assert employee._worked_overtime == 0
        employee.register_time(10)
        assert employee._worked_normal_hours == 13
        assert employee._worked_overtime == 2

    def test_employee_pay_salary_when_worked_hours(self):
        employee = Employee("Jan", "Nowak", 100.0)
        employee.register_time(5)
        assert employee.pay_salary() == 500.0
        assert employee.pay_salary() == 0
        employee.register_time(15)
        assert employee._worked_normal_hours == 8
        assert employee._worked_overtime == 7
        employee.register_time(10)
        assert employee._worked_normal_hours == 16
        assert employee._worked_overtime == 9
        assert employee.pay_salary() == 3400

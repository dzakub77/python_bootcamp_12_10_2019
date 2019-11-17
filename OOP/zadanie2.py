

class Employee:
    def __init__(self, name, surname, rate):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.pay_salary = 0
        self.register_time = 0

    def pracuj(self):
        print(f"{self.name} pracuje 1 godzine")
        self.register_time += 1
        self.pay_salary += 100
    def wyplata(self):
        if self.register_time == 8:
            self.rate = 8 * rate
            self.register_time = 0
        elif self.register_time == 10:
            self.rate = 8 * rate + 4 * rate
            self.register_time = 0
        if self.register_time == 0:
            self.pay_salary == 0


def test_employee_init():
    employee = Employee("Rafał", "Korzeniewski", 200)
    assert employee.name == "Rafał"
    assert employee.surname == "Korzeniewski"
    assert employee.rate == 200
def test_employee_
from employee import Employee, PremiumEmployee
def test_employee_init():
    employee = Employee("Rafał", "Korzeniewski", 200)
    assert employee.name == "Rafał"
    assert employee.last_name == "Korzeniewski"
    assert employee.rate == 200

def test_employee_register_time():
    employee = Employee("Rafał", "Korzeniewski", 200)
    employee.register_time(5)
    assert employee._Employee__registered_time == 5

def test_employee_pay_salary():
    employee = Employee("Rafał", "Korzeniewski", 200)
    assert employee.pay_salary() == 0
    employee.register_time(5)
    assert employee.pay_salary() == 5*200
    assert employee.pay_salary() == 0
    employee.register_time(10)
    assert employee.pay_salary() == 8*200+2*2*200
    assert employee.pay_salary() == 0

def test_premium_employee():
    premium = PremiumEmployee("Rafał", "Korzeniewski", 200)
    premium.give_bonus(100)
    assert  premium.give_bonus == 100

def test_premium_employee_pay_salary():
    premium = PremiumEmployee("Rafał", "Korzeniewski", 200)
    premium.give_bonus(100)
    premium.register_time(5)
    assert  premium.pay_salary() == 1100




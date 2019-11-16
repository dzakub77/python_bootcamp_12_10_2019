
class CashMachine:

    def __init__(self):
        self.bills = []


    @property
    def is_available(self):
        if self.bills:
            return True
        return False
     #   return bool(self.bills)

    def put_money(self, bills):
        self.bills.extend(bills)

    def withdraw_money(self, amount):
        money = []
        for bill in sorted(self.bills, reverse=True):
            if bill + sum(money) <= amount:
                money.append(bill)
        if sum(money) == amount:
            for bill in money:
                self.bills.remove(bill)
        else:
            return []
        return money









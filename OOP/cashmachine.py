
class CashMachine:

    def __init__(self):
        self.__bills = [] # zmienna prywatna / __ zaczyna sie tak


    @property
    def is_available(self):
        if self.__bills:
            return True
        return False
     #   return bool(self.bills)

    def put_money(self, bills):
        self.__bills.extend(bills)

    def withdraw_money(self, amount):
        money = []
        for bill in sorted(self.__bills, reverse=True):
            if bill + sum(money) <= amount:
                money.append(bill)
        if sum(money) == amount:
            for bill in money:
                self.__bills.remove(bill)
        else:
            return []
        return money

    def print_bills(self):
        print(self.__bills)

bankomat = CashMachine()
bankomat.__bills = [100, 200]
bankomat.put_money([100, 200, 200])
print(bankomat.is_available)
print(bankomat.__bills)
bankomat.print_bills()






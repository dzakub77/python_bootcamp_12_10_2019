
class Product:
    NEXT_ID = 1
    def __init__(self, name, price):
        self.id = Product.NEXT_ID
        self.name = name
        self.price = price
        Product.NEXT_ID += 1

class BasketEntry:
    def __init__(self, product: Product, amount: int):
        self.product = product
        self.amount = amount
    def count_price(self):
        return self.product.price * self.amount

class ValueDiscount:
    def __init__(self, amount):
        self.amount = amount

class Basket:
    def __init__(self):
        self.basket_entries = []
        self.discounts = []

    def add_product(self, product: Product, amount: int) -> None:
        basket_entry = BasketEntry(product, amount)

        in_basket = False
        for be in self.basket_entries:
           # if be['product'] == product:
           #     be['amount'] += amount
           #     in_basket = True
            if be.product == product:
                be.amount += amount
                in_basket = True
        if not in_basket:
            self.basket_entries.append(basket_entry)
    @staticmethod
    def with_products(produkty):
        koszyk = Basket()
        for product in produkty:
            koszyk.add_product(product, 1)
        return koszyk

    def count_total_price(self):
        total_price = 0
        for be in self.basket_entries:
            total_price += be.count_price()

        #trzeba od tego odjąc upusty
        value_discount = sum(self.discounts)
        total_price -= value_discount
        return total_price
    def generate_report(self):
        report = "Produkty w koszyku\n"
        for be in self.basket_entries:
            report += f"- {be.product.name} ({be.product.id}), cena: {be.product.price} x {be.amount}\n"
        report += f"W sumie: {self.count_total_price()}"
        return report
    def add_discount(self, discount):
        self.discounts.append(discount)



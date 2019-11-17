
from basket import Basket, Product

def test_basket_init():
    basket = Basket()
    assert basket

def test_product_init():
    product = Product("woda", 10.0)
    assert product.id == 1
    assert product.name == "woda"
    assert product.price == 10.0

def test_add_product_to_basket():
    product = Product("woda", 10.0)
    basket = Basket()
    basket.add_product(product, 5)

def test_basket_count_total_price():
    basket = Basket()
    product = Product("woda", 10.0)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50.0
    product = Product("Piwo", 3)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 65

def test_basket_generate_report():
    basket = Basket()
    product = Product("Woda", 10.0)
    basket.add_product(product, 5)
    expected = """
Produkty w koszyku
- Woda (1), cena: 10.0 x 5
W sumie: 50.0
"""
    assert basket.generate_report() == expected

def test_basket_add_discount():
    product = Product("woda", 10.0)
    basket = Basket()
    discount = ValueDiscount(10)
    basket.add_discount(discount)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50.0 - 10
    product = Product("Piwo", 3)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 115 - 10

def test_basket_add_percent_discount():
    product = Product("Woda", 10.0)
    basket = Basket()

def test_basket_with_products():
    pr1 = Product("Woda", 1)
    pr2 = Product("Chleb", 2)
    Basket.with_products([pr1, pr2])
    assert koszyk.count_total_price(3)
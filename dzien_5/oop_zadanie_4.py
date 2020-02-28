class Basket:
    def __init__(self):
        self.products = []

    def add_product(self, product, amount):
        self.products.append(BasketEntry(product, amount))

    def count_total_price(self):
        total_price = 0
        for be in self.products:
            total_price += be.count_price()
        return total_price

    def generate_report(self):
        report = "Produkty w koszyku:\n"
        for be in self.products:
            report += be.report()
        report += f"W sumie: {self.count_total_price():.2f}"
        return report

    @classmethod
    def with_products(cls, product_list):
        basket = cls()
        for p in product_list:
            basket.add_product(p, 1)
        return basket


class BasketEntry:
    def __init__(self, product, amount):
        self.product = product
        self.amount = amount

    def count_price(self):
        return self.product.price * self.amount

    def report(self):
        return f'- {self.product.name} ({self.product.id}), cena: {self.product.price:.2f} x {self.amount}\n'


class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class TestBasket:

    def test_initialization(self):
        basket = Basket()
        assert basket

    def test_add_product(self):
        basket = Basket()
        product = Product(1, "Woda", 10)
        product2 = Product(2, "Chleb", 3)
        assert len(basket.products) == 0
        basket.add_product(product, 5)
        assert len(basket.products) == 1
        assert basket.products[0].amount == 5
        assert basket.products[0].product == product
        basket.add_product(product2, 5)
        assert len(basket.products) == 2
        assert basket.products[1].amount == 5
        assert basket.products[1].product == product2
        # assert basket.products[0][1] == 5

    def test_count_total_price(self):
        basket = Basket()
        product = Product(1, "Woda", 10)
        product2 = Product(2, "Chleb", 3)
        basket.add_product(product, 2)
        basket.add_product(product2, 3)
        assert basket.count_total_price() == 2 * 10 + 3 * 3

    def test_generate_report(self):
        basket = Basket()
        product = Product(1, "Woda", 10)
        basket.add_product(product, 2)
        expected = """Produkty w koszyku:
- Woda (1), cena: 10.00 x 2
W sumie: 20.00"""
        assert basket.generate_report() == expected

    def test_with_products(self):
        pr1 = Product(1, "woda", 4)
        pr2 = Product(2, "piwo", 4)
        basket = Basket.with_products([pr1, pr2])
        assert len(basket.products) == 2


class TestProduct:

    def test_initialization(self):
        product = Product(1, "Woda", 10)
        assert product.id == 1
        assert product.name == "Woda"
        assert product.price == 10

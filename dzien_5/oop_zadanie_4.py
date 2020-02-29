class Product:
    NEXT_ID = 1

    def __init__(self, product: str, price: float):
        self.id = Product.NEXT_ID
        Product.NEXT_ID += 1
        self.product = product
        self.price = price

    def __str__(self):
        print(f"{self.product} ({self.id}), cena: {self.price} ")

    def print_info(self):
        print(f'Produkt: "{self.product}", id: {self.id}, cena: {self.price} PLN')


class BasketEntry:
    def __init__(self, product, amount):
        self.product = product
        self.amount = amount

    def count_price(self):
        return self.product.price * self.amount

    def report(self):
        return f"- {self.product.product} ({self.product.id}), cena: {self.product.price} x {self.amount}\n"

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
            report+= be.report()

        report+= f"W sumie: {self.count_total_price()}"
        return report


class TestBasket:
    def test_init(self):
        basket = Basket()
        assert basket

    def test_add_product(self):
        basket = Basket()
        product = Product('Woda', 10.00)
        assert len(basket.products) == 0
        basket.add_product(product, 5)
        assert len(basket.products) == 1
        assert basket.products[0].product == product

    def test_count_total_price(self):
        basket = Basket()
        product = Product('Woda', 10.00)
        basket.add_product(product, 5)
        assert basket.count_total_price() == 50.0
    def test_generate_report(self):
        Product.NEXT_ID=1
        basket = Basket()
        product = Product('Woda', 10.00)
        basket.add_product(product, 5)
        assert basket.generate_report() == "Produkty w koszyku:\n- Woda (1), cena: 10.0 x 5\nW sumie: 50.0"

class Product:
    def __init__(self, id: int, product: str, price: float):
        self.id = id
        self.product = product
        self.price = price

    def print_info(self):
        print(f'Produkt: "{self.product}", id: {self.id}, cena: {self.price} PLN')

class Basket:
    def __init__(self):
        self._total_price = 0
    def add_product(self,product,num):

# class TestBasket:
#     def test_init(self):
#         basket = Basket()
#         product = Product(1, 'Woda',10.00)
#         basket.add_product(product,5)
#         assert basket.count_total_price() == 50.0
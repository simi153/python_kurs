class Product:
    def __init__(self, id: int, product: str, price: float):
        self.id = id
        self.product = product
        self.price = price

    def print_info(self):
        print(f'Produkt: "{self.product}", id: {self.id}, cena: {self.price} PLN')


prod1 = Product(1, "Woda", 10.99)
prod1.print_info()

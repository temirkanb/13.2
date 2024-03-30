from src.product import Product


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country_prod: str, germin_period, color: str):
        super().__init__(name, description, price, quantity)
        self.country_prod = country_prod
        self.germin_period = germin_period
        self.color = color
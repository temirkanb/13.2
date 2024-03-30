from src.product import Product


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 performance, model: str, memory, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

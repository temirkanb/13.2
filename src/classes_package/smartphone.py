from src.classes_package.product import Product


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 performance, model: str, memory, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
        if type(self) is Smartphone:
            self.print_ec()

    def __repr__(self) -> str:
        """
        Возвращает отладочную информацию о экземпляре класса "продукт"
        :return: ф-строку
        """
        return (f"{self.__class__.__name__}({self.name}, {self.description},"
                f" {self.quantity}, {self.performance}, {self.model},"
                f" {self.memory}, {self.color})")


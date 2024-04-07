from src.classes_package.product import Product


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country_prod: str, germin_period, color: str):
        super().__init__(name, description, price, quantity)
        self.country_prod = country_prod
        self.germin_period = germin_period
        self.color = color
        if type(self) is LawnGrass:
            self.print_ec()

    def __repr__(self) -> str:
        """
            Возвращает отладочную информацию о экземпляре класса "продукт"
            :return: ф-строку
            """
        return (f"{self.__class__.__name__}({self.name}, {self.description},"
                f" {self.quantity}, {self.country_prod}, {self.germin_period},"
                f" {self.color})")

from src.classes_package.mixinlog import MixinLog
from src.classes_package.pattern_product import PatternProduct


class Product(MixinLog, PatternProduct):
    """
    Класс продуктов
    внутри непосредственно класса только список продуктов - общий,
    то есть при инициализации каждого нового экземпляра класса ссылка на него
    будет ложиться так же и в этот список
    """
    products_list: list
    products_list = []

    def __init__(self, name: str, description: str, price: float,
                 quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.products_list.append(self)
        if type(self) is Product:
            self.print_ec()

    @classmethod
    def init_new_product(cls, dict_with_prod) -> object:
        """
        Класс метод для распаковки одного товара из словаря с данными о товаре.
        Если товар ранее с таким названием ранее находился в системе,
        то увеличивает его количество,
        иначе отправляет на добавление в указанную категорию
        :param dict_with_prod: словарь с данными о товаре
        :return: None
        """
        name = dict_with_prod['name']
        description = dict_with_prod['description']
        price = dict_with_prod['price']
        quantity = dict_with_prod['quantity']
        for product in Product.products_list:
            if product.name == name:
                product.quantity += quantity
                if product.price < price:
                    product.price = price
                return product
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """
        геттер для цены товара
        :return: цену товара
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Сеттер для цены товара. Если введенная цена меньше нуля - дает фидбэк
        и цену не увеличивает. Если новая цена товара оказалась выше той, что
        у товара уже есть - запрашивает подтверждение на изменение
        в меньшую сторону(при подтверждение изменяет цену на новую)
        :param new_price: новая цена
        :return: None
        """
        if new_price <= 0:
            print('Новая цена не соответствует условиям')
        elif new_price < self.__price:
            confirm = input("Новая цена ниже текущей. Для подтверждения "
                            "введите 'y'")
            if confirm == 'y':
                self.__price = new_price
        else:
            self.__price = new_price

    def sum_price_prod(self):
        return self.quantity * self.price

    def __add__(self, other) -> int:
        """
        вызывается при попытке сложить два экземпляра класса
        "продукт" и складывает стоимость, также проверяет, что сложение ведется
        с объектом допустимого типа
        :param other: другой экземпляр класса продукт
        :return: целочисленное значение
        """
        if type(self) is not type(other):
            raise TypeError("сложение допустимо только между экземплярами "
                            "одного и того же класса")
        return self.sum_price_prod() + other.sum_price_prod()

    def __len__(self) -> int:
        """
        вызывается при обращении к классу в функции len()
        :return: целочисленное значение - количество товаров
        """
        return self.quantity

    def __str__(self) -> str:
        """
        Возвращает строковое представление
        информации о продукте(имя, цена, количество)
        :return: ф-строку
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self) -> str:
        """
        Возвращает отладочную информацию о экземпляре класса "продукт"
        :return: ф-строку
        """
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.quantity})"
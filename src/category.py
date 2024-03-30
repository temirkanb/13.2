from src.product import Product


class Category:
    """
    Класс категорий
    Непосредственно в классе находятся два счетчика - один считает количество
    категорий и увеличивается только при инициализации нового экземпляра
    класса, второй считает товары - увеличивается на длину списка отдаваемого
    при инициализации класса и в отдельном методе на добавление товара в категорию
    """
    category_count: int
    products_count: int

    category_count = 0
    products_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Конструктор класса Category
        :param name: имя категории
        :param description: описание категории
        :param products: содержит список
        экземпляров класса продукт(иначе говоря продукты)
        """
        for product in products:
            if not isinstance(product, Product):
                raise TypeError("элементы списка продуктов, должны является"
                                "экземпляры класса 'продукт' или экземплярами"
                                "классов наследуемых от 'продукта'")
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.products_count += len(products)

    def add_product(self, new_product: Product) -> None:
        """
        метод отвечающий за добавление нового продукта в текущую категорию
        и увеличивающий счетчик видов товара
        :param new_product: экземпляр класса продукты
        :return: None
        """
        if not isinstance(new_product, Product):
            raise TypeError("элементы списка продуктов, должны является"
                            "экземпляры класса 'продукт' или экземплярами"
                            "классов наследуемых от 'продукта'")
        self.__products.append(new_product)
        Category.products_count = len(self.__products)

    @property
    def products(self) -> list:
        """
        геттер для возврата списка описаний продуктов текущей категории
        :return: список с описанием продуктов
        """
        list_of_products = []
        for product in self.__products:
            list_of_products.append(str(product))
        return list_of_products

    def __len__(self) -> int:
        """
        Вызывается при обращении к экземпляру класса в функции len()
        и возвращает длину списка продуктов, принадлежащих данной категории
        :return: целочисленное значение - длину списка продуктов экземпляра
        класса "категория"
        """
        return len(self.__products)

    def __str__(self) -> str:
        """
        Возвращает строковое отображение информации о категории, содержащее
        информации о сумме единиц товара в ней
        :return: ф-строка
        """
        list_of_quantity = []
        for product in self.__products:
            list_of_quantity.append(len(product))
        return f"{self.name}, количество продуктов: {sum(list_of_quantity)} шт."

    def __repr__(self) -> str:
        """
        Возвращает отладочную информацию об экземпляре класса "категория"
        :return: ф - строку
        """
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.__products})"
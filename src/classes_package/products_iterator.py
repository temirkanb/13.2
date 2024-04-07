class ProductsIterator:
    """
    Класс созданный для итерации по списку экземпляров класса "продукт", лежащий
    внутри экземпляра класса "категория". Экземпляр класса "категория" принимается
    при создании экземпляра текущего класса
    """
    def __init__(self, category: object):
        self.category = category

    def __iter__(self):
        """
        Создает атрибут для дальнейших итераций. Счетчиком является длина списка
        "продуктов" внутри self.category
        :return: self
        """
        self.iter_index = len(self.category)
        return self

    def __next__(self):
        """
        Уменьшает счетчик self.iter_index и возвращает экземпляр класса "продукт"
        :return: экземпляр класса "продукт" из списка "продуктов" self.category
        с индексом self.iter_index
        """
        if self.iter_index == 0:
            raise StopIteration
        self.iter_index -= 1
        return self.category.products[self.iter_index]
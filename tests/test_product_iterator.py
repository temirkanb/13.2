#from src.products_iterator import ProductsIterator


def test_init(for_iterator):
    assert str(for_iterator.category) == ("Смартфоны,"
                                          " количество продуктов: 13 шт.")


def test_iter_and_next(for_iterator):
    for i in for_iterator:
        pass
    assert for_iterator.iter_index == 0
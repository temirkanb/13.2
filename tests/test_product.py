import pytest
from src.product import Product


def test_init(for_product_1):
    assert for_product_1.name == "Xiaomi Redmi Note 11"
    assert for_product_1.description == "1024GB, Синий"
    assert for_product_1.price == 31000.0
    assert for_product_1.quantity == 14


def test_init_new_product(null, dict_with_product):
    assert len(Product.products_list) == 0
    Product.init_new_product(dict_with_product)
    assert Product.products_list[0].quantity == 14
    Product.init_new_product(dict_with_product)
    assert Product.products_list[0].quantity == 28
    dict_with_product['price'] = 35000.0
    Product.init_new_product(dict_with_product)
    assert Product.products_list[0].quantity == 42


def test_price_getter(for_product_1):
    assert for_product_1.price == 31000.0


def test_price_setter(for_product_1):
    for_product_1.price = 30000.0  # При вводе 'n'
    assert for_product_1.price == 31000.0
    for_product_1.price = 30000.0  # При вводе 'y'
    assert for_product_1.price == 30000.0
    for_product_1.price = 0.0
    assert for_product_1.price == 30000.0
    for_product_1.price = 32000.0
    assert for_product_1.price == 32000.0


def test_add(null, for_product_2, for_product_3, for_lawn_grass):
    assert for_product_2 + for_product_3 == 2580000.0
    with pytest.raises(TypeError):
        for_lawn_grass + for_product_2


def test_len(for_product_1):
    assert len(for_product_1) == 14


def test_str(for_product_1):
    str_product = "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    assert str(for_product_1) == str_product


def test_repr(for_product_1):
    repr_product = "Product(Xiaomi Redmi Note 11, 1024GB, Синий, 14)"
    assert repr(for_product_1) == repr_product
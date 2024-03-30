import pytest
import os
from config import ROOT_DIR
from src.product import Product
from src.category import Category
from src.products_iterator import ProductsIterator
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


@pytest.fixture
def for_load_json():
    return os.path.join(ROOT_DIR, 'src', 'products.json')


@pytest.fixture
def for_category(for_product_2, for_product_3):
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и "
                    "получение дополнительных функций для удобства жизни",
                    [for_product_2, for_product_3])


@pytest.fixture
def for_product_1():
    return Product("Xiaomi Redmi Note 11",
                   "1024GB, Синий",
                   31000.0, 14)


@pytest.fixture
def for_product_2():
    return Product("Samsung Galaxy C23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0, 5)


@pytest.fixture
def for_product_3():
    return Product("Iphone 15", "512GB, Gray space",
                   210000.0, 8)


@pytest.fixture
def for_smartphone():
    return Smartphone('Redmi Note 9 Pro', '256GB, Breeze',
                      20_000, 23, 'Мощный', 'Note 9 Pro',
                      '256GB', 'Breeze')


@pytest.fixture
def for_lawn_grass():
    return LawnGrass('Трава газонная', 'Свежая газонная трава',
                     1_500, 235, 'Бразилия',
                     '3-4 недели', 'Салатовый')


@pytest.fixture()
def for_iterator(for_category):
    return ProductsIterator(for_category)


@pytest.fixture
def dict_with_product():
    return {'name': "Xiaomi Redmi Note 11",
            'description': "1024GB, Синий",
            'price': 31000.0,
            'quantity': 14}


@pytest.fixture
def null():
    Category.category_count = 0
    Category.products_count = 0
    Product.products_list = []
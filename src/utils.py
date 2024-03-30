import json
from src.product import Product
from src.category import Category


def load_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def unpacker(json_list):
    category_list = []
    products_list = []
    for categ in json_list:
        prod_from_cat = []
        for prod in categ.get('products'):
            product = Product(prod['name'], prod['description'],
                              prod['price'], prod['quantity'])
            prod_from_cat.append(product)
        category = Category(categ['name'], categ['description'], prod_from_cat)
        category_list.append(category)
        products_list.append(prod_from_cat)
    return category_list, products_list

from src.category import Category
from src.product import Product
from src.products_iterator import ProductsIterator
from src.utils import load_json, unpacker
import os
from config import ROOT_DIR

PATH_TO_PRODUCTS = os.path.join(ROOT_DIR, 'src', 'products.json')


def main():
    response = load_json(PATH_TO_PRODUCTS)
    category_list, product_list = unpacker(response)
    # print(Product.products_list[0] + Product.products_list[1])
    for product in ProductsIterator(category_list[0]):
        print(product)


if __name__ == '__main__':
    main()
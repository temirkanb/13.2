from src.classes_package.smartphone import Smartphone
from src.utils import load_json, unpacker
import os
from config import ROOT_DIR

PATH_TO_PRODUCTS = os.path.join(ROOT_DIR, 'src', 'products.json')


def main():
    response = load_json(PATH_TO_PRODUCTS)
    category_list, product_list = unpacker(response)
    # print(Product.products_list[0] + Product.products_list[1])
    redmi = Smartphone('Redmi Note 9 Pro', '256GB, Breeze',
                       20_000, 23, 'Мощный', 'Note 9 Pro',
                       '256GB', 'Breeze')
    print(redmi)


if __name__ == '__main__':
    main()

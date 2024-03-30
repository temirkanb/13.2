from src.utils import load_json, unpacker


def test_load_json(for_load_json):
    assert load_json(for_load_json)[1:] == [{
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться "
                       "просмотром, станет вашим другом и помощником",
        "products": [
            {
                "name": "55\" QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000.0,
                "quantity": 7
            }
        ]
    }]


def test_unpacker(for_load_json):
    assert unpacker(load_json(for_load_json))[0][0].name == "Смартфоны"
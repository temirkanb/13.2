def test_init(for_lawn_grass):
    assert for_lawn_grass.name == 'Трава газонная'
    assert for_lawn_grass.description == 'Свежая газонная трава'
    assert for_lawn_grass.price == 1_500
    assert for_lawn_grass.quantity == 235
    assert for_lawn_grass.country_prod == 'Бразилия'
    assert for_lawn_grass.germin_period == '3-4 недели'
    assert for_lawn_grass.color == 'Салатовый'
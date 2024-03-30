def test_init(for_smartphone):
    assert for_smartphone.name == "Redmi Note 9 Pro"
    assert for_smartphone.description == "256GB, Breeze"
    assert for_smartphone.price == 20_000
    assert for_smartphone.quantity == 23
    assert for_smartphone.performance == 'Мощный'
    assert for_smartphone.model == 'Note 9 Pro'
    assert for_smartphone.memory == '256GB'
    assert for_smartphone.color == 'Breeze'
import price_info

def test_total_cost_shopping():
    result = price_info.total_cost_shopping()
    expected = 46.75
    assert(result == expected)

def test_cost_of_fruits():
    result1 = price_info.cost_of_fruits('apple', 10)
    expected1 = 12.0
    assert(result1 == expected1)
    
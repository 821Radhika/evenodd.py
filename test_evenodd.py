from even_odd import even_odd

def test_even():
    assert even_odd(10) == "Even number"

def test_odd():
    assert even_odd(7) == "Odd number"
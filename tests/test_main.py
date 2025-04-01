from main import add

def test_add_positive_numbers():
    # Test adding two positive numbers
    assert add(2, 3) == 5

def test_add_negative_numbers():
    # Test adding two negative numbers
    assert add(-2, -3) == -5

def test_add_mixed_numbers():
    # Test adding a positive and a negative number
    assert add(2, -3) == -1
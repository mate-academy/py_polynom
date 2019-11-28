import polynom


def test_constant():
    assert polynom.get_poly(1)(123) == 1


def test_linear():
    assert polynom.get_poly(1, 1)(1) == 2


def test_quadratic():
    assert polynom.get_poly(1, 1, 1)(0) == 1
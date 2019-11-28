"""
docstring
"""
import polynom


def test_constant():
    """

    :return:
    """
    assert polynom.get_poly(1)(123) == 1


def test_linear():
    """

    :return:
    """
    assert polynom.get_poly(1, 1)(1) == 2


def test_quadratic():
    """

    :return:
    """
    assert polynom.get_poly(1, 1, 1)(0) == 1

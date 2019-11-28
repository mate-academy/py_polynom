"""
module polynomial
"""
from typing import Callable


def get_poly(*coeffs: float) -> Callable[[float], float]:
    """
    Function that, for given coefficients, returns a function
    for calculating the value of a polynomial of a given degree.
    The degree of the polynomial is determined by the number of factors.
    For instance: (1, 2, 3) -> 1 * x * x + 2 * x + 3
    :param coeffs: float
    :return: Callable[[float], float]
    """

    def polynomial(x_repr):
        return sum(coeff * x_repr ** idx for idx, coeff in enumerate(coeffs[::-1]))

    return polynomial

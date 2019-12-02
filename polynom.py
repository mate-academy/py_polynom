"""Create a function that, for given coefficients,
returns a function for calculating the value of a polynomial of a given degree. """
from typing import Callable


def get_poly(*koeffs: float) -> Callable[[float], float]:
    """Function that, for given coefficients, returns a function"""
    def get_poly_sum(number):
        """Function for calculating the value of a polynomial of a given degree"""
        return sum([value * number ** key for key, value in enumerate(koeffs)])
    return get_poly_sum

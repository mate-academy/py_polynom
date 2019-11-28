"""polynom module"""
from typing import Callable


def get_poly(*koeffs: float) -> Callable[[float], float]:
    """takes coefficients and passes them"""
    def sum_poly(argument):
        """considers the sum of the polynomial"""
        poly = []
        for index, value in enumerate(koeffs):
            poly.append(value * argument ** index)
        return sum(poly)
    return sum_poly

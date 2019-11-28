"""docstring"""
from typing import Callable


def get_poly(*koeffs: float) -> Callable[[float], float]:
    """

    :param koeffs: float
    :return:
    """
    def poly_sum(arg):
        polinom = []
        max_pow = len(koeffs) - 1
        for idx, coeff in enumerate(koeffs):
            power = max_pow - idx
            polinom.append(coeff * arg ** power)
        return sum(polinom)

    return poly_sum

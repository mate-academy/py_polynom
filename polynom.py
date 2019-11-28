"""module docstring"""

from typing import Callable


def get_poly(*coeffs: float) -> Callable[[float], float]:
    """return function to calculate polynomial"""
    def pol(value):
        """calculate polynomial"""
        result = 0
        degree = len(coeffs) - 1
        for i, coef in enumerate(coeffs):
            result += value ** (degree - i) * coef
        return result

    return pol

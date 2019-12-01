"""The function that, for given coefficients, returns a function for
calculating the value of a polynomial of a given degree.
"""

from typing import Callable


def get_poly(*koeffs: float) -> Callable[[float], float]:
    """Return function for calculating the value of a polynomial of a given
    degree.The degree of the polynomial is determined by the number of factors.
    """
    return lambda x: sum([pow(x, i) * val for i, val in enumerate(koeffs)])

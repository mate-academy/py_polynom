"""The script takes coefficients and
value of variable and calculates polynomial value"""
from typing import Callable


def get_poly(*koeffs: float) -> Callable[[float], float]:
    """
    Convert the list of coefficients provided into the one
    used for Horner's polynomial evaluation algorithm calculation
    :param koeffs: list of coefficients to be multiplied
    by respective parts of polynom
    :return: polynomial value calculated in currying function
    """
    coefficients = koeffs[::-1]

    def inner_f(value):
        """Currying function that takes the value of polynomial variable
        and calculates polynomial value
        based on coefficients processed in outer function"""
        result = 0
        for seq, coef in enumerate(coefficients):
            result += coef * (value ** seq)
        return result
    return inner_f

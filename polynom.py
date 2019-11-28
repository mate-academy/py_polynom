"""
Polynomial of a given degree
"""


from typing import Callable


def get_poly(*koeffs: float) -> Callable[[float], float]:
    """Calculate polinomial"""
    def pol_sum(value):
        lst_polinom = []
        for indx, koeff in enumerate(koeffs):
            lst_polinom.append(koeff * value ** indx)
        return sum(lst_polinom)
    return pol_sum

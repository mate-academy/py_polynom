"""docstring"""
from typing import Callable


def get_poly(*koeffs: float) -> Callable[[float], float]:
    """get poly"""
    def g_get_poly(number):
        return sum([x*number**id_x for id_x, x in enumerate(koeffs)])
    return g_get_poly

from typing import Callable


def get_poly(*koeffs: float) -> Callable[[float], float]:

    return lambda x: 42
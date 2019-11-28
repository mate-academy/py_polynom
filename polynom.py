'''
Module
'''
from typing import Callable


def get_poly(*koeffs: float) -> Callable[[float], float]:
    '''

    :param koeffs:
    :return:
    '''
    def zamkn(number):
        result = 0
        for num, item in enumerate(koeffs):
            result += number ** num * item
        return result
    return zamkn

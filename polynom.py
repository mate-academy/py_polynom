"""
docstring
"""


def get_poly(*coffs):
    """

    :param coffs:
    :return:
    """
    def poly(num):
        """

        :param num:
        :return:
        """
        res = 0
        for index, item in enumerate(coffs):
            res += item * num ** index
        return res
        #return sum(cof * num ** index for index, cof in enumerate(coffs))
    return poly

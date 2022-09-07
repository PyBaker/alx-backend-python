#!/usr/bin/env python3
''' Description: takes a list mxd_lst of floats and integers and
    returns their sum as a float.
    Arguments: mxd_lst: list[Union[int, float]]
'''

from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    ''' Return sum of elements of mxd_list. '''
    return sum(mxd_lst)

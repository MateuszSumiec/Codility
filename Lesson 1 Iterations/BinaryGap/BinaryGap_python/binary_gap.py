# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:53:06 2018
Edited on Sun Nov 25 16:42 2018
@author: Mateusz
"""


def solution(N):
    """
    Returns maximum length of a sequence of 0's
    bounded by 1's in binary representation of an integer.
    N is an integer within the range [1..2 147 483 647]
    """
    binaryN = bin(N)[2:].split('1')

    binaryN.remove(binaryN[-1])

    return len(max(binaryN, default=0))

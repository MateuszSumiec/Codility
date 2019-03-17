# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 01:10:54 2019

@author: Mateusz
"""


def solution(X, A):
    """
    Decides the first possible time when "frog" can jump
    to other bank of the river.

    len(A) and X are integers within the range [1,..., 100 000];
    Each element of array A is an integer within the range [1, ..., X].
    """
    count = [0] * X
    leaf = 0
    for index, element in enumerate(A):
        if count[element - 1] == 0:
            leaf += 1

        count[element - 1] += 1
        if leaf == X:
            return index
    else:
        return -1

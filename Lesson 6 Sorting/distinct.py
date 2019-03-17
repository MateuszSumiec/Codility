# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:03:24 2019

@author: Mateusz
"""


def solution(A):
    """
    Returns distinct values of array A.

    A[k] in [−1 000 000, ..., 1 000 000] for k in [0..100,000].
    """
    return sorted(A)


A = [2, 1, 1, 2, 3, 1]
print(solution(A))

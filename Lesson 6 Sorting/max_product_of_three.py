# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:17:23 2019

@author: Mateusz
"""


def solution(A):
    """
    Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).

    A[k] is an integer within the range [−1 000, ..., 1 000]
    for k in in [3..100,000].
    """
    if len(A) > 2:
        sorted_A = sorted(A)
        return max(sorted_A[0] * sorted_A[1] * sorted_A[-1],
                   sorted_A[-1] * sorted_A[-2] * sorted_A[-3])

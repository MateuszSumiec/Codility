# -*- coding: utf-8 -*-
"""
@author: Mateusz
"""


def solution(A):
    """
    Returns a number in array that occurs odd number of times.
    A array of lengts [1, ..., 1 000 000];
    Each element of A is within range [1, ..., 1 000 000 000];
    One element occurs odd number of times
    """
    slownikA = dict(zip(set(A), [0] * len(A)))

    for i in A:
        slownikA[i] += 1

    for i in A:
        if slownikA[i] % 2:
            return i

    return None

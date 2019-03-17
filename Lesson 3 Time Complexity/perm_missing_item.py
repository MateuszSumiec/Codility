# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:03:24 2019

@author: Mateusz
"""


def solution(A):
    """
    Returns item that doesn't occurs in an array A.
    len(A) is an integer within the range [0, ..., 100 000];
    The elements of A are all distinct;
    Each element of array A is an integer within the range [1, ..., (N + 1)]
    """
    return sum(range(len(A)+2)) - sum(A)

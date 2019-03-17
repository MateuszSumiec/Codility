# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 15:30:09 2019
# 100%, level: Medium
@author: Mateusz
"""


from math import floor


def solution(A, B, K):
    """
    Returns number of dividers by K within the range [A, ..., B]
    A and B (A <= B) are integers within the range [0, ..., 2 000 000 000];
    K is an integer within the range [1, ..., 2 000 000 000];
    """
    divisions = floor(B / K) - floor(A / K)
    if A % K == 0:
        return divisions + 1
    else:
        return divisions

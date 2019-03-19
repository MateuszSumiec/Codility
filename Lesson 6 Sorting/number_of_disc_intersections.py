# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:45:03 2019

@author: Mateusz
"""


def solution(A):
    """
    Returns number of intersecting discs with different centers.
    A[k] is a radius in [0, ..., 2 147 483 647]
    for disc k in [0, ..., 100 000].
    """
    count = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if (j-A[j] <= i-A[i] <= j+A[j]) or (j-A[j] <= i+A[i] <= j+A[j]) or ((i-A[i] <= j-A[j]) and (j+A[j] <= i+A[i])):
                count += 1
    return count


B = [1, 1, 1]

print('sol B ', solution(B))

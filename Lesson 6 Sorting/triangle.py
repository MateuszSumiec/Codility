# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:49:14 2019

@author: Mateusz
"""


def is_triangle(A, p, q, r):
    """
    Returns 1 if a triangle can be constructed, 0 otherwise.
    """
    if (A[p] + A[q] > A[r]) and (A[q] + A[r] > A[p]) and (A[r] + A[p] > A[q]):
        return 1
    else:
        return 0


def solution(A):
    """
    Returns 1 if there exist a constructable triangle in A, 0 otherwise.

    A[k] is an integer within the range [−2,147,483,648..2,147,483,647],
    for k in [0..100,000]
    """
    sorted_A = sorted(A)
    for i in range(len(A) - 2):
        if is_triangle(sorted_A, i, i + 1, i + 2) == 1:
            return 1
    else:
        return 0


assert solution([10, 2, 5, 1, 8, 20]) == 1, "not a triangle"
assert solution([10, 50, 5, 1]) == 0, "not a triangle"
assert solution([0, 1, 0.5, 0.5, 1, 0, 0.5]) == 1, "not a triangle"

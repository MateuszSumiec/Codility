# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 23:01:01 2019

@author: Mateusz
"""
def solution(A):
    """
    Returns the minimal absolute value of difference between splitted parts of array.
    
    len(A) is  within the range [2, ..., 100 000];
    each element of array A is an integer within the range [−1,000..1,000].
    """
    if A:
        suma = A[0] - sum(A[1:])
        best = abs(suma)
        for i in range(len(A) - 2):
            suma += 2 * A[i+1]
            if abs(suma) <= abs(best):
                best = suma
        return abs(best)
    else:
        return -1

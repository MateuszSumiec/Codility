# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 23:01:01 2019

@author: Mateusz
"""
def solution(A):
    # write your code in Python 3.6
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

    

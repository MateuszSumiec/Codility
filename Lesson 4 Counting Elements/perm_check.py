# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:57:07 2019

@author: Mateusz
"""


def solution(A):
    if A:
        if max(A) > len(A):
            return 0
        else:
            count = [0] * len(A)

        for integer in A:
            if count[integer - 1] > 1:
                return 0

            count[integer - 1] += 1

        for check in count:
            if check == 0:
                return 0
        else:
            return 1


A = [1, 1]
print(solution(A))

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 01:10:54 2019

@author: Mateusz
"""


def solution(X, A):
    count = [0] * X
    leaf = 0
    for index, element in enumerate(A):
        if count[element - 1] == 0:
            leaf += 1

        count[element - 1] += 1
        if leaf == X:
            return index
    else:
        return -1


print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))

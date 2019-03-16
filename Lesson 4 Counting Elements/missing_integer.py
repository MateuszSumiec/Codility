# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:35:43 2019

@author: Mateusz
"""


def solution(A):
    count_int = [0] * (max(A)+1)
    for index, element in enumerate(A):
        if element > 0:
            count_int[element] += 1

    if count_int == []:
        return 1

    for index, element in enumerate(count_int[1:]):
        if element == 0:
            return index + 1
    else:
        return len(count_int)

    return 1


A = [1, 2, 3]
print(solution(A))

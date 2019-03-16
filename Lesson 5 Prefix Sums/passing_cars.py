# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:55:20 2019

@author: Mateusz
"""


def solution(A):
    if not A:
        return 0
    elif A[0] == 1:
        return solution(A[1:])
    else:
        count_passing_cars = 0
        count_ones = 0
        for car in A[::-1]:
            if car == 1:
                count_ones += 1
            elif car == 0:
                count_passing_cars += count_ones
            if count_passing_cars > 1000000000:
                return -1
    return count_passing_cars


A = [0, 1, 0, 1, 1] * 1000000
print(solution(A))

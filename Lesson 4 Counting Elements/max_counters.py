# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 20:57:50 2019

@author: Mateusz
"""
import numpy as np


def solution(N, A):
    # write your code in Python 3.6
    counters = [0] * N
    max_counter = 0
    for element in A:
        if element <= N:
            counters[element - 1] += 1

            if max_counter < counters[element - 1]:
                max_counter = counters[element - 1]

        elif element == N + 1:
            counters = [max_counter] * N

    return counters


B = np.random.randint(0, 10, 10)
A = [3, 4, 4, 6, 1, 4, 4]
print('solution A: {} is {}'.format(A, solution(5, A)))
print()
print('solution B: {} is {}'.format(B, solution(6, B)))

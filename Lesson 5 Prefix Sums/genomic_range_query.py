# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:54:24 2019

@author: Mateusz
"""

nucleotide_dict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
S = 'CAGCCTA'
P = [2, 5, 0]
Q = [4, 5, 6]


def solution(S, P, Q):
    # write your code in Python 3.6
    nucleotide_dict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    minimal_list = []
    for query in range(min(len(P), len(Q))):
        minimal_query = 4
        for bound in range(P[query], Q[query] + 1):
            if minimal_query > nucleotide_dict[S[bound]]:
                minimal_query = nucleotide_dict[S[bound]]
        minimal_list.append(minimal_query)
    return minimal_list


print(solution(S, P, Q))

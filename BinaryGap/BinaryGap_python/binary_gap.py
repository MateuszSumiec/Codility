# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:53:06 2018
Edited on Sun Nov 25 16:42 2018
@author: Mateusz
"""

def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:].split('1')
    
    if (binary[-1] != ''):
        binary.remove(binary[-1])
    
    return len(max(binary))


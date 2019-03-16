# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:53:06 2018
Edited on Sun Nov 25 16:42 2018
@author: Mateusz
"""

def solution(N):
    binaryN = bin(N)[2:].split('1')
    
    if (binaryN[-1] != ''):
        binaryN.remove(binaryN[-1])
    
    return len(max(binaryN))


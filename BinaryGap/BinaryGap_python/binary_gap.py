def solution(A, K):
    # write your code in Python 3.6
    if A:
        return A[(len(A)-K) % len(A):] + A[:(len(A)-K) % len(A)]
    else:
        return A

def solution(A, K):
    if A:
        return A[(len(A)-K) % len(A):] + A[:(len(A)-K) % len(A)]
    else:
        return A

def solution(A, K):
    """
    Rotate an array A to the right by given number of steps K.
    len(A) and K are integers within the range [0..100];
    Each element of array A is an integer within the range [−1 000..1 000].
    """
    if A:
        return A[(len(A)-K) % len(A):] + A[:(len(A)-K) % len(A)]
    else:
        return A

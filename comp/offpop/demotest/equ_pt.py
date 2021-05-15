# equilibrium point

def solution(A):
    # write your code in Python 2.7
    tot = sum(A)
    left = 0
    for i in range(len(A)):
        if tot - A[i] == 2 * left:
            return i
        else:
            left += A[i]
    return -1

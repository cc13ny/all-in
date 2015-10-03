# O(n log n)
# Challenge: O(n)

def solution(A):
    origin = A[:]
    A.sort()

    cnt = 0
    for i in range(len(A)):
        if A[i] != origin[i]:
            cnt += 1
    if cnt == 0 or cnt == 2:
        return True
    return False

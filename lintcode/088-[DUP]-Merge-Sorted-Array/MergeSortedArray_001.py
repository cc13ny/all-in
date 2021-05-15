class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """

    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        for k in range(m - 1, -1, -1):
            A[k + n] = A[k]

        i, j, idx = n, 0, 0
        while i < m + n and j < n:
            if A[i] > B[j]:
                A[idx] = B[j]
                j += 1
            else:
                A[idx] = A[i]
                i += 1
            idx += 1

        while j < n:
            A[idx] = B[j]
            j += 1
            idx += 1

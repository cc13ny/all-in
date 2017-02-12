class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, q, n = len(A), len(B), len(B[0])
        # C = [[0] * n] * m
        C = [[0] * n for _ in range(m)]
        for i in range(m):
            for k in range(q):
                if A[i][k]:
                    for j in range(n):
                        if B[k][j]:
                            C[i][j] += A[i][k] * B[k][j]
        return C

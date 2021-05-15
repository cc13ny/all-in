class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: Cosine similarity.
    """

    def cosineSimilarity(self, A, B):
        # write your code here
        from math import sqrt

        a, b, ab = 0.0, 0.0, 0.0

        for i in range(len(A)):
            a += A[i] * A[i]
            b += B[i] * B[i]
            ab += A[i] * B[i]

        if a == 0 or b == 0:
            return 2.0000
        a, b = sqrt(a), sqrt(b)

        return ab / (a * b)

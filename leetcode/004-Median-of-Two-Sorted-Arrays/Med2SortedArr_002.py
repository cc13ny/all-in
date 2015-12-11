class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        m, n = len(A), len(B)
        if (m + n) % 2 == 0:
            l = self.findK(A, B, (m + n) / 2)
            r = self.findK(A, B, (m + n) / 2 + 1)
            return (l + r) / 2.0
        else:
            return self.findK(A, B, (m + n) / 2 + 1)

    def findK(self, A, B, k):
        m, n = len(A), len(B)
        if m == 0:
            return B[k - 1]
        if n == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])

        if m < k / 2:
            return self.findK(A, B[k / 2:], k - k / 2)
        if n < k / 2:
            return self.findK(A[k / 2:], B, k - k / 2)

        if A[k / 2 - 1] < B[k / 2 - 1]:
            return self.findK(A[k / 2:], B, k - k / 2)
        else:
            return self.findK(A, B[k / 2:], k - k / 2)

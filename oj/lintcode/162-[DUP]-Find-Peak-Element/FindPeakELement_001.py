class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        l, r = 1, len(A) - 2
        while l <= r:
            m = (l + r) / 2
            if A[m - 1] >= A[m]:
                r = m - 1
            elif A[m] <= A[m + 1]:
                l = m + 1
            else:
                return m

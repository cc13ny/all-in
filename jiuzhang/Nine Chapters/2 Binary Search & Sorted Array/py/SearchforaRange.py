class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        res = []

        l, r = 0, len(A) - 1
        while l <= r:
            m = (l + r) / 2
            if A[m] >= target:
                r = m - 1
            else:
                l = m + 1
        res.append(l)

        l, r = 0, len(A) - 1
        while l <= r:
            m = (l + r) / 2
            if A[m] > target:
                r = m - 1
            else:
                l = l + 1
        res.append(r)

        if res[0] > res[1]: return [-1, -1]

        return res

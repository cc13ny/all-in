class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        l, r = 0, len(A) - 1
        while l <= r:
            m = (l + r) / 2
            if A[m] == target:
                return m
            elif A[m] > target:
                r = m - 1
            else:
                l = m + 1
        return l

sl = Solution()
A = [1, 3, 5, 6]
target = [5, 2, 7, 0]
for t in target:
    print sl.searchInsert(A, t)

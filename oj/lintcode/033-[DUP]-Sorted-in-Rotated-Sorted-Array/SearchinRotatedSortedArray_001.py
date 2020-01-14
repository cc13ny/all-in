class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        l, r = 0, len(A) - 1
        while l <= r:
            m = (l + r) / 2
            if A[m] == target:
                return m
            elif A[m] < A[r]:
                if A[m] < target <= A[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if A[l] <= target < A[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

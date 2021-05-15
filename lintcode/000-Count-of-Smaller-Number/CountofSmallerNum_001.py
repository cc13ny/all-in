class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """

    def binSearch(self, nums, q):
        if len(nums) == 0 or nums[-1] < q:
            return len(nums)
        l, r, res = 0, len(nums) - 1, 0
        while l <= r:
            m = (l + r) / 2
            if nums[m] < q:
                res += m + 1 - l
                l = m + 1
            else:
                r = m - 1
        return res

    def countOfSmallerNumber(self, A, queries):
        # write your code here
        A.sort()
        res = []
        for q in queries:
            res.append(self.binSearch(A, q))
        return res

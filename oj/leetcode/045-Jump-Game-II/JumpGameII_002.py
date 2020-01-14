class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        start, end, newend = 0, nums[0], nums[0]
        for cnt in range(1, n):
            for i in range(start, end + 1):
                newend = max(i + nums[i], newend)
                if newend >= n - 1:
                    return cnt + 1 if newend > end else cnt
            start, end = end + 1, newend

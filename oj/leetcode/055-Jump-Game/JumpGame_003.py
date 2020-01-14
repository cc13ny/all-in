class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return True
        
        start, end, newend = 0, nums[0], nums[0]
        for cnt in range(1, n):
            for i in range(start, end + 1):
                newend = max(i + nums[i], newend)
                if newend >= n - 1:
                    return True
            if end == newend:
                return False
            start, end = end + 1, newend

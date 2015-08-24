class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        com = (1 + len(nums)) * len(nums) / 2
        tot = sum(nums)
        return com - tot

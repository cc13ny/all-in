class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[i], nums[j] = 0, nums[i]
                j += 1

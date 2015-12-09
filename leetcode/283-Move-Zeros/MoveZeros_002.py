class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = -1
        for i in range(len(nums)):
            if j < 0 and nums[i] == 0:
                j = i
            if j >= 0 and nums[i] != 0:
                nums[j], nums[i] = nums[i], 0
                j += 1

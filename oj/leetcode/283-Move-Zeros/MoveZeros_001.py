class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeropos = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeropos.append(i)
            elif zeropos != []:
                idx = zeropos.pop(0)
                nums[idx] = nums[i]
                nums[i] = 0
                zeropos.append(i)

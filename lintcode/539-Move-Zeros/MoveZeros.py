class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        # Write your code here
        i = 0
        for j in xrange(len(nums)):
            if nums[j]:
                num = nums[j]
                nums[j] = 0
                nums[i] = num
                i += 1

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        a = [0, 0, 0]
        for i in nums:
            if i == 0:
                a[0] += 1
            elif i == 1:
                a[1] += 1
            else:
                a[2] += 1
        
        a[1] += a[0]
        a[2] += a[1]
        for i in range(len(nums)):
            if i < a[0]:
                nums[i] = 0
            elif i < a[1]:
                nums[i] = 1
            else:
                nums[i] = 2

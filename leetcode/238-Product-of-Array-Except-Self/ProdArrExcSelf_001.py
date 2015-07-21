class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        if len(nums) < 2:
            return nums
        
        res = nums[:]
        for i in range(1, len(res)):
            res[i] *= res[i - 1]

        for j in range(len(nums) - 1, 0, -1):
            nums[j - 1] *= nums[j]
        
        res[-1] = res[-2]
        for i in range(len(res) - 2, 0, -1):
            res[i] = res[i - 1] * nums[i + 1]
        res[0] = nums[1]
        
        return res

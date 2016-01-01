class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        res, tmp = nums[0], nums[0]
        for i in range(1, len(nums)):
            tmp = max(tmp + nums[i], nums[i])
            res = max(res, tmp)

        return res

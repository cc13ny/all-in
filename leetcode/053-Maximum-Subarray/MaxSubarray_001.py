class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        minnum = nums[:]
        for i in range(1, len(nums)):
            minnum[i] = min(minnum[i - 1], nums[i - 1], 0)

        for i in range(1, len(nums)):
            nums[i] -= minnum[i]

        return max(nums)

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        tmp = [False] * len(nums)
        tmp[-1] = True
        nearestrue = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nearestrue <= min(i + nums[i], len(nums) - 1):
                tmp[i] = True
                nearestrue = i
        return tmp[0]

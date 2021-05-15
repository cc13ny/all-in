class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]

        res = []
        for i in range(len(nums)):
            tmp = nums[:i] + nums[i + 1:]
            sub = self.permute(tmp)
            res.extend([[nums[i]] + s for s in sub])

        return res

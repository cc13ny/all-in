class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        if len(nums) == 1:
            return [nums]
    
        res, bag = [], set()
        for i in range(len(nums)):
            if nums[i] not in bag:
                bag.add(nums[i])
                tmp = nums[:i] + nums[i+1:]
                sub = self.permuteUnique(tmp)
                res.extend([[nums[i]] + s for s in sub])

        return res

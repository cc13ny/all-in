class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        if len(nums) == 1:
            return [nums]
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            sym = nums[i]
            tmp = nums[:i] + nums[i+1:]
            sub = self.permuteUnique(tmp)
            res.extend([[nums[i]] + s for s in sub])
            while i < len(nums):
                if nums[i] != sym:
                    break
                i += 1
        return res

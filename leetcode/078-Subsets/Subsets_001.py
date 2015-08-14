class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.sort()
        res = [[]]
        for i in range(1, len(nums) + 1):
            res += self.subset(i, nums)
        return res
    
    def subset(self, i, nums):
        if i == 0:
            return [[]]
        
        res = []
        for j in range(len(nums) - i + 1):
            tmp = self.subset(i - 1, nums[j + 1:])
            for t in tmp:
                res.append([nums[j]] + t)
        return res

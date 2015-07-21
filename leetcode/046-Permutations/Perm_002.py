class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if len(nums) == 0:
            return nums
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            tmp = nums[:]
            head = tmp.pop(i)
            tail = self.permute(tmp)
            
            [ t.insert(0, head) for t in tail]
            res.extend(tail[:])
        return res

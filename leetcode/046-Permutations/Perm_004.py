class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        
        if len(nums) == 1:
            return [ nums ]
        
        n = nums[:len(nums) - 1]
        pre = self.permute(n)
        res = []
        m = len(nums) - 1
        a = nums[len(nums) - 1]
        
        for row in pre:
            for i in range(m+1):
                tmp = row[:]
                tmp.insert(i, a)
                res.append(tmp)
                
        return res

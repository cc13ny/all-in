class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        cumnums = [0] + nums
        n = len(cumnums)
        for i in range(1, n):
            cumnums[i] += cumnums[i - 1]
        
        minnum = 0
        res = cumnums[1]
        for i in range(2, n):
            if cumnums[i - 1] < minnum:
                minnum = cumnums[i - 1]
            if cumnums[i] - minnum > res:
                res = cumnums[i] - minnum
        return res

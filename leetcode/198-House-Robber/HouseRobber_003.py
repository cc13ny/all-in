class Solution:
    # @param {integer[]} nums
    # @return {integer}

    def rob(self, nums):
        res = [0, 0] + nums
        for i in range(2, len(res)):
            res[i] = max(res[i] + res[i - 2], res[i - 1])
        return res[len(res) - 1]

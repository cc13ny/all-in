'''
  Based on sol in http://www.cnblogs.com/grandyang/p/4650187.html
  It's pretty awsesome in details so I have to comment them
'''


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        res = [1] * len(nums)  # The key point is that res[0] should be 1
        for i in range(1, len(res)):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1  # Avoid using res[-1] in case of res == []
        for j in range(len(res) - 1, -1, -1):
            res[j] *= right
            right *= nums[j]

        return res

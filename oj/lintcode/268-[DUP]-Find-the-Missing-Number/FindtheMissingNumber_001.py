class Solution:
    # @param nums: a list of integers
    # @return: an integer
    def findMissing(self, nums):
        # write your code here
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)

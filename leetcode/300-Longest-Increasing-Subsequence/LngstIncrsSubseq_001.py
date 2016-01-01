class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 0:
            return 0
        
        maxlen = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i] and maxlen[j] + 1 > maxlen[i]:
                    maxlen[i] = maxlen[j] + 1

        return max(maxlen)

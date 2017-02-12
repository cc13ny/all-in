'''
  a possible more efficient solution: 
    https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/?tab=Solutions
'''

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mx, sm = 0, 0
        map = {0: -1}
        for i in range(len(nums)):
            sm += nums[i]
            if (sm - k) in map:
                mx = max(mx, i - map[sm -k])
            if sm not in map:
                map[sm] = i
        return mx

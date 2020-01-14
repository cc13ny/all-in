class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, tot, first_idx = 0, 0, {0: -1}
        for i in range(len(nums)):
            tot += 1 if nums[i] else -1
            if tot in first_idx:
                res = max(res, i - first_idx[tot]
            else:
                first_idx[tot] = i
        return res

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 1, len(nums) - 1
        while l < r:
            m = l + (r - l) / 2
            cnt = 0
            for num in nums:
                if num <= m:
                    cnt += 1
            print l, r, m
            if cnt > m:
                r = m
            else:
                l = m + 1
        return l

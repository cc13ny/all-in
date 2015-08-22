class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0
        tmp, res = 0, len(nums)
        if sum(nums) < s:
            return 0
        while j < len(nums):
            if tmp < s:
                tmp += nums[j]
                j += 1
            else:
                while tmp >= s:
                    tmp -= nums[i]
                    i += 1
                if j - i + 1 < res:
                    res = j - i + 1
        while tmp >= s:
            tmp -= nums[i]
            i += 1
            if j - i + 1 < res:
                res = j - i + 1
        return res

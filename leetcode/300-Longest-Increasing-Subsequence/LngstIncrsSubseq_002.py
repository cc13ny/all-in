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
        dq = [nums[0]]
        for i in range(1, n):
            if dq[-1] < nums[i]:
                dq.append(nums[i])
            elif dq[0] > nums[i]:
                dq[0] = nums[i]
            else:
                l, r = 0, len(dq) - 1
                while l <= r:
                    m = l + (r - l) / 2
                    if dq[m] >= nums[i]:
                        r = m - 1
                    else:
                        l = m + 1
                dq[l] = nums[i]

        return len(dq)

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        res = 0
        ma = sum(nums)
        tmp = [0] * (2 * ma + 1)
        cnt = tmp[:]
        cnt[ma] = 1
        for num in nums:
            for i in range(len(cnt)):
                if cnt[i]:
                    tmp[i + num] += cnt[i]
                    tmp[i - num] += cnt[i]
            cnt = tmp[:]
            tmp = [0] * (2 * ma + 1)
        if -ma <= S <= ma:
            res = cnt[S + ma]
        return res

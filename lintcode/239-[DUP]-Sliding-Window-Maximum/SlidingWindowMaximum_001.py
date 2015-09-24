class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums == []:
            return []
        dq = [(nums[0], 0)]
        for i in range(1, k):
            while dq != [] and nums[i] > dq[-1][0]:
                dq.pop()
            dq.append((nums[i], i))
        res = [dq[0][0]]
        for j in range(k, len(nums)):
            if dq[0][1] < j - k + 1:
                dq.pop(0)
            while dq != [] and nums[j] > dq[-1][0]:
                dq.pop()
            dq.append((nums[j], j))
            res.append(dq[0][0])
        return res

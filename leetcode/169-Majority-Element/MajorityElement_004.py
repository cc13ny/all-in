class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, cnt = 0, 1
        for i in xrange(1, len(nums)):
            if nums[i] == nums[idx]:
                cnt += 1
            else:
                cnt -= 1

            if not cnt:
                idx = i
                cnt = 1
        return nums[idx]

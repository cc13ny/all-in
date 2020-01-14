class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num, cnt = nums[0], 1
        for i in xrange(1, len(nums)):
            if nums[i] == num:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt == 0:
                num = nums[i]
                cnt = 1
        return num

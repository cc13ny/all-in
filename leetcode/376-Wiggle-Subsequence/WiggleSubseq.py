class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        res = 0
        for i in xrange(1, len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i+1], nums[i] = nums[i], nums[i - 1]
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                res += 1
            if nums[i-1] > nums[i] and nums[i] < nums[i+1]:
                res += 1
        if res or nums[0] != nums[-1]:
            res += 2
        else:
            res = 1
        return res

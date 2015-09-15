class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
        if nums[l] == target:
            return l
        return -1

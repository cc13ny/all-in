class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) / 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                if nums[m] > nums[r] and target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] < nums[r] and target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1

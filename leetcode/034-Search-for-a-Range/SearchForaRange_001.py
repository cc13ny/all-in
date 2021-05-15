class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        res = []
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        res.append(l)

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1
        res.append(r)

        res = [-1, -1] if res[0] > res[1] else res

        return res

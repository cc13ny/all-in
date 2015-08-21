class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        tb = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in tb:
                tb[num] = i
            elif i - tb[num] <= k:
                return True
            else:
                tb[num] = i
        return False

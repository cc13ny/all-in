class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        nearestrue = n - 1

        for i in range(n - 1, -1, -1):
            if i + nums[i] >= nearestrue:
                nearestrue = i
        return nearestrue == 0

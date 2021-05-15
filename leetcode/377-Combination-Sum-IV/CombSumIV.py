class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def func(nums, target, combSum):
            res = 0
            if target < 0 or target in combSum:
                return combSum
            for num in nums:
                combSum = func(nums, target - num, combSum)
                res += combSum.get(target - num, 0)
            combSum[target] = res
            return combSum

        return func(nums, target, {0: 1})[target]

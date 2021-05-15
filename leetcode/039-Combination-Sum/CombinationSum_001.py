class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        candidates.sort()
        return self.combsum(candidates, target)

    def combsum(self, nums, target):
        if target == 0:
            return [[]]
        if not nums or nums[0] > target or target < 1:
            return []

        res = []
        for i in range(len(nums)):
            num = nums[i]
            pre = [num]
            t = target
            while t >= num:
                t -= num
                subs = self.combsum(nums[i + 1:], t)
                for sub in subs:
                    res.append(pre + sub)
                pre += [num]
        return res

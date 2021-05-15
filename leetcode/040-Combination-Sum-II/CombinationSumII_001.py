# Node simplification, improvement & optimization
# How, it's good because it can be done on the original code of "Combination Sum"

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates.sort()
        return self.combsum(candidates, target)

    def combsum(self, nums, target):
        if target == 0:
            return [[]]
        if not nums or nums[0] > target or target < 1:
            return []

        res = []
        i = 0
        while i < len(nums):
            num = nums[i]
            cnt = 1
            while i + cnt < len(nums) and nums[i + cnt] == num:
                cnt += 1
            j = i + cnt
            pre = [num]
            t = target
            while t >= num and cnt > 0:
                t -= num
                cnt -= 1
                subs = self.combsum(nums[j:], t)
                for sub in subs:
                    res.append(pre + sub)
                pre += [num]
            i = j
        return res

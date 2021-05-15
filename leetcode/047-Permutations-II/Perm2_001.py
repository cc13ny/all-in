class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        if len(nums) == 0:
            return nums
        if len(nums) == 1:
            return [nums]

        res = []
        bag = set()
        for i in range(len(nums)):
            if nums[i] not in bag:
                tmp = nums[:]
                head = tmp.pop(i)
                tail = self.permuteUnique(tmp)
                [t.insert(0, head) for t in tail]
                res.extend(tail)
                bag.add(nums[i])

        return res

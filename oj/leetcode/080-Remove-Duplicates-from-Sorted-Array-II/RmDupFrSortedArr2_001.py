class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) < 3:
            return len(nums)
        cnt = 2
        tmp = nums[0]
        res = 0
        p = 0

        for i in range(len(nums)):
            if nums[i] == tmp and cnt > 0:
                res += 1
                nums[p] = nums[i]
                p += 1
                cnt -= 1
            elif nums[i] != tmp:
                tmp = nums[i]
                res += 1
                nums[p] = nums[i]
                p += 1
                cnt = 1
        return res

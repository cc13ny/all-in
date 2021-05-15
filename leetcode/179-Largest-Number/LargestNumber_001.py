class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = sorted(nums, cmp=self.compare)
        res, j = '', 0
        for i in range(len(nums) - 1):
            if nums[i] != 0:
                break
            else:
                j += 1
        for k in range(j, len(nums)):
            res += str(nums[k])

        return res

    def compare(self, x, y):
        tmp1, tmp2 = str(x) + str(y), str(y) + str(x)
        res = 0
        if tmp1 > tmp2:
            res = -1
        elif tmp1 < tmp2:
            res = 1
        return res

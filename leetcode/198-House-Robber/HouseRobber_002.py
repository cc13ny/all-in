class Solution:
    # @param {integer[]} nums
    # @return {integer}

    def robaux(self, nums, aux):
        i = len(nums) - 1

        if i < 0:
            return 0

        if aux[i] > -1:
            return aux[i]

        if i == 0:
            return nums[0]

        aux[i] = max(nums[0] + self.robaux(nums[2:], aux),
                     nums[1] + self.robaux(nums[3:], aux))

        return aux[i]

    def rob(self, nums):
        aux = [-1] * len(nums)

        return self.robaux(nums, aux)

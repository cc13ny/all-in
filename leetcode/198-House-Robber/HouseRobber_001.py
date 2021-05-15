class Solution:
    # @param {integer[]} nums
    # @return {integer}

    def robaux(self, i, j, nums, aux):
        n = len(nums)

        if (0 <= i < n and 0 <= j < n) == False:
            return 0

        if aux[i][j] > -1:
            return aux[i][j]

        if i == j:
            return nums[i]

        aux[i][j] = max(nums[i] + self.robaux(i + 2, j, nums, aux),
                        nums[i + 1] + self.robaux(i + 3, j, nums, aux))

        return aux[i][j]

    def rob(self, nums):
        if nums == []:
            return 0

        n = len(nums)

        if n == 1:
            return nums[0]

        aux = [[-1 if i <= j else 0 for j in range(n)] for i in range(n)]

        return self.robaux(0, n - 1, nums, aux)

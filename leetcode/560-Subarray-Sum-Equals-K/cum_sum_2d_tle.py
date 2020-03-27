class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        cum_sums = [0] + nums

        cnt = 0

        for i in range(len(cum_sums)):
            for j in range(i + 1, len(cum_sums)):
                if cum_sums[j] - cum_sums[i] == k:
                    cnt += 1
        return cnt
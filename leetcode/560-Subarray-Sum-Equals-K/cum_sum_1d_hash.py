class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        cum_sums = [0] + nums

        cnt = 0
        val_cnts = {0: 1}
        for i in range(1, len(cum_sums)):
            diff = cum_sums[i] - k
            if diff in val_cnts:
                cnt += val_cnts[diff]
            val_cnts[cum_sums[i]] = val_cnts.get(cum_sums[i], 0) + 1

        return cnt
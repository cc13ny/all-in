class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        a, b = nums[:], nums[:]
        n = len(nums)
        
        tmp, res = nums[0], nums[0]
        for i in range(1, n):
            tmp = max(tmp + nums[i], nums[i])
            res = max(res, tmp)
            a[i] = res
        
        tmp, res = nums[-1], nums[-1]
        for i in range(n - 2, -1, -1):
            tmp = max(tmp + nums[i], nums[i])
            res = max(res, tmp)
            b[i] = res
        
        mx = a[0] + b[1]
        for i in range(1, n - 1):
            mx = max(mx, a[i] + b[i + 1])

        return mx

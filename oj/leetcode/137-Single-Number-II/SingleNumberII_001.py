# Have to handle two many details for negative numbers


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        count = [0] * 32
        for i in range(32):
            for j in range(len(nums)):
                if (abs(nums[j]) >> i) & 1:
                    count[i] = (count[i] + 1) % 3
            res |= count[i] << i

        signs = {}
        for j in range(len(nums)):
            num = nums[j]
            if num not in signs:
                signs[num] = 1 if num > 0 else -1
            else:
                signs[num] += 1 if num > 0 else -1
        for k in signs:
            if abs(signs[k]) == 1:
                break
        return signs[k] * res

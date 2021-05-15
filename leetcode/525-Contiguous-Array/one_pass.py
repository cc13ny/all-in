# 2/18/17 (better)
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, tot, first_idx = 0, 0, {0: -1}
        for i in range(len(nums)):
            tot += 1 if nums[i] else -1
            if tot in first_idx:
                res = max(res, i - first_idx[tot])
            else:
                first_idx[tot] = i
        return res


# 4/13/19
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prev = 0
        mapping = {0: -1}  # diff:idx

        res = 0
        for i, num in enumerate(nums):
            prev += 2 * num - 1
            if prev in mapping:
                res = max(res, i - mapping[prev])
            else:
                mapping[prev] = i

        return res


## TLE
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zos = [[0, 0]]
        for num in nums:
            zos.append(zos[-1][:])
            zos[-1][num] += 1

        for l in range(int(len(nums) / 2), -1, -1):
            ln = 2 * l
            for i in range(0, len(zos) - ln):
                if zos[i + ln][0] - zos[i][0] == zos[i + ln][1] - zos[i][1]:
                    return ln
        return 0

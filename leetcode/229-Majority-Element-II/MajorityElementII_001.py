class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c1, c2, num1, num2 = 0, 0, 0, 0
        for c in nums:
            if c == c1:
                num1 += 1
            elif c == c2:
                num2 += 1
            elif num1 == 0:
                c1, num1 = c, 1
            elif num2 == 0:
                c2, num2 = c, 1
            else:
                num1 -= 1
                num2 -= 1

        num1, num2 = 0, 0
        for c in nums:
            if c == c1:
                num1 += 1
            elif c == c2:
                num2 += 1

        res = []
        if num1 > len(nums) / 3: res.append(c1)
        if num2 > len(nums) / 3: res.append(c2)

        return res

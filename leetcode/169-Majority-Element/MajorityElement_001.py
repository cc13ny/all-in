class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        candidate1, count1 = None, 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif count1 == 0:
                count1 += 1
                candidate1 = num
            else:
                count1 -= 1
        return candidate1

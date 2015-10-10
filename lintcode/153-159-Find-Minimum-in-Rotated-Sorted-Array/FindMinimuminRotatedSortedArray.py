class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        l, r = 0, len(num) - 1
        while l <= r:
            m = (l + r) /2
            if num[m] < num[r]:
                r = m
            else:
                l = m + 1
        return num[r]

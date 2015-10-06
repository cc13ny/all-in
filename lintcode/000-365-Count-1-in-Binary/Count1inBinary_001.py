class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        cnt = 0
        while num != 0:
            cnt += num & 1
            num = num >> 1
        return cnt

class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        return num - (num - 1) / 9 * 9 if num else 0

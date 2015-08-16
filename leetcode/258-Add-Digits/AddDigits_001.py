# Ref: https://en.wikipedia.org/wiki/Digital_root

class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        if num == 0:
            return 0
        return num - (num - 1) / 9 * 9

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False

        left, right = 10, 1
        while left <= x:
            left *= 10
        left /= 10

        while right < left:
            l = (x / left) % 10
            r = (x / right) % 10
            if l != r:
                return False
            left /= 10
            right *= 10

        return True

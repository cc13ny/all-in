class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        tmp, left, right = x, 1, 1
        while tmp > 9:
            tmp /= 10
            left *= 10

        while right < left:
            l = (x / left) % 10
            r = (x / right) % 10
            if l == r:
                left /= 10
                right *= 10    
            else:
                return False
        
        return True

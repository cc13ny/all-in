class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        if n == 0:
            return False
        
        a, b = True, True

        for i in range(2, n):
            c = not (a and b)
            a, b = b, c

        return b

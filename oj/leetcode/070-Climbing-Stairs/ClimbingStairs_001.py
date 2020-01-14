class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        a = [0, 1]
        for i in range(n):
            a += [a[i] + a[i+1]]
            
        return a[-1]

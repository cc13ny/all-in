class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n < 0: 
            return 1 / self.pow(x, -n)
        return self.pow(x, n)
        
    def pow(self, x, n):
        if n == 0:
            return 1
        half = self.pow(x, n/2)
        if n % 2 == 0:
            return half * half
        return half * half * x

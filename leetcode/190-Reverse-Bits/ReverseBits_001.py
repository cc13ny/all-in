class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        a = bin(n)[2:].zfill(32)
        
        num = len(a)
        res = ''
        
        for i in range(num - 1, -1, -1):
            res = res + a[i]
        
        return int(res, 2)

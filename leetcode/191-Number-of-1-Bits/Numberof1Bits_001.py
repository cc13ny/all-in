class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        a = bin(n)
        b = a[2:]
        c = b.split('0')
        sm = 0

        for d in c:
            sm += len(d)

        return sm

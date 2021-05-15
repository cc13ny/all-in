class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        alen, blen = len(a), len(b)
        if alen > blen:
            b = '0' * (alen - blen) + b
            nlen = alen
        else:
            a = '0' * (blen - alen) + a
            nlen = blen

        res, c = '', 0
        for i in range(nlen - 1, -1, -1):
            at, bt = int(a[i]), int(b[i])
            if at + bt + c > 1:
                res = str(at + bt + c - 2) + res
                c = 1
            else:
                res = str(at + bt + c) + res
                c = 0

        if c == 1:
            res = '1' + res
        return res

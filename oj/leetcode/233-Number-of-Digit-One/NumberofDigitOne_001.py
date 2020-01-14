class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        res, d = 0, 10
        while 10 * n >= d:
            t = d / 10
            r = n % d
            res += n / d * t
            if t - 1 < r < 2 * t - 1:
                res += r - t + 1
            elif 2 * t - 1 <= r:
                res += t
            d *= 10
        return res

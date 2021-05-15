class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        minn = prices[:-1]
        maxn = prices[1:]

        mi = minn[0]
        for i in range(1, len(minn)):
            if minn[i] > mi:
                minn[i] = mi
            else:
                mi = minn[i]

        ma = maxn[-1]  # the last element
        for i in range(len(maxn) - 1, 0, -1):
            if maxn[i] > ma:
                ma = maxn[i]
            else:
                maxn[i] = ma

        res = 0
        for i in range(len(maxn)):
            if maxn[i] - minn[i] > res:
                res = maxn[i] - minn[i]
        return res

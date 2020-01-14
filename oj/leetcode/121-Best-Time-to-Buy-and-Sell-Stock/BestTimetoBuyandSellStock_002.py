class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
            
        res, minval = 0, prices[0]
        
        for price in prices:
            tmp = price - minval
            
            if tmp < 0:
                minval = price
            elif tmp > res:
                res = tmp
        return res

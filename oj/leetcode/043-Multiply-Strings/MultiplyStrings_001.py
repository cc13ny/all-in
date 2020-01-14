class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0] * (len(num1) + len(num2))
        for j in xrange(len(num2)):
            for i in xrange(len(num1)):
                t = int(num1[- i - 1]) * int(num2[- j - 1])
                res[i + j] += t
                
        for k in xrange(len(res) - 1):
            res[k + 1] += res[k] / 10
            res[k] %= 10
       
        result = ''
        for num in res:
            result = str(num) + result
        return result.lstrip('0')

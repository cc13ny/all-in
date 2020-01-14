class Solution:
    # @param {integer} n
    # @return {string[]}
    def gen(self, lcnt, rcnt):
        if lcnt == 0:
            return [')'*rcnt]
        tmp1 = self.gen(lcnt - 1, rcnt)
        res1 = ['(' + t for t in tmp1]
        if lcnt <= rcnt - 1:
            tmp2 = self.gen(lcnt, rcnt - 1)
            res2 = [')' + t for t in tmp2]
        else:
            res2 = []
        
        return res1 + res2
        
    def generateParenthesis(self, n):
        tmp = self.gen(n - 1, n)
        res = [ '(' + t for t in tmp]
        return res

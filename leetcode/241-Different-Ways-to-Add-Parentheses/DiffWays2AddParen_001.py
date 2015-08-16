# code not optimized which can be optimized easily by DP

class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        s = input
        t = s.split()
        s = ''.join(t)
        if s.isdigit():
            return [int(s)]
        res = []
        for i in range(len(s)):
            if not s[i].isdigit():
                res1 = self.diffWaysToCompute(s[:i])
                res2 = self.diffWaysToCompute(s[i + 1:])
                for r1 in res1:
                    for r2 in res2:
                        r1, r2 = int(r1), int(r2)
                        tmp = 0
                        if s[i] == '*':
                            res.append(r1 * r2)
                        elif s[i] == '+':
                            res.append(r1 + r2)
                        else:
                            res.append(r1 - r2)
        return res

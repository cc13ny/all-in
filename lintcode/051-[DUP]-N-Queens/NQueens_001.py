# I learned a lot from programming for this prob
#   1. Obviously, it's not the optimized solution, which merely beat 3.10% person
#   2. What's more, it's still TLE if I still use SET as the element of 'cnt'
#   3. Lintcode is more restricted than Leetcode. TLE in Lintcode when n == 10 (the last case)
#   4. This code will be optimized latter based on the similar idea instead of the totally new ideas.
#   5. Interesting problem, and I have a lot of funs!

import copy


class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """

    def solveNQueens(self, n):
        if n < 1:
            return []
        cnt = [range(n) for k in range(n)]
        res = self.solve(0, cnt)
        return self.draw(res)

    def solve(self, start, cnt):
        n = len(cnt)
        res = []
        if start == n - 1:
            for k in cnt[start]:
                tmp = [-1] * n
                tmp[k] = n - 1
                res.append(tmp)
            return res

        for i in cnt[start]:
            newcnt = copy.deepcopy(cnt)
            tmp = []
            for j in range(start + 1, n):
                for k in range(3):
                    idx = i + (j - start) * (k - 1)
                    if idx in newcnt[j]:
                        newcnt[j].remove(idx)
                if len(newcnt[j]) == 0:
                    break
            tmp = [] if len(newcnt[j]) == 0 else self.solve(start + 1, newcnt)
            for t in tmp:
                t[i] = start
                res.append(t)
        return res

    def draw(self, res):
        pics = []
        for case in res:
            n = len(case)
            pic = []
            for i in range(n):
                start = case[i]
                tmp = '.' * start + 'Q' + '.' * (n - start - 1)
                pic.append(tmp)
            pics.append(pic)
        return pics

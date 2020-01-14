# I just use a tricky technique here
# Improved from 3.10% to 14.34 %
# Far from perfect, however, better
# {Leetcode : AC, Lintcode : AC}
# Based on the 001 version, and make use of the SYMMETRY of this problem

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 1:
            return []
        cnt = [range(n) for k in range(n)]
        if n == 1:
            return self.draw(self.solve(0, cnt))
        cnt[0] = range(n / 2)
        res = self.solve(0, cnt)
        m = len(res)
        if n % 2 == 1:
            cnt[0] = [n / 2]
            tmp = self.solve(0, cnt)
            res.extend(tmp)
        for i in range(m):
            res.append(res[i][::-1])
        
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

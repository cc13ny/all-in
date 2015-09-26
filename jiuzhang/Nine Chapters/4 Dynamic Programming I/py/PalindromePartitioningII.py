class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here

        n = len(s)
        if n < 2:
            return 0

        isPal = [[False for j in range(n)] for i in range(n)]

        for d in range(n):
            isPal[d][d] = True
            for l in range(1, n):
                if 0 <= d - l and d + l < n and s[d - l] == s[d + l]:
                    isPal[d - l][d + l] = True
                else:
                    break
        for d in range(n - 1):
            for l in range(n):
                if 0 <= d - l and d + 1 + l < n and s[d - l] == s[d + 1 + l]:
                    isPal[d - l][d + 1 + l] = True
                else:
                    break

        mincut = 0
        cand = set()
        isNotVisited = [True] * n
        for j in range(n):
            if isPal[0][j]:
                cand.add(j)
                isNotVisited[j] = False

        if n - 1 in cand:
            return 0

        while len(cand) != 0:
            nextcand = set()
            mincut += 1
            for c in cand:
                for nc in range(c + 1, n):
                    if isPal[c + 1][nc] and isNotVisited[nc]:
                        if nc == n - 1:
                            return mincut
                        isNotVisited[c] = False
                        nextcand.add(nc)
            cand = nextcand

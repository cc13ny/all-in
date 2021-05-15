# {Leetcode : AC, Lintcode : TLE}

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        r = [True] + [False] * len(s)
        wordDict = set(wordDict)

        for i in range(1, len(s) + 1):
            for j in range(i + 1):
                if r[j] and s[j: i] in wordDict:
                    r[i] = True
                    break
        return r[-1]

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        mi = len(min(strs, key = lambda s: len(s)))
        for j in xrange(mi):
            for i in xrange(1, len(strs)):
                if strs[i][j] != strs[i - 1][j]:
                    return strs[i][:j]

        return strs[0][:mi]

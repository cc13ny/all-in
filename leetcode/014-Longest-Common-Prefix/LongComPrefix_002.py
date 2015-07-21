#author: cchen

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        res = ''
        if strs == []:
            return res
            
        lens = [len(s) for s in strs]
        mi = min(lens)
        for i in range(mi):
            a = set([s[i] for s in strs])
            if len(a) != 1:
                break
            else:
                res+=a.pop()
        return res

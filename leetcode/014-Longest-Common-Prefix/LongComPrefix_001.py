#@author: cchen

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        prefix = ''
        
        if len(strs) == 0:
            return prefix
        if len(strs) == 1:
            return strs[0]
        
        num = len(strs)
        mi = len(strs[0])
        
        for i in xrange(num):
            if mi > len(strs[i]):
                mi = len(strs[i])
        
        flag = False
        for j in xrange(mi):
            tmp = strs[0][j]
            for i in xrange(len(strs)):
                if strs[i][j] != tmp:
                    flag = True
                    break
            if flag:
                break
            prefix = prefix + tmp
        
        return prefix

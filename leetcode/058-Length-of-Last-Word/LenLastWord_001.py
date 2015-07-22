class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        s = s.strip()
        ss = s.split()
        
        if len(ss) == 0:
            return 0
            
        res = ss[len(ss) - 1]
        
        return len(res)

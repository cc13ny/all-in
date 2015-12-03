class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def anaRepresentation(self, s):
        p = {}
        for c in s:
            if c in p:
                p[c] += 1
            else:
                p[c] = 1
        return p
        
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        p = self.anaRepresentation(s)
        q = self.anaRepresentation(t)
        
        for c in p:
            if c not in q or (c in q and p[c] != q[c]):
                return False
        
        return True

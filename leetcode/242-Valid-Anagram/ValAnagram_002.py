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

        for c in t:
            if c not in p:
                return False
            else:
                p[c] -= 1
                if p[c] < 0:
                    return False
        return True

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        m = [0] * 128
        for c in s:
            m[ord(c)] += 1

        for c in t:
            m[ord(c)] -= 1
            if m[ord(c)] < 0:
                return False
        return True

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        chs = {}
        for ch in s:
            chs[ch] = chs.get(ch, 0) + 1
        for ch in t:
            if ch not in chs or chs[ch] == 0:
                return False
            chs[ch] -= 1
        return True

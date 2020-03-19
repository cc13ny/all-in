class Solution:
    def lex_min_string(self, s):
        if len(s) < 2:
            return ''
        i = 0
        while i < len(s) - 1:
            if s[i] > s[i+1]:
                break
            i += 1
        return s[:i] + s[i+1:]
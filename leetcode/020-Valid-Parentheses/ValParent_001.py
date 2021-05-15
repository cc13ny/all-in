class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        l = ['(', '{', '[']
        r = [')', '}', ']']
        tb = {'(': ')', '{': '}', '[': ']'}

        if s == '':
            return True

        if s[0] in r:
            return False

        ls = []
        for i in range(len(s)):
            if s[i] in l:
                ls.append(s[i])
            elif s[i] in r:
                if len(ls) == 0:
                    return False
                end = ls.pop()
                if s[i] != tb[end]:
                    return False
        if len(ls) != 0:
            return False
        return True

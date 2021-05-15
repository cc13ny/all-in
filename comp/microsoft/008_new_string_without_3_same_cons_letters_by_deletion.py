class Solution:
    def new_str(self, s):
        if not s or len(s) < 3:
            return s
        res = s[0]
        cnt = 1
        i = 1
        while i < len(s):
            if s[i] == res[-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                res += s[i]
            i += 1
        return res

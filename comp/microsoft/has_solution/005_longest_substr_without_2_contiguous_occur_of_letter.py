class Solution:
    def longest_substr(self, s):
        res = []
        ac, bc = 0, 0
        start = 0
        for i, l in enumerate(s):
            if l == 'a':
                ac += 1
                bc = 0
            elif l == 'b':
                bc += 1
                ac = 0
            if ac == 3 or bc == 3 or i == len(s) - 1:
                res = [start, i - 1] if res == [] or (res[1] - res[0] < i - 1 - start) else res
                start = i - 1
                ac = 2 if l == 'a' else 0
                bc = 2 if l == 'b' else 0
        return s if res == [] else s[res[0]:res[1] + 1]

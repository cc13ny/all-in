class Solution:
    def min_moves(self, S):
        res = 0
        ac, bc = 0, 0
        for l in S:
            if l == 'a':
                ac += 1
                bc = 0
            elif l == 'b':
                bc += 1
                ac = 0
            if ac == 3 or bc == 3:
                ac, bc = 0, 0
                res += 1
        return res

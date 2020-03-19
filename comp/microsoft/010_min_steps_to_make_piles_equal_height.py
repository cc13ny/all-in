class Solution:
    def min_steps(self, piles):
        piles.sort(reverse = True)
        res = 0
        for i in range(1, len(piles)):
            if piles[i] != piles[i-1]:
                res += i
        return res
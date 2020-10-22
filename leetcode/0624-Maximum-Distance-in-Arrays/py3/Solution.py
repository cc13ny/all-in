class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res, min_val, max_val = 0, arrays[0][0], arrays[0][-1]
        for i in range(1, len(arrays)):
            l, r = arrays[i][0], arrays[i][-1]
            res = max([res, abs(r - min_val), abs(l - max_val)])
            min_val = min(min_val, l)
            max_val = max(max_val, r)
        return res
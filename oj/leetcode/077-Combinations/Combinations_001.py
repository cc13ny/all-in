class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        if k < 1 or k > n:
            return []
        if k == 1:
            return [[i] for i in range(1, n+1)]
        
        res = self.combine(n - 1, k -1)
        [i.append(n) for i in res ]
        second = self.combine(n - 1, k)
        res.extend(second)
        
        return res

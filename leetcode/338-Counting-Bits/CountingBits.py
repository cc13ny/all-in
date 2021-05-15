class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        seed = 1
        res = [0]

        while num > 0:
            res += [res[i] + 1 for i in xrange(min(num, seed))]
            num -= seed
            seed = seed << 1
        return res

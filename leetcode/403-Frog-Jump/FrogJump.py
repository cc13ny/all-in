class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        steps = {}
        for idx in stones:
            steps[idx] = set()
        steps[0] = set([1])
        for i in xrange(len(stones)):
            idx = stones[i]
            if (stones[-1] - idx) in steps[idx]:
                return True
            for s in steps[idx]:
                if (idx + s) in steps:
                    steps[idx + s].add(s + 1)
                    steps[idx + s].add(s)
                    if s > 1:
                        steps[idx + s].add(s - 1)

    return False

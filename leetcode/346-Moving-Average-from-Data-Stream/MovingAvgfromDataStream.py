class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.tot = 0
        self.size = size
        self.q = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        tot, size, q = self.tot, self.size, self.q
        q.append(val)
        tot += val
        if len(q) > size:
            tot -= q.pop(0)
        self.tot = tot
        return float(tot) / len(q)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

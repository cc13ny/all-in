class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tot, sum, start = 0, 0, 0
        for i in range(len(gas)):
            tot += gas[i] - cost[i]
            sum += gas[i] - cost[i]
            if sum < 0:
                sum = 0
                start = i + 1
        if tot < 0: return -1
        return start

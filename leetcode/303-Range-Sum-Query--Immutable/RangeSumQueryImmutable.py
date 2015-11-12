class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        csums = [0] + nums
        for i in range(len(nums)):
            csums[i + 1] += csums[i]
        self.csums = csums
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        csums = self.csums
        assert -1 < i < len(csums) and -1 < j < len(csums)
        return csums[j + 1] - csums[i]

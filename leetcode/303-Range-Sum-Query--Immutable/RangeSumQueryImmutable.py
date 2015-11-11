class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        tmp = nums[:]
        for i in range(1, len(nums)):
            tmp[i] += tmp[i - 1]
        self.ladder = tmp
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        ladder = self.ladder
        assert -1 < i < len(ladder)
        assert -1 < j < len(ladder)
        res = ladder[j] if i == 0 else ladder[j] - ladder[i - 1]
        return res
        
# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
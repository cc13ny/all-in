class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        tb = set()
        
        for n in nums:
            if n in tb:
                return True
            else:
                tb.add(n)
        return False

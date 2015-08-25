class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tb = {}
        for i in range(len(nums)):
            tb[nums[i]] = i
        
        res = 1
        for num in nums:
            if num in tb:
                n = 1
                del tb[num]
                
                inc = 1
                while num + inc in tb:
                    del tb[num + inc]
                    n += 1
                    inc += 1
                
                inc = -1
                while num + inc in tb:
                    del tb[num + inc]
                    n += 1
                    inc -= 1
                    
                res = max(res, n)
        return res

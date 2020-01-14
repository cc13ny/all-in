class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        sort = [0]
        res = 0
        for i in range(len(nums)):
            lb = nums[i] - upper
            ub = nums[i] - lower
            ucnt, lcnt = 0, 0
            
            # lower than lb
            l, r = 0, i
            while l <= r:
                m = l + (r - l) / 2
                if sort[m] < lb:
                    l = m + 1
                else:
                    r = m - 1
            res -= l
                    
            # lower than or equal to ub
            l, r = 0, i
            while l <= r:
                m = l + (r - l) / 2
                if sort[m] <= ub:
                    l = m + 1
                else:
                    r = m - 1
            res += l
            
            # insert nums[i] into sort
            l, r = 0, i
            while l <= r:
                m = l + (r - l) / 2
                if sort[m] < nums[i]:
                    l = m + 1
                else:
                    r = m - 1
            sort.insert(l, nums[i])
        return res

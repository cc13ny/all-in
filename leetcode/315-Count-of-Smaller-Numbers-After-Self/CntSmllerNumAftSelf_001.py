class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []

        res = []
        sorted_nums = []
        rev = nums[::-1]

        for num in rev:
            l, r = 0, len(res) - 1
            while l <= r:
                m = l + (r - l) / 2
                if num <= sorted_nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            res.insert(0, l)
            sorted_nums.insert(l, num)
        return res

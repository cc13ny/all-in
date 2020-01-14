class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        sect = {}
        res = []
        for num in nums1:
            if num in sect:
                sect[num][0] += 1
            else:
                sect[num] = [1, 0]
        for num in nums2:
            if num in sect:
                sect[num][1] += 1
        for k in sect:
            res += min(sect[k]) * [k]
        return res

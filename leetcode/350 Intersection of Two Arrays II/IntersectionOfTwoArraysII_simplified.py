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
            sect[num] = sect.get(num, 0) + 1
        for num in nums2:
            if num in sect and sect[num]:
                res += [num]
                sect[num] -= 1
        return res

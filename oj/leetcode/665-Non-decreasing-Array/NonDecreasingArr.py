class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        is_modified = False
        
        for i in xrange(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if is_modified:
                    return False
                else:
                    if i == 0 or nums[i-1] <= nums[i+1]:
                        nums[i] = nums[i+1]
                    else:
                        nums[i+1] = nums[i]
                    is_modified = True
        return True

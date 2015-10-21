#@author: cchen
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        idx = sorted(range(len(nums)), key = lambda x:nums[x])
        nums.sort()
        i, j = 0, len(nums)-1
        
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                if idx[i] > idx[j]:
                    return [idx[j] + 1, idx[i] + 1]
                else:
                    return [idx[i] + 1, idx[j] + 1]

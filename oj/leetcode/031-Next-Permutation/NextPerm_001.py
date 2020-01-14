#@author: cchen

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        if len(nums) > 1:
            flag = True
            for i in range(1, len(nums)):
                j = len(nums) - 1 - i
                if nums[j] < nums[j+1]:
                    flag = False
                    tmp = nums[j]
                    for k in range(len(nums) -1 , j, -1):
                        if nums[k] > tmp:
                            break
                    nums[j] = nums[k]
                    nums[k] = tmp
                    l = j + 1
                    r = len(nums) - 1
                    while l < r:
                        tmp = nums[l]
                        nums[l] = nums[r]
                        nums[r] = tmp
                        l = l + 1
                        r = r - 1
                    break
            if flag:
                nums.sort()

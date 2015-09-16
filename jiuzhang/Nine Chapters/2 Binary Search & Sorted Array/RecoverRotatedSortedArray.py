class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        pivot = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pivot = i
                break

        if pivot != -1:
            start, end = 0, len(nums) - 1
            nums = self.swap(nums, pivot, start, end)

    def swap(self, nums, pivot, start, end):
        l, r = pivot - start + 1, end - pivot
        if l < r:
            nums = self.swap(nums, pivot, start, pivot + l)
            nums = self.swap(nums, pivot + l, pivot + 1, end)
        elif l > r:
            nums = self.swap(nums, pivot, pivot - r + 1, end)
            nums = self.swap(nums, pivot - r, start, pivot)
        else:
            for i in range(start, pivot + 1):
                step = pivot + 1 - start
                nums[i], nums[i + step] = nums[i + step], nums[i]
        return nums
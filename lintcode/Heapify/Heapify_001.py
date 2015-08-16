class Solution:
    # @param A: Given an integer array
    # @return: void
    def siftdown(self, nums, i):
        while i < len(nums):
            smallest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < len(nums) and nums[l] < nums[smallest]:
                smallest = l
            if r < len(nums) and nums[r] < nums[smallest]:
                smallest = r
            if smallest == i:
                break
            nums[smallest], nums[i] = nums[i], nums[smallest]
            i = smallest
        return nums

    def heapify(self, A):
        # write your code here
        for i in range((len(A) - 2) / 2, -1, -1):
            A = self.siftdown(A, i)

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i, num in enumerate(nums):
            idx = index[i]
            target = target[:idx] + [num] + target[idx:]
        return target

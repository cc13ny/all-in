class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        numIdx = {}
        for i, num in enumerate(numbers):
            if (target - num) in numIdx:
                return [numIdx[target - num], i]
            numIdx[num] = i
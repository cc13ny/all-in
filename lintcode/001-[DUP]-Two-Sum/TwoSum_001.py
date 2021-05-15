class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here
        idx = sorted(range(len(numbers)), key=lambda x: numbers[x])
        numbers.sort()
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                if idx[i] > idx[j]:
                    return [idx[j] + 1, idx[i] + 1]
                else:
                    return [idx[i] + 1, idx[j] + 1]

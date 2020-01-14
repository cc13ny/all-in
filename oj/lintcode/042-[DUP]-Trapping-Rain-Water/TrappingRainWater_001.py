class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        i, j = 0, len(heights) - 1

        res = 0
        while i < j:
            if heights[i] < heights[j]:
                h = heights[i]
                i += 1
                while i <= j and heights[i] < h:
                    res += h - heights[i]
                    i += 1
            else:
                h = heights[j]
                j -= 1
                while i <= j and heights[j] < h:
                    res += h - heights[j]
                    j -= 1
        return res

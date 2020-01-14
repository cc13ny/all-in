class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        i, j = 0, len(height) - 1

        res = 0
        while i < j:
            if height[i] < height[j]:
                h = height[i]
                i += 1
                while i <= j and height[i] < h:
                    res += h - height[i]
                    i += 1
            else:
                h = height[j]
                j -= 1
                while i <= j and height[j] < h:
                    res += h - height[j]
                    j -= 1
        return res

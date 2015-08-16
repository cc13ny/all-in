class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        maxval = 0
        if not height:
            return maxval
        cand = [[0, height[0]]]
        for i in range(1, len(height)):
            h = height[i]
            if h >= height[cand[-1][0]]:
                cand.append([i, height[i]])
            else:
                j = len(cand) - 1
                while j > -1:
                    if height[cand[j][0]] > h:
                        idx = cand[j][0]
                        pre = cand[j][1]
                        tmp = pre + height[idx] * (i - idx - 1)
                        if tmp > maxval:
                            maxval = tmp
                        cand.pop()
                        j -= 1
                    else:
                        break
                cnt = pre / height[idx] + i - idx
                cand.append([i, height[i] * cnt])
        for i in range(len(cand)):
            idx = cand[i][0]
            tmp = height[idx] * (cand[-1][0] - idx) + cand[i][1]
            if tmp > maxval:
                maxval = tmp
        return maxval

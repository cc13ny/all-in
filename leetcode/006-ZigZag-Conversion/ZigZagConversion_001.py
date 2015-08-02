class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows < 2:
            return s
        halfsize = numRows - 1
        size = 2 * halfsize
        res = ''
        for i in range(numRows):
            j = i
            if i % halfsize == 0:
                while j < len(s):
                    res += s[j]
                    j += size
            else:
                cnt = 1
                while j < len(s):
                    res += s[j]
                    j = cnt * size - j
                    cnt += 1
        return res

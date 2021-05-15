class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        if len(s) < 11:
            return []
        a = {}
        for t in range(len(s) - 9):
            if s[t:t + 10] not in a:
                a[s[t:t + 10]] = 1
            else:
                a[s[t:t + 10]] += 1
        b = []
        for i in a:
            if a[i] > 1:
                b.append(i)
        return b

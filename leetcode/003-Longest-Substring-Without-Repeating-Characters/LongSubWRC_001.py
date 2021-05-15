# @author: cchen

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start, maxlen = 0, 0
        dict = {c: -1 for c in s}
        for i in xrange(len(s)):
            if dict[s[i]] != -1:
                while start <= dict[s[i]]:
                    dict[s[start]] = -1
                    start += 1
            maxlen = max(maxlen, i - start + 1)
            dict[s[i]] = i
        return maxlen

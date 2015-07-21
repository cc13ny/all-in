class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start, maxlen = 0, 0
        dict = {s[i]: -1 for i in range(len(s))}
        for i in range(len(s)):
            if dict[s[i]] != -1:
                while start <= dict[s[i]]:
                    dict[s[start]] = -1
                    start += 1
            if i - start + 1 > maxlen: maxlen = i - start + 1
            dict[s[i]] = i
        return maxlen

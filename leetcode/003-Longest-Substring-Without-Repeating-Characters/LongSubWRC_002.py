'''
  Reference:
    Approach#3 in
    - https://leetcode.com/articles/longest-substring-without-repeating-characters/
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        res = 0
        dict = {}
        for j in xrange(len(s)):
            if s[j] in dict:
                i = max(i, dict[s[j]])
            res = max(res, j-i+1)
            dict[s[j]] = j + 1
        return res

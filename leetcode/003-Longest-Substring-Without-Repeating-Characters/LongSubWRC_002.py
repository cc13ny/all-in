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
        res = 0
        i = -1
        map = {}
        for j in range(len(s)):
            i = max(i, map.get(s[j], -1))
            res = max(res, j - i)
            map[s[j]] = j
        return res

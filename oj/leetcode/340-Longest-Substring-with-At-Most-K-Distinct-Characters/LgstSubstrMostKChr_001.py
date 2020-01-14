class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        i, j = 0, 0
        cnt = 0
        chrs = {ch: [] for ch in set(s)}
        while j < len(s) or cnt > k:
            if cnt <= k:
                pre = j
                while j < len(s) and s[pre] == s[j]:
                    j += 1
                if not chrs[s[pre]]:
                    cnt += 1
                chrs[s[pre]].append(j - pre)
            else:
                if len(chrs[s[i]]) == 1:
                    cnt -= 1
                i += chrs[s[i]].pop(0)
            if cnt <= k:
                res = max(res, j - i)

        return res

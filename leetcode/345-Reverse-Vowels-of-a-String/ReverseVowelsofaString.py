class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        ls = list(s)
        idx = [i for i in xrange(len(s)) if s[i] in vowels]

        for i in xrange(len(idx) / 2):
            l, r = idx[i], idx[-i - 1]
            ls[l], ls[r] = ls[r], ls[l]
        return ''.join(ls)

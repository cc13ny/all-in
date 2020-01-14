'''
https://leetcode.com/contest/leetcode-weekly-contest-18a/problems/keyboard-row/
'''

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lines = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        res = []
        for word in words:
            st = set(word.lower())
            for line in lines:
                if st.issubset(line):
                    res.append(word)
                    break
        return res

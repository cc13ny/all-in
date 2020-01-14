class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cnts = [0] * 26
        for l in magazine:
            cnts[ord(l) - 97] += 1
        for l in ransomNote:
            i = ord(l) - 97
            if not cnts[i]:
                return False
            cnts[i] -= 1
        return True

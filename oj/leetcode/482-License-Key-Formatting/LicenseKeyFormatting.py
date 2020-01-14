class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        M = ''.join(S.split('-'))
        sec = [M[max(i-K, 0):i].upper() for i in range(len(M), -1, -K)][::-1]
        sec = sec if sec[0] else sec[1:]
        return '-'.join(sec)

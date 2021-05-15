class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        interleaved = [[False] * (n + 1) for i in range(m + 1)]
        interleaved[0][0] = True

        for j in range(1, n + 1):
            if interleaved[0][j - 1] and s3[j - 1] == s2[j - 1]:
                interleaved[0][j] = True

        for i in range(1, m + 1):
            if interleaved[i - 1][0] and s3[i - 1] == s1[i - 1]:
                interleaved[i][0] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (interleaved[i - 1][j] and s3[i + j - 1] == s1[i - 1]) or (
                        interleaved[i][j - 1] and s3[i + j - 1] == s2[j - 1]):
                    interleaved[i][j] = True
        return interleaved[m][n]

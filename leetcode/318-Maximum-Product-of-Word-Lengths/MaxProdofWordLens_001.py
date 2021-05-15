class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ones = [0] * 26
        t = 1
        for i in range(26):
            ones[i] = t
            t = t << 1

        pairs = []
        for word in words:
            rep = 0
            visited = [False] * 26
            for ch in word:
                idx = ord(ch) - 97
                if not visited[idx]:
                    rep += ones[idx]
                visited[idx] = True
            pairs.append((len(word), rep))
        pairs.sort()

        res = 0
        n = len(words)
        for i in xrange(n - 2, -1, -1):
            for j in xrange(n - 1, i, -1):
                if res >= pairs[i][0] * pairs[j][0]:
                    break

                commn = pairs[i][1] & pairs[j][1]

                if not commn:
                    mul = pairs[i][0] * pairs[j][0]
                    if mul > res:
                        res = mul
                    break
        return res

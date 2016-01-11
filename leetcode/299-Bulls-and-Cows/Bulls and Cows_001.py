class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        nbulls, ncows = 0, 0
        s, g = {}, {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                nbulls += 1
            else:
                sec, gus = secret[i], guess[i]
                s[sec] = s.get(sec, 0) + 1
                g[gus] = g.get(gus, 0) + 1
                if sec in g and g[sec] > 0:
                    s[sec] -= 1
                    g[sec] -= 1
                    ncows += 1
                if gus in s and s[gus] > 0:
                    s[gus] -= 1
                    g[gus] -= 1
                    ncows += 1
        return str(nbulls) + 'A' + str(ncows) + 'B'

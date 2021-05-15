# Faster than 001

# {Leetcode : AC, Lintcode : Runtime Error}


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if s == '' and wordDict == {}:
            return True
        lendict, lenlist = {}, []
        for word in wordDict:
            l = len(word)
            if l in lendict:
                lendict[l].add(word)
            else:
                lendict[l] = set([word])
                lenlist.append(l)
            lenlist.sort()

        ladder = [0] * len(s)
        ladder = self.wordladder(s, 0, lendict, lenlist, ladder)
        return ladder[-1] == 1

    def wordladder(self, w, start, tb, ls, ladder):
        for l in ls:
            idx = start + l - 1
            if idx + 1 > len(w):
                break
            else:
                flag = ladder[idx]
                if flag == 0 and w[start: idx + 1] in tb[l]:
                    ladder[idx] = 1
                    ladder = self.wordladder(w, idx + 1, tb, ls, ladder)
                    if ladder[-1] == 1:
                        return ladder

        return ladder

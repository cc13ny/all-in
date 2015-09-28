# Complicated, not clear and straightforward
# Have to handle special cases
# O(n^2), same speed on leetcode tests as 002
# {Leetcode: AC, Lintcode : AC}

class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        if s == '' and dict == {}:
            return True
        lendict, lenlist = {}, []
        for word in dict:
            l = len(word)
            if l in lendict:
                lendict[l].add(word)
            else:
                lendict[l] = set([word])
                lenlist.append(l)
        lenlist.sort()
        cand = []
        for l in lenlist:
            if l <= len(s):
                if s[:l] in lendict[l]:
                    if l == len(s):
                        return True
                    cand.append(l - 1)
            else:
                break

        notVisited = [True] * len(s)

        while len(cand) != 0:
            newcand = []
            for c in cand:
                for l in lenlist:
                    idx = c + l
                    if idx > len(s) - 1:
                        break
                    else:
                        word = s[c + 1: idx + 1]
                        if notVisited[idx] and word in lendict[l]:
                            newcand.append(idx)
                            notVisited[idx] = False
                            if idx == len(s) - 1:
                                return True
            cand = newcand

        return False

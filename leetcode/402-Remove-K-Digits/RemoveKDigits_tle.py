class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        l, r = 0, k
        idx, kk = l, k
        res = ''
        while len(res) != len(num) - kk:
            idx = l
            tmp = num[l]
            for i in xrange(l, min(r, len(num) - 1) + 1):
                if num[i] == 0:
                    idx = i
                    break
                if num[i] < tmp:
                    idx = i
                    tmp = num[i]
            k -= (idx - l)
            l = idx + 1
            r = l + k
            res += num[idx]
        if k == 0:
            res += num[idx + 1:]
        idx = -1
        for i in xrange(len(res)):
            if res[i] != '0':
                idx = i
                break
        res = '0' if idx == -1 else res[idx:]
        return res

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if len(s) <2:
            return [[s]]
        l = 0
        r = 0
        ls = []
        lst = []
        res = []
        j = 1

        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                r = i
            else:
                ls.append([[l, r], s[i-1]])
                if s[i] == s[0]:
                    lst.append(j)
                j += 1
                l = i
                r = i
        ls.append([[l, r], s[i]])
        r = ls[0][0][1]
        size = r+1
        for i in range(size):
            tmp = self.partition(s[i+1:])
            for t in tmp:
                tm = s[:i+1]
                if t != ['']:
                    t.insert(0, tm)
                else:
                    t = [tm]
                res.append(t)    
        for idx in lst:
            llen = ls[idx][0][1] - ls[idx][0][0] + 1
            flag = True
            if size <= llen:
                l = 1
                r = idx - 1
                while l < r:
                    llen = ls[l][0][1] - ls[l][0][0]
                    rlen = ls[r][0][1] - ls[r][0][0]
                
                    if ls[l][1] == ls[r][1] and llen == rlen:
                        l += 1
                        r -= 1
                    else:
                        flag = False
                        break
            else:
                flag = False
            if flag:
                rr = ls[idx][0][0] + size - 1
                tmp = self.partition(s[rr+1:])
                for t in tmp:
                    tm = s[:rr+1]
                    if t != ['']:
                        t.insert(0, tm)
                    else:
                        t = [tm]

                    res.append(t)
            
        
        return res

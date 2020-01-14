#@author: cchen
#pretty long and should be simplified later

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        size  = len(s)
        ls = []
        ll = 0
        rr = 0
        l = 0
        r = 0
        maxlen = r - l + 1
    
        for i in range(1, size):
            if s[i-1] == s[i]:
                r = i
            else:
                if r - l + 1 > maxlen:
                    maxlen = r - l + 1
                    ll = l
                    rr = r
                ls.append([[l, r], s[i-1]])
            
                l = i
                r = i
        if r - l + 1 > maxlen:
            maxlen = r - l + 1
            ll = l
            rr = r
        ls.append([[l, r], s[size - 1]])
    
        for i in range(1, len(ls) - 1):
            l = i - 1
            r = i + 1
            clen = ls[i][0][1] - ls[i][0][0] + 1
        
            while -1 < l and r < len(ls) and ls[l][1] == ls[r][1]:
                llen = ls[l][0][1] - ls[l][0][0] + 1
                rlen = ls[r][0][1] - ls[r][0][0] + 1
                if llen == rlen:
                    clen += 2 * llen
                    if clen > maxlen:
                        maxlen = clen
                        ll = ls[l][0][0]
                        rr = ls[r][0][1]  
                    l -= 1
                    r += 1
                else:
                    if llen > rlen:
                        clen += 2*rlen
                    else:
                        clen += 2*llen
                
                    if clen > maxlen:
                        maxlen = clen
                        if llen > rlen:
                            ll = ls[l][0][1] - rlen + 1
                            rr = ls[r][0][1]
                        else:
                            ll = ls[l][0][0]
                            rr = ls[r][0][0] + llen - 1
                    
                    break
            
        return s[ll:rr+1]

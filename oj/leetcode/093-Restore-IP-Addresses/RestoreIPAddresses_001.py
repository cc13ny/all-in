class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        return self.segIp(s, 4)
    
    def segIp(self, s, nsegs):
        res = []
        if len(s) > 3 * nsegs or len(s) < nsegs:
            return res
     
        if nsegs == 1:
             if s == '0' or (s[0] != '0' and 0 <= int(s) <= 255):
                  res.append(s)
             return res
        
        for i in range(min(len(s), 3)):
            num = int(s[:i + 1])
            if 0 <= num <= 255:
                tmp = self.segIp(s[i + 1:], nsegs - 1)
                for t in tmp:
                    res.append(str(num) + '.' + t)
            if num == 0:
                 break
               
        return res

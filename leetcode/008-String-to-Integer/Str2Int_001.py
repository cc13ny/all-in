# @author: cchen
# Terrible code, and it will be updated and simplified later.

class Solution:
    # @param {string} str
    # @return {integer}
    def extractnum(self, ss):
        num = 0
        for i in range(len(ss)):
            if ss[i].isdigit() == False:
                break
            else:
                num = num + 1
        return ss[:num]

    def isoverflow(self, sss, ispos):

        if ispos:
            tmp = '2147483647'
            if len(sss) > len(tmp):
                return True
            elif len(sss) < len(tmp):
                return False
            for j in range(len(tmp)):
                if sss[j] > tmp[j]:
                    return True
                elif sss[j] < tmp[j]:
                    return False
            return False
        else:
            tmp = '2147483648'
            if len(sss) > len(tmp):
                return True
            elif len(sss) < len(tmp):
                return False
            for j in range(len(tmp)):
                if sss[j] > tmp[j]:
                    return True
                elif sss[j] < tmp[j]:
                    return False
            return False

    def myAtoi(self, str):
        str = str.strip()
        if len(str) == 0:
            return 0
        flag = True
        if str[0] == '+':
            str = str[1:]
        elif str[0] == '-':
            str = str[1:]
            flag = False
        if len(str) == 0 or str[0].isdigit() == False:
            return 0
        if flag:
            n = self.extractnum(str)
            if self.isoverflow(n, True) == True:
                return 2147483647
            else:
                return int(n)
        else:
            n = self.extractnum(str)
            if self.isoverflow(n, False) == True:
                return -2147483648
            else:
                return -int(n)

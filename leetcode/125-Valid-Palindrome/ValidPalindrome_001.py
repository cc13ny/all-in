class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        p = 0
        num = len(s)
        q = num - 1
        
        while p < q:
            if s[p].isalnum() and s[q].isalnum():
                if s[p].lower() != s[q].lower():
                    return False
                else:
                    p = p + 1
                    q = q - 1
            else:
                while p <= q and s[p].isalnum() == False:
                    p = p + 1
                
                while p <= q and s[q].isalnum() == False:
                    q = q - 1
                
        return True

def is_palindrome(st):
    l, r = 0, len(st)-1
    while l < r:
        if st[l] != st[r]:
            return False
        l += 1
        r -= 1
    return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if is_palindrome(s):
            return True
        for i in range(len(s)):
            if is_palindrome(s[:i] + s[i+1:]):
                return True
        return False
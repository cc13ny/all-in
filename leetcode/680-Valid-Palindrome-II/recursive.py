def is_palindrome(st):
    l, r = 0, len(st) - 1
    while l < r:
        if st[l] != st[r]:
            return False
        l += 1
        r -= 1

    return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True

        res = False
        if s[0] == s[-1]:
            res = res or self.validPalindrome(s[1:-1])

        res = res or is_palindrome(s[1:]) or is_palindrome(s[:-1])

        return res

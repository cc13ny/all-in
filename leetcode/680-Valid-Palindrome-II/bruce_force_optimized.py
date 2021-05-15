# my original version
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
        if is_palindrome(s):
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                break
            l += 1
            r -= 1

        return is_palindrome(s[l:r]) or is_palindrome(s[l + 1:r + 1])


# simplified version
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
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_palindrome(s[l:r]) or is_palindrome(s[l + 1:r + 1])
            l += 1
            r -= 1

        return True

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c == ')' or c == ']' or c == '}':
                if not stack or pairs[stack.pop()] != c:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True

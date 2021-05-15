class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        res = ''
        for c in s:
            if c == ')':
                if len(stack) > 0:
                    stack.pop()
                    res += c
            else:
                res += c
                if c == '(':
                    stack.append(len(res) - 1)

        res = list(res)
        for idx in stack:
            res[idx] = ''

        return ''.join(res)

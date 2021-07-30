'''
Don't think this solution is good enough for the following reasons.

1. Don't need to check isnumeric and to concatenate string


'''


class SolutionWithOneStack:
    def decodeString(self, s: str) -> str:
        stack = []
        num = ""
        strs = ""

        for c in s:
            if c.isnumeric():
                num += c
            elif c == "[":
                stack.append(num)
                num = ""
            elif c == "]":
                while stack:
                    c = stack.pop()
                    if c.isnumeric():
                        stack.append(int(c) * strs)
                        strs = ""
                        break
                    else:
                        strs = c + strs
            else:
                stack.append(c)
        return "".join(stack)


'''

That's the best.

'''


class SolutionWithTwoStacks:
    def decodeString(self, s: str) -> str:
        i = 0
        num = ''
        res = ''

        num_stack = []
        str_stack = []

        while i < len(s):
            if s[i].isnumeric():
                num = ''
                while s[i].isnumeric():
                    num += s[i]
                    i += 1  # by doing that, we skip "[" at the end in fact
                num_stack.append(num)
                str_stack.append(res)  # the string ahead, not that we need the stack
                # before there are more thn one string ahead.
                res = ''
            elif s[i] == ']':
                res = str_stack.pop() + int(num_stack.pop()) * res
            else:
                res += s[i]
            i += 1

        return res

# Wrong: we don't really two stacks


class SolutionTryToRemoveStringStackWrong:
    def decodeString(self, s: str) -> str:
        i = 0
        num = ''
        res = ''

        num_stack = []
        pre_str = ""

        while i < len(s):
            if s[i].isnumeric():
                num = ''
                while s[i].isnumeric():
                    num += s[i]
                    i += 1
                num_stack.append(num)
                pre_str = res
                res = ""
            elif s[i] == ']':
                res = pre_str + int(num_stack.pop()) * res
                pre_str = ""
            else:
                res += s[i]
            i += 1

        return res

'''

'''


class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        num = ''
        tmp_str = ''

        num_stack = []
        str_stack = []

        for c in s:
            if c.isnumeric():
                if num == '':
                    str_stack.append(tmp_str)
                    tmp_str = ''
                num += c
            elif c == '[':
                num_stack.append(num)
                num = ''
            elif c == ']':
                tmp_str = str_stack.pop() + int(num_stack.pop()) * tmp_str
                if len(num_stack) == 0:
                    res += tmp_str
                    tmp_str = ''
            else:
                tmp_str += c
        res += tmp_str
        return res




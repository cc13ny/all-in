# @author: cchen
class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        i = 0
        while len(tokens) != 1:
            if not tokens[i].strip('-').isdigit():  # 1st prob in py, integer checker including negative ones
                if tokens[i] == '*':
                    tokens[i - 2] = str(int(tokens[i - 2]) * int(tokens[i - 1]))
                if tokens[i] == '/':  # 2nd prob in py, ceiling func
                    tmp1 = int(tokens[i - 2])
                    tmp2 = int(tokens[i - 1])
                    if tmp1 / tmp2 < 0 and tmp1 % tmp2 != 0:
                        tokens[i - 2] = str(tmp1 / tmp2 + 1)
                    else:
                        tokens[i - 2] = str(tmp1 / tmp2)
                if tokens[i] == '+':
                    tokens[i - 2] = str(int(tokens[i - 2]) + int(tokens[i - 1]))
                if tokens[i] == '-':
                    tokens[i - 2] = str(int(tokens[i - 2]) - int(tokens[i - 1]))
                del tokens[i - 1]
                del tokens[i - 1]
                i -= 1
            else:
                i += 1

        return int(tokens[0])

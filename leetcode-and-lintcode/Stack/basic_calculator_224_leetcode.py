'''
这是真正处理好 "48 - -48"这样的case
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        sign_stack = [1]
        current_sign = 1

        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = ""
                while i < len(s):
                    if s[i].isdigit():
                        num += s[i]
                        i += 1
                    else:
                        break
                i -= 1
                res += int(num) * current_sign * sign_stack[-1]
                current_sign = 1
            elif c == "(":
                sign_stack.append(current_sign * sign_stack[-1])
                current_sign = 1
            elif c == ")":
                sign_stack.pop()
            elif c == "-":
                current_sign *= -1
            i += 1
        return res

'''
原答案基础上处理 "48 - -48"这样的case
'''
class Solution(object):
    def calculate(self, s):
        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                if operand > 0:
                    sign = -1
                else:
                    sign *= -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand




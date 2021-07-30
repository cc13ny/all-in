'''
cp: the count of "(" plus "*"
df: the count of "(" minus "*"

If cp < 0 during the process, it means that the count of ")" is more than the total of "(" plus "*".
If df > 0 at the end, it means that the count of "(" is more than the total of "*" plus ")".

'''


class Solution1:
    """
    @param s: the given string
    @return: whether this string is valid
    """
    def checkValidString(self, s):
        # Write your code here
        cp, df = 0, 0
        for c in range(s):
            if c == "(":
                cp += 1
                df += 1
            elif c == "*":
                cp += 1
                if df > 0:
                    df -= 1
            else:
                cp -= 1
                if df > 0:
                    df -= 1
                if cp < 0:
                    return False

        return df == 0

    def checkValidString_Cleaner(self, s):
        # Write your code here
        low = high = 0
        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                low -= 1
                high -= 1
            if c == '*':
                low -= 1
                high += 1
            if high < 0:
                return False
            low = max(low, 0)
        return low == 0


# ToDo: think about other solutions

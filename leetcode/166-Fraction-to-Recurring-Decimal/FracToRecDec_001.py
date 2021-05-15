class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if numerator == 0: return '0'

        s1 = 1 if numerator > 0 else -1
        s2 = 1 if denominator > 0 else -1
        sign = s1 * s2
        num, den = abs(numerator), abs(denominator)
        out, rem = num / den, num % den
        res = str(out) if sign == 1 else '-' + str(out)

        if rem == 0: return res

        res += '.';
        s = '';
        pos = 0;
        tb = {}
        while rem != 0:
            if rem in tb:
                start = tb[rem]
                s = s[:start] + '(' + s[start:] + ')'
                break

            tb[rem] = pos
            s += str(rem * 10 / den)
            rem = rem * 10 % den
            pos += 1
        return res + s

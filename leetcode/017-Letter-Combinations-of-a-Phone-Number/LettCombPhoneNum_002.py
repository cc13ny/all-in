class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        def comb(digits, d2l):
            if not digits:
                return [""]

            res = []
            for c in d2l[int(digits[0])]:
                for suffix in comb(digits[1:], d2l):
                    res.append(c + suffix)
            return res

        if not digits:
            return []

        d2l = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
               6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        return comb(digits, d2l)

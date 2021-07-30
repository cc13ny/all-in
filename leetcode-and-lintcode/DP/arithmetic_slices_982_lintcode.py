'''
Permutation, Combination, how much is added

Don't forget the context is, continuous subarray.
So the calculation formulas of Permutation and Combination don't apply.
'''


'''
Non-DP, Space O(1)
'''


class Solution1:
    """
    @param A: an array
    @return: the number of arithmetic slices in the array A.
    """
    def numberOfArithmeticSlices(self, A):
        # Write your code here
        def getSliceNum(num):
            return num * (num+1) // 2

        n = len(A)
        if n < 3:
            return 0

        res = 0
        ntriples = 0
        for i in range(1, n-1):
            if 2 * A[i] == A[i-1] + A[i+1]:
                ntriples += 1
            else:
                res += getSliceNum(ntriples)
                ntriples = 0

        return res + getSliceNum(ntriples) if ntriples > 0 else res


'''
DP, Space O(1)

dp[i] represents the amount of addition.

The idea of NineChapter's solution is same as this one. However, less concise.
'''


class Solution2:
    """
    @param A: an array
    @return: the number of arithmetic slices in the array A.
    """
    def numberOfArithmeticSlices(self, A):
        if A is None or len(A) < 3:
            return 0

        n = len(A)
        dp = [0] * n
        for i in range(2, n):
            if 2 * A[i-1] == A[i] + A[i-2]:
                dp[i] = dp[i-1]+1
        return sum(dp)
